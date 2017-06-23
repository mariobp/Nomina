import { Component, Input, OnInit } from '@angular/core';
import { FormGroup} from '@angular/forms';
import { ActivatedRoute } from '@angular/router'

declare var $: any;

export interface RenderInput {
    column: string;
    title: string;
    type: string;
    name: string;
    class?: string;
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

    item: any;

    constructor(private _ar: ActivatedRoute) {

    }

    ngOnInit() {
        if (Object.keys(this._ar.snapshot.data['item']).length !== 0) {
            this.item = this._ar.snapshot.data['item'];
            this.form.patchValue(this.item);
        }
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

    isRender(col1, col2, item): boolean {
        if (item) {
            return col1 === col2 && !this.item;
        } else {
            return col1 === col2;
        }
    }

    save() {
        console.error('Debes sobre escribir la function save()');
    }
}
