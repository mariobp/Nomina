import { Component, ViewChild, AfterViewInit, AfterContentInit } from '@angular/core';
import { Router } from '@angular/router';
import { FormGroup, Validators, FormBuilder } from '@angular/forms';
import { FormComponent, TableComponent, RenderInput } from '../../../lib/components'
import { ConfiguracionService } from './general.service';

@Component({
    template: '<router-outlet></router-outlet>'
})
export class GeneralComponent { }


@Component({
    template: `<ex-form #f icon="settings" title="Configuración general"
        [form]="form"
        [service]="service"
        [columns]="columns"
        [renderinputs]="renderinputs"
        [deleteable]="deleteable"
        [otro]="otro"></ex-form>`
})
export class EditGeneralComponent implements AfterViewInit, AfterContentInit {

    form: FormGroup;
    columns: string[];
    renderinputs: RenderInput[];
    service = this._s;
    otro = false;
    deleteable = false;
    @ViewChild('f') private _form: FormComponent;

    constructor(private _fb: FormBuilder, private _s: ConfiguracionService, private _rt: Router) {
        this.form = this._fb.group({
            tipo_corte: [[], Validators.required],
            primer_dia: ['', [Validators.required, Validators.min(1), Validators.max(31)]],
            segundo_dia: ['', [Validators.required, Validators.min(1), Validators.max(31)]],
            h_recargo_nocturno_inicio: ['', Validators.required],
            h_recargo_nocturno_fin: ['', Validators.required],
            h_almuerzo_inicio: ['', [Validators.required, Validators.min(0)]],
            h_almuerzo_fin: ['', [Validators.required, Validators.min(0)]],
            nocturna: ['', [Validators.required, Validators.min(0)]],
            dominical: ['', [Validators.required, Validators.min(0)]],
            nocturna_dominical: ['', [Validators.required, Validators.min(0)]],
            extra_diurna: ['', [Validators.required, Validators.min(0)]],
            extra_nocturna: ['', [Validators.required, Validators.min(0)]],
            extra_dominical_diurna: ['', [Validators.required, Validators.min(0)]],
            extra_dominical_nocturna: ['', [Validators.required, Validators.min(0)]],
            descuento_salud: ['', [Validators.required, Validators.min(0)]],
            prestaciones_sociales: ['', [Validators.required, Validators.min(0)]],
        });
        this.columns = ['col1', 'col2'];
        this.renderinputs = [
            {
                column: 'col1', title: 'Tipo de corte', type: 'null', name: 'tipo_corte', isSelect: true, options: [
                    { title: 'Quincenal', value: 0 },
                    { title: 'Mensual', value: 1 }
                ]
            },
            { column: 'col1', title: 'Primer dia de corte', type: 'number', name: 'primer_dia' },
            { column: 'col1', title: 'Segundo dia de corte', type: 'number', name: 'segundo_dia' },
            { column: 'col1', title: 'Hora de inicio de recargo nocturno', type: 'text', name: 'h_recargo_nocturno_inicio', class: 'timepicker' },
            { column: 'col1', title: 'Hora de finalización de recargo nocturno', type: 'text', name: 'h_recargo_nocturno_fin', class: 'timepicker' },
            { column: 'col1', title: 'Hora de inicio de almuerzo', type: 'text', name: 'h_almuerzo_inicio', class: 'timepicker' },
            { column: 'col1', title: 'Hora de finalización del almuerzo', type: 'text', name: 'h_almuerzo_fin', class: 'timepicker' },
            { column: 'col2', title: 'Valor recargo nocturno %', type: 'number', name: 'nocturna' },
            { column: 'col2', title: 'Valor recargo dominical %', type: 'number', name: 'dominical' },
            { column: 'col2', title: 'Valor recargo nocturno dominical %', type: 'number', name: 'nocturna_dominical' },
            { column: 'col2', title: 'Valor hora extra diurna %', type: 'number', name: 'extra_diurna' },
            { column: 'col2', title: 'Valor hora extra nocturna %', type: 'number', name: 'extra_nocturna' },
            { column: 'col2', title: 'Valor hora extra dominical diurna %', type: 'number', name: 'extra_dominical_diurna' },
            { column: 'col2', title: 'Valor hora extra dominical nocturna %', type: 'number', name: 'extra_dominical_nocturna' },
            { column: 'col2', title: 'Descuento de salud y pensión para empleado %', type: 'number', name: 'descuento_salud' },
            { column: 'col2', title: 'Pago de salud y pensión del empleador %', type: 'number', name: 'prestaciones_sociales' },
        ];
    }

    ngAfterViewInit() {
        this._form.prePatchValue = value => {
            // console.log(value);
            if (value) {
                if (!Array.isArray(value.tipo_corte)) {
                    value.tipo_corte = [value.tipo_corte];
                }
            }
            return value;
        }
        this._form.preSave = data => {
            if (Array.isArray(data.tipo_corte)) {
                data.tipo_corte = data.tipo_corte[0];
            }
            return data;
        };
        this._form.successful = data => {
            this._rt.navigate(['configuracion/general']);
        }

    }

    ngAfterContentInit() {
        this._form.setReady(true);
        this._s.list({}).then(data => data.json()).then(data => {
            this._form.setItem(data.object_list[0]);
            this._form.setReady(false);
        });
    }
}
