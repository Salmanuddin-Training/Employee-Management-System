import { ComponentFixture, TestBed } from '@angular/core/testing';

import { CrudOperarionsComponent } from './crud-operarions.component';

describe('CrudOperarionsComponent', () => {
  let component: CrudOperarionsComponent;
  let fixture: ComponentFixture<CrudOperarionsComponent>;

  beforeEach(() => {
    TestBed.configureTestingModule({
      declarations: [CrudOperarionsComponent]
    });
    fixture = TestBed.createComponent(CrudOperarionsComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
