class Equipment:
    def __init__(self, _player):
        self.player = _player
        self.items = {}
        self.currency = {
            "copper": 0,
            "silver": 0,
            "electrum": 0,
            "gold": 0,
            "platinum": 0
        }
