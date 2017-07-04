import { NgModule, CUSTOM_ELEMENTS_SCHEMA} from '@angular/core';
import { RouterModule } from '@angular/router';
import { CommonModule } from '@angular/common'
import { FormsModule, ReactiveFormsModule } from '@angular/forms';
import { MdAutocompleteModule, MdInputModule } from '@angular/material';

import { ToolbarComponent } from './toolbar/toolbar.component';
import { SidebarComponent } from './sidebar/sidebar.component';
import { LoaderComponent } from './loader/loader.component';
import { CardComponent} from './card/card.component';
import { BaseComponent } from './base/base.component';
import { P404Component } from './404/404.component';
import { TableComponent } from './table/table.component';
import { BsNotify } from './bs.notify';
import { FormComponent} from './form/form.component'
import { NavbarComponent } from './navbar/navbar.component'

const LibComponents = [
    P404Component,
    BaseComponent,
    CardComponent,
    LoaderComponent,
    SidebarComponent,
    ToolbarComponent,
    TableComponent,
    FormComponent,
    NavbarComponent
];

@NgModule({
    imports: [
        RouterModule,
        CommonModule,
        FormsModule,
        ReactiveFormsModule,
        MdAutocompleteModule,
        MdInputModule,
    ],
    declarations: LibComponents,
    exports: LibComponents
})
export class LibModule { }
