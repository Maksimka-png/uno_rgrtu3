class check_win():
    def test_check_win():
        game = unogame(['Player 1', 'Player 2'])
        game.hand[0] = []
        assert game.check_win()