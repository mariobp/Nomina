import { Component, ViewChild, OnInit } from '@angular/core';
import { Router } from '@angular/router';
import { FormGroup, Validators, FormBuilder } from '@angular/forms';
import { FormComponent, TableComponent, RenderInput } from '../../../lib/components'
import { BancoService } from './banco.service';

@Component({
    template: '<router-outlet></router-outlet>'
})
export class BancoComponent { }

@Component({
    template: `<ex-form #f icon="attach_money" title="Banco"
        [form]="form"
        [service]="service"
        [columns]="columns"
        [renderinputs]="renderinputs"></ex-form>`
})
export class EditBancoComponent implements OnInit {

    form: FormGroup;
    columns: string[];
    renderinputs: RenderInput[];
    service = this._s;

    @ViewChild('f') private _form: FormComponent;

    constructor(private _fb: FormBuilder, private _s: BancoService, private _rt: Router) {
        this.form = this._fb.group({
            nombre: ['', [Validators.required, Validators.maxLength(30)]],
            codigo: ['', [Validators.required, Validators.maxLength(30)]]
        });
        this.columns = ['col1',];
        this.renderinputs = [
            { column: 'col1', title: 'Nombre', type: 'text', name: 'nombre' },
            { column: 'col1', title: 'Código', type: 'text', name: 'codigo' },
        ];
    }

    ngOnInit() {
        this._form.successful = data => {
            this._rt.navigate(['configuracion/banco']);
        }
    }
}
@Component({
    templateUrl: './list.banco.component.html'
})
export class BancoListComponent {

    @ViewChild('table') private table: TableComponent;

    icon = 'attach_money';
    title = 'Banco';
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
        { data: 'codigo' },
    ]

    constructor(private _as: BancoService) { }

    onChange($event) {
        // console.log($event);
    }

}
