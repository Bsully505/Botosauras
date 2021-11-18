import { Component, OnInit } from '@angular/core';
import { ApiServiceService } from '../api-service.service';

@Component({
  selector: 'app-abilities',
  templateUrl: './abilities.component.html',
  styleUrls: ['./abilities.component.css']
})
export class AbilitiesComponent implements OnInit {
  abilities = [
    {"name": "", "score": 0}
  ]
  isEditing = true;

  constructor(private apiService: ApiServiceService) {
  }

  ngOnInit(): void {
   this.getAbilities()
  }

  getAbilities(): void {
    this.apiService.getAbilities().subscribe(abilities => this.abilities = abilities);
  }

  calculateModifier(value: number) {
    return Math.floor((value - 10)/2)
  }
  

}
