import { Component, OnInit } from '@angular/core';
import { ApiServiceService } from '../api-service.service';

@Component({
  selector: 'app-abilities',
  templateUrl: './abilities.component.html',
  styleUrls: ['./abilities.component.css']
})
export class AbilitiesComponent implements OnInit {
  abilities = [
    {"name": "Strength", "score": 0},
    {"name": "Dexterity", "score": 0},
    {"name": "Constitution", "score": 0},
    {"name": "Intelligence", "score": 0},
    {"name": "Wisdom", "score": 0},
    {"name": "Charisma", "score": 0}
  ]
  isEditing = true;
  user = ""

  constructor(private apiService: ApiServiceService) {
  }

  ngOnInit(): void {
  }

  getAbilities(): void {
    this.apiService.getAbilities(this.user).subscribe(abilities => this.abilities = abilities);
  }

  calculateModifier(value: number) {
    return Math.floor((value - 10)/2)
  }
  

}
