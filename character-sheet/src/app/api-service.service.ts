import { Injectable } from '@angular/core';
import { Observable, of} from 'rxjs';
import { Ability } from './Ability';
import { HttpClient } from '@angular/common/http';

@Injectable({
  providedIn: 'root'
})
export class ApiServiceService {
  url = 'https://slackevent.herokuapp.com/'

  constructor(private http: HttpClient) { }

  getAbilities(user: String): Observable<Ability[]> {
    const abilities = of([
        {"name": "STRENGTH", "score": 20},
        {"name": "DEXTERITY",  "score": 20}, 
        {"name": "CONSTITUTION", "score": 20},
        {"name": "INTELLIGENCE", "score": 20},
        {"name": "WISDOM", "score": 20},
        {"name": "CHARISMA", "score": 20}
    ])
    let player = {}

    this.http.get(this.url + "players/" + user).subscribe((player) => {
      player = player
    })
    
    return abilities
  }
}
