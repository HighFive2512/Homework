from project.player import Player


class Guild:
    def __init__(self, name: Player):
        self.name: str = str(name)
        self.players: dict = {}

    def assign_player(self, player: Player) -> str:
        if player.name in self.players:
            return f"Player {player.name} is already in the guild."
        if player.guild != "Unaffiliated":
            return f"Player {player.name} is in another guild."
        self.players[player.name] = player
        player.guild = self.name
        return f"Welcome player {player.name} to the guild {self.name}"

    def kick_players(self, player_name: str):
        if player_name not in self.players:
            return f"Player {player_name} is not in the guild."
        else:
            kicked_player = self.players.pop(player_name)
            kicked_player.guild = "Unaffiliated"
            self.players[player_name] = "Unaffiliated"
            return f"Player {player_name} has been removed from the guild."

    def guild_info(self):
        return "\n".join([k.player_info() for k in self.players.values()])


player = Player("George", 50, 100)
print(player.add_skill("Shield Break", 20))
print(player.player_info())
guild = Guild("UGT")
print(guild.assign_player(player))
print(guild.guild_info())
print(guild.kick_players(player))
print(guild.guild_info())
print(guild.guild_info())
print(guild.guild_info())
print(guild.guild_info())
