import { NgModule } from '@angular/core';
import { RouterModule } from '@angular/router';
import { CommonModule } from '@angular/common';
import { FormsModule, ReactiveFormsModule } from '@angular/forms';
import { MdAutocompleteModule, MdInputModule } from '@angular/material';

import { LibModule } from '../../lib/lib.module';
import { TurnoComponent, TurnoEditComponent, TurnoListComponent } from './turno/turno.component';
import { TurnoService } from './turno/turno.service';
import { EmpleadoService } from '../empleados/empleado/empleado.service';
import { TurnoRoutes } from './route';

@NgModule({
    imports: [
        LibModule,
        FormsModule,
        CommonModule,
        MdInputModule,
        ReactiveFormsModule,
        MdAutocompleteModule,
        RouterModule.forChild(TurnoRoutes)
    ],
    declarations: [
        TurnoComponent,
        TurnoEditComponent,
        TurnoListComponent
    ],
    providers: [
        TurnoService,
        EmpleadoService
    ]
})
export class TurnoModule { }
