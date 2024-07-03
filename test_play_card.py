class unogame:
    def test_play_card(self):
        game = unogame(['Player 1', 'Player 2'])
        game.hand[0] = ['0','1']
        assert game.play_card('0')
        assert '0' not in game.hand[0]