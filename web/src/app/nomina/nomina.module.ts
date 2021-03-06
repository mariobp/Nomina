import { NgModule } from '@angular/core';
import { RouterModule } from '@angular/router';
import { CommonModule } from '@angular/common';
import { FormsModule, ReactiveFormsModule } from '@angular/forms';
import { MdAutocompleteModule, MdInputModule } from '@angular/material';
import { LibModule } from '../../lib/lib.module';
import { HttpModule } from '@angular/http';

import { NominaComponent, NominaListComponent } from './nomina/nomina.component';
import { CorteComponent, CorteListComponent, CorteEditComponent } from './corte/corte.component';
import { DescuentoComponent, DescuentoListComponent, DescuentoEditComponent } from './descuento/descuento.component';

import { NominaService } from './nomina/nomina.service';
import { CorteService } from './corte/corte.service';
import { DescuentoService } from './descuento/descuento.service';
import { ContratoService } from '../empleados/contrato/contrato.service';

import { NominaRoutes } from './route';
@NgModule({
    imports: [
        LibModule,
        HttpModule,
        FormsModule,
        CommonModule,
        MdInputModule,
        ReactiveFormsModule,
        MdAutocompleteModule,
        RouterModule.forChild(NominaRoutes)
    ],
    declarations: [
        NominaComponent,
        NominaListComponent,
        CorteComponent,
        CorteListComponent,
        CorteEditComponent,
        DescuentoComponent,
        DescuentoListComponent,
        DescuentoEditComponent,
    ],
    providers: [
        NominaService,
        CorteService,
        DescuentoService,
        ContratoService
    ]
})
export class NominaModule { }
