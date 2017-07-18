import { Component, Input, Output, forwardRef, OnInit, EventEmitter } from '@angular/core';
import { ControlValueAccessor, NG_VALUE_ACCESSOR } from '@angular/forms';

@Component({
    selector: 'ex-autocomplete',
    templateUrl: './auto.component.html',
})
export class AutoComponent {
    public options = [];

    @Output() cambio: EventEmitter<any>;
    @Input() service: any;
    @Input() item: any;
    @Input() form: any;
    @Input() name: string
    @Input('value') _value: any = '';
    @Input() render: any = (val: any) => val.nombre;
    @Input() itemVal: any = (item: any) => item.id;
    @Input() params = {};

    displayFn = val => {
        if (this.options.length === 0 && !!this.item) {
            return this.itemVal(this.item);
        } else {
            const value = this.options.filter(data => data.id === val)[0];
            this.cambio.emit({ item: value });
            return val ? (value ? this.render(value) : '') : null;
        }
    }

    get value() {
        return this._value;
    }

    set value(val) {
        this._value = val;
    }

    constructor() {
        this.cambio = new EventEmitter();
    }

    private onKeyPress(event) {
        this.onChange(event.target.value !== '' ? event.target.value : null);

    }
    private onChange(value) {
        this.filterVal(value)

    }

    private onFocus(event) {
        this.filterVal(null);
    }


    writeValue(value) {
        if (value) {
            this.value = value;
        }
    }

    filterVal(val) {
        this.params['q'] = val ? val : '';
        this.service.list(this.params)
            .then(data => data.json())
            .then(data => {
                this.options = data.object_list
            }).catch(error => console.log(error));
    }


}
