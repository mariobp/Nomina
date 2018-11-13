import { Resolve, ActivatedRouteSnapshot, RouterStateSnapshot, Router } from '@angular/router';
import { CallService } from './call.service';

declare var $: any;

export interface CrudConf {
    redirect?: string;
    list?: string;
    add?: string;
    edit?: string;
    delete?: string;
}

export class CrudBase implements Resolve<any> {

    public data: any[];

    protected conf: CrudConf;

    constructor(protected _cl: CallService, protected router: Router) {
        this.conf = {};
    }

    protected init(conf: CrudConf) {
        this.conf = conf;
    }

    setAddUrl(val: string) {
        this.conf.add = val;
    }

    setEditUrl(val: string) {
        this.conf.edit = val;
    }

    setRedirectUrl(val: string) {
        this.conf.redirect = val;
    }

    setDeleteUrl(val: string) {
        this.conf.delete = val;
    }

    setListUrl(val: string) {
        this.conf.list = val;
    }

    get addUrl() {
        return this.conf.add;
    }
    get editUrl() {
        return this.conf.edit;
    }
    get redirectUrl() {
        return this.conf.redirect;
    }
    get deleteUrl() {
        return this.conf.delete;
    }
    get listUrl() {
        return this.conf.list;
    }

    getById(id) {
        if (id === 0) {
            return Promise.resolve({})
        };
        if (this.data) {
            const res = this.data.filter(item => item.id === id);
            if (!!res[0]) {
                return Promise.resolve(res[0]);
            }
        }
        return this.list({ id: id }).then(data => data.json()).then(data => Promise.resolve(data.object_list[0]));
    }

    list(query) {
        if (!!this.conf.list) {
            return this._cl.get(this.conf.list, query, this._cl.json);
        } else {
            throw new SyntaxError('No se ha configurado url para listar');
        }
    }

    add(body: any) {
        if (!!this.conf.add) {
            return this._cl.post(this.conf.add, body);
        } else {
            throw new SyntaxError('No se ha configurado url para agregar');
        }
    }

    edit(id: number, body: any) {
        if (!!this.conf.edit) {
            return this._cl.post(this.conf.edit.replace('$(id)', `${id}`), body);
        } else {
            throw new SyntaxError('No se ha configurado url para editar')
        }
    }

    delete(id: number) {
        if (!!this.conf.delete) {
            return this._cl.delete(this.conf.delete.replace('$(id)', `${id}`));
        } else {
            throw new SyntaxError('No se ha configurado url para borrar')
        }
    }

    resolve(route: ActivatedRouteSnapshot, state: RouterStateSnapshot) {
        const id = route.params['id'];
        if (isNaN(+id)) {
            // console.log(`Item id was not a number: ${id}`);
            this.router.navigate([this.conf.redirect || '/']);
            return null;
        }
        return this.getById(+id)
            .then(item => {
                if (item) {
                    return item;
                }
                this.router.navigate([this.conf.redirect || '/']);
                return null;
            })
            .catch(error => {
                this.router.navigate([this.conf.redirect || '/']);
                return null;
            });
    }

    down(aurl: string, id: string, formt: number) {
        const url = `${this._cl.getUrl(aurl)}${id}`;
        const form = document.createElement('form');
        const input = document.createElement('input');
        const button = document.createElement('button');
        button.setAttribute('type', 'submit')
        input.setAttribute('type', 'hidden');
        input.setAttribute('name', 'file_format');
        input.setAttribute('value', '' + formt);
        form.setAttribute('action', url);
        form.setAttribute('method', 'POST');
        form.setAttribute('target', '_blank')
        form.appendChild(input);
        form.appendChild(button);
        document.body.appendChild(form);
        button.click();
        document.body.removeChild(form);
    }
}

export class CrudService extends CrudBase {

    constructor(protected _cl: CallService, protected _rt: Router, public base_url: string) {
        super(_cl, _rt);
        this.setBaseUrl(base_url);
    }
    setBaseUrl(val) {
        this.base_url = val;
        super.init({
            redirect: this.base_url,
            list: `${this.base_url}list/`,
            add: `${this.base_url}form/`,
            edit: `${this.base_url}form/$(id)/`,
            delete: `${this.base_url}delete/$(id)/`
        });
    }
}
