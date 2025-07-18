class Club:
    def __init__(self, name):
        self.name = name
        self.players = []
        
    def __len__(self):
        return len(self.players)
        
    def __getitem__(self,i):
        
        return self.players[i]
        
some_club = Club("Arsenal")
some_club.players.append["Tonono"]
some_club.players.append["Yeray Viera"]
print(len(some_club.players))