import { Component, OnInit, ViewChild } from '@angular/core';
import { ActivatedRoute } from '@angular/router';
import { FormGroup, FormControl, Validators, FormBuilder } from '@angular/forms';
import { TableComponent } from '../../../lib/table/table.component';
import { EpsService } from './eps.service';

@Component({
    template: '<router-outlet></router-outlet>'
})
export class EpsComponent {}

@Component({
  templateUrl: './list.eps.component.html'
})
export class EpsListComponent implements OnInit {

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

    ngOnInit() { }
}
