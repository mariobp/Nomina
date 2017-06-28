import { Component, OnInit, ViewChild, AfterViewInit } from '@angular/core';
import { Router } from '@angular/router';
import { FormGroup, FormControl, Validators, FormBuilder } from '@angular/forms';
import { TableComponent, RenderInput, FormComponent } from '../../../lib/components';
import { AsistenteService } from './asistente.service';

declare var $: any;

@Component({
    template: '<router-outlet></router-outlet>'
})
export class AsistenteComponent { }

@Component({
    template: `<ex-form #f icon="supervisor_account" title="Asistente"
        [form]="form"
        [service]="service"
        [columns]="columns"
        [renderinputs]="renderinputs"></ex-form>`
})
export class AsistenteEditComponent implements AfterViewInit {

    form: FormGroup;
    columns: string[];
    renderinputs: RenderInput[];
    service = this._as;

    @ViewChild('f') private _form: FormComponent;

    constructor(private _fb: FormBuilder, private _as: AsistenteService, private _rt: Router) {
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

    ngAfterViewInit() {
        this._form.successful = data => {
            this._rt.navigate(['usuarios/asistente']);
        }
    }
}

@Component({
    templateUrl: './list.asistente.component.html'
})
export class AsistenteListComponent {
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
        {
            className: 'text-center',
            orderable: false,
            searchable: false,
            data: 'imagen',
            render: TableComponent.renderAvatar
        },
        { data: 'username' },
        { data: 'first_name' },
        { data: 'last_name' },
        { data: 'identificacion' },
        { data: 'email' },
        { data: 'telefono' }
    ];

    constructor(private _as: AsistenteService) { }
}
