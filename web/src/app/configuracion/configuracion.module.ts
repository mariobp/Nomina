import { NgModule } from '@angular/core';
import { RouterModule } from '@angular/router';
import { CommonModule } from '@angular/common';
import { FormsModule, ReactiveFormsModule } from '@angular/forms';
import { DateValueAccessorModule } from 'angular-date-value-accessor';
import { LibModule } from '../../lib/lib.module';
import { CargoComponent, CargoListComponent } from './cargo/cargo.component';
import { TipocontratoComponent } from './tipocontrato/tipocontrato.component';
import { GeneralComponent } from './general/general.component';
import {  CargoService } from './cargo/cargo.service';
import { ConfiguracionRoutes } from './configuracion.route';

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
      TipocontratoComponent,
      GeneralComponent
    ],
    providers: [
      CargoService,
    ]
})
export class ConfiguracionModule { }
