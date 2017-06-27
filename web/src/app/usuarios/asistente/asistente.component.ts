import { Component, OnInit, ViewChild } from '@angular/core';
import { ActivatedRoute } from '@angular/router';
import { FormGroup, FormControl, Validators, FormBuilder } from '@angular/forms';
import { TableComponent } from '../../../lib/table/table.component';
import { AsistenteService } from './asistente.service';

declare var $: any;

@Component({
    template: '<router-outlet></router-outlet>'
})
export class AsistenteComponent { }

@Component({
    templateUrl: './edit.asistente.component.html'
})
export class AsistenteEditComponent implements OnInit {

    form: FormGroup;
    asistente: any;

    constructor(private _ar: ActivatedRoute, private _fb: FormBuilder, private _as: AsistenteService) {

        this.form = this._fb.group({
            username: ['', Validators.required],
            password1: ['', Validators.required],
            password2: ['', Validators.required],
            email: ['', Validators.required],
            first_name: ['', Validators.required],
            last_name: ['', Validators.required],
            identificacion: ['', Validators.required],
            fecha_nacimiento: ['', Validators.required],
            direccion: ['', Validators.required],
            telefono: ['', Validators.required],
            fijo: ['', Validators.required]
        });
        this.asistente = this._ar.snapshot.data['asistente'];
        this.form.patchValue(this.asistente);
    }

    ngOnInit() {
        $('.datetimepicker').datetimepicker({
            format: 'DD/MM/YYYY',
            icons: {
                time: 'fa fa-clock-o',
                date: 'fa fa-calendar',
                up: 'fa fa-chevron-up',
                down: 'fa fa-chevron-down',
                previous: 'fa fa-chevron-left',
                next: 'fa fa-chevron-right',
                today: 'fa fa-screenshot',
                clear: 'fa fa-trash',
                close: 'fa fa-remove'
            }
        });
    }

    isValid(): boolean {
        return this.form.valid;
    }

    save() {
        console.log('save');
        if (!!this.asistente.id) {
            this._as.edit(this.asistente.id, this.form.value);
        } else {
            this._as.add(this.form.value);
        }
    }
}

@Component({
    templateUrl: './list.asistente.component.html'
})
export class AsistenteListComponent {

    @ViewChild('table') private table: TableComponent;

    icon = 'supervisor_account';
    title = 'Asistente';
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
        { data: 'username' },
        { data: 'first_name' },
        { data: 'last_name' },
        { data: 'identificacion' },
        { data: 'email' },
        { data: 'telefono' },
        {
            className: 'ex-table-btn',
            orderable: false,
            searchable: false,
            data: 'id'
        },
    ];

    constructor(private _as: AsistenteService) { }
}
