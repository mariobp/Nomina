import { Component, OnInit, ViewChild } from '@angular/core';
import { ActivatedRoute } from '@angular/router';
import { FormGroup, FormControl, Validators, FormBuilder } from '@angular/forms';
import { TableComponent } from '../../../lib/table/table.component';
import { CompensacionService } from './compensacion.service';

@Component({
    template: '<router-outlet></router-outlet>'
})
export class CompensacionComponent {}

@Component({
    templateUrl: './list.compensacion.component.html'
})
export class CompensacionListComponent implements OnInit {

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

      ngOnInit() { }
}
