import { Resolve, ActivatedRouteSnapshot, RouterStateSnapshot, Router } from '@angular/router';
import { CallService } from './call.service';

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

    getById(id) {
        if (id === 0) {
            return Promise.resolve({})
        };
        let res;
        if (this.data) {
            res = this.data.filter(item => item.id === id);
            if (res) {
                return Promise.resolve(res[0]);
            }
            return Promise.reject(null);
        }
        return Promise.reject(null);
    }

    list(query) {
        if (!!this.conf.list) {
            return this._cl.get(this.conf.list, query, this._cl.json);
        }
    }

    add(body: any) {
        if (!!this.conf.add) {
            return this._cl.post(this.conf.add, body);
        }
    }

    edit(id: number, body: any) {
        if (!!this.conf.edit) {
            return this._cl.post(this.conf.edit.replace('$(id)', `${id}`), body);
        }
    }

    delete(id: number) {
        if (!!this.conf.delete) {
            return this._cl.delete(this.conf.delete.replace('$(id)', `${id}`));
        }
    }

    resolve(route: ActivatedRouteSnapshot, state: RouterStateSnapshot) {
        const id = route.params['id'];
        if (isNaN(+id)) {
            console.log(`Item id was not a number: ${id}`);
            this.router.navigate([this.conf.redirect || '/']);
            return null;
        }
        return this.getById(+id)
            .then(item => {
                if (item) {
                    // console.log(item);
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
}

export class CrudService extends CrudBase {

    constructor(protected _cl: CallService, protected _rt: Router, public base_url: string) {
        super(_cl, _rt);
        this.setBaseUrl(base_url);
    }
    setBaseUrl(val) {
        this.base_url = val;
        super.init({
            redirect: val,
            list: `${val}list/`,
            add: `${val}form/`,
            edit: `${val}form/$(id)/`,
            delete: `${val}delete/$(id)/`
        });
    }
}
