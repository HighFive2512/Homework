class SteamUser:
    def __init__(self,username:str,games:list):
        self.username = username
        self.games = games
        self.played_hours = 0

    def play(self,game,hours):
        self.game = game
        self.hours = hours

        if self.game in self.games:
            self.played_hours += self.hours
            return f'{self.username} is playing {self.game}'
        else:
            return f'{self.game} is not in library'
    def buy_game(self,game):
        self.game = game
        if self.game in self.games:
            return f'{self.game} is already in your library'
        else:
            self.games.append(self.game)
            return f'{self.username} bought {self.game}'

    def status(self):
        return f'{self.username} has {len(self.games)} games. Total play time: {self.played_hours}'

