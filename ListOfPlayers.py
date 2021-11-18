
class Players:
    _instance = None
    global players
    players = []
    def __new__(cls, *args, **kwargs):
        if not cls._instance:
           
            cls._instance = super(Players, cls).__new__(
                                cls, *args, **kwargs)
        return cls._instance
        
    def addPlayer(self,PlayerID):
        self.players.append(PlayerID)

    def ReturnPlayers(self):
        return self.players