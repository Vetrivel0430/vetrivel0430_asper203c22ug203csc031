class player :
    def play(self):
        print("The player is playin cricket")
class batsman(player):
    def play (self):
        print("The Batsman is batting")
class bowler(player):
    def play(self):
        print("The bowler is bowling")
batsman=batsman()
bowler=bowler()
batsman.play()
bowler.play()
