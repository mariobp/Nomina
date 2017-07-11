import { NgModule } from '@angular/core';
import { RouterModule } from '@angular/router';
import { CommonModule } from '@angular/common';
import { FormsModule, ReactiveFormsModule } from '@angular/forms';
import { DateValueAccessorModule } from 'angular-date-value-accessor';
import { LibModule } from '../../lib/lib.module';
import { CargoComponent, CargoListComponent, EditCargoComponent } from './cargo/cargo.component';
import { TipocontratoComponent, TipoContratoListComponent, EditTipoContratoComponent } from './tipocontrato/tipocontrato.component';
import { GeneralComponent, EditGeneralComponent } from './general/general.component';
import { CargoService } from './cargo/cargo.service';
import { ConfiguracionRoutes } from './configuracion.route';
import { TipoContratoService } from './tipocontrato/tipocontrato.service';
import { ConfiguracionService } from './general/general.service';
import { TarifarioComponent, TarifarioListComponent, EditTarifarioComponent } from './tarifario/tarifario.component';
import { UnidadproduccionComponent, UnidadProduccionListComponent, EditUnidadProduccionComponent } from './unidadproduccion/unidadproduccion.component';
import { UnidadProduccionService } from './unidadproduccion/unidadproduccion.service';
import { TarifarioService } from './tarifario/tarifario.service';

@NgModule({
    imports: [
        CommonModule,
        LibModule,
        FormsModule,
        ReactiveFormsModule,
        DateValueAccessorModule,
        RouterModule.forChild(ConfiguracionRoutes)
    ],
    declarations: [
        CargoComponent,
        CargoListComponent,
        EditCargoComponent,
        TipocontratoComponent,
        TipoContratoListComponent,
        EditTipoContratoComponent,
        GeneralComponent,
        EditGeneralComponent,
        TarifarioComponent,
        TarifarioListComponent,
        EditTarifarioComponent,
        UnidadproduccionComponent,
        UnidadProduccionListComponent,
        EditUnidadProduccionComponent
    ],
    providers: [
        CargoService, TipoContratoService, ConfiguracionService, UnidadProduccionService, TarifarioService
    ]
})
export class ConfiguracionModule { }
