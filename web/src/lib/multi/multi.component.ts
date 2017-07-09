import { Component, Input, forwardRef, OnInit } from '@angular/core';

@Component({
    selector: 'ex-multi',
    templateUrl: './multi.component.html'
})
export class MultiComponent implements OnInit {
    @Input() service: any;
    @Input() item: any;
    @Input() form: any;
    @Input() name: string;
    @Input() placeholder: string;
    @Input() render = item => item.id;

    options = [];


    constructor() {

    }

    ngOnInit() {
        this.service.list({})
            .then(data => data.json())
            .then(data => {
                this.options = data.object_list
            }).catch(error => console.log(error));


        if (!!this.item && this.item[this.name]) {
            console.log(this.item);
            this.form[this.name] = this.item[this.name];
        }
    }
}
