import { Injectable } from '@angular/core';
import { Router } from '@angular/router';
import { CallService, CrudBase } from '../../../lib/services';

@Injectable()
export class NominaService extends CrudBase {

    constructor(protected _cl: CallService, protected _rt: Router) {
        super(_cl, _rt);
        this.setListUrl('nomina/historial/');
        this.setRedirectUrl('/nomina');
    }

}
