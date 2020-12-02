import { Component, OnInit } from '@angular/core';
import { cityItems } from './city-items';
import { FormGroup, FormControl } from '@angular/forms';

@Component({
  selector: 'app-landing',
  templateUrl: './landing.component.html',
  styleUrls: ['./landing.component.scss']
})
export class LandingComponent implements OnInit {

  cityItems : cityItems[] = [
    {
      city: 'Bangalore',
      route:'',
    },
    {
      city: 'Chennai',
      route: ''
    }
  ]

  constructor() { }

  ngOnInit(): void {
  }

}
