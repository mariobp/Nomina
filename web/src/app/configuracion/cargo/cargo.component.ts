import { Component, ViewChild, AfterViewInit } from '@angular/core';
import { Router } from '@angular/router';
import { FormGroup, Validators, FormBuilder } from '@angular/forms';
import { FormComponent, TableComponent, RenderInput } from '../../../lib/components'
import { CargoService } from './cargo.service';

@Component({
    template: '<router-outlet></router-outlet>'
})
export class CargoComponent {}

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
          { data: 'valor_hora_diurna' },
          { data: 'valor_hora_festivo' },
          { data: 'valor_hora_nocturna' }
      ]

      constructor(private _as: CargoService) { }

      onChange($event) {
        //   console.log($event);
      }
}

@Component({
    template: `<ex-form #f icon="turned_in" title="Cargos"
        [form]="form"
        [service]="service"
        [columns]="columns"
        [renderinputs]="renderinputs"></ex-form>`
})
export class EditCargoComponent implements AfterViewInit {

    form: FormGroup;
    columns: string[];
    renderinputs: RenderInput[];
    service = this._s;

    @ViewChild('f') private _form: FormComponent;

    constructor(private _fb: FormBuilder, private _s: CargoService, private _rt: Router) {
        this.form = this._fb.group({
            nombre: ['', Validators.required],
            valor_hora_diurna: ['', [Validators.required, Validators.min(1)]],
            valor_hora_nocturna: ['', [Validators.required, Validators.min(1)]],
            valor_hora_festivo: ['', [Validators.required, Validators.min(1)]],
        });
        this.columns = ['col1', ];
        this.renderinputs = [
            { column: 'col1', title: 'Nombre', type: 'text', name: 'nombre' },
            { column: 'col1', title: 'Valor hora diurna', type: 'number', name: 'valor_hora_diurna'},
            { column: 'col1', title: 'Valor hora nocturna', type: 'number', name: 'valor_hora_nocturna'},
            { column: 'col1', title: 'Valor hora festivo', type: 'number', name: 'valor_hora_festivo'}
        ];
    }

    ngAfterViewInit() {
        this._form.successful = data => {
            this._rt.navigate(['configuracion/cargos']);
        }
    }
}
