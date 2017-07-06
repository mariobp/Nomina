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
        // this._cs.conf('104.236.33.228', '8010');
        this._cs.conf('isabela.com.co', '80');
    }
    ngOnInit() {
        $.material.init();
    }
}
