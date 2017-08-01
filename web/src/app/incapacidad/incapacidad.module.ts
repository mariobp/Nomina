import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { RouterModule } from '@angular/router';
import { LibModule } from '../../lib/lib.module';
import { FormsModule, ReactiveFormsModule } from '@angular/forms';
import { TipoIncapacidadComponent, TipoIncapacidadListComponent, TipoIncapacidadEditComponent } from './tipo/tipo.incapacidad.component';
import { PagoIncapacidadComponent, PagoIncapacidadListComponent, PagoIncapacidadEditComponent } from './pago/pago.incapacidad.component';
import { TipoIncapacidadService } from './tipo/tipo.incapacidad.service';
import { PagoIncapacidadService } from './pago/pago.incapacidad.service'
import { IncapacidadRoutes } from './route';
@NgModule({
    imports: [
        LibModule,
        FormsModule,
        CommonModule,
        ReactiveFormsModule,
        RouterModule.forChild(IncapacidadRoutes)
    ],
    declarations: [
        TipoIncapacidadComponent,
        TipoIncapacidadListComponent,
        TipoIncapacidadEditComponent,
        PagoIncapacidadComponent,
        PagoIncapacidadEditComponent,
        PagoIncapacidadListComponent
    ],
    providers: [
        TipoIncapacidadService,
        PagoIncapacidadService
    ]
})
export class IncapacidadModule { }
