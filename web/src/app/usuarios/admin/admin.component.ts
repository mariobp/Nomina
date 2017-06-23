import { Component, OnInit } from '@angular/core';
import {FormGroup, FormBuilder, Validators } from '@angular/forms';
import { FormComponent, TableComponent, RenderInput } from '../../../lib/components'
import { AdminService } from './admin.service';

@Component({
    template: '<router-outlet></router-outlet>',
})
export class AdminComponent { }

@Component({
    template: `<ex-form
        icon="account_circle"
        title="Administrador"
        [columns]="columns"
        [form]="form"
        [renderinputs]="renderinputs">
    </ex-form>`
})
export class EditAdminComponent {

    form: FormGroup;
    columns: string[];
    renderinputs: RenderInput[];

    constructor(private _fb: FormBuilder) {
        this.form = this._fb.group({
            username: ['', Validators.required],
            password1: ['', Validators.required],
            password2: ['', Validators.required],
            email: ['', Validators.required],
            first_name: ['', Validators.required],
            last_name: ['', Validators.required],
            identificacion: ['', Validators.required],
            fecha_nacimiento: ['', Validators.required],
            direccion: ['', Validators.required],
            telefono: ['', Validators.required],
            fijo: ['', Validators.required]
        });
        this.columns = ['col1', 'col2'];
        this.renderinputs = [
            { column: 'col2', title: 'Nombre de Usuario', type: 'text', name: 'username' },
            { column: 'col2', title: 'Contraseña', type: 'password', name: 'password1', noitem: true },
            { column: 'col2', title: 'Confirmar contraseña', type: 'password', name: 'password2', noitem: true },
            { column: 'col2', title: 'Correo', type: 'email', name: 'email' },
            { column: 'col1', title: 'Nombre', type: 'text', name: 'first_name' },
            { column: 'col1', title: 'Apellido', type: 'text', name: 'last_name' },
            { column: 'col1', title: 'Identificacion', type: 'text', name: 'identificacion' },
            { column: 'col1', title: 'Fecha de nacimiento', type: 'date', name: 'fecha_nacimiento', class: 'datetimepicker' },
            { column: 'col1', title: 'Direccion', type: 'text', name: 'direccion' },
            { column: 'col1', title: 'Celular', type: 'text', name: 'telefono' },
            { column: 'col1', title: 'Telefono', type: 'text', name: 'fijo' }
        ]
    }
}

@Component({
    templateUrl: './list.admin.component.html'
})
export class ListAdminComponent {

    service = this._as;
    multiselect = true;
    columns = [
        {
            className: 'text-center',
            orderable: false,
            searchable: false,
            data: 'id',
            render: TableComponent.renderCheckRow
        },
        { data: 'username' },
        { data: 'first_name' },
        { data: 'last_name' },
        { data: 'identificacion' },
        { data: 'email' },
        { data: 'telefono' },
    ];

    constructor(private _as: AdminService) { }
}
