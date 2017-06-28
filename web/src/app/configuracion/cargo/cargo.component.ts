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
          { data: 'nombre' }
      ]

      constructor(private _as: CargoService) { }

      onChange($event) {
          console.log($event);
      }
}
