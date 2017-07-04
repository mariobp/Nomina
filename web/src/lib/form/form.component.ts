import { Component, Input, OnInit, AfterViewInit } from '@angular/core';
import { FormGroup} from '@angular/forms';
import { ActivatedRoute } from '@angular/router'
import { BsNotify } from '../../lib/bs.notify';

declare var $: any;
declare var swal: any;
export interface SelectInput {
    title: string;
    value: any;
}
export interface RenderInput {
    column: string;
    title: string;
    type: string;
    name: string;
    isSelect?: boolean;
    multiple?: boolean;
    disabled?: boolean;
    step?: string;
    options?: SelectInput[];
    class?: string;
    error?: string;
    noitem?: boolean;
}

@Component({
    selector: 'ex-form',
    templateUrl: './form.component.html'
})
export class FormComponent implements OnInit, AfterViewInit {

    @Input('title') title: string;
    @Input('icon') icon: string;
    @Input('columns') columns: string[];
    @Input('renderinputs') renderinputs: RenderInput[];
    @Input('form') form: FormGroup;
    @Input('service') service: any;
    @Input('deleteable') public deleteable = true;
    @Input('saveable') public saveable = true;
    public _ready: boolean;
    item: any;
    private errorMessages = {
        email: 'texto para error de email'
    }
    constructor(private _ar: ActivatedRoute) { }

    setReady(val: boolean) {
        this._ready = val;
    }

    setItem(item: any) {
        item = this.prePatchValue(item);
        this.item = item;
        this.form.patchValue(this.item);
        if ($('.selectpicker').length !== 0) {
            $('.selectpicker').selectpicker('refresh')
        }
    }

    prePatchValue(value) {
        return value;
    }

    ngOnInit() {
        if (!!this._ar.snapshot.data['item'] && Object.keys(this._ar.snapshot.data['item']).length !== 0) {
            this.setItem(this._ar.snapshot.data['item']);
        }
        this.form.valueChanges.subscribe(data => this.onValueChanged(data));
    }

    ngAfterViewInit() {
        if ($('.selectpicker').length !== 0) {
            $('.selectpicker').selectpicker();
        }
        $('.datetimepicker').datetimepicker({
            format: 'DD/MM/YYYY h:mm A',
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
        $('.datepicker').datetimepicker({
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
                close: 'fa fa-remove',
                inline: true
            }
        });
        $('.timepicker').datetimepicker({
            // format: 'H:mm',    // use this format if you want the 24hours timepicker
            format: 'h:mm A',    // use this format if you want the 12hours timpiecker with AM/PM toggle
            icons: {
                time: 'fa fa-clock-o',
                date: 'fa fa-calendar',
                up: 'fa fa-chevron-up',
                down: 'fa fa-chevron-down',
                previous: 'fa fa-chevron-left',
                next: 'fa fa-chevron-right',
                today: 'fa fa-screenshot',
                clear: 'fa fa-trash',
                close: 'fa fa-remove',
                inline: true
            }
        });

        const self = this;

        $('.datetimepicker').on('dp.change', function(e) {
            self.form.get($(this).attr('ng-reflect-name')).setValue($(this).datetimepicker({ format: 'DD/MM/YYYY h:mm A' }).val());
        });
        $('.datepicker').on('dp.change', function(e) {
            self.form.get($(this).attr('ng-reflect-name')).setValue($(this).datetimepicker({ format: 'DD/MM/YYYY' }).val());
        });
        $('.timepicker').on('dp.change', function(e) {
            self.form.get($(this).attr('ng-reflect-name')).setValue($(this).datetimepicker({ format: 'h:mm A' }).val());
        });
    }

    onValueChanged(data) {
        if (!this.form) { return; }
        for (const input of this.renderinputs) {
            input.error = (() => {
                const control = this.form.get(input.name);
                if (control && control.dirty && !control.valid) {
                    let res = '';
                    for (const key in control.errors) {
                        if (!!control.errors[key]) {
                            res += this.errorMessages[key] || key + ' ';
                        }
                    }
                    return res;
                }
                return null;
            })();
        }
    }

    isValid(): boolean {
        return this.form.valid;
    }

    isRender(col1, col2, item): boolean {
        if (item) {
            return col1 === col2 && !this.item;
        } else {
            return col1 === col2;
        }
    }

    save(back?: boolean) {

        if (!!this.service && this.form.valid) {
            const body = this.preSave(this.form.value);
            console.log(body)
            this._ready = true;
            if (!!this.item) {
                this.service.edit(this.item.id, body)
                    .then(data => {
                        this._ready = false;
                        this.successful(data);
                        swal({
                            title: 'Guardado!',
                            text: 'Registro se guardo con exito',
                            type: 'success',
                            confirmButtonColor: '#213b78',
                        });
                    })
                    .catch(error => {
                        this._ready = false;
                        this.error(error);
                    });
            } else {
                this.service.add(body)
                    .then(data => {
                        this.form.reset();
                        this._ready = false;
                        swal({
                            title: 'Guardado!',
                            text: 'Registro se guardo con exito',
                            type: 'success',
                            confirmButtonColor: '#213b78',
                        });
                        if (!back) {
                            this.successful(data);
                        }
                    })
                    .catch(error => {
                        this._ready = false;
                        this._findErros(error.json());
                        this.error(error);
                    });
            }
        } else {
            console.error('no se ha definido un service para este formulario')
        }
    }
    _findErros(errs) {
        if (errs) {
            for (const input of this.renderinputs) {
                input.error = (() => {
                    for (const key in errs) {
                        if (!!errs[key] && input.name === key) {
                            return errs[key];
                        }
                    }
                    return null;
                })();
            }
        }

    }

    delete() {
        if (!!this.service && !!this.item && this.deleteable) {
            swal({
                title: 'Está seguro?',
                text: 'Se eliminará 1 registro.',
                type: 'warning',
                showCancelButton: true,
                confirmButtonColor: '#213b78',
                cancelButtonColor: '#ff9800',
                cancelButtonText: 'Cancelar',
                confirmButtonText: 'Eliminar'
            }).then(() => {
                this.service.delete(this.item.id)
                    .then(data => {
                        this.successful(data);
                        swal({
                            title: 'Eliminado!',
                            text: 'Registros se eliminado con exito',
                            type: 'success',
                            confirmButtonColor: '#213b78',
                        });
                    })
                    .catch(err => {
                        BsNotify.error('No se han podido eliminar los registros');
                        console.error(err);
                    })
            }, () => { });
        }
    }

    preSave(body): any {
        return body;
    }

    successful(data) { }

    error(error) {
        BsNotify.error('Ha ocurrido un error al intentar gurdar los datos')
    }
}
