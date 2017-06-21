import { Injectable } from '@angular/core';
import { Resolve, ActivatedRouteSnapshot, RouterStateSnapshot, Router } from '@angular/router';
import { CallService } from '../../../lib/services/call.service';

@Injectable()
export class AsistenteService {

    constructor(public _cl: CallService) { }

    public data: any[];

    getById(id) {
        if (id === 0) return Promise.resolve({});
        let res;
        if (this.data) {
            res = this.data.filter(item => item.id === id);
            if (res) return Promise.resolve(res[0]);
            return Promise.reject(null);
        }
        return Promise.reject(null);
    }
    list(query) {
        return this._cl.get('usuarios/asistente/list/', query, this._cl.json);
    }
    add(body: any) {
        return this._cl.post('usuarios/asistente/from/', body);
    }
    edit(id: number, body: any) {
        return this._cl.post(`usuarios/asistente/from/${id}/`);
    }
    delete(id: number) {
        return this._cl.get(`usuarios/asistente/delete/${id}/`);
    }
}

@Injectable()
export class AsistenteResolver implements Resolve<any> {

    constructor(private _as: AsistenteService,
        private router: Router) { }

    resolve(route: ActivatedRouteSnapshot, state: RouterStateSnapshot) {
        let id = route.params['id'];
        // let id = route.paramMap.get('id');
        if (isNaN(+id)) {
            console.log(`Asistente id was not a number: ${id}`);
            this.router.navigate(['/usuarios/asistente']);
            return null;
        }
        return this._as.getById(+id)
            .then(asistente => {
                if (asistente) {
                    console.log(asistente);
                    return asistente;
                }
                console.log(`Product was not found: ${id}`);
                this.router.navigate(['/usuarios/asistente']);
                return null;
            })
            .catch(error => {
                console.log(`Retrieval error: ${error}`);
                this.router.navigate(['/usuarios/asistente']);
                return null;
            });
    }
}