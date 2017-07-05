import { Component, OnInit, ViewChild, AfterViewInit } from '@angular/core';
import { Router } from '@angular/router';
import { FormGroup, FormControl, Validators, FormBuilder } from '@angular/forms';
import { TableComponent, RenderInput, FormComponent } from '../../../lib/components';
import { EmpleadoService } from './empleado.service';

@Component({
    template: '<router-outlet></router-outlet>',
    styleUrls: ['./empleado.component.scss']
})
export class EmpleadoComponent { }

@Component({
    templateUrl: './list.empleado.component.html'
})
export class EmpleadoListComponent {
    service = this._as;
    multiselect = true;
    aggregable = false;
    editable = true;
    columns = [
        {
            className: 'text-center',
            orderable: false,
            searchable: false,
            data: 'id',
            render: TableComponent.renderCheckRow
        },
        { data: 'nombre' },
        { data: 'apellidos' },
        { data: 'cargo__nombre' },
        { data: 'cedula' },
        {
            data: 'eps__nombre',
            orderable: false,
            searchable: false,
        },
        {
            data: 'pension__nombre',
            orderable: false,
            searchable: false,
        },
        {
            data: 'cesantia__nombre',
            orderable: false,
            searchable: false,
        },
        {
            data: 'cajacompensacion__nombre',
            orderable: false,
            searchable: false,
        },


    ];

    constructor(private _as: EmpleadoService) { }
}
;

@Component({
    template: `<ex-form #f icon="assignment_ind" title="Empleado"
        [form]="form"
        [service]="service"
        [columns]="columns"
        [renderinputs]="renderinputs"></ex-form>`
})
export class EmpleadoEditComponent implements AfterViewInit {

    form: FormGroup;
    columns: string[];
    renderinputs: RenderInput[];
    service = this._s;

    @ViewChild('f') private _form: FormComponent;

    constructor(private _fb: FormBuilder, private _s: EmpleadoService, private _rt: Router) {
        this.form = this._fb.group({
            nombre: ['', [Validators.required]],
            apellidos: ['', [Validators.required]],
            cedula: ['', [Validators.required, Validators.min(0)]],
            fecha_nacimiento: ['', [Validators.required]],
        });
        this.columns = ['col1',];
        this.renderinputs = [
            { column: 'col1', title: 'Nombre', type: 'text', name: 'nombre' },
            { column: 'col1', title: 'Apellidos', type: 'text', name: 'apellidos', },
            { column: 'col1', title: 'Cedela', type: 'number', name: 'cedula' },
            { column: 'col2', title: 'Fecha nacimiento', type: 'number', name: 'fecha_nacimiento',  class: 'datepicker' },
        ];
    }

    ngAfterViewInit() { }
}
