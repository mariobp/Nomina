import { BrowserModule } from '@angular/platform-browser';
import { CommonModule } from '@angular/common';
import { HttpModule } from '@angular/http';
import { AppRouteModule } from './app.route.module';
import { AuthModule } from './auth/auth.module';
import { LibModule } from '../lib/lib.module'
import { NgModule } from '@angular/core';
import { CallService } from '../lib/services/call.service';
import { AppComponent } from './app.component';
import { AuthService } from './auth/auth.service';
@NgModule({
    declarations: [
        AppComponent
    ],
    imports: [
        BrowserModule,
        HttpModule,
        CommonModule,
        LibModule,
        AppRouteModule,
        AuthModule,
    ],
    providers: [CallService],
    bootstrap: [AppComponent]
})
export class AppModule { }
