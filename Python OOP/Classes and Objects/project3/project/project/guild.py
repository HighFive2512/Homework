from project.player import Player
class Guild:
    def __init__(self,name: Player):
        self.name:str = str(name)
        self.players:dict = {}

    def assign_player(self,player:Player) -> str:
        if player.name in self.players:
            return f"Player {player.name} is already in the guild."
        if player.guild != 'Unaffiliated':
            return f"Player {player.name} is in another guild."
        self.players[player.name] = player
        player.guild = self.name
        return f"Welcome player {player.name} to the guild {self.name}"

    def kick_players(self,player_name:str):
        try:
            self.players.pop(player_name)
            return f"Player {player_name} is not in the guild."
        except:
            self.players.pop(player_name)
            Player(player_name).guild = 'Unaffiliated'
            return f"Player {player_name} has been removed from the guild."

    def guild_info(self):
        pinfo = '\n'.join([k.player_info() for k in self.players.values()])
        return f"Guild: {self.name}\n{pinfo}"


