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
    editable = false;
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
            aprobado: [false, [Validators.required]],
            empleado: [[], [Validators.required]],
            entrada: ['', [Validators.required]],
            salida: ['', [Validators.required]],
            h_diurna: [{ value: 0, disabled: true }],
            h_dominical: [{ value: 0, disabled: true }],
            h_extras: [{ value: 0, disabled: true }],
            h_nocturna: [{ value: 0, disabled: true }],
        });
        this.columns = ['col1', 'col2'];
        this.renderinputs = [
            { column: 'col1', title: 'Empleado', type: 'text', name: 'empleado' },
            { column: 'col1', title: 'Hora de entrada', type: 'text', name: 'entrada', class: 'datetimepicker' },
            { column: 'col1', title: 'Hora de salida', type: 'text', name: 'salida', class: 'datetimepicker' },
            { column: 'col2', title: 'Horas diurnas', type: 'number', name: 'h_diurna', step: '2' },
            { column: 'col2', title: 'Horas nocturnas', type: 'number', name: 'h_nocturna', step: '2' },
            { column: 'col2', title: 'Horas extras', type: 'number', name: 'h_extras', step: '2' },
            { column: 'col2', title: 'Horas dominicales', type: 'number', name: 'h_dominical', step: '2' },
        ];
    }

    ngAfterViewInit() { }
}
