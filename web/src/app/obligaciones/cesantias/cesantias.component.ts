import { Component, OnInit, ViewChild } from '@angular/core';
import { TableComponent } from '../../../lib/table/table.component';
@Component({
    selector: 'app-cesantias',
    templateUrl: './cesantias.component.html',
    styleUrls: ['./cesantias.component.scss']
})
export class CesantiasComponent implements OnInit {

    @ViewChild('table') private table: TableComponent;

    constructor() { }

    ngOnInit() {
        this.table.multiSelectable = true;
        // this.table.service = this._as;
        this.table.preAjax = data => {
            if (data.sort_property === 'nombre') {
                data.sort_property = 'first_name';
            }
            return data;
        };
        this.table.columns = [
            {
                className: 'text-center',
                orderable: false,
                searchable: false,
                data: 'id',
                render: this.table.renderCheckRow
            },
            { data: 'username' },
            {
                data: 'nombre',
                render: (data, type, full, meta) => {
                    return `${data.first_name} ${data.last_name}`;
                }
            },
            { data: 'identificacion' },
            { data: 'email' },
            { data: 'telefono' },
            {
                className: 'ex-table-btn',
                orderable: false,
                searchable: false,
                data: 'id'
            },
        ];
    }

}
