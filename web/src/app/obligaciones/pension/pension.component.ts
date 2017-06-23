import { Component, OnInit, ViewChild } from '@angular/core';
import { ActivatedRoute } from '@angular/router';
import { FormGroup, FormControl, Validators, FormBuilder } from '@angular/forms';
import { TableComponent } from '../../../lib/table/table.component';
import { PensionService } from './pension.service';

@Component({
    template: '<router-outlet></router-outlet>'
})
export class PensionComponent {}

@Component({
  templateUrl: './list.pension.component.html'
})
export class PensionListComponent implements OnInit {

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
        console.log($event);
    }

    ngOnInit() { }

}
