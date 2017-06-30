import { Component, Input } from '@angular/core';
import { AuthService } from '../../app/auth/auth.service';
@Component({
    selector: 'ex-navbar',
    templateUrl: 'navbar.component.html',
})
export class NavbarComponent {

    @Input('right') private right = false;
    @Input('mobile') private mobile = false;

    constructor(private _as: AuthService) { }
}
