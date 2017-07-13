import { Component, OnInit, ViewChild, AfterViewInit } from '@angular/core';
import { Router, ActivatedRoute } from '@angular/router';
import { FormGroup, FormControl, Validators, FormBuilder } from '@angular/forms';
import { RenderInput, FormComponent } from '../../../lib/components';
import { TableComponent } from '../../../lib/components';
import { DescuentoService } from './descuento.service';
import { ContratoService } from '../../empleados/contrato/contrato.service';

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
    order = [[2, 'asc']]

    @ViewChild('table') private table: TableComponent;

    private corte: any;
    public title: any;
    addlink = [{ outlets: { 'descuento': [0, 'edit'] } }]


    columns = [
        {
            className: 'text-center',
            orderable: false,
            searchable: false,
            data: 'id',
            render: TableComponent.renderCheckRow
        },
        {
            orderable: false,
            searchable: false,
            className: 'truncate',
            data: 'empleados'
        },
        { data: 'cantidad', render: TableComponent.renderDecimal }
    ];

    constructor(private _s: DescuentoService, private _r: ActivatedRoute) {
        if (!!this._r.snapshot.data['item'] && Object.keys(this._r.snapshot.data['item']).length !== 0) {
            this.corte = this._r.snapshot.data['item'];
            this.title = `Descuentos deste ${this.corte.fecha_inicio}` + (!!this.corte.fecha_fin ? ` hasta ${this.corte.fecha_fin}` : '');
        }
    }

    ngOnInit() {
        this.table.success = data => console.log(data);
        this.table.editlink = () => {
            const aux = this.table.itemSelected;
            if (!!aux) {
                return [{ outlets: { 'descuento': [aux.id, 'edit'] } }]
            }
            return [{ outlets: { 'descuento': [aux] } }]
        };
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
    template: `<ex-form #f icon="money_off"
        [title]="title"
        [form]="form"
        [service]="service"
        [columns]="columns"
        [renderinputs]="renderinputs">
            <div bottom-form class="row">
                <div class="col-lg-12">
                    <div class="form-horizontal">
                        <div class="row">
                            <label class="col-lg-2 label-on-left" for="id_tarifario">Unidades de producción</label>
                            <div class="col-lg-10">
                                <div class="form-group label-floating is-empty">
                                    <ex-multi #multi name="contratos" placeholder="Seleccione las contratos"
                                        [form]="form" [service]="_c" [render]="nombre" [item]="_form.item"></ex-multi>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </ex-form>`
})
export class DescuentoEditComponent implements OnInit {

    form: FormGroup;
    columns: string[];
    renderinputs: RenderInput[];
    service = this._s;

    @ViewChild('f') public _form: FormComponent;

    private corte: any
    public title: string

    constructor(private _fb: FormBuilder, private _s: DescuentoService, private _rt: Router, private _r: ActivatedRoute,
        public _c: ContratoService) {
        if (!!this._r.parent.snapshot.data['item'] && Object.keys(this._r.parent.snapshot.data['item']).length !== 0) {
            this.corte = this._r.parent.snapshot.data['item'];
            this.title = `Descuentos deste ${this.corte.fecha_inicio}` + (!!this.corte.fecha_fin ? ` hasta ${this.corte.fecha_fin}` : '');
        }
        this.form = this._fb.group({
            cantidad: [0, [Validators.required, Validators.pattern(/\d/)]],
            contratos: [[], [Validators.required]],
            corte: this.corte.id
        });
        this.columns = ['col1'];
        this.renderinputs = [
            { title: 'Cantidad', type: 'number', column: 'col1', name: 'cantidad' }
        ];
    }

    ngOnInit() {
        this._form.successful = data => {
            this._rt.navigate(['nomina', this.corte.id, 'edit']);
        }
    }

    nombre = item => `${item.empleado__nombre} ${item.empleado__apellidos}`
}
