class AbilityScores:
        global player 
        global strength 
        global dexterity 
        global constitution 
        global intelligence 
        global wisdom 
        global charisma 
        def __init__(self, _player,*args):
                self.player = _player
                try:
                        
                        self.strength = args.strength
                        self.dexterity = args.dexterity
                        self.constitution = args.constitution
                        self.intelligence = args.intelligence
                        self.wisdom =  args.wisdom
                        self.charisma = args.charisma
                except:
                        
                        self.strength = 0
                        self.dexterity = 0
                        self.constitution = 0
                        self.intelligence = 0
                        self.wisdom = 0
                        self.charisma = 0

        def getStats(self,_player):
                return {
                        "Player":self.player ,
                        "Strength":self.strength,
                        "Dexterity":self.dexterity,
                        "Constitution":self.constitution,
                        "Intelligence":self.intelligence ,
                        "Wisdom":self.wisdom ,
                        "Charisma":self.charisma 
                }

