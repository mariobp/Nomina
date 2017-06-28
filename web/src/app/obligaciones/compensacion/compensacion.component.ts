import { Component, ViewChild, AfterViewInit } from '@angular/core';
import { Router } from '@angular/router';
import { FormGroup, Validators, FormBuilder } from '@angular/forms';
import { FormComponent, TableComponent, RenderInput } from '../../../lib/components'
import { CompensacionService } from './compensacion.service';

@Component({
    template: '<router-outlet></router-outlet>'
})
export class CompensacionComponent {}

@Component({
    template: `<ex-form #f icon="wc" title="Caja de Compensación"
        [form]="form"
        [service]="service"
        [columns]="columns"
        [renderinputs]="renderinputs"></ex-form>`
})
export class EditCompensacionComponent implements AfterViewInit {

    form: FormGroup;
    columns: string[];
    renderinputs: RenderInput[];
    service = this._s;

    @ViewChild('f') private _form: FormComponent;

    constructor(private _fb: FormBuilder, private _s: CompensacionService, private _rt: Router) {
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
          this._rt.navigate(['obligaciones/compensacion']);
      }
    }
}
@Component({
    templateUrl: './list.compensacion.component.html'
})
export class CompensacionListComponent {

      @ViewChild('table') private table: TableComponent;

      icon = 'wc';
      title = 'Caja de compensación familiar';
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

      constructor(private _as: CompensacionService) { }

      onChange($event) {
          console.log($event);
      }
}
