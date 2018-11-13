import { Http, Headers, RequestOptions, URLSearchParams, Response } from '@angular/http';
import { Injectable } from '@angular/core';
import { Observable } from 'rxjs/Rx';
import 'rxjs/add/operator/catch';
import 'rxjs/add/operator/map';
import 'rxjs/add/operator/toPromise';

declare var WebSocket: any;
declare var window: any

export interface Ip {
    protocol?: string;
    host: string;
    port?: string;
}

@Injectable()
export class CallService {

    public json: any = { 'Content-Type': 'application/json' };
    public _ip: Ip


    constructor(private _http: Http) {
        window._server = this.ip;
    }


    getUrl(url: string): string {
        const ip = this.ip;
        let auxUrl = `/${url}`;
        if (ip) {
            auxUrl = `${ip}${auxUrl}`;
        }
        return auxUrl;
    }

    conf(ip: Ip) {
        this._ip = ip;
        window._server = this.ip;
    }

    get ip(): string {
        if (!!this._ip) {
            const proto = !!this._ip.protocol ? this._ip.protocol : 'http';
            const port = !!this._ip.port && this._ip.port !== '80' ? `:${this._ip.port}` : '';
            return `${proto}://${this._ip.host}${port}`;
        }
        return '';
    }

    getOptions(headersList: any, par?: any): RequestOptions {
        const options = new RequestOptions();
        const headers = new Headers();
        headersList = headersList || this.json;
        for (const key in headersList) {
            if (headersList[key]) {
                headers.append(key, headersList[key]);
            }
        }
        if (!!par) {
            const query = new URLSearchParams();
            for (const key in par) {
                if (par[key] !== '') {
                    query.set(key, par[key]);
                }
            }
            options.search = query;
        }
        options.headers = headers;
        options.withCredentials = true;
        return options;
    }

    get(url: string, params?: any, head?: any): Promise<Response> {
        return this._http.get(this.getUrl(url), this.getOptions(head, params)).toPromise();
    }

    delete(url: string, head?: any) {
        return this._http.delete(this.getUrl(url), this.getOptions(head)).toPromise();
    }

    head(url: string, head?: any) {
        return this._http.delete(this.getUrl(url), this.getOptions(head)).toPromise();
    }

    post(url: string, body?: any, head?: any): Promise<Response> {
        return this._http.post(this.getUrl(url), body, this.getOptions(head)).toPromise();
    }


    put(url: string, body?: any, head?: any): Promise<Response> {
        return this._http.put(this.getUrl(url), body, this.getOptions(head)).toPromise();
    }

    patch(url: string, body?: any, head?: any): Promise<Response> {
        return this._http.patch(this.getUrl(url), body, this.getOptions(head)).toPromise();
    }

}
