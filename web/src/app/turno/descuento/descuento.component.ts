import { Component, ViewChild, OnInit, AfterViewInit } from '@angular/core';
import { Router, ActivatedRoute } from '@angular/router';
import { FormGroup, Validators, FormBuilder } from '@angular/forms';
import { FormComponent, TableComponent, RenderInput } from '../../../lib/components'
import { DescuentoService } from './descuento.service';
import { UnidadProduccionService } from '../../configuracion/unidadproduccion/unidadproduccion.service';


@Component({
    template: '<router-outlet></router-outlet>'

})
export class DescuentoComponent { }


@Component({
    templateUrl: './list.descuento.component.html'
})
export class DescuentoListComponent {

    @ViewChild('table') private table: TableComponent;

    icon = 'money_off';
    title = 'Descuentos de producción';
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
        { data: 'unidad__nombre' },
        { data: 'concepto' },
        { data: 'cantidad' },
        { data: 'fecha' },
    ]

    constructor(private _as: DescuentoService) { }


}


@Component({
    templateUrl: './edit.descuento.html'
})
export class EditDescuentoComponent implements OnInit {

    form: FormGroup;
    columns: string[];
    renderinputs: RenderInput[];
    service = this._s;
    debug = false;
    unidadFilter = false;
    private produccion: any;
    public auto = false;
    placeholder = '';
    paramsUnidad = {};

    @ViewChild('f') public _form: FormComponent;

    constructor(private _fb: FormBuilder, private _s: DescuentoService, public _u: UnidadProduccionService,
        private _rt: Router, private _r: ActivatedRoute) {
        this.form = this._fb.group({
            unidad: [[], Validators.required],
            cantidad: ['', [Validators.required, Validators.min(1)]],
            concepto: ['', [Validators.required]],
            fecha: ['', Validators.required]
        });
        this.columns = ['col1'];
        this.renderinputs = [
            { column: 'col1', title: 'Cantidad', type: 'number', step: '3', name: 'cantidad' },
            { column: 'col1', title: 'Concepto', type: 'text', name: 'concepto' },
            { column: 'col1', title: 'Fecha', type: 'text', name: 'fecha', class: 'datetimepicker' },


        ];
    }

    itemUnidad = item => `${item.unidad__nombre}`;

    ngOnInit() {
        this._form.successful = data => {
            this._rt.navigate(['produccion/descuento']);
        }
    }
}
