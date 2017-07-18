import { Component, OnInit, ViewChild } from '@angular/core';
@Component({
    template: '<router-outlet></router-outlet>',
    styleUrls: ['./corte.component.scss']
})
export class CorteComponent { }

import { TableComponent } from '../../../lib/components';
import { CorteService } from './corte.service';
@Component({ templateUrl: './list.corte.component.html' })
export class CorteListComponent implements OnInit {
    service = this._s;
    multiselect = true;
    aggregable = false;
    editable = true;
    deleteable = false;
    order = [[1, 'desc']]

    @ViewChild('table') private table: TableComponent;

    columns = [
        {
            className: 'text-center',
            orderable: false,
            searchable: false,
            data: 'id',
            render: TableComponent.renderCheckRow
        },
        { className: 'text-center', data: 'fecha_inicio' },
        { className: 'text-center', data: 'fecha_fin' },
        {
            className: 'text-center', data: 'cerrado', render: data => {
                let icon = 'lock_open';
                let color = 'green';
                let title = 'Abierto';
                if (data) {
                    color = 'red';
                    icon = 'lock_outline';
                    title = 'Cerrado';
                }
                return `<i class="material-icons ${color}" title="${title}">${icon}</i>`
            }
        }
    ];


    constructor(private _s: CorteService) { }

    ngOnInit() { }
}

import { Router } from '@angular/router';
import { FormGroup, FormControl, Validators, FormBuilder } from '@angular/forms';
import { RenderInput, FormComponent } from '../../../lib/components';
import {  } from './';

@Component({
    templateUrl: './edit.corte.component.html'
})
export class CorteEditComponent implements OnInit {

    form: FormGroup;
    columns: string[];
    renderinputs: RenderInput[];
    service = this._s;
    deleteable = false
    saveable = false

    @ViewChild('f') private _form: FormComponent;
    Component;

    constructor(private _fb: FormBuilder, private _s: CorteService, private _rt: Router) {
        this.form = this._fb.group({
            fecha_inicio: [{ value: '', disabled: true }],
            fecha_fin: [{ value: '', disabled: true }],
            cerrado: [{ value: false, disabled: true }]
        });
        this.columns = ['col1', 'col2'];
        this.renderinputs = [
            { column: 'col1', title: 'Fecha de Inicio', type: 'text', name: 'fecha_inicio' },
            { column: 'col2', title: 'Fecha de Finalizacion', type: 'text', name: 'fecha_fin' },
            { column: 'col2', title: 'Cerrado', type: 'checkbox', name: 'cerrado' }
        ];
    }

    ngOnInit() {
        this._form.successful = data => {
            this._rt.navigate(['/nomina']);
        }
    }

    plano1() {
        this._s.down('admin/nomina/nomina/export/free/?corte__id__exact=', this._form.item.id, 1);
    }
    plano2() {
        this._s.down('admin/nomina/nomina/export/free/?corte__id__exact=', this._form.item.id, 3);
    }
    finiquito() {
        console.log('finiquito')
    }
}
