import { Injectable } from '@angular/core';
import { Router } from '@angular/router';
import { CallService, CrudService } from '../../../lib/services';

@Injectable()
export class ProduccionService extends CrudService {

    constructor(protected _cl: CallService, protected _rt: Router) {
        super(_cl, _rt, 'turnos/produccion/');
        super.setRedirectUrl('/operacion/produccion');
    }

}
