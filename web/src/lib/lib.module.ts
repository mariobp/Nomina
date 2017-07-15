import { NgModule, CUSTOM_ELEMENTS_SCHEMA} from '@angular/core';
import { RouterModule } from '@angular/router';
import { CommonModule } from '@angular/common'
import { FormsModule, ReactiveFormsModule } from '@angular/forms';
import { MdAutocompleteModule, MdInputModule, MdCheckboxModule, MdSelectModule, MdButtonModule } from '@angular/material';
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
import { AutoComponent } from './auto/auto.component';
import { MultiComponent } from './multi/multi.component';
import { MigaComponent } from './miga/miga.component';

const LibComponents = [
    AutoComponent,
    P404Component,
    BaseComponent,
    CardComponent,
    LoaderComponent,
    SidebarComponent,
    ToolbarComponent,
    TableComponent,
    FormComponent,
    NavbarComponent,
    MultiComponent,
    MigaComponent
];

@NgModule({
    imports: [
        RouterModule,
        CommonModule,
        FormsModule,
        ReactiveFormsModule,
        MdAutocompleteModule,
        MdCheckboxModule,
        MdInputModule,
        MdSelectModule,
        MdButtonModule
    ],
    declarations: LibComponents,
    exports: LibComponents
})
export class LibModule { }
