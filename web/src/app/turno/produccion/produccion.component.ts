import { Component, ViewChild, OnInit, AfterViewInit } from '@angular/core';
import { Router, ActivatedRoute } from '@angular/router';
import { FormGroup, Validators, FormBuilder } from '@angular/forms';
import { FormComponent, TableComponent, RenderInput } from '../../../lib/components'
import { ProduccionService } from './produccion.service';
import { EmpleadoService } from '../../empleados/empleado/empleado.service';
import { UnidadProduccionService } from '../../configuracion/unidadproduccion/unidadproduccion.service';


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
        { data: 'cantidad' },
        { data: 'fecha' }
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
    private produccion: any;
    @ViewChild('f') public _form: FormComponent;
    @ViewChild('multi') private _multi: any;

    constructor(private _fb: FormBuilder, private _s: ProduccionService, public _e: EmpleadoService,
        public _u: UnidadProduccionService, private _rt: Router, private _r: ActivatedRoute) {
        this.form = this._fb.group({
            unidad: [[], Validators.required],
            empleados: [[], Validators.required],
            cantidad: ['', [Validators.required, Validators.min(0)]]
        });
        this.columns = ['col1'];
        this.renderinputs = [
            { column: 'col1', title: 'Cantidad', type: 'text', name: 'cantidad' },
        ];
        if (!!this._r.snapshot.data['item'] && Object.keys(this._r.snapshot.data['item']).length !== 0) {
            this.produccion = this._r.snapshot.data['item'];
            this.form.get('unidad').setValue(this.produccion.unidad);
            this.form.get('unidad').disable();
        }
    }
    empleado = item => `${item.nombre} ${item.apellidos}(${item.cargo__nombre})`;
    itemUnidad = item => `${item.unidad__nombre}`;

    ngOnInit() {
        if (this.produccion) {
            this._form.setReady(true);
            this.empleadosList({ cargo__tarifario__unidad: this.produccion.unidad });
        } else {
            this.form.get('empleados').disable();
        }

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
            this.form.get('empleados').setValue([]);
            this.empleadosList({ cargo__tarifario__unidad: event.item.id });
            this.form.get('empleados').enable();
        }
    }

    empleadosList(query: any) {
        Promise.all([this._e.list(query), this._multi.complete]).then(data => {
            const datos = data[0].json();
            console.log(datos);
            this._form.setReady(false);
        });
    }

}
