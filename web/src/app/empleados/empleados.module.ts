import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { ContratoComponent } from './contrato/contrato.component';
import { FiniquitoComponent } from './finiquito/finiquito.component';

@NgModule({
  imports: [
    CommonModule
  ],
  declarations: [ContratoComponent, FiniquitoComponent]
})
export class EmpleadosModule { }
