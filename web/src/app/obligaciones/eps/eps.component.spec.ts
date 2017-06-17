import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { EpsComponent } from './eps.component';

describe('EpsComponent', () => {
  let component: EpsComponent;
  let fixture: ComponentFixture<EpsComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ EpsComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(EpsComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should be created', () => {
    expect(component).toBeTruthy();
  });
});
