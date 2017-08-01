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
import { DescuentoComponent, DescuentoListComponent, EditDescuentoComponent } from './descuento/descuento.component';
import { DescuentoService } from '../turno/descuento/descuento.service';
import { IncapacidadComponent, EditIncapacidadComponent, IncapacidadListComponent } from './incapacidad/incapacidad.component';
import { IncapacidadService } from './incapacidad/incapacidad.service';
import { TipoIncapacidadService } from '../incapacidad/tipo/tipo.incapacidad.service';

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
        EditProduccionComponent,
        DescuentoComponent,
        DescuentoListComponent,
        EditDescuentoComponent,
        IncapacidadComponent,
        EditIncapacidadComponent,
        IncapacidadListComponent
    ],
    providers: [
        TurnoService,
        EmpleadoService,
        ProduccionService,
        UnidadProduccionService,
        CargoService,
        DescuentoService,
        IncapacidadService,
        TipoIncapacidadService
    ]
})
export class TurnoModule { }
