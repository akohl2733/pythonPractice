class Player:

    def __init__(self, name: str, position: str, team: str):
        self.name = name
        self.team = team
        self.position = position
        self.yards = 0
        self.touchdowns = 0

    def add_touchdowns(self, tds: int):
        if not isinstance(tds, int) or tds <= 0:
            raise ValueError
        self.touchdowns += tds
        

    def add_yards(self, yards: int):
        if not isinstance(yards, int) or yards <= 0:   
            raise ValueError
        self.yards += yards

    def __str__(self) -> str:
        return f'{self.name} is a {self.position} on the {self.team}.\nHe has {self.yards} yards and {self.touchdowns} TDs.'
    

player1 = Player("Justin Jefferson", "Wide Receiver", 'Vikings')
player2 = Player("Breece Hall", "Running Back", "NYJ")