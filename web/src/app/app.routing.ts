import { Routes } from '@angular/router';

import { BaseComponent } from '../lib/base/base.component';
import { P404Component } from '../lib/404/404.component';
import { AuthGuard } from './auth/auth.guard';

export interface MenuMeta {
    title: string;
    icon: string;
    url?: string;
    children?: MenuMeta[];
}

export const AppRoutes: Routes = [
    { path: '', redirectTo: 'turno', pathMatch: 'full' },
    {
        path: '', component: BaseComponent, canActivate: [AuthGuard], data: { preload: true }, children: [
            // { path: '', loadChildren: './home/home.module#HomeModule' },
            { path: '', loadChildren: './turno/turno.module#TurnoModule' },
            { path: '', loadChildren: './empleados/empleados.module#EmpleadosModule' },
            { path: '', loadChildren: './nomina/nomina.module#NominaModule' },
            { path: 'usuarios', loadChildren: './usuarios/usuarios.module#UsuariosModule' },
            { path: 'obligaciones', loadChildren: './obligaciones/obligaciones.module#ObligacionesModule', },
            { path: 'configuracion', loadChildren: './configuracion/configuracion.module#ConfiguracionModule' }
        ]
    },
    // { path: '**', component: P404Component }
];

import { UsuariosMenuMeta } from './usuarios/route';
import { ObligacionesMenuMeta } from './obligaciones/route';
import { ConfiguracionMenuMeta } from './configuracion/configuracion.route';

export const AppMenuMeta: MenuMeta[] = [
    // { title: 'Inico', url: '/dashboard', icon: 'dashboard' },
    { title: 'Usuarios', icon: 'supervisor_account', children: UsuariosMenuMeta },
    { title: 'Turno', icon: 'assignment_ind', url: '/turno' },
    { title: 'Obligaciones', icon: 'assignment', children: ObligacionesMenuMeta },
    { title: 'Empleados', icon: 'account_box', url: '/empleados' },
    { title: 'Nomina', icon: 'monetization_on', url: '/nomina' },
    { title: 'Configuración', icon: 'settings_applications', children: ConfiguracionMenuMeta }
];
