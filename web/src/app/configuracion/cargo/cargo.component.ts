import { Component, ViewChild, OnInit } from '@angular/core';
import { Router } from '@angular/router';
import { FormGroup, Validators, FormBuilder } from '@angular/forms';
import { FormComponent, TableComponent, RenderInput } from '../../../lib/components'
import { CargoService } from './cargo.service';
import { UnidadProduccionService } from '../unidadproduccion/unidadproduccion.service';

@Component({
    template: '<router-outlet></router-outlet>'
})
export class CargoComponent { }

@Component({
    templateUrl: './list.cargo.component.html'
})
export class CargoListComponent {

    @ViewChild('table') private table: TableComponent;

    icon = 'turned_in';
    title = 'Cargos';
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
        { data: 'nombre' },
    ]

    constructor(private _as: CargoService) { }

    onChange($event) {
        //   console.log($event);
    }
}

@Component({
    templateUrl: './form.cargo.component.html'
})
export class EditCargoComponent implements OnInit {

    form: FormGroup;
    columns: string[];
    renderinputs: RenderInput[];
    service = this._s;
    opciones = [];
    nombre = item => item.nombre;

    @ViewChild('f') private _form: FormComponent;
    @ViewChild('multi') private _multi: any;

    constructor(private _fb: FormBuilder, private _s: CargoService, private _u: UnidadProduccionService, private _rt: Router) {
        this.form = this._fb.group({
            nombre: ['', Validators.required],
            unidades_produccion: [[], Validators.required],
        });
        this.columns = ['col1',];
        this.renderinputs = [
            { column: 'col1', title: 'Nombre', type: 'text', name: 'nombre' },

        ];

    }

    ngOnInit() {
        this._form.setReady(true);
        Promise.all([this._multi.complete]).then(data => {
            this._form.setReady(false);
        });
        this._form.successful = data => {
            this._rt.navigate(['configuracion/cargos']);
        }
    }
}
