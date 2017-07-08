import { Component, ViewChild, AfterViewInit } from '@angular/core';
import { Router } from '@angular/router';
import { FormGroup, FormControl, Validators, FormBuilder } from '@angular/forms';
import { FormComponent, TableComponent, RenderInput } from '../../../lib/components'
import { UnidadProduccionService } from './unidadproduccion.service';

@Component({
    template: '<router-outlet></router-outlet>'
})
export class UnidadproduccionComponent { }

@Component({
    templateUrl: './list.unidadproduccion.component.html'
})
export class UnidadProduccionListComponent {

    @ViewChild('table') private table: TableComponent;

    icon = 'label';
    title = 'Unidad de producción';
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

    constructor(private _as: UnidadProduccionService) { }

}


@Component({
    template: `<ex-form #f icon="label" title="Unidad de producción"
        [form]="form"
        [service]="service"
        [columns]="columns"
        [renderinputs]="renderinputs"></ex-form>`
})
export class EditUnidadProduccionComponent implements AfterViewInit {

    form: FormGroup;
    columns: string[];
    renderinputs: RenderInput[];
    service = this._s;

    @ViewChild('f') private _form: FormComponent;

    constructor(private _fb: FormBuilder, private _s: UnidadProduccionService, private _rt: Router) {
        this.form = this._fb.group({
            nombre: ['', [Validators.required, Validators.maxLength(30)]],
        });
        this.columns = ['col1'];
        this.renderinputs = [
            { column: 'col1', title: 'Nombre', type: 'text', name: 'nombre' },
        ];
    }

    ngAfterViewInit() {
        this._form.successful = data => {
            this._rt.navigate(['configuracion/unidad/produccion']);
        }
    }
}
