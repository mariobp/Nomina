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
                console.log(`Item was not found: ${id}`);
                this.router.navigate([this.conf.redirect || '/']);
                return null;
            })
            .catch(error => {
                console.log(`Retrieval error: ${error}`);
                this.router.navigate([this.conf.redirect || '/']);
                return null;
            });
    }

    down(aurl: string, id: string, formt: number, getName: any) {
        const url = `${this._cl.getUrl(aurl)}${id}`;
        $.ajax({
            url: url,
            method: 'POST',
            data: { file_format: formt },
            xhrFields: {
                withCredentials: true
            },
            success: function(data) {
                const blob = new Blob([data]);
                const link = document.createElement('a');
                const date = new Date();
                link.href = window.URL.createObjectURL(blob);
                link.download = getName();
                link.click();
            }
        });
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
