import { Component, OnInit } from '@angular/core';
import { CallService } from '../lib/services/call.service';

declare var $: any;

@Component({
    selector: 'ex-nomina',
    template: `<router-outlet></router-outlet>`,
    styleUrls: ['./app.component.scss']
})

export class AppComponent implements OnInit {
    title = 'angular'
    constructor(private _cs: CallService) {
        this._cs.conf({ host: '13.58.110.230', port: '8888' });
        // this._cs.conf({ host: 'isabela.com.co' });
    }
    ngOnInit() {
        $.material.init();
    }
}
