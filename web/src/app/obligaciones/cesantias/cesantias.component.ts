import { Component, ViewChild, AfterViewInit } from '@angular/core';
import { Router } from '@angular/router';
import { FormGroup, Validators, FormBuilder } from '@angular/forms';
import { FormComponent, TableComponent, RenderInput } from '../../../lib/components'
import { CesantiasService } from './cesantias.service';

@Component({
    template: '<router-outlet></router-outlet>'
})
export class CesantiasComponent { }

@Component({
    template: `<ex-form #f icon="accessibility" title="Cesantías"
        [form]="form"
        [service]="service"
        [columns]="columns"
        [renderinputs]="renderinputs"></ex-form>`
})
export class EditCesantiasComponent implements AfterViewInit {
    form: FormGroup;
    columns: string[];
    renderinputs: RenderInput[];
    service = this._cs;

    @ViewChild('f') private _form: FormComponent;

    constructor(private _fb: FormBuilder, private _cs: CesantiasService, private _rt: Router) {
      this.form = this._fb.group({
          nombre: ['', Validators.required, Validators.maxLength(30)],
          codigo: ['', Validators.required, Validators.maxLength(30)]
      });
      this.columns = ['col1', ];
      this.renderinputs = [
          { column: 'col1', title: 'Nombre', type: 'text', name: 'nombre' },
          { column: 'col1', title: 'Código', type: 'text', name: 'codigo' },
      ];
    }

    ngAfterViewInit() {
        this._form.successful = data => {
            this._rt.navigate(['obligaciones/cesantias']);
        }
    }
}

@Component({
    templateUrl: './list.cesantias.component.html'
})
export class CesantiasListComponent {

    @ViewChild('table') private table: TableComponent;

    icon = 'accessibility';
    title = 'Cesantías';
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
        { data: 'codigo' },
    ]

    constructor(private _cs: CesantiasService) { }
}
