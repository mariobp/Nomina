import { Component, ViewChild, OnInit } from '@angular/core';
import { Router } from '@angular/router';
import { FormGroup, Validators, FormBuilder } from '@angular/forms';
import { FormComponent, TableComponent, RenderInput } from '../../../lib/components'
import { TipoContratoService } from './tipocontrato.service';

@Component({
    template: '<router-outlet></router-outlet>'
})
export class TipocontratoComponent { }

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
        { data: 'modalidad_nombre' }
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
export class EditTipoContratoComponent implements OnInit {

    form: FormGroup;
    columns: string[];
    renderinputs: RenderInput[];
    service = this._s;

    @ViewChild('f') private _form: FormComponent;

    constructor(private _fb: FormBuilder, private _s: TipoContratoService, private _rt: Router) {
        this.form = this._fb.group({
            nombre: ['', Validators.required],
            modalidad: [[], Validators.required]
        });
        this.columns = ['col1'];
        this.renderinputs = [
            { column: 'col1', title: 'Nombre', type: 'text', name: 'nombre' },
            {
                column: 'col1', title: 'Modalidad', type: null, name: 'modalidad', isSelect: true, options: [
                    { title: 'Por hora', value: 1 },
                    { title: 'Salario fijo', value: 2 },
                    { title: 'Por producción', value: 3 }
                ]
            }
        ];
    }

    ngOnInit() {
        this._form.successful = data => {
            this._rt.navigate(['configuracion/tipo/contrato']);
        }
    }
}
