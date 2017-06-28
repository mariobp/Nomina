import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { LibModule } from '../../lib/lib.module';
import { FormsModule, ReactiveFormsModule } from '@angular/forms';
import { RouterModule } from '@angular/router';

import { PensionComponent, PensionListComponent } from './pension/pension.component';
import { EpsComponent, EpsListComponent } from './eps/eps.component';
import { CompensacionComponent, CompensacionListComponent } from './compensacion/compensacion.component';
import { CesantiasComponent, CesantiasListComponent } from './cesantias/cesantias.component';

import { PensionService } from './pension/pension.service';
import { EpsService } from './eps/eps.service';
import { CompensacionService } from './compensacion/compensacion.service';
import { CesantiasService } from './cesantias/cesantias.service';

import { ObligacionesRoutes } from './route';
@NgModule({
    imports: [
        CommonModule,
        LibModule,
        FormsModule,
        ReactiveFormsModule,
        RouterModule.forChild(ObligacionesRoutes)
    ],
    declarations: [
      PensionComponent,
      PensionListComponent,
      EpsComponent,
      EpsListComponent,
      CompensacionComponent,
      CompensacionListComponent,
      CesantiasComponent,
      CesantiasListComponent
    ],
    providers: [PensionService, EpsService, CompensacionService, CesantiasService]
})
export class ObligacionesModule { }
