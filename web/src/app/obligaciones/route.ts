import { Routes } from '@angular/router';
import { MenuMeta } from '../app.routing';

import { PensionComponent, PensionListComponent } from './pension/pension.component';
import { EpsComponent, EpsListComponent } from './eps/eps.component';
import { CompensacionComponent, CompensacionListComponent } from './compensacion/compensacion.component';
import { CesantiasComponent, CesantiasListComponent } from './cesantias/cesantias.component';


export const ObligacionesRoutes: Routes = [
    {
        path: '', children: [
            { path: 'pension', component: PensionComponent , children:[
                { path: '', component: PensionListComponent },
            ]},
            { path: 'eps', component: EpsComponent, children: [
                { path: '', component: EpsListComponent } ,
            ]},
            { path: 'compensacion', component: CompensacionComponent, children: [
                { path: '', component: CompensacionListComponent}
            ]},
            { path: 'cesantias', component: CesantiasComponent, children:[
                { path: '', component: CesantiasListComponent}
            ] }
        ]
    }

];

export const ObligacionesMenuMeta: MenuMeta[] = [
    { title: 'Pensión', url: '/obligaciones/pension', icon: 'extension' },
    { title: 'Eps', url: '/obligaciones/eps', icon: 'extension' },
    { title: 'Caja de Compensación', url: '/obligaciones/compensacion', icon: 'extension' },
    { title: 'Cesantías', url: '/obligaciones/cesantias', icon: 'extension' },
];
