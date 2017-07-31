import { Injectable } from '@angular/core';
import { Router } from '@angular/router';
import { CallService, CrudService } from '../../../lib/services';

@Injectable()
export class IncapacidadService extends CrudService {

    constructor(protected _cl: CallService, protected _rt: Router) {
        super(_cl, _rt, 'nomina/dia/incapacidad/');
        super.setRedirectUrl('/operacion/incapacidad');

    }

}
