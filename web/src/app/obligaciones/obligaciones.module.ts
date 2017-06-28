import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { LibModule } from '../../lib/lib.module';
import { FormsModule, ReactiveFormsModule } from '@angular/forms';
import { RouterModule } from '@angular/router';

import { PensionComponent, PensionListComponent, EditPensionComponent } from './pension/pension.component';
import { EpsComponent, EpsListComponent, EditEpsComponent } from './eps/eps.component';
import { CompensacionComponent, CompensacionListComponent, EditCompensacionComponent } from './compensacion/compensacion.component';
import { CesantiasComponent, CesantiasListComponent, EditCesantiasComponent } from './cesantias/cesantias.component';

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
      EditPensionComponent,
      EpsComponent,
      EpsListComponent,
      EditEpsComponent,
      CompensacionComponent,
      CompensacionListComponent,
      EditCompensacionComponent,
      CesantiasComponent,
      CesantiasListComponent,
      EditCesantiasComponent
    ],
    providers: [PensionService, EpsService, CompensacionService, CesantiasService]
})
export class ObligacionesModule { }
