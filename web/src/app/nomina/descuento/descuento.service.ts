import { Injectable } from '@angular/core';
import { Router } from '@angular/router';
import { CallService, CrudService } from '../../../lib/services';
import { SampleComponent } from 'ex-componentex';

@Injectable()
export class DescuentoService extends CrudService {

    constructor(protected _cl: CallService, protected _rt: Router) {
        super(_cl, _rt, 'nomina/descuento/');
        this.setRedirectUrl('/nomina')
    }

}
