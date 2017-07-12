import { Component, OnInit, ViewChild, AfterViewInit } from '@angular/core';
import { Router, ActivatedRoute } from '@angular/router';
import { FormGroup, FormControl, Validators, FormBuilder } from '@angular/forms';
import { TableComponent, RenderInput, FormComponent } from '../../../lib/components';
import { NominaService } from './nomina.service';

declare var $: any;
declare var window: any;

@Component({
    template: '<router-outlet></router-outlet>',
    styleUrls: ['./nomina.component.scss']
})
export class NominaComponent { }

@Component({
    templateUrl: './list.nomina.component.html'
})
export class NominaListComponent implements OnInit {
    service = this._as;
    multiselect = true;
    aggregable = false;
    editable = false;
    deleteable = false;
    order = [[2, 'asc']]

    private corte: any;
    private title: string

    @ViewChild('table') private table: TableComponent;

    columns = [
        {
            className: 'text-center',
            orderable: false,
            searchable: false,
            data: 'id',
            render: TableComponent.renderCheckRow
        },
        {
            className: 'text-center',
            orderable: false,
            searchable: false,
            data: 'id',
            render: (data, type, full, meta) => {
                return `<a style="cursor: pointer;"class="down" data-down="${data}" data-empleado="${full.empleado_f.nombre} ${full.empleado_f.apellidos}">
                    <i class="material-icons">file_download</i>
                </a>`;
            }
        },
        {
            data: 'contrato__empleado',
            render: (data, type, full, meta) => {
                return `${full.empleado_f.nombre} ${full.empleado_f.apellidos}`;
            }
        },
        {
            data: 'salario_produccion',
            orderable: false,
            searchable: false,
            render: TableComponent.renderDecimal
        },
        {
            data: 'salario_legal',
            orderable: false,
            searchable: false,
            render: TableComponent.renderDecimal
        },
        {
            data: 'recargos',
            orderable: false,
            searchable: false,
            render: TableComponent.renderDecimal
        },
        {
            data: 'bonificacion',
            orderable: false,
            searchable: false,
            render: TableComponent.renderDecimal
        },
        {
            data: 'prestaciones_sociales',
            orderable: false,
            searchable: false,
            render: TableComponent.renderDecimal
        },
        {
            data: 'descuento_salud',
            orderable: false,
            searchable: false,
            render: TableComponent.renderDecimal
        },
        {
            data: 'neto',
            orderable: false,
            searchable: false,
            render: TableComponent.renderDecimal
        },
        {
            data: 'total',
            orderable: false,
            searchable: false,
            render: TableComponent.renderDecimal
        },
    ];
    /*
        nombre empleado
        salario base
    */

    constructor(private _as: NominaService, private _r: ActivatedRoute) {
        if (!!this._r.snapshot.data['item'] && Object.keys(this._r.snapshot.data['item']).length !== 0) {
            this.corte = this._r.snapshot.data['item'];
            this.title = `Nominas deste ${this.corte.fecha_inicio}` + (!!this.corte.fecha_fin ? ` hasta ${this.corte.fecha_fin}` : '');
        }
    }

    ngOnInit() {
        this.table.preAjax = data => {
            if (this.corte) {
                data['corte'] = this.corte.id;
            }
            return data;
        }
        this.table.drawCallback = () => {
            $('.down').click(function(e) {
                e.preventDefault();
                const url = `${window._server}/admin/nomina/nomina/export/free/?id=${$(this).attr('data-down')}`;
                const empelado = $(this).attr('data-empleado')
                $.ajax({
                    url: url,
                    method: 'POST',
                    data: { file_format: 0 },
                    xhrFields: {
                        withCredentials: true
                    },
                    success: function(data) {
                        const blob = new Blob([data]);
                        const link = document.createElement('a');
                        const date = new Date();
                        link.href = window.URL.createObjectURL(blob);
                        link.download = `Finiquito_${empelado}_${date.toLocaleDateString('es-CO')}.pdf`;
                        link.click();
                    }
                });
            });
        }
    }
}
