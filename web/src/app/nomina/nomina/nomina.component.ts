import { Component, OnInit, ViewChild, AfterViewInit } from '@angular/core';
import { Router } from '@angular/router';
import { FormGroup, FormControl, Validators, FormBuilder } from '@angular/forms';
import { TableComponent, RenderInput, FormComponent } from '../../../lib/components';
import { NominaService } from './nomina.service';

declare var $: any;
declare var window: any;

@Component({
    template: '<router-outlet></router-outlet>',
    styleUrls: ['./nomina.component.scss']
})
export class NominaComponent { }

@Component({
    templateUrl: './list.nomina.component.html'
})
export class NominaListComponent implements OnInit {
    service = this._as;
    multiselect = true;
    aggregable = false;
    editable = false;
    deleteable = false;
    order = [[2, 'asc']]

    @ViewChild('table') private table: TableComponent;

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
            data: 'id',
            render: (data, type, full, meta) => {
                return `<a style="cursor: pointer;"class="down" data-down="${data}" data-empleado="${full.empleado_f.nombre} ${full.empleado_f.apellidos}">
                    <i class="material-icons">file_download</i>
                </a>`;
            }
        },
        {
            data: 'empleado',
            render: (data, type, full, meta) => {
                return `${full.empleado_f.nombre} ${full.empleado_f.apellidos}`;
            }
        },
        {
            data: 'salario_base',
            render: TableComponent.renderDecimal
        },
        {
            data: 'salario_produccion',
            orderable: false,
            searchable: false,
            render: TableComponent.renderDecimal
        },
        {
            data: 'salario_legal',
            orderable: false,
            searchable: false,
            render: TableComponent.renderDecimal
        },
        {
            data: 'recargos',
            orderable: false,
            searchable: false,
            render: TableComponent.renderDecimal
        },
        {
            data: 'bonificacion',
            orderable: false,
            searchable: false,
            render: TableComponent.renderDecimal
        },
        {
            data: 'subsidio_trasporte',
            orderable: false,
            searchable: false,
            render: TableComponent.renderDecimal
        },
        {
            data: 'prestaciones_sociales',
            orderable: false,
            searchable: false,
            render: TableComponent.renderDecimal
        },
        {
            data: 'descuento_salud',
            orderable: false,
            searchable: false,
            render: TableComponent.renderDecimal
        },
        {
            data: 'neto',
            orderable: false,
            searchable: false,
            render: TableComponent.renderDecimal
        },
        {
            data: 'total',
            orderable: false,
            searchable: false,
            render: TableComponent.renderDecimal
        },
    ];
    /*
        nombre empleado
        salario base
    */

    constructor(private _as: NominaService) { }

    ngOnInit() {
        this.table.drawCallback = () => {
            $('.down').click(function(e) {
                e.preventDefault();
                const url = `${window._server}/admin/nomina/nomina/export/free/?id=${$(this).attr('data-down')}`;
                const empelado = $(this).attr('data-empleado')
                $.ajax({
                    url: url,
                    method: 'POST',
                    data: { file_format: 0 },
                    xhrFields: {
                        withCredentials: true
                    },
                    success: function(data) {
                        const blob = new Blob([data]);
                        const link = document.createElement('a');
                        const date = new Date();
                        link.href = window.URL.createObjectURL(blob);
                        link.download = `Finiquito_${empelado}_${date.toLocaleDateString('es-CO')}.pdf`;
                        link.click();
                    }
                });
            });
        }
    }
}


@Component({
    template: `<ex-form #f icon="assignment_ind" title="Nomina"
        [form]="form"
        [service]="service"
        [columns]="columns"
        [renderinputs]="renderinputs"></ex-form>`
})
export class NominaEditComponent implements AfterViewInit {

    form: FormGroup;
    columns: string[];
    renderinputs: RenderInput[];
    service = this._s;

    @ViewChild('f') private _form: FormComponent;

    constructor(private _fb: FormBuilder, private _s: NominaService, private _rt: Router) {
        this.form = this._fb.group({
            aprobado: [false, [Validators.required]],
            nomina: [[], [Validators.required]],
            entrada: ['', [Validators.required]],
            salida: ['', [Validators.required]],
            h_diurna: [{ value: 0, disabled: true }],
            h_dominical: [{ value: 0, disabled: true }],
            h_extras: [{ value: 0, disabled: true }],
            h_nocturna: [{ value: 0, disabled: true }],
        });
        this.columns = ['col1', 'col2'];
        this.renderinputs = [
            { column: 'col1', title: 'Nomina', type: 'text', name: 'nomina' },
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
