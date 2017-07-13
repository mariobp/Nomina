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
    options = [];
    complete: Promise<any>;
    constructor() {

    }

    @Input() render = item => item.id;
    ngOnInit() {
        this.service.list({ num_page: 0 })
            .then(data => data.json())
            .then(data => {
                this.options = data.object_list;
                this.complete = Promise.resolve();
            }).catch(error => console.log(error));

        if (!!this.item && this.item[this.name]) {
            this.form[this.name] = this.item[this.name];
        }
    }

}
