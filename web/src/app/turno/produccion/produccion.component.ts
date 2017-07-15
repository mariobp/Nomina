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
    columns = [
        {
            className: 'text-center',
            orderable: false,
            searchable: false,
            data: 'id',
            render: TableComponent.renderCheckRow
        },
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
    cargoFilter = false;
    private produccion: any;
    public auto = false;
    params = {};

    @ViewChild('f') public _form: FormComponent;
    @ViewChild('multi') private _multi: MultiComponent;

    constructor(private _fb: FormBuilder, private _s: ProduccionService, public _e: EmpleadoService,
        public _u: UnidadProduccionService, public _c: CargoService, private _rt: Router, private _r: ActivatedRoute) {
        this.form = this._fb.group({
            unidad: [[], Validators.required],
            empleados: [[], Validators.required],
            cantidad: ['', [Validators.required, Validators.min(0)]],
            concepto__nombre: ['', Validators.required]
        });
        this.columns = ['col1'];
        this.renderinputs = [
            { column: 'col1', title: 'Cantidad', type: 'text', name: 'cantidad' },
            { column: 'col1', title: 'Concepto', type: 'text', name: 'concepto__nombre' },

        ];
        if (!!this._r.snapshot.data['item'] && Object.keys(this._r.snapshot.data['item']).length !== 0) {
            this.produccion = this._r.snapshot.data['item'];
            this.form.get('unidad').setValue(this.produccion.unidad);
            this.form.get('unidad').disable();
        }
    }

    empleado = item => `${item.nombre} ${item.apellidos}(${item.cargo__nombre})`;
    itemUnidad = item => `${item.unidad__nombre}`;
    itemCargo = item => `${item.nombre}`;

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

    onChange(event) {
        if (!!event.item) {
            const empleado = this.form.get('empleados');
            empleado.setValue([]);
            this.params['cargo__tarifario__unidad'] = event.item.id;
            this.empleadosList(this.params);
            if (!empleado.enabled) {
                empleado.enable();
            }
        }
    }

    onChange2(event) {
        if (!!event.item) {
            const empleado = this.form.get('empleados');
            empleado.setValue([]);
            this.params['cargo'] = event.item.id;
            this.empleadosList(this.params);
            this.cargoFilter = true;
            if (!empleado.enabled) {
                empleado.enable();
            }
        }
    }


    multiReady(event) {
        if (this.produccion) {
            this.params['cargo__tarifario__unidad'] = this.produccion.unidad;
            this.empleadosList(this.params);
        } else {
            this.form.get('empleados').disable();
        }
    }

    completeAjax(event) {
        this._form.setReady(false);
        if (this.cargoFilter) {
            this._multi.selectAll();
            this.cargoFilter = false;
        }
    }

    empleadosList(query: object) {
        this._form.setReady(true);
        this._multi.filterList(query);
    }

}
