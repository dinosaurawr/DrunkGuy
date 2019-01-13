from Player import Player

class Game(object):

    one_turn_cards = []

    def __init__(self):
        
        first_player_name = input("Введите имя первого игрока:\n")
        second_player_name = input("Введите имя второго игрока:\n")
        self.first_player = Player(first_player_name)
        self.second_player = Player(second_player_name)

    def play_one_turn(self):
        
        fpc = self.first_player.get_upper_card()
        spc = self.second_player.get_upper_card()

        print("{} выложил {}, а {} выложил {}".format(self.first_player.name, fpc, self.second_player.name, spc))

        if fpc > spc:

            print("{} победил, {} берет карты {} и {}".format(self.first_player.name, self.second_player.name, fpc, spc))
            self.second_player.take_cards(fpc, spc)
            self.first_player.add_point()

        if spc > fpc:

            print("{} победил, {} берет карты {} и {}".format(self.second_player.name, self.first_player.name, fpc, spc))
            self.first_player.take_cards(fpc, spc)
            self.second_player.add_point()

        if spc == fpc:
            print('одинаковые карты, следующий ход')
            self.play_one_turn()


game = Game()
resp = 'y'
while resp == 'y':
    print("\n")
    game.play_one_turn()
    print('{} карт в колоде у {} \n{} карт в колоде у {}'.format(len(game.first_player.deck.cards), game.first_player.name, len(game.second_player.deck.cards), game.second_player.name))
    resp = input("играть еще ход? y/n\n\n")

print("игра окончена\n{} - {} очков\n{} - {} очков".format(game.first_player.name, game.first_player.get_points(), game.second_player.name, game.second_player.get_points()))
