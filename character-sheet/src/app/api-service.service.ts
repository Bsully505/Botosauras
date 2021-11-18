import { Injectable } from '@angular/core';
import { Observable, of} from 'rxjs';
import { Ability } from './Ability';

@Injectable({
  providedIn: 'root'
})
export class ApiServiceService {

  constructor() { }

  getAbilities(): Observable<Ability[]> {
    const abilities = of([
        {"name": "STRENGTH", "score": 20},
        {"name": "DEXTERITY",  "score": 20}, 
        {"name": "CONSTITUTION", "score": 20},
        {"name": "INTELLIGENCE", "score": 20},
        {"name": "WISDOM", "score": 20},
        {"name": "CHARISMA", "score": 20}
    ])
    
    return abilities
  }
}
