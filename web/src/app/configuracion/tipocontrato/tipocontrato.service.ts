import { Injectable } from '@angular/core';
import { Router } from '@angular/router';
import { CallService, CrudService } from '../../../lib/services';

@Injectable()
export class TipoContratoService extends CrudService {
    constructor(protected _cl: CallService, protected _rt: Router) {
        super(_cl, _rt, 'recursos/tipo/contrato/');
        super.setRedirectUrl('/configuracion/tipo/contrato');
    }
}
