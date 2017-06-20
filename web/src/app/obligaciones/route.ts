import { Routes } from '@angular/router';
import { MenuMeta } from '../app.routing';

import { SaludComponent } from './salud/salud.component';
import { EpsComponent } from './eps/eps.component';
import { CompensacionComponent } from './compensacion/compensacion.component';
import { CesantiasComponent } from './cesantias/cesantias.component';


export const ObligacionesRoutes: Routes = [
    {
        path: '', children: [
            { path: 'salud', component: SaludComponent },
            { path: 'eps', component: EpsComponent },
            { path: 'compensacion', component: CompensacionComponent },
            { path: 'cesantias', component: CesantiasComponent }
        ]
    }

];

export const ObligacionesMenuMeta: MenuMeta[] = [
    { title: 'Salud', url: '/obligaciones/salud', icon: 'extension' },
    { title: 'Eps', url: '/obligaciones/eps', icon: 'extension' },
    { title: 'Caja de Compensación', url: '/obligaciones/compensacion', icon: 'extension' },
    { title: 'Casantias', url: '/obligaciones/cesantias', icon: 'extension' },
];
