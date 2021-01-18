import unittest
from RockPaperScissorChallenge import RockPaperScissorsChallenge
from RockPaperScissor import RockPaperScissors

class TestRockPaperScissorsChallenge(unittest.TestCase):   

    def test_Tie(self):
            arrayinput=["Tie" ,"Tie","Tie"]
            result=RockPaperScissorsChallenge.Checkroundwinner(self,arrayinput)
            self.assertEqual("Tie",result)

    def test_Player1IsWinner_IfAllGamesWonByPlayer1(self):
            arrayinput=["Player1" ,"Player1","Player1"]
            result=RockPaperScissorsChallenge.Checkroundwinner(self,arrayinput)
            self.assertEqual("Player1 is winner",result)
    
    def test_Player2IsWinner_IfAllGamesWonByPlayer2(self):
            arrayinput=["Player2" ,"Player2","Player2"]
            result=RockPaperScissorsChallenge.Checkroundwinner(self,arrayinput)
            self.assertEqual("Player2 is winner",result)

    def test_Player1IsWinner_IfPlayer1WinsTwoGames(self):
            arrayinput=["Player1" ,"Player1","Player2"]
            result=RockPaperScissorsChallenge.Checkroundwinner(self,arrayinput)
            self.assertEqual("Player1 is winner",result)

    def test_Player1IsWinner_IfPlayer1WinsOneGameOtherTwoTie(self):
            arrayinput=["Player1" ,"Tie","Tie"]
            result=RockPaperScissorsChallenge.Checkroundwinner(self,arrayinput)
            self.assertEqual("Player1 is winner",result)

    def test_Player2IsWinner_IfPlayer2WinsTwoGames(self):
            arrayinput=["Player2" ,"Player2","Player1"]
            result=RockPaperScissorsChallenge.Checkroundwinner(self,arrayinput)
            self.assertEqual("Player2 is winner",result)

    def test_Player2IsWinner_IfPlayer2WinsOneGameOtherTwoTie(self):
            arrayinput=["Player2" ,"Tie","Tie"]
            result=RockPaperScissorsChallenge.Checkroundwinner(self,arrayinput)
            self.assertEqual("Player2 is winner",result)

    def test_TieIfPlayer1AndPlayer2AreSame(self):
        result=RockPaperScissors.CheckWinner(self,"Paper","Paper")
        self.assertEqual("Tie",result)

    def test_Player1IsWinnerWhenPlayer1IsRockAndPlayer2IsScissors(self):
        result=RockPaperScissors.CheckWinner(self,"Rock","Scissors")
        self.assertEqual("Winner is Player1",result)

    def test_Player2IsWinnerWhenPlayer1IsRockAndPlayer2IsPaper(self):
        result=RockPaperScissors.CheckWinner(self,"Rock","Paper")
        self.assertEqual("Winner is Player2",result)

    def test_Player1IsWinnerWhenPlayer1IsScissorsAndPlayer2IsPaper(self):
        result=RockPaperScissors.CheckWinner(self,"Scissors","Paper")
        self.assertEqual("Winner is Player1",result)

    def test_Player2IsWinnerWhenPlayer1IsScissorsAndPlayer2IsRock(self):
        result=RockPaperScissors.CheckWinner(self,"Scissors","Rock")
        self.assertEqual("Winner is Player2",result)

    def test_Player1IsWinnerWhenPlayer1IsPaperAndPlayer2IsRock(self):
        result=RockPaperScissors.CheckWinner(self,"Paper","Rock")
        self.assertEqual("Winner is Player1",result)

    def test_Player2IsWinnerWhenPlayer1IsPaperAndPlayer2IsScissors(self):
        result=RockPaperScissors.CheckWinner(self,"Paper","Scissors")
        self.assertEqual("Winner is Player2",result)

    def test_test_Player2IsWinnerWhenPlayer1IsPaperAndPlayer2IsScissors(self):
        result=RockPaperScissors.CheckWinner(self,"Paper","Scissors")
        self.assertEqual("Winner is Player2",result)
    
if __name__ == '__main__':
    unittest.main()
