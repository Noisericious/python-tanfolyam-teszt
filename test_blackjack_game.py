import importlib
import sys
import pytest
import builtins



@pytest.fixture
def blackjack_module(monkeypatch):
    inputs = iter([
        "0", # tétes input
        "m", # húz v megáll
        "n" # új játék
    ])
    monkeypatch.setattr(builtins, "input", lambda prompt="" : next(inputs))
    module = importlib.import_module("blackjack_game")
    yield module
    sys.modules.pop("blackjack_game", None)


def test_carddata_constructor_raises(blackjack_module):
    CardData = blackjack_module.CardData
    with pytest.raises(RuntimeError):
        CardData()


@pytest.mark.parametrize("rank, value", [
    ("kettő", 2),
    ("három", 3),
    ("kilenc", 9),
    ("bubi", 10),
    ("ász", 11)
])
def test_carddata_get_value_valid(blackjack_module, rank, value):
    CardData = blackjack_module.CardData
    assert CardData.get_value(rank) == value

def test_carddata_get_value_invalid(blackjack_module):
    CardData = blackjack_module.CardData
    with pytest.raises(ValueError):
        CardData.get_value("invalid")

def test_valid_and_str(blackjack_module):
    Card = blackjack_module.Card
    c = Card("kör", "kettő")
    assert c.color == "kör"
    assert c.rank == "kettő"
    assert str(c) == "kettő - kör"

@pytest.mark.parametrize("bad_color", ["K", "12", "AB"])
def test_invalid_color(blackjack_module, bad_color):
    Card = blackjack_module.Card
    with pytest.raises(ValueError):
        Card(bad_color, "ketto")

@pytest.mark.parametrize("bad_rank", ["A", "Z", ""])
def test_invalid_rank(blackjack_module, bad_rank):
    Card = blackjack_module.Card
    with pytest.raises(ValueError):
        Card("kör", bad_rank)

def test_deck_init_lenght(blackjack_module):
    Deck = blackjack_module.Deck
    deck = Deck()
    expected_lenght = len(blackjack_module.Carddata.colors) * len(blackjack_module.Carddata.ranks)
    assert len(deck) == expected_lenght

def test_deck_mix_calls_shuffle(monkeypatch, blackjack_module):
    Deck = blackjack_module.Deck
    calls = []
    monkeypatch.setattr(blackjack_module, "shuffle", lambda lst: calls.append(True))
    deck = Deck()
    deck.mix()
    assert calls

def test_deck_div_and_append(blackjack_module):
    Deck = blackjack_module.Deck
    deck = Deck()
    top = deck[-1]
    popped = deck.div()
    assert popped == top
    assert len(deck) == len(blackjack_module.CardData.colors) * len(blackjack_module.CardData.ranks) - 1
    deck.append(popped)
    assert deck[-1] == popped
    with pytest.raises(TypeError):
        deck.append("not_card")

def test_hand_append_and_ace_adjustment(blackjack_module):
    Hand = blackjack_module.Hand
    Card = blackjack_module.Card
    hand = Hand()
    ace1 = Card("káró", "ász")
    ace2 = Card("treff", "ász")
    hand.append(ace1)
    hand.append(ace2)
    assert hand.value == 22
    assert hand.ace == 2
    hand.set_ace()
    assert hand.value == 12
    assert hand.ace == 1

def test_chips_initial_and_sum_setter(blackjack_module):
    Chips = blackjack_module.Chips
    chips = Chips()
    assert chips.sum == 100
    chips.sum = 200
    assert chips.sum == 200
    with pytest.raises(ValueError):
        chips.sum = 0

def test_chips_bet_setter_and_win_lose(blackjack_module):
    Chips = blackjack_module.Chips
    chips = Chips()
    chips.bet = 10
    assert chips.bet == 10
    with pytest.raises(ValueError):
        chips.bet = -1
    with pytest.raises(ValueError):
        chips.bet = 250
    chips.bet = 20
    chips.win_bet()
    assert chips.sum == 120
    chips.loose_bet()
    assert chips.sum == 100

def test_bet_set_bet(monkeypatch, blackjack_module):
    Rules = blackjack_module.Rules
    Chips = blackjack_module.Chips
    chips = Chips(sum=50)
    monkeypatch.setattr(builtins, "input", lambda prompt="": "15")
    Rules.betting(chips)
    assert chips.bet == 15

def test_draw_append_and_updates(blackjack_module):
    Rules = blackjack_module.Rules
    Hand = blackjack_module.Hand
    class StubDeck:
        def __init__(self):
            self.called = False
        def div(self):
            self.called = True
            return blackjack_module.Card("pikk", "négy")

    hand = Hand()
    deck = StubDeck()
    Rules.draw(deck, hand)
    assert deck.called
    assert hand.value == blackjack_module.CardData.get_value("négy")

def test_player_and_dealer_outcomes(blackjack_module, capsys):
    Rules = blackjack_module.Rules
    Hand = blackjack_module.Hand
    Chips = blackjack_module.Chips

    def run_logic(player_value, dealer_value, card_rank, expected_message, expected_sum):
        player = Hand()
        player.value = player_value
        player.ace = 0
        dealer = Hand()
        dealer.value = dealer_value
        dealer.ace = 0
        chips = Chips()
        chips.bet = 10
        class StubDeck:
            def __init__(self):
                self.card = blackjack_module.Card("kör", card_rank)

            def div(self):
                return self.card

        deck = StubDeck()
        if player_value > 21:
            Rules.player_loose(chips)
        else:
            while dealer.value < 17:
                Rules.draw(deck, dealer)
            if dealer.value > 21:
                Rules.dealer_loose(chips)
            elif dealer.value > player_value:
                Rules.dealer_win(chips)
            elif dealer.value < player_value:
                Rules.player_win(chips)
            else:
                Rules.equals()
        out = capsys.readouterr().out
        assert expected_message in out
        assert chips.sum == 100 + expected_sum

    run_logic(20, 10, "nyolc", "A játékos nyert", 10)
    run_logic(5, 15, "négy", "Az osztó nyert", -10)
    run_logic(20, 15, "öt", "Döntetlen", 0)





