import { Component, Input, OnInit, AfterContentChecked } from '@angular/core';
import { FormGroup} from '@angular/forms';
import { ActivatedRoute } from '@angular/router'
import { BsNotify } from '../../lib/bs.notify';

declare var $: any;
declare var swal: any;

export interface RenderInput {
    column: string;
    title: string;
    type: string;
    name: string;
    class?: string;
    error?: string;
    noitem?: boolean;
}

@Component({
    selector: 'ex-form',
    templateUrl: './form.component.html'
})
export class FormComponent implements OnInit {

    @Input('title') title: string;
    @Input('icon') icon: string;
    @Input('columns') columns: string[];
    @Input('renderinputs') renderinputs: RenderInput[];
    @Input('form') form: FormGroup;
    @Input('service') service: any;

    private ready: Boolean = false;
    item: any;

    constructor(private _ar: ActivatedRoute) {

    }

    ngOnInit() {
        if (Object.keys(this._ar.snapshot.data['item']).length !== 0) {
            this.item = this._ar.snapshot.data['item'];
            this.form.patchValue(this.item);
        }
    }

    onLast(last: boolean) {
        if (last) {
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
        if (!!this.service) {
            const body = this.preSave(this.form.value);
            this.ready = true;
            if (!!this.item) {
                this.service.edit(this.item.id, body)
                    .then(data => {
                        this.ready = false;
                        this.successful(data);
                    })
                    .catch(error => {
                        this.ready = false;
                        this.error(error);
                    });
            } else {
                this.service.add(body)
                    .then(data => {
                        this.form.reset();
                        this.ready = false;
                        if (!back) {
                            this.successful(data);
                        }
                    })
                    .catch(error => {
                        this.ready = false;
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
        if (!!this.service && !!this.item) {
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
                        swal('Eliminado!', 'Registros se eliminado con exito', 'success');
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
