import { NgModule } from '@angular/core';
import { RouterModule } from '@angular/router';
import { CommonModule } from '@angular/common';
import { FormsModule, ReactiveFormsModule } from '@angular/forms';
import { MdAutocompleteModule, MdInputModule } from '@angular/material';
import { LibModule } from '../../lib/lib.module';

import { ContratoComponent, EditContratoComponent, ContratoListComponent } from './contrato/contrato.component';
import { FiniquitoComponent } from './finiquito/finiquito.component';
import { EmpleadoComponent, EmpleadoEditComponent, EmpleadoListComponent } from './empleado/empleado.component';

import { EmpleadoService } from './empleado/empleado.service';
import { CompensacionService } from '../obligaciones/compensacion/compensacion.service';
import { CesantiasService } from '../obligaciones/cesantias/cesantias.service';
import { PensionService } from '../obligaciones/pension/pension.service';
import { EpsService } from '../obligaciones/eps/eps.service';
import { ContratoService } from './contrato/contrato.service';

import { EmpleadoRoutes } from './route';

@NgModule({
    imports: [
        LibModule,
        FormsModule,
        CommonModule,
        MdInputModule,
        ReactiveFormsModule,
        MdAutocompleteModule,
        RouterModule.forChild(EmpleadoRoutes)
    ],
    declarations: [
        ContratoComponent,
        EditContratoComponent,
        ContratoListComponent,
        FiniquitoComponent,
        EmpleadoComponent,
        EmpleadoListComponent,
        EmpleadoEditComponent
    ],
    providers: [
        EmpleadoService,
        CompensacionService,
        CesantiasService,
        PensionService,
        EpsService,
        ContratoService
    ]
})
export class EmpleadosModule { }
