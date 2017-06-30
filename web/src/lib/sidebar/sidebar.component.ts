import { Component, OnInit } from '@angular/core';
import { AppMenuMeta } from '../../app/app.routing';
declare var $: any;

@Component({
    selector: 'ex-sidebar',
    templateUrl: './sidebar.component.html'
})
export class SidebarComponent implements OnInit {

    menuInfo: any[];

    user: any;

    constructor() {
        this.user = JSON.parse(localStorage.getItem('user'));
        console.log(this.user);
    }

    ngOnInit() {
        $.getScript('../../assets/js/sidebar-moving-tab.js');
        this.menuInfo = AppMenuMeta.filter(menuItem => menuItem);
    }

    isNotMobileMenu() {
        if ($(window).width() > 991) {
            return false;
        }
        return true;
    }

}
