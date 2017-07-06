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
        EmpleadoService, ContratoService
    ]
})
export class EmpleadosModule { }
