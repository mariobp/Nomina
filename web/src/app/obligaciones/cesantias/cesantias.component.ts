import { Component, OnInit, ViewChild } from '@angular/core';
import { ActivatedRoute } from '@angular/router';
import { FormGroup, FormControl, Validators, FormBuilder } from '@angular/forms';
import { TableComponent } from '../../../lib/table/table.component';
import { CesantiasService } from './cesantias.service';

@Component({
    template: '<router-outlet></router-outlet>'
})
export class CesantiasComponent {}

@Component({
  templateUrl: './list.cesantias.component.html'
})
export class CesantiasListComponent implements OnInit {

  @ViewChild('table') private table: TableComponent;

  icon = 'accessibility';
  title = 'Cesantía';
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

  constructor(private _as: CesantiasService) { }

  onChange($event) {
      console.log($event);
  }

  ngOnInit() { }

}
