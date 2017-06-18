import { Routes } from '@angular/router';

import { BaseComponent } from '../lib/base/base.component';
import { P404Component } from '../lib/404/404.component';
import { AuthGuard } from './auth/auth.guard';

export interface MenuMeta {
    title: string;
    url?: string;
    icon: string;
    children?: MenuMeta[];
}

export const AppRoutes: Routes = [
    { path: '', redirectTo: 'dashboard', pathMatch: 'full' },
    {
        path: '', component: BaseComponent, canActivate: [AuthGuard], data: { preload: true }, children: [
            { path: '', loadChildren: './home/home.module#HomeModule' },
            { path: 'usuarios', loadChildren: './usuarios/usuarios.module#UsuariosModule' },
            { path: 'obligaciones', loadChildren: './obligaciones/obligaciones.module#ObligacionesModule' },
            /*{ path: 'novedades', loadChildren: './novedades/novedades.module#NovedadesModule' },
            { path: 'informes', loadChildren: './informes/informes.module#InformesModule' },
            { path: 'perfil', loadChildren: './usuarios/usuarios.module#UsuariosModule' },*/
        ]
    },
    { path: '**', component: P404Component }
];

import { UsuariosMenuMeta } from './usuarios/route';
import { ObligacionesMenuMeta } from './obligaciones/route';

export const AppMenuMeta: MenuMeta[] = [
    { title: 'Inico', url: '/dashboard', icon: 'dashboard' },
    { title: 'Usuarios', icon: 'supervisor_account', children: UsuariosMenuMeta },
    { title: 'Obligaciones', icon: 'assignment', children: ObligacionesMenuMeta },
];
