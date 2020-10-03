#pick a random location for the player 
#pick a radom location for the monster
#pick a random location to exit the door
#draw the player in the grid
#take inout or a movement 
#move player unless invalid move()


import random
from os import system , name 
#draw a square grid

CELLS= [(0,0),(1,0),(2,0),(3,0),(4,0),
       (0,1),(1,1),(2,1),(3,1),(4,1),
       (0,2),(1,2),(2,2),(3,2),(4,2),
       (0,3),(1,3),(2,3),(3,3),(4,3),
       (0,4),(1,4),(2,4),(3,4),(4,4),
]

# define our clear function 
def clear_screen(): 
  
    # for windows 
    if name == 'nt': 
        _ = system('cls') 
  
    # for mac and linux(here, os.name is 'posix') 
    else: 
        _ = system('clear') 


def find_location():

    return random.sample(CELLS,3) 


def move_player(move,player):
    x,y=player
    if move=='RIGHT':
        x=x+1
    if move=='LEFT':
        x=x-1
    if move=='UP':
        y=y-1
    if move=='DOWN':
        y=y+1
    return x,y 


def get_move(player):
    moves=['LEFT','RIGHT','UP','DOWN']
    x,y=player
    if x==0: 
        moves.remove('LEFT')
    if x==4:
        moves.remove('RIGHT')
    if y==0:
        moves.remove('UP')
    if y==4:
        moves.remove('DOWN')

    return moves


def draw_map(player):

    print(" _" * 5)
    tile = "|{}"


    for cell in CELLS:
        x, y = cell

        if x < 4:
            line_end = ""
            if cell == player:
                output = tile.format("X")
            else:
                output = tile.format("_")
        else:
            line_end = "\n"
            if cell == player:
                output = tile.format("X|")
            else:
                output = tile.format("_|")
        print(output, end=line_end)



def game_loop():

    monster,player,door=find_location()

    playing=True
    clear_screen()
    while playing:
        valid_moves=get_move(player)
        draw_map(player)
        print('welcome to dungeon game')
        print('you are currently in the room {}'.format(player))
        #print('The monster is in the room {}'.format(monster))
        #print('The door to exit is{}'.format(door))
        print('You can move the player{}'.format(get_move(player)))
        print("Enter 'QUIT' to quit the game ")
        move=input('> ').upper()
        if move=='QUIT':
            break
        clear_screen()
        if move in valid_moves:
            player=move_player(move,player)
        else:
            print('there are walls! becareful! ')
        

        if player==monster:
            print('\n **The monster got U! better chance next time** \n')
            playing=False
           
        if player==door:
            print('\n **You found the exit door, U win!** \n ')
            playing=False


    else:
        if input('want to play again? [y/n]').lower() != 'n':
            game_loop()

clear_screen()

print('press enter to start the game')
clear_screen()
game_loop()
