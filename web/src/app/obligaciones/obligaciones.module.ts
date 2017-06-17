import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { SaludComponent } from './salud/salud.component';
import { EpsComponent } from './eps/eps.component';
import { CompensacionComponent } from './compensacion/compensacion.component';
import { CesantiasComponent } from './cesantias/cesantias.component';

@NgModule({
  imports: [
    CommonModule
  ],
  declarations: [SaludComponent, EpsComponent, CompensacionComponent, CesantiasComponent]
})
export class ObligacionesModule { }
