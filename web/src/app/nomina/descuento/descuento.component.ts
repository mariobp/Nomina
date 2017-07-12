import { Component, OnInit, ViewChild, AfterViewInit } from '@angular/core';
import { Router, ActivatedRoute } from '@angular/router';
import { FormGroup, FormControl, Validators, FormBuilder } from '@angular/forms';
import { RenderInput, FormComponent } from '../../../lib/components';
import { TableComponent } from '../../../lib/components';
import { DescuentoService } from './descuento.service';
import {  } from './';

@Component({
    template: '<router-outlet></router-outlet>'
})
export class DescuentoComponent { }

@Component({
    templateUrl: './list.descuento.component.html'
})
export class DescuentoListComponent implements OnInit {
    service = this._s;
    multiselect = true;
    icon = 'money_off'
    // order = [[2, 'asc']]

    @ViewChild('table') private table: TableComponent;

    private corte: any;
    private title: any;

    columns = [
        {
            className: 'text-center',
            orderable: false,
            searchable: false,
            data: 'id',
            render: TableComponent.renderCheckRow
        },
        { data: 'id' }
    ];

    constructor(private _s: DescuentoService, private _r: ActivatedRoute) {
        if (!!this._r.snapshot.data['item'] && Object.keys(this._r.snapshot.data['item']).length !== 0) {
            this.corte = this._r.snapshot.data['item'];
            this.title = `Descuentos deste ${this.corte.fecha_inicio}` + (!!this.corte.fecha_fin ? ` hasta ${this.corte.fecha_fin}` : '');
        }
    }

    ngOnInit() {
        this.table.success = data => console.log(data);
    }

    get aggregable() {
        return !this.corte.cerrado
    };
    get deleteable() {
        return !this.corte.cerrado
    };
    get editable() {
        return !this.corte.cerrado
    };
}


@Component({
    template: `<ex-form #f icon="" title=""
        [form]="form"
        [service]="service"
        [columns]="columns"
        [renderinputs]="renderinputs"></ex-form>`
})
export class DescuentoEditComponent implements AfterViewInit {

    form: FormGroup;
    columns: string[];
    renderinputs: RenderInput[];
    service = this._s;

    @ViewChild('f') private _form: FormComponent;

    constructor(private _fb: FormBuilder, private _s: DescuentoService, private _rt: Router) {
        this.form = this._fb.group({

        });
        this.columns = [];
        this.renderinputs = [

        ];
    }

    ngAfterViewInit() { }
}
