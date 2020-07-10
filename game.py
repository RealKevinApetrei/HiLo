import config
from score import Score
import random

range_decrease_rate = config.decrease_rate # Range Decrease Rate per round
Player = Score(score=config.start_score) # Initialise Player Object

def random_number(): # Random Number
    return random.randint(1, number_range)


def game_instance(): # Game Instance
    global number_range
    number_range = config.num_range # Starting Number Range

    while True: # Game Loop
        if number_range < 2: # If game is over...
            print(f"\n\n()()()()()()()()()()\n\n GAME OVER \n\n YOU SCORED (  {Player.score}  ) \n\n()()()()()()()()()()")
            print(f"\n\n GAME WAS MADE BY (( KEVIN APETREI ))\n\n")
            break
        else:
            Player.show_score() # Show Score

            print(f"\n**********\n     1-{number_range}     \n**********\n")

            number_picked = random_number() # Random Number
            print(f"\n<><><><><><><><><><>\n     {number_picked}     \n<><><><><><><><><><>\n")
            
            response = input("\n>>> Higher (H) or Lower (L) <<< : \n") # Ask for Response

            if response.upper() == "H": # Check Answer (Higher)
                number_picked_2 = random_number() # Random Number
                print(f"\n<><><><><><><><><><>\n     {number_picked_2}     \n<><><><><><><><><><>\n")

                if number_picked_2 > number_picked:
                    print("\n++++++++++++++++++++\n You WIN! \n++++++++++++++++++++\n")

                    Player.add_score() # Add Score
                    number_range -= range_decrease_rate # New Number Range (-1 each round)
                else:
                    print("\n--------------------\n You LOSE! \n--------------------\n")

                    Player.remove_score() # Remove Score
                    number_range -= range_decrease_rate # New Number Range (-1 each round)

            elif response.upper() == "L": # Check Answer (Lower)
                number_picked_2 = random_number() # Random Number
                print(f"\n<><><><><><><><><><>\n     {number_picked_2}     \n<><><><><><><><><><>\n")

                if number_picked_2 < number_picked:
                    print("\n++++++++++++++++++++\n You WIN! \n++++++++++++++++++++\n")

                    Player.add_score() # Add Score
                    number_range -= range_decrease_rate # New Number Range (-1 each round)
                else:
                    print("\n--------------------\n You LOSE! \n--------------------\n")

                    Player.remove_score() # Remove Score
                    number_range -= range_decrease_rate # New Number Range (-1 each round)
            
            else:
                print("\nInvalid Response! Try Again.\n")
                Player.show_score() # Show current Score
                
#                    GNU GENERAL PUBLIC LICENSE
#                       Version 3, 29 June 2007
#
# Copyright (C) 2007 Free Software Foundation, Inc. <https://fsf.org/>
# Everyone is permitted to copy and distribute verbatim copies
# of this license document, but changing it is not allowed.






    
