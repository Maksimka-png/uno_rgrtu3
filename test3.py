class draw_card():
    def test_draw_card():
        game = unogame(['Player 1','Player 2'])
        game.deal_cards()
        hand_size_before = len(game.hand[0])
        game.draw_card()
        assert len(game.hand[0]) == hand_size_before + 1