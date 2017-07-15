import { Component, OnInit, ViewChild, Input } from '@angular/core';
import { Router } from '@angular/router';
import { FormGroup, FormControl, Validators, FormBuilder } from '@angular/forms';
import { TableComponent, RenderInput, FormComponent } from '../../../lib/components';

import { EmpleadoService } from './empleado.service';
import { CompensacionService } from '../../obligaciones/compensacion/compensacion.service';
import { CesantiasService } from '../../obligaciones/cesantias/cesantias.service';
import { PensionService } from '../../obligaciones/pension/pension.service';
import { EpsService } from '../../obligaciones/eps/eps.service';
import { CargoService } from '../../configuracion/cargo/cargo.service';
import { BancoService } from '../../configuracion/banco/banco.service';

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
    deleteable = false
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
        { data: 'banco__nombre' },
        { data: 'numero' },
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
export class EmpleadoEditComponent implements OnInit {

    form: FormGroup;
    columns: string[];
    renderinputs: RenderInput[];
    service = this._s;
    cajacompensacions = [];
    deleteable = false;
    @Input('empleado') empleado: number;
    @ViewChild('f') public _form: FormComponent;

    constructor(private _fb: FormBuilder, private _s: EmpleadoService, private _rt: Router,
        public _cs: CompensacionService, public _ces: CesantiasService, public _es: EpsService, public _ps: PensionService,
        public _cas: CargoService, public _b: BancoService) {
        this.form = this._fb.group({
            nombre: ['', Validators.required],
            apellidos: ['', Validators.required],
            cedula: ['', [Validators.required, Validators.min(0)]],
            fecha_nacimiento: ['', [Validators.required]],
            cargo: [[], [Validators.required, Validators.pattern(/\d/)]],
            cajacompensacion: [[], [Validators.required, Validators.pattern(/\d/)]],
            cesantia: [[], [Validators.required, Validators.pattern(/\d/)]],
            eps: [[], [Validators.required, Validators.pattern(/\d/)]],
            pension: [[], [Validators.required, Validators.pattern(/\d/)]],
            banco: [[], [Validators.required, Validators.pattern(/\d/)]],
            numero: ['', [Validators.required, Validators.min(0)]],

        });
        this.columns = ['col1', 'col2'];
        this.renderinputs = [
            { column: 'col1', title: 'Nombre', type: 'text', name: 'nombre' },
            { column: 'col1', title: 'Apellidos', type: 'text', name: 'apellidos', },
            { column: 'col2', title: 'Cedula', type: 'number', name: 'cedula' },
            { column: 'col2', title: 'Fecha nacimiento', type: 'text', name: 'fecha_nacimiento', class: 'datepicker' },
        ];
    }

    ngOnInit() {
        this._form.back = () => {
            this._rt.navigate(['empleados']);
        }
        this._form.successful = data => {
            const item = data.json();
            this._rt.navigate([`empleados/${item.id}/edit`]);
        }
    }

    itemCaja = item => item.cajacompensacion__nombre;
    itemCargo = item => item.cargo__nombre;
    itemCesantia = item => item.cesantia__nombre;
    itemEps = item => item.eps__nombre;
    itemPension = item => item.pension__nombre;
    itemBanco = item => item.banco__nombre;
}
