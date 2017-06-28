import { Component, ViewChild, AfterViewInit } from '@angular/core';
import { Router } from '@angular/router';
import { FormGroup, Validators, FormBuilder } from '@angular/forms';
import { FormComponent, TableComponent, RenderInput } from '../../../lib/components'
import { EpsService } from './eps.service';

@Component({
    template: '<router-outlet></router-outlet>'
})
export class EpsComponent {}

@Component({
    template: `<ex-form #f icon="local_hospital" title="Eps"
        [form]="form"
        [service]="service"
        [columns]="columns"
        [renderinputs]="renderinputs"></ex-form>`
})
export class EditEpsComponent implements AfterViewInit {

    form: FormGroup;
    columns: string[];
    renderinputs: RenderInput[];
    service = this._s;

    @ViewChild('f') private _form: FormComponent;

    constructor(private _fb: FormBuilder, private _s: EpsService, private _rt: Router) {
        this.form = this._fb.group({
            nombre: ['', Validators.required],
            codigo: ['', Validators.required]
        });
        this.columns = ['col1',];
        this.renderinputs = [
            { column: 'col1', title: 'Nombre', type: 'text', name: 'nombre' },
            { column: 'col1', title: 'Código', type: 'text', name: 'codigo' },
        ];
    }

    ngAfterViewInit() {
        this._form.successful = data => {
            this._rt.navigate(['obligaciones/eps']);
        }
     }
}
@Component({
  templateUrl: './list.eps.component.html'
})
export class EpsListComponent {

    @ViewChild('table') private table: TableComponent;

    icon = 'local_hospital';
    title = 'Eps';
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

    constructor(private _as: EpsService) { }

    onChange($event) {
        console.log($event);
    }

}
