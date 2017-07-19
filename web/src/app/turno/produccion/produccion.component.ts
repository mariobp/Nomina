import { Component, ViewChild, OnInit, AfterViewInit } from '@angular/core';
import { Router, ActivatedRoute } from '@angular/router';
import { FormGroup, Validators, FormBuilder } from '@angular/forms';
import { FormComponent, TableComponent, RenderInput } from '../../../lib/components'
import { ProduccionService } from './produccion.service';
import { EmpleadoService } from '../../empleados/empleado/empleado.service';
import { UnidadProduccionService } from '../../configuracion/unidadproduccion/unidadproduccion.service';
import { MultiComponent } from '../../../lib/multi/multi.component';
import { CargoService } from '../../configuracion/cargo/cargo.service';

@Component({
    template: '<router-outlet></router-outlet>'

})
export class ProduccionComponent { }


@Component({
    templateUrl: './list.produccion.component.html'
})
export class ProduccionListComponent {

    @ViewChild('table') private table: TableComponent;

    icon = 'work';
    title = 'Producción';
    service = this._as;
    multiselect = true;
    order = [[2, 'asc']]

    columns = [
        {
            className: 'text-center',
            orderable: false,
            searchable: false,
            data: 'id',
            render: TableComponent.renderCheckRow
        },
        { data: 'cargo__nombre' },
        { data: 'unidad__nombre' },
        { data: 'concepto__nombre' },
        { data: 'cantidad' },
        { data: 'fecha' },
    ]

    constructor(private _as: ProduccionService) { }


}


@Component({
    templateUrl: './edit.produccion.html'
})
export class EditProduccionComponent implements OnInit {

    form: FormGroup;
    columns: string[];
    renderinputs: RenderInput[];
    service = this._s;
    debug = false;
    unidadFilter = false;
    private produccion: any;
    public auto = false;
    placeholder = '';
    params = {};
    paramsUnidad = {};

    @ViewChild('f') public _form: FormComponent;
    @ViewChild('multi') private _multi: MultiComponent;

    constructor(private _fb: FormBuilder, private _s: ProduccionService, public _e: EmpleadoService,
        public _u: UnidadProduccionService, public _c: CargoService, private _rt: Router, private _r: ActivatedRoute) {
        this.form = this._fb.group({
            cargo: [[]],
            unidad: [{ value: [], disabled: true }, Validators.required],
            empleados: [[], Validators.required],
            cantidad: ['', [Validators.required, Validators.min(0)]],
            concepto__nombre: ['', Validators.required],
            fecha: ['', Validators.required]
        });
        this.columns = ['col1'];
        this.renderinputs = [
            { column: 'col1', title: 'Cantidad', type: 'text', name: 'cantidad' },
            { column: 'col1', title: 'Concepto', type: 'text', name: 'concepto__nombre' },
            { column: 'col1', title: 'Fecha', type: 'text', name: 'fecha', class: 'datetimepicker' },


        ];
        if (!!this._r.snapshot.data['item'] && Object.keys(this._r.snapshot.data['item']).length !== 0) {
            this.produccion = this._r.snapshot.data['item'];
            this.form.get('cargo').disable();
        }
    }

    empleado = item => `${item.nombre} ${item.apellidos}(${item.cargo__nombre})`;
    itemUnidad = item => `${item.unidad__nombre}`;
    itemCargo = item => `${item.cargo__nombre}`;

    ngOnInit() {
        this._form.successful = data => {
            this._rt.navigate(['produccion/produccion']);
        }

        this._form.preSave = data => {

            if (this.produccion) {
                const datos = data;
                datos['unidad'] = this.produccion.unidad
            }
            return data;
        }
    }

    onChangeUnidad(event) {
        const empleado = this.form.get('empleados');
        this.cleanEmpleado();
        if (!!event.item) {
            this.params['cargo__tarifario__unidad'] = event.item.id;
            this.empleadosList(this.params);
            this.placeholder = 'Seleccione los empleados';
            if (!empleado.enabled) {
                empleado.enable();
            }
        }
    }

    onChangeCargo(event) {
        if (!!event.item) {
            const unidad = this.form.get('unidad');
            this.cleanEmpleado();
            unidad.setValue([]);
            this.placeholder = '';
            this.params = {};
            this.params['cargo'] = event.item.id;
            this.paramsUnidad['tarifario__cargo'] = event.item.id;
            if (!unidad.enabled) {
                unidad.enable();
            }

        }
    }

    cleanEmpleado() {
        const empleado = this.form.get('empleados');
        empleado.setValue([]);
        this._multi.todos = false;
        if (empleado.enabled) {
            empleado.disable();
        }
    }

    multiReady(event) {
        if (this.produccion) {
            this.params['cargo__tarifario__unidad'] = this.produccion.unidad;
            this.params['cargo'] = this.produccion.cargo;
            this.empleadosList(this.params);
        } else {
            this.form.get('empleados').disable();
        }
    }

    completeAjax(event) {
        this._form.setReady(false);
        if (this.unidadFilter) {
            this._multi.selectAll();
            this.unidadFilter = false;
        }
    }

    empleadosList(query: object) {
        this._form.setReady(true);
        this.unidadFilter = true;
        this._multi.filterList(query);
    }

}
