import { Component, OnInit, ViewChild, AfterViewInit, Input } from '@angular/core';
import { Router } from '@angular/router';
import { FormGroup, FormControl, Validators, FormBuilder } from '@angular/forms';
import { TableComponent, RenderInput, FormComponent } from '../../../lib/components';

import { EmpleadoService } from './empleado.service';
import { CompensacionService } from '../../obligaciones/compensacion/compensacion.service';
import { CesantiasService } from '../../obligaciones/cesantias/cesantias.service';
import { PensionService } from '../../obligaciones/pension/pension.service';
import { EpsService } from '../../obligaciones/eps/eps.service';
import { CargoService } from '../../configuracion/cargo/cargo.service';

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
    aggregable = true;
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

@Component({
    templateUrl: './edit.empleado.component.html'
})
export class EmpleadoEditComponent implements AfterViewInit {

    form: FormGroup;
    columns: string[];
    renderinputs: RenderInput[];
    service = this._s;
    cajacompensacions = [];
    deleteable = false;
    @Input('empleado') empleado: number;
    @ViewChild('f') private _form: FormComponent;

    constructor(private _fb: FormBuilder, private _s: EmpleadoService, private _rt: Router,
        private _cs: CompensacionService, private _ces: CesantiasService, private _es: EpsService, private _ps: PensionService,
        private _cas: CargoService) {
        this.form = this._fb.group({
            nombre: ['', Validators.required],
            apellidos: ['', Validators.required],
            cedula: ['', [Validators.required, Validators.min(0)]],
            fecha_nacimiento: ['', [Validators.required]],
            cargo: [0, [Validators.required, Validators.pattern(/\d/)]],
            cajacompensacion: [0, [Validators.required, Validators.pattern(/\d/)]],
            cesantia: [0, [Validators.required, Validators.pattern(/\d/)]],
            eps: [0, [Validators.required, Validators.pattern(/\d/)]],
            pension: [0, [Validators.required, Validators.pattern(/\d/)]]
        });
        this.columns = ['col1', 'col2'];
        this.renderinputs = [
            { column: 'col1', title: 'Nombre', type: 'text', name: 'nombre' },
            { column: 'col1', title: 'Apellidos', type: 'text', name: 'apellidos', },
            { column: 'col2', title: 'Cedula', type: 'number', name: 'cedula' },
            { column: 'col2', title: 'Fecha nacimiento', type: 'text', name: 'fecha_nacimiento', class: 'datepicker' },
        ];
    }

    ngAfterViewInit() {
        this._form.back = () => {
            this._rt.navigate(['empleados']);
        }
        this._form.successful = data => {
            console.log(data);
            this._rt.navigate([`empleados/${data.id}/edit/`]);
        }
    }

    itemCaja = item => item.cajacompensacion__nombre;
    itemCargo = item => item.cargo__nombre;
    itemCesantia = item => item.cesantia__nombre;
    itemEps = item => item.eps__nombre;
    itemPension = item => item.pension__nombre;
}
