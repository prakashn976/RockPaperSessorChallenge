class RockPaperScissors:

    def CheckWinner(self,player1,player2):
        if player1==player2:
            return "Tie"

        elif player1=="Rock":
                if player2=="Scissors":
                    return "Winner is Player1"
                else:
                    return "Winner is Player2"

        elif player1=="Scissors":
                if player2=="Rock":
                    return "Winner is Player2"
                else:
                    return "Winner is Player1"
        
        else: 
                if player2=="Rock":
                    return "Winner is Player1"
                else:
                    return "Winner is Player2"

        