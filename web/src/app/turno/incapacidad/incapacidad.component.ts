import { Component, OnInit, ViewChild, AfterViewInit } from '@angular/core';
import { Router } from '@angular/router';
import { FormGroup, FormControl, Validators, FormBuilder } from '@angular/forms';
import { RenderInput, FormComponent, TableComponent } from '../../../lib/components';
import { IncapacidadService } from './incapacidad.service';
import { EmpleadoService } from '../../empleados/empleado/empleado.service';
import { TipoIncapacidadService } from '../../incapacidad/tipo/tipo.incapacidad.service';

@Component({
    template: '<router-outlet></router-outlet>'
})
export class IncapacidadComponent {

}

@Component({
    templateUrl: './list.incapacidad.component.html'
})
export class IncapacidadListComponent {

    @ViewChild('table') private table: TableComponent;

    icon = 'accessible';
    title = 'Incapacidades';
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
        { data: 'tipo__nombre' },
        { data: 'dias' },
        { data: 'empleado__nombre' },
        { data: 'empleado__apellidos' },
        { data: 'fecha' },
    ]

    constructor(private _as: IncapacidadService) { }


}


@Component({
    templateUrl: './edit.incapacidad.html'
})
export class EditIncapacidadComponent implements OnInit {

    form: FormGroup;
    columns: string[];
    renderinputs: RenderInput[];
    service = this._s;
    empleadoRender = item => `${item.nombre} ${item.apellidos}`;

    @ViewChild('f') public _form: FormComponent;

    constructor(private _fb: FormBuilder, private _s: IncapacidadService, public _t: TipoIncapacidadService, public _e: EmpleadoService, private _rt: Router) {
        this.form = this._fb.group({
            tipo: [[], Validators.required],
            empleado: [[], Validators.required],
            dias: ['', [Validators.required, Validators.min(1)]],
            fecha: ['', Validators.required]
        });
        this.columns = ['col1'];
        this.renderinputs = [
            { column: 'col1', title: 'Días', type: 'number', name: 'dias' },
            { column: 'col1', title: 'Fecha', type: 'text', name: 'fecha', class: 'datepicker' }
        ];
    }

    itemTipo = item => `${item.tipo__nombre}`;
    itemEmpleado = item => `${item.empleado__nombre} ${item.empleado__apellidos}`;


    ngOnInit() {
        this._form.successful = data => {
            this._rt.navigate(['operacion/incapacidad']);
        }
    }
}
