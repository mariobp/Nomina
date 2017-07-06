import { Component, ViewChild, AfterViewInit } from '@angular/core';
import { Router } from '@angular/router';
import { FormGroup, FormControl, Validators, FormBuilder } from '@angular/forms';
import { FormComponent, TableComponent, RenderInput } from '../../../lib/components'
import { PensionService } from './pension.service';

@Component({
    template: '<router-outlet></router-outlet>'
})
export class PensionComponent {}

@Component({
    template: `<ex-form #f icon="local_atm" title="Pensión"
        [form]="form"
        [service]="service"
        [columns]="columns"
        [renderinputs]="renderinputs"></ex-form>`
})
export class EditPensionComponent implements AfterViewInit {

    form: FormGroup;
    columns: string[];
    renderinputs: RenderInput[];
    service = this._s;

    @ViewChild('f') private _form: FormComponent;

    constructor(private _fb: FormBuilder, private _s: PensionService, private _rt: Router) {
        this.form = this._fb.group({
            nombre: ['', [Validators.required, Validators.maxLength(30)]],
            codigo: ['', [Validators.required, Validators.maxLength(30)]]
        });
        this.columns = ['col1', ];
        this.renderinputs = [
            { column: 'col1', title: 'Nombre', type: 'text', name: 'nombre' },
            { column: 'col1', title: 'Código', type: 'text', name: 'codigo' },
        ];
    }

    ngAfterViewInit() {
      this._form.successful = data => {
          this._rt.navigate(['obligaciones/pension']);
      }
    }
}
@Component({
  templateUrl: './list.pension.component.html'
})
export class PensionListComponent {

    @ViewChild('table') private table: TableComponent;

    icon = 'local_atm';
    title = 'Pensión';
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

    constructor(private _as: PensionService) { }

    onChange($event) {
        // console.log($event);
    }

}
