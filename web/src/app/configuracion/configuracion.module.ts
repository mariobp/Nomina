import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { CargoComponent } from './cargo/cargo.component';
import { GeneralComponent } from './general/general.component';
import { TipocontratoComponent } from './tipocontrato/tipocontrato.component';
@NgModule({
  imports: [
    CommonModule
  ],
  declarations: [CargoComponent, TipocontratoComponent, GeneralComponent]
})
export class ConfiguracionModule { }
