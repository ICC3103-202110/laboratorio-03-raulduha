from player import Player
from cards import Cards
from game import Game
players = []
game = Game()
p1 = Player(0,0,0)

def start_game():

    game.welcome_board()
    while True:
        if game.actual_turn == game.final_turn:
            game.actual_turn = 0 
            print('nueva ronda...')
            break 

        elif game.actual_turn != game.final_turn:
            
            print('es el turno de', players[game.actual_turn].name) 
            option = p1.player_action()
            while True:
                
                if option == 1:
                    print('you chose ingreso')
                    players[game.actual_turn].money += 1
                    print(players[game.actual_turn].name,'monedas: ',players[game.actual_turn].money)
                    break
                elif option == 2:
                    print('you chose ayuda externa')
                    players[game.actual_turn].money += 2
                    print(players[game.actual_turn].name,'monedas: ',players[game.actual_turn].money)
                    break
                elif option == 3:
                    print('you chose Coup')
                    '''
                    if players[game.actual_turn].money < 7:
                        print('you do not have enough money to use this option.')
                    else:
                        print('you do you want to kill:')
                        print('1) kill', players[0].name)
                        print('2) kill', players[1].name)
                        print('3) kill', players[2].name)
                        kill = int(input('select the number in here: '))
                        if kill == 1:
                            player[0].cards.remove[0]
                            print(player[0].cards)
                        elif kill == 2:
                            player[1].cards.remove[0]
                            print(player[1].cards)
                        elif kill == 2:
                            player[2].cards.remove[0]
                            print(player[2].cards)
                    '''
                    break
                elif option == 4:
                    print('you chose Capitan')
                    break
                elif players_move == 5:
                    print('you chose Asesino ')
                    break
                elif players_move == 6:  
                    print('you chose Embajador') 
                    break
                elif players_move == 7:  
                    print('you chose Duque') 
                    break
                elif players_move == 6:  
                    print('you chose Condesa') 
                    break
            game.actual_turn +=1
            
        
def show_people():
    print("\nPeople Created: ")
    for (i, _) in enumerate(players):
        print(f"{i+1}: name: {players[i].name} - cards: {players[i].cards} - money: {players[i].money}")


def create_player(numero):
    n = 1
    while numero >= n:
        n +=1
        name = input('Whats your players name: ')
        p1 = Player(name, 2, [])
        print('')
        p1.recieve_cards(game.deck_of_cards[0])
        game.deck_of_cards.remove(game.deck_of_cards[0])
        p1.recieve_cards(game.deck_of_cards[0])
        game.deck_of_cards.remove(game.deck_of_cards[0])
        players.append(p1)
    return players


def print_menu_and_select():
    print("\nSelect one of these options")
    print("3. start game")
    print("2. show players")
    print("1. create players")
    print("0. exit")
    return int(input('what option are you selecting: '))

def menu():
    while True:
        selection = print_menu_and_select()
        if selection == 0:
            break
        elif selection == 1:
            while True:
                number_of_players = int(input('how many players are playing (3/4):  '))
                if number_of_players > 4 or number_of_players < 3:
                    False
                else:
                    game.final_turn = number_of_players
                    players = create_player(number_of_players)
                    
                    break
                    
        elif selection == 2:
            show_people()
        
        elif selection == 3:
            start_game()
            break
  

if __name__ == "__main__":
    menu()
