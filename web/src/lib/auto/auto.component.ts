import { Component, Input, forwardRef, OnInit } from '@angular/core';
import { ControlValueAccessor, NG_VALUE_ACCESSOR } from '@angular/forms';

@Component({
    selector: 'ex-autocomplete',
    templateUrl: './auto.component.html',
    providers: [
        {
            provide: NG_VALUE_ACCESSOR,
            useExisting: forwardRef(() => AutoComponent),
            multi: true
        }
    ]
})
export class AutoComponent {
    @Input() service: any;
    @Input() item: any;
    @Input() form: any;
    @Input() name: string
    @Input('value') _value: any = '';
    @Input() render: any = (val: any) => val.nombre;
    @Input() itemVal: any = (item: any) => item.id;
    options = [];


    displayFn = val => {
        if (this.options.length === 0 && !!this.item) {
            return this.itemVal(this.item);
        } else {
            const value = this.options.filter(data => data.id === val)[0];
            return val ? (value ? this.render(value) : '') : null;
        }
    }

    get value() {
        return this._value;
    }

    set value(val) {
        this._value = val;
    }

    constructor() { }

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
        this.service.list({ q: val ? val : '' })
            .then(data => data.json())
            .then(data => {
                this.options = data.object_list
            }).catch(error => console.log(error));
    }


}
