from random import shuffle


class CardData:

    def __init__(self):
        raise RuntimeError("Az osztály statikus, nem példányosítható!")

    colors = ("kör", "káró", "treff", "pikk")
    ranks = ("kettő", "három", "négy", "öt", "hat", "hét", "nyolc", "kilenc", "tíz", "bubi", "dáma", "király", "ász")

    @staticmethod
    def get_value(item):
        values = {"kettő": 2, "három": 3, "négy": 4, "öt": 5, "hat":6,
                  "hét": 7, "nyolc": 8, "kilenc": 9, "tíz": 10, "bubi": 10,
                  "dáma": 10, "király": 10, "ász": 11}
        if not item in values.keys():
            raise ValueError('A megadott érték nem található!')
        return values[item]

    is_playing = True

class Card:

    def __init__(self, color, rank):
        self.color = color
        self.rank = rank

    @property
    def color(self):
        return self.__color

    @color.setter
    def color(self, color):
        if len(color) >= 3:
            self.__color = color
        else:
            raise ValueError("Az érték nem egy kártyaszín!")

    @property
    def rank(self):
        return self.__rank

    @rank.setter
    def rank(self, rank):
        if len(rank) >= 2:
            self.__rank = rank
        else:
            raise ValueError("Az érték nem egy kártya rang!")

    def __str__(self):
        return self.rank + " - " + self.color


class Deck(list):
    def __init__(self):
        super().__init__()
        for color in CardData.colors:
            for rank in CardData.ranks:
                self.append(Card(color, rank))

    def __str__(self):
        tmp = ""
        for card in self:
            tmp += card.__str__() + "\n"
        return tmp

    def mix(self):
        shuffle(self)

    def div(self):
        return self.pop()

    def append(self, card):
        if not isinstance(card, Card):
            raise TypeError("Csak kártyatípust lehet hozzáadni!")
        super().append(card)

class Hand(list):

    def __init__(self):
        super().__init__()
        self.value = 0
        self.ace = 0

    def append(self, card):
        if not isinstance(card, Card):
            raise TypeError("Csak kártya lehet a kezedben!")
        super().append(card)
        self.value += CardData.get_value(card.rank)
        if card.rank == "ász":
            self.ace += 1

    def set_ace(self):
        while self.value > 21 and self.ace:
            self.value -= 10
            self.ace -= 1

class Chips:

    def __init__(self, sum = 100):
        self.sum = sum
        self.bet = 0

    @property
    def sum(self):
        return self.__sum

    @sum.setter
    def sum(self, value):
        if value > 0:
            self.__sum = value
        else:
            raise ValueError("Az érték nem lehet 0 vagy negatív")

    @property
    def bet(self):
        return self.__bet

    @bet.setter
    def bet(self, value):
        if value >= 0 and self.sum - value >= 0:
            self.__bet = value
        else:
            raise ValueError("Nincs money a téthez!")

    def win_bet(self):
        self.sum += self.bet

    def loose_bet(self):
        self.sum -= self.bet

class Rules:

    def __init__(self):
        raise RuntimeError("Az osztály nem példányosítható!")

    @staticmethod
    def betting(chips: Chips):
        while True:
            try:
                chips.bet = int(input("Mennyit zsetont szeretnél feltenni? "))
            except ValueError as error:
                print(error)
            else:
                break

    @staticmethod
    def draw(card_deck: Deck, hand: Hand):
        hand.append(card_deck.div())
        hand.set_ace()

    @staticmethod
    def draw_or_stop(card_deck: Deck, hand: Hand):
        while True:
            var = input("Húzol vagy megállsz? Myomj 'h'-t vagy 'm'-et: ")
            if var[0].lower() == "h":
                Rules.draw(card_deck, hand)
            elif var[0].lower() == "m":
                print("Megálltál, az osztó játszik!")
                CardData.is_playing = False
            else:
                print("Ilyen opció nincs!")
                continue
            break

    @staticmethod
    def player_cards(card_player: Hand):
        print("A játékos kezében van:\n", *card_player, sep="\n")
        print("A játékos kezében lévő lapok értéke: ", card_player.value)

    @staticmethod
    def not_show_all(card_player: Hand, card_dealer: Hand):
        print("Az osztó lapjai:")
        print("<kártya rejtve>")
        print(card_dealer[1])
        Rules.player_cards(card_player)

    @staticmethod
    def show_all(card_player: Hand, card_dealer: Hand):
        print("Az osztó lapjai:\n", *card_dealer, sep="\n")
        Rules.player_cards(card_player)

    @staticmethod
    def player_loose(chips: Chips):
        print("A játékos vesztett!")
        chips.loose_bet()

    @staticmethod
    def player_win(chips: Chips):
        print("A játékos nyert!")
        chips.win_bet()

    @staticmethod
    def dealer_loose(chips: Chips):
        print("Az játékos nyert!")
        chips.win_bet()

    @staticmethod
    def dealer_win(chips: Chips):
        print("Az osztó nyert!")
        chips.loose_bet()

    @staticmethod
    def equals():
        print("Döntetlen")

chips = Chips()

while True:
    print("Üdv a pénznyelőben! Blackjacket játszunk!\n"
          "Az osztó addig húz, amíg el nem éri a 17-et\n"
          "Az ász a szabályok alapján 11-et vag 1-et ér!")
    deck = Deck()
    deck.mix()
    Rules.betting(chips)

    player = Hand()
    dealer = Hand()

    Rules.draw(deck, player)
    Rules.draw(deck, player)
    Rules.draw(deck, dealer)
    Rules.draw(deck, dealer)

    Rules.not_show_all(player, dealer)
    while CardData.is_playing:
        Rules.draw_or_stop(deck, player)
        Rules.not_show_all(player, dealer)

        if player.value > 21:
            Rules.player_loose(chips)
            break
        elif player.value <= 21:
            while dealer.value < 17:
                Rules.draw(deck, dealer)
            if dealer.value > 21:
                Rules.dealer_loose(chips)
            elif dealer.value > player.value:
                Rules.dealer_win(chips)
            elif dealer.value < player.value:
                Rules.player_win(chips)
            else:
                Rules.equals()

    Rules.show_all(player, dealer)
    print("\nA játékos egyenlege: ", chips.sum)
    new_game = input("Új játék? Nyomj i-t, vagy n-t: ")
    if new_game[0].lower() == "i":
        CardData.is_playing = True
        continue
    print("Köszöjünk a játékot")
    break
























