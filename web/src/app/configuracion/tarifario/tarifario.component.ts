import { Component, ViewChild, OnInit } from '@angular/core';
import { Router } from '@angular/router';
import { FormGroup, FormControl, Validators, FormBuilder } from '@angular/forms';
import { FormComponent, TableComponent, RenderInput } from '../../../lib/components'
import { TarifarioService } from './tarifario.service';
import { UnidadProduccionService } from '../unidadproduccion/unidadproduccion.service';
import { CargoService } from '../cargo/cargo.service';

@Component({
    template: '<router-outlet></router-outlet>'

})
export class TarifarioComponent { }

@Component({
    templateUrl: './list.tarifario.component.html'
})
export class TarifarioListComponent {

    @ViewChild('table') private table: TableComponent;

    icon = 'local_atm';
    title = 'Tarifario';
    service = this._s;
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
        { data: 'cargo__nombre' },
        { data: 'precio' }
    ]

    constructor(private _s: TarifarioService) { }
}

@Component({
    templateUrl: './edit.tarifario.component.html'
})
export class EditTarifarioComponent implements OnInit {

    form: FormGroup;
    columns: string[];
    renderinputs: RenderInput[];
    service = this._s;

    @ViewChild('f') public _form: FormComponent;

    constructor(private _fb: FormBuilder, private _s: TarifarioService,
        public _u: UnidadProduccionService, public _c: CargoService, public _rt: Router) {
        this.form = this._fb.group({
            unidad: [[], [Validators.required, Validators.pattern(/\d/)]],
            cargo: [[], [Validators.required, Validators.pattern(/\d/)]],
            precio: ['', [Validators.required, Validators.min(0)]]
        });
        this.columns = ['col1'];
        this.renderinputs = [
            { column: 'col1', title: 'Precio', type: 'number', name: 'precio', },
        ];
    }

    itemCargo = item => item.cargo__nombre;
    itemUnidad = item => item.unidad__nombre;

    ngOnInit() {
        this._form.successful = data => {
            this._rt.navigate(['configuracion/tarifario']);
        }
    }
}
