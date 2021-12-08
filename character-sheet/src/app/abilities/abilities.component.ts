import { Component, OnInit } from '@angular/core';
import { ApiServiceService } from '../api-service.service';

@Component({
  selector: 'app-abilities',
  templateUrl: './abilities.component.html',
  styleUrls: ['./abilities.component.css']
})
export class AbilitiesComponent implements OnInit {

  abilities =
    {"Charisma": 0,
    "Constitution": 0,
    "Dexterity": 0,
    "Intelligence": 0,
    "Strength": 0,
    "Wisdom": 0}
  isEditing = true;
  user = ""

  constructor(private apiService: ApiServiceService) {
  }

  ngOnInit(): void {
  }

  getAbilities(): void {
    this.apiService.getAbilities(this.user).subscribe(player => {
      this.abilities = player[this.user].AbilityScore
    });
    
  }

  calculateModifier(value: number) {
    return Math.floor((value - 10)/2)
  }
  

}
