import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { LibModule } from '../../lib/lib.module';
import { FormsModule, ReactiveFormsModule } from '@angular/forms';
import { RouterModule } from '@angular/router';

import { SaludComponent } from './salud/salud.component';
import { EpsComponent } from './eps/eps.component';
import { CompensacionComponent } from './compensacion/compensacion.component';
import { CesantiasComponent } from './cesantias/cesantias.component';

import { SaludService } from './salud/salud.service';
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
    declarations: [SaludComponent, EpsComponent, CompensacionComponent, CesantiasComponent],
    providers: [SaludService, EpsService, CompensacionService, CesantiasService]
})
export class ObligacionesModule { }
