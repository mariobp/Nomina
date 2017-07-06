import { NgModule } from '@angular/core';
import { RouterModule } from '@angular/router';
import { CommonModule } from '@angular/common';
import { FormsModule, ReactiveFormsModule } from '@angular/forms';
import { MdAutocompleteModule, MdInputModule } from '@angular/material';
import { LibModule } from '../../lib/lib.module';
import { HttpModule } from '@angular/http';

import { NominaComponent, NominaEditComponent, NominaListComponent } from './nomina/nomina.component';
import { NominaService } from './nomina/nomina.service';
import { NominaRoutes } from './route';
@NgModule({
    imports: [
        LibModule,
        HttpModule,
        FormsModule,
        CommonModule,
        MdInputModule,
        ReactiveFormsModule,
        MdAutocompleteModule,
        RouterModule.forChild(NominaRoutes)
    ],
    declarations: [
        NominaComponent,
        NominaEditComponent,
        NominaListComponent
    ],
    providers: [
        NominaService
    ]
})
export class NominaModule { }
