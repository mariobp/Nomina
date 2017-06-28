import { Component, ViewChild, AfterViewInit } from '@angular/core';
import { Router } from '@angular/router';
import { FormGroup, Validators, FormBuilder } from '@angular/forms';
import { FormComponent, TableComponent, RenderInput } from '../../../lib/components'
import { TipoContratoService } from './tipocontrato.service';

@Component({
    template: '<router-outlet></router-outlet>'
})
export class TipocontratoComponent {}

@Component({
    templateUrl: './list.tipocontrato.component.html'
})
export class TipoContratoListComponent {

    @ViewChild('table') private table: TableComponent;

    icon = 'assignment_ind';
    title = 'Tipo de Contrato';
    service = this._cs;
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
        { data: 'extra_diurna' },
        { data: 'extra_nocturna' },
        { data: 'extra_dominical' },
        { data: 'extra_dominical_nocturna' }
    ]

    constructor(private _cs: TipoContratoService) { }
}

@Component({
    template: `<ex-form #f icon="assignment_ind" title="Tipo de contrato"
        [form]="form"
        [service]="service"
        [columns]="columns"
        [renderinputs]="renderinputs"></ex-form>`
})
export class EditTipoContratoComponent implements AfterViewInit {

    form: FormGroup;
    columns: string[];
    renderinputs: RenderInput[];
    service = this._s;

    @ViewChild('f') private _form: FormComponent;

    constructor(private _fb: FormBuilder, private _s: TipoContratoService , private _rt: Router) {
        this.form = this._fb.group({
          nombre: ['', Validators.required],
          extra_diurna: ['', Validators.required, Validators.min(1), Validators.max(100)],
          extra_nocturna: ['', Validators.required, Validators.min(1), Validators.max(100)],
          extra_dominical: ['', Validators.required, Validators.min(1), Validators.max(100)],
          extra_dominical_nocturna: ['', Validators.required, Validators.min(1), Validators.max(100)],
        });
        this.columns = [ 'col1' ];
        this.renderinputs = [
          { column: 'col1', title: 'Nombre', type: 'text', name: 'nombre'},
          { column: 'col1', title: 'Hora extra diurna', type: 'number', name: 'extra_diurna'},
          { column: 'col1', title: 'Hora extra nocturna', type: 'number', name: 'extra_nocturna'},
          { column: 'col1', title: 'Hora extra dominical', type: 'number', name: 'extra_dominical'},
          { column: 'col1', title: 'Hora extra dominical nocturna', type: 'number', name: 'extra_dominical_nocturna'}
        ];
    }

    ngAfterViewInit() {
        this._form.successful = data => {
            this._rt.navigate(['configuracion/tipo/contrato']);
        }
    }
}
