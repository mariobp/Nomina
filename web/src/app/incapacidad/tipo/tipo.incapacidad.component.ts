import { Component, OnInit, ViewChild, AfterViewInit } from '@angular/core';
import { TableComponent } from '../../../lib/components';
import { TipoIncapacidadService } from './tipo.incapacidad.service';
import { Router } from '@angular/router';
import { FormGroup, FormControl, Validators, FormBuilder } from '@angular/forms';
import { RenderInput, FormComponent } from '../../../lib/components';

@Component({
    template: '<router-outlet></router-outlet>'
})

export class TipoIncapacidadComponent { }


@Component({
    templateUrl: './list.tipo.incapacidad.component.html'
})
export class TipoIncapacidadListComponent {
    service = this._s;
    multiselect = true;
    aggregable = false;
    editable = false;
    deleteable = false;


    columns = [
        {
            className: 'text-center',
            orderable: false,
            searchable: false,
            data: 'id',
            render: TableComponent.renderCheckRow
        },
        { data: 'nombre' }
    ];


    constructor(private _s: TipoIncapacidadService) { }

}


@Component({
    template: `<ex-form #f icon="accessible" title="Tipo de Incapacidad"
        [form]="form"
        [service]="service"
        [columns]="columns"
        [renderinputs]="renderinputs"></ex-form>`
})
export class TipoIncapacidadEditComponent implements OnInit {

    form: FormGroup;
    columns: string[];
    renderinputs: RenderInput[];
    service = this._s;

    @ViewChild('f') private _form: FormComponent;

    constructor(private _fb: FormBuilder, private _s: TipoIncapacidadService, private _rt: Router) {
        this.form = this._fb.group({
            nombre: ['', [Validators.required]]
        });
        this.columns = ['col1'];
        this.renderinputs = [
            { title: 'Nombre', column: 'col1', name: 'nombre', type: 'text' }
        ];
    }

    ngOnInit() {
        this._form.successful = data => {
            this._rt.navigate(['incapacidad/tipo']);
        }
    }
}
