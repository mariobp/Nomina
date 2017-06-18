import { Component, OnInit } from '@angular/core';
import { CallService } from '../lib/services/call.service';

declare var $: any;

@Component({
    selector: 'ex-nomina',
    templateUrl: './app.component.html',
    styleUrls: ['./app.component.scss']
})

export class AppComponent implements OnInit {
    title = 'angular'
    constructor(private _cs: CallService) {
       this._cs.conf('104.236.33.228', '8000');
        // this._cl.conf('192.168.1.16', '8000');
    }
    ngOnInit() {
        $.material.init();
    }
}
