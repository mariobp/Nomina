import { Component, OnInit, ViewChild, AfterViewInit } from '@angular/core';
import { Router, ActivatedRoute } from '@angular/router';
import { FormGroup, FormControl, Validators, FormBuilder } from '@angular/forms';
import { RenderInput, FormComponent, TableComponent } from '../../../lib/components';
import { ContratoService } from './contrato.service';
import { TipoContratoService } from '../../configuracion/tipocontrato/tipocontrato.service';

@Component({
    template: '<router-outlet></router-outlet>',
})
export class ContratoComponent {
}

@Component({
    templateUrl: './list.contrato.component.html'
})
export class ContratoListComponent implements OnInit {

    @ViewChild('table') private table: TableComponent;

    private empleado: any;
    multiselect = true;
    visibility = true;
    aggregable = true;
    icon = 'description';
    title = 'Contrato';
    service = this._cs;
    redirect = '0/edit/';
    columns = [
        {
            className: 'text-center',
            orderable: false,
            searchable: false,
            data: 'id',
            render: TableComponent.renderCheckRow
        },
        { data: 'tipo_contrato__nombre' },
        { data: 'salario_base' },
        { data: 'subsidio_transporte' },
        { data: 'fecha_inicio' },
        {
            data: 'fecha_finalizacion',
            render: (data, type, full, meta) => {
                if (!data) {
                    return '-';
                }
                return data;
            }
        },
        {
            data: 'descanso_turno',
            render: (data, type, full, meta) => {
                if (data) {
                    return 'Si';
                }
                return 'No';
            }
        },
        { data: 'inicio_descanso' },
        { data: 'duracion_descanso' },
        { data: 'horas_trabajo' },
        { data: 'horas_trabajo_semanal' },
        { data: 'horas_trabajo_corte' }
    ];
    constructor(protected _cs: ContratoService, private _r: ActivatedRoute) {
        if (!!this._r.snapshot.data['item'] && Object.keys(this._r.snapshot.data['item']).length !== 0) {
            this.empleado = this._r.snapshot.data['item'];
            this.title = `Contratos de ${this.empleado.nombre} ${this.empleado.apellidos}`;
        } else {
            this.aggregable = false;
            this.visibility = false;
        }

    }

    ngOnInit() {
        this.table.preAjax = data => {
            if (this.empleado) {
                data['empleado'] = this.empleado.id;
            }
            return data;
        }
    }

}

@Component({
    templateUrl: './edit.contrato.component.html'
})
export class EditContratoComponent implements OnInit {

    private empleado: any;
    form: FormGroup;
    columns: string[];
    renderinputs: RenderInput[];
    service = this._s;

    @ViewChild('f') public _form: FormComponent;

    constructor(private _fb: FormBuilder, public _s: ContratoService,
        public _tc: TipoContratoService, private _rt: Router, private _r: ActivatedRoute) {
        this.form = this._fb.group({
            empleado: [0],
            tipo_contrato: [0, [Validators.required, Validators.pattern(/\d/)]],
            fecha_inicio: ['', Validators.required],
            salario_base: ['', [Validators.required, Validators.min(0)]],
            subsidio_transporte: ['', [Validators.required, Validators.min(0)]],
            descanso_turno: [false],
            inicio_descanso: ['', Validators.min(0)],
            fecha_finalizacion: ['']
        });
        this.columns = ['col1'];
        this.renderinputs = [
            { column: 'col1', title: 'Fecha inicio', type: 'text', name: 'fecha_inicio', class: 'datepicker' },
            { column: 'col1', title: 'Salario base legal', type: 'number', name: 'salario_base' },
            { column: 'col1', title: 'Subsidio de transporte', type: 'number', name: 'subsidio_transporte' },
            { column: 'col1', title: 'Descanso entre turnos', type: 'checkbox', name: 'descanso_turno' },
            { column: 'col1', title: 'Hora de inicio de descanso', type: 'number', name: 'inicio_descanso' },
            { column: 'col1', title: 'Fecha finalización', type: 'text', name: 'fecha_finalizacion', class: 'datepicker' }
        ];

        if (!!this._r.parent.snapshot.data['item'] && Object.keys(this._r.parent.snapshot.data['item']).length !== 0) {
            this.empleado = this._r.parent.snapshot.data['item'];
        }
    }

    ngOnInit() {
        this._form.preSave = data => {
            if (data.empleado === 0) {
                data.empleado = this.empleado.id;
            }
            return data;
        }
        this._form.successful = data => {
            this._rt.navigate([`empleados/${this.empleado.id}/edit`]);
        }
    }

    itemTipo = item => item.tipo_contrato__nombre;
}
