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
    { path: '', redirectTo: 'operacion/turno', pathMatch: 'full' },
    {
        path: '', component: BaseComponent, canActivate: [AuthGuard], data: { preload: true }, children: [
            // { path: '', loadChildren: './home/home.module#HomeModule' },
            { path: 'operacion', loadChildren: './turno/turno.module#TurnoModule' },
            { path: '', loadChildren: './empleados/empleados.module#EmpleadosModule' },
            { path: '', loadChildren: './nomina/nomina.module#NominaModule' },
            { path: '', loadChildren: './empleados/empleados.module#EmpleadosModule' },
            { path: 'produccion', loadChildren: './turno/turno.module#TurnoModule' },
            { path: 'usuarios', loadChildren: './usuarios/usuarios.module#UsuariosModule' },
            { path: 'obligaciones', loadChildren: './obligaciones/obligaciones.module#ObligacionesModule', },
            { path: 'configuracion', loadChildren: './configuracion/configuracion.module#ConfiguracionModule' },
            { path: 'incapacidad', loadChildren: './incapacidad/incapacidad.module#IncapacidadModule' }
        ]
    },
    // { path: '**', component: P404Component }
];

import { UsuariosMenuMeta } from './usuarios/route';
import { ObligacionesMenuMeta } from './obligaciones/route';
import { ConfiguracionMenuMeta } from './configuracion/configuracion.route';
import { ProduccionMenuMeta } from './turno/route';
import { IncapacidadMenuMeta } from './incapacidad/route';

export const AppMenuMeta: MenuMeta[] = [
    // { title: 'Inico', url: '/dashboard', icon: 'dashboard' },
    { title: 'Usuarios', icon: 'supervisor_account', children: UsuariosMenuMeta },
    { title: 'Operación', icon: 'work', children: ProduccionMenuMeta },
    { title: 'Obligaciones', icon: 'assignment', children: ObligacionesMenuMeta },
    { title: 'Empleados', icon: 'account_box', url: '/empleados' },
    { title: 'Nomina', icon: 'monetization_on', url: '/nomina' },
    { title: 'Incapacidad', icon: 'accessible', children: IncapacidadMenuMeta },
    { title: 'Configuración', icon: 'settings_applications', children: ConfiguracionMenuMeta }
];
