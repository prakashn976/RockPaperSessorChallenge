class RockPaperScissorsChallenge:
   
    def Checkroundwinner(self,arrayinput): 
        
        player1count=0
        player2count=0

        for x in arrayinput:
            RoundWinner=x   

            if RoundWinner=="Player1":
                player1count=player1count+1

            elif RoundWinner=="Player2":
                player2count=player2count+1
    
        if player1count>player2count: 
            return "Player1 is winner"

        elif player2count>player1count:
            return "Player2 is winner"
        else:
            return "Tie"
        

             