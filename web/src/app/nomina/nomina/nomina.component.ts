import { Component, OnInit, ViewChild, AfterViewInit } from '@angular/core';
import { Router, ActivatedRoute } from '@angular/router';
import { FormGroup, FormControl, Validators, FormBuilder } from '@angular/forms';
import { TableComponent, RenderInput, FormComponent } from '../../../lib/components';
import { NominaService } from './nomina.service';

declare var $: any;
declare var window: any;
declare var swal: any;

@Component({
    template: '<router-outlet></router-outlet>',
    styleUrls: ['./nomina.component.scss']
})
export class NominaComponent {
    static getQuery(ids: any[]) {
        let res = '';
        for (const value of ids) {
            if (res !== '') {
                res += '&';
            } else {
                res += '?'
            }
            res += `ids=${value}`
        }
        return res
    }
    static sendMail(d: string) {
        swal({
            title: 'Estás seguro? ',
            text: `Se enviaran uno mas correos.`,
            type: 'warning',
            showCancelButton: true,
            confirmButtonColor: '#213b78',
            cancelButtonColor: '#ff9800',
            cancelButtonText: 'Cancelar',
            confirmButtonText: 'Enviar'
        }).then(() => {
            $.ajax({
                url: `${window._server}/nomina/send/mail/${d}`,
                method: 'GET',
                xhrFields: {
                    withCredentials: true
                },
                success: function(data) {
                    swal({
                        title: 'Correos enviados!',
                        text: 'Todos los correos fueron enviados con exito',
                        type: 'success',
                        confirmButtonColor: '#213b78',
                    });
                }
            })
        }, () => { });
    }
}

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
    public title: string;
    public itemList = [];

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
                return `<a style="cursor: pointer;"class="down" data-down="${data}">
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

    onSelectedItemsChange(event) {
        this.itemList = event.selectedItems
    }

    finiquito() {
        const array = [];
        for (const variable of this.itemList) {
            array.push(variable.id)
        }
        NominaComponent.sendMail(NominaComponent.getQuery(array));
    }

    ngOnInit() {
        this.table.preAjax = data => {
            if (this.corte) {
                data['corte'] = this.corte.id;
            }
            return data;
        }
        this.table.drawCallback = () => {
            const self = this;
            $('.down').click(function(e) {
                self._as.down('admin/nomina/nomina/export/free/?corte__id__exact=', $(this).attr('data-down'), 0);
                e.preventDefault();
            });
        }
    }
}
