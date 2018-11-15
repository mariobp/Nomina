import { Component, OnInit, ViewChild } from '@angular/core';
import { Router } from '@angular/router';
import { FormGroup, Validators, FormBuilder } from '@angular/forms';
import { TableComponent, RenderInput, FormComponent } from '../../../lib/components';
import { TurnoService } from './turno.service';
import { BsNotify } from '../../../lib/bs.notify';
import { EmpleadoService } from '../../empleados/empleado/empleado.service';
import 'rxjs/add/operator/startWith';
import 'rxjs/add/operator/map';

declare var swal: any;

@Component({
    template: '<router-outlet></router-outlet>',
    styleUrls: ['./turno.component.scss']
})
export class TurnoComponent { }

@Component({
    templateUrl: './list.turno.component.html'
})
export class TurnoListComponent {
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
            data: 'empleado',
            render: (data, type, full, meta) => {
                return `<a href="#/empleados/${data}/edit/">${full.empleado__nombre} ${full.empleado__apellidos}</a>`;
            }
        },
        { data: 'entrada', className: 'text-center' },
        { data: 'salida', className: 'text-center' },
        {
            data: 'h_diurna',
            orderable: false,
            searchable: false,
            className: 'text-center',
            render: TableComponent.renderDecimal
        },
        {
            data: 'h_extras',
            orderable: false,
            searchable: false,
            className: 'text-center',
            render: TableComponent.renderDecimal
        },
        {
            data: 'h_nocturna',
            orderable: false,
            searchable: false,
            className: 'text-center',
            render: TableComponent.renderDecimal
        },
        {
            data: 'h_nocturna_extras',
            orderable: false,
            searchable: false,
            className: 'text-center',
            render: TableComponent.renderDecimal
        },
        {
            data: 'h_dominical',
            orderable: false,
            searchable: false,
            className: 'text-center',
            render: TableComponent.renderDecimal
        },
        {
            data: 'h_dominical_extra',
            orderable: false,
            searchable: false,
            className: 'text-center',
            render: TableComponent.renderDecimal
        },
        {
            data: 'h_dominical_nocturna',
            orderable: false,
            searchable: false,
            className: 'text-center',
            render: TableComponent.renderDecimal
        },
        {
            data: 'h_dominical_extra_nocturna',
            orderable: false,
            searchable: false,
            className: 'text-center',
            render: TableComponent.renderDecimal
        }
    ];

    constructor(private _as: TurnoService) { }
}
;

@Component({
    templateUrl: './edit.turno.component.html'
})
export class TurnoEditComponent implements OnInit {

    form: FormGroup;
    columns: string[];
    renderinputs: RenderInput[];
    service = this._s;
    isUpdated = false;

    @ViewChild('f') public _form: FormComponent;

    options: any[] = [];

    constructor(
        private _fb: FormBuilder,
        private _s: TurnoService,
        private _rt: Router,
        private _es: EmpleadoService,
        ) {
        this.form = this._fb.group({
            aprobado: [false, [Validators.required]],
            empleado: ['', [Validators.required, Validators.pattern(/\d/)]],
            entrada: ['', [Validators.required]],
            salida: ['', []],
            descontar_almuerzo: [true, []],
            h_diurna: [{ value: 0, disabled: true }],
            h_dominical: [{ value: 0, disabled: true }],
            h_extras: [{ value: 0, disabled: true }],
            h_nocturna: [{ value: 0, disabled: true }],
            h_dominical_extra: [{ value: 0, disabled: true }],
            h_dominical_extra_nocturna: [{ value: 0, disabled: true }],
            h_dominical_nocturna: [{ value: 0, disabled: true }],
            h_nocturna_extras: [{ value: 0, disabled: true }]
        });
        this.columns = ['col1', 'col2'];
        this.renderinputs = [
            { column: 'col1', title: 'Hora de entrada', type: 'text', name: 'entrada', class: 'datetimepicker' },
            { column: 'col1', title: 'Hora de salida', type: 'text', name: 'salida', class: 'datetimepicker' },
            { column: 'col1', title: 'Descontar hora de almuerzo', type: 'checkbox', name: 'descontar_almuerzo' },
            { column: 'col2', title: 'Horas diurnas', type: 'number', name: 'h_diurna', step: '2' },
            { column: 'col2', title: 'Horas nocturnas', type: 'number', name: 'h_nocturna', step: '2' },
            { column: 'col2', title: 'Horas extras', type: 'number', name: 'h_extras', step: '2' },
            { column: 'col2', title: 'Horas dominicales', type: 'number', name: 'h_nocturna_extras', step: '2' },
            { column: 'col2', title: 'Horas dominicales', type: 'number', name: 'h_dominical', step: '2' },
            { column: 'col2', title: 'Horas dominicales extras', type: 'number', name: 'h_dominical_extra', step: '2' },
            { column: 'col2', title: 'Horas dominicales nocturnas', type: 'number', name: 'h_dominical_nocturna', step: '2' },
            { column: 'col2', title: 'Horas dominicales nocturnas extras ', type: 'number', name: 'h_dominical_extra_nocturna', step: '2' },
        ];
        this.form.get('empleado').valueChanges
            .startWith(null)
            .subscribe(name => {
                if (this.isUpdated) {
                    this.filterVal('');
                } else {
                    this.filterVal(name);
                }
            });
    }

    aprobate() {
        swal({
            title: 'Estás seguro de aprobar este turno? ',
            text: `Una vez aprobado el turno no sera modificable.`,
            type: 'warning',
            showCancelButton: true,
            confirmButtonColor: '#213b78',
            cancelButtonColor: '#ff9800',
            cancelButtonText: 'Cancelar',
            confirmButtonText: 'Aprobar'
        }).then(() => {
            this.form.get('aprobado').setValue(true);
            this._form.save();
        }, () => { });
    }
    ngOnInit() {
        this._form.prePatchValue = data =>  this.setData(data);

        this._form.successful = data => {
            if (data && data._body !== '') {
                const item = this._form.item;
                const info = data.json();
                if (item) {
                    this.isUpdated = true;
                    this._form.setItem(info);
                } else {
                    const url = `/operacion/turno/${info.id}/edit`;
                    this._rt.navigate(['operacion', 'redirect'], { queryParams: { url }});
                }
            }
        }

        this._form.back = () => {
            this._rt.navigate(['/produccion/turno']);
        }

        this._form.error = data => {
            this.form.get('aprobado').setValue(false);
        }
    }

    filterVal(val) {
        this._es.list({ q: val ? val : '' })
            .then(data => data.json())
            .then(data => { this.options = data.object_list })
            .catch(error => console.log(error));
    }

    displayFn = val => {

        if (this.options.length === 0 && !!this._form.item) {
            return `${this._form.item.empleado__nombre} ${this._form.item.empleado__apellidos}`;
        }else if (!!this._form.item) {
            return `${this._form.item.empleado__nombre} ${this._form.item.empleado__apellidos}`;
        } else {
            const value = this.options.filter(data => data.id === val)[0];
            return val ? (value ? `${value.nombre} ${value.apellidos}` : '') : null;
        }
    }

    private setData(data): any {
        this._form.deleteable = !data.aprobado;
        this._form.saveable = !data.aprobado;
        if (!!data.empleado_id) {
            data.empleado__nombre = data.empleado;
            data.empleado__apellidos = '';
            data.empleado = data.empleado_id;
        }
        return data;
    }
}
