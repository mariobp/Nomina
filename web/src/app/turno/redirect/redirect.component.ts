import { Component, OnInit } from '@angular/core';
import { ActivatedRoute, Router } from '@angular/router';

@Component({
  selector: 'ex-redirect',
  templateUrl: './redirect.component.html',
  styleUrls: ['./redirect.component.scss']
})
export class RedirectComponent implements OnInit {

  constructor(
    private router: Router,
    private active: ActivatedRoute
  ) { }

  ngOnInit() {
    const redirect = this.active.snapshot.queryParams['url'];
    console.log('snapshot', redirect);
    const url = redirect ? redirect : '/';
    console.log('url', url);
    this.router.navigate([url]);
  }

}
