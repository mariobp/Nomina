import { Component, OnInit, ViewChild, AfterViewInit } from '@angular/core';
import { TableComponent } from '../../../lib/components';
import { PagoIncapacidadService } from './pago.incapacidad.service';
import { TipoIncapacidadService } from '../tipo/tipo.incapacidad.service';
import { Router } from '@angular/router';
import { FormGroup, FormControl, Validators, FormBuilder } from '@angular/forms';
import { RenderInput, FormComponent } from '../../../lib/components';

@Component({
    template: '<router-outlet></router-outlet>'
})

export class PagoIncapacidadComponent { }


@Component({
    templateUrl: './list.pago.incapacidad.component.html'
})
export class PagoIncapacidadListComponent implements OnInit {
    service = this._s;
    multiselect = true;
    aggregable = false;
    editable = false;
    deleteable = false;

    @ViewChild('table') private table: TableComponent;

    columns = [
        {
            className: 'text-center',
            orderable: false,
            searchable: false,
            data: 'id',
            render: TableComponent.renderCheckRow
        },
        { className: 'text-center', data: 'tipo__nombre' },
        { className: 'text-center', data: 'dia' },
        { className: 'text-center', data: 'porcentaje' }

    ];


    constructor(private _s: PagoIncapacidadService) { }

    ngOnInit() {
        this.table.success = data => console.log(data);
    }

}


@Component({
    template: `<ex-form #f icon="accessible" title="Pago de Incapacidad"
        [form]="form"
        [service]="service"
        [columns]="columns"
        [renderinputs]="renderinputs">
            <div top-form class="row">
            <div class="col-lg-12">
                <div class="row">
                    <label class="col-lg-3 label-on-left" for="id_cargo">Tipo:</label>
                    <div class="col-lg-9">
                        <div class="form-group label-floating is-empty">
                            <label class="control-label"></label>
                            <ex-autocomplete
                                    name="tipo"
                                    [form]="form"
                                    [service]="_t"
                                    [item]="_form.item"
                                    [itemVal]="itemTipo">
                            </ex-autocomplete>
                        </div>
                    </div>
                </div>
            </div>
            </div>
        </ex-form>`
})
export class PagoIncapacidadEditComponent implements OnInit {

    form: FormGroup;
    columns: string[];
    renderinputs: RenderInput[];
    service = this._s;

    @ViewChild('f') public _form: FormComponent;

    itemTipo = item => `${item.tipo__nombre}`;

    constructor(private _fb: FormBuilder, private _s: PagoIncapacidadService, private _rt: Router, public _t: TipoIncapacidadService) {
        this.form = this._fb.group({
            tipo: ['', [Validators.required]],
            dia: ['', [Validators.required, Validators.min(1)]],
            porcentaje: ['', [Validators.required, Validators.min(0), Validators.max(100)]]
        });
        this.columns = ['col1'];
        this.renderinputs = [
            { title: 'Dia', column: 'col1', name: 'dia', type: 'number' },
            { title: 'Porcentaje', column: 'col1', name: 'porcentaje', type: 'number' }
        ];
    }

    ngOnInit() {
        this._form.successful = data => {
            this._rt.navigate(['incapacidad/pago']);
        }
    }
}
