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
import { ProduccionComponent, ProduccionListComponent, EditProduccionComponent } from './produccion/produccion.component';
import { ProduccionService } from './produccion/produccion.service';
import { UnidadProduccionService } from '../configuracion/unidadproduccion/unidadproduccion.service';
import { CargoService } from '../configuracion/cargo/cargo.service';

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
        TurnoListComponent,
        ProduccionComponent,
        ProduccionListComponent,
        EditProduccionComponent
    ],
    providers: [
        TurnoService,
        EmpleadoService,
        ProduccionService,
        UnidadProduccionService,
        CargoService
    ]
})
export class TurnoModule { }
