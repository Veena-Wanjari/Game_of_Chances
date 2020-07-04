

import random

money = 100
    
#This is the game of flipping coin. If either "Head" or "Tail" matches with random result, will deside the winning amount.            
def flipping_coin(guessing_side, dollars):
    if 0 < dollars < money :
        print("The game of flipping coin begins....")
    else:
        print(f"The betting amount is: {dollars}")
        print(f"The limit for betting amount is from 1 to 100 dollars only")
        return False
    
    
    result = random.randint(1,2)
    
    print(f"The random generated side for H-1 and T-2 is : {result}")
         
    if guessing_side == "Head" or guessing_side == "Tail":
        print(f"You have bet $ {dollars} on flipping side of: {guessing_side}")
    
    else:
        print("What you have typed? Please choose Head or Tail only !!")
        return False
    
    if (guessing_side == "Head" and result == 1) or (guessing_side == "Tail" and result == 2):
        print(f"Money won on flipping coin game is : $ {dollars + money}")    
        return dollars
    else:
        print(f" Money lost on flipping coin game is : $ {money - dollars}")
        return -dollars


"""
Welcome to the game of Cho - Han. The function should simulate rolling two dice and adding the results together.
The player predicts whether the sum of those dice is odd or even and wins if their prediction is correct.
"""

def rolling_two_dice(guess_o_or_e, bet):
    if 0 < bet < money :
        print("The game of rolling dice begins....")
    else:
        print(f"The betting amount is: {bet}")
        print(f"The limit for betting amount is from 1 to 100 dollars only")
        return False
    
    result_1 = random.randint(1,6)
    result_2 = random.randint(1,6)
    final_result = result_1 + result_2
    check_e_o = final_result % 2
    print(f"Two dice is rolled and the output is: {result_1} and {result_2}")
    print(f"The sum of two output is : {final_result}")
    if (check_e_o == 0 and guess_o_or_e == "Even"):
        print(f"Money won on guessing {guess_o_or_e} with betting amount ${bet}: ${money + bet}")
        return +bet
    elif (check_e_o != 0 and guess_o_or_e == "Odd"):
        print(f"Money won on guessing {guess_o_or_e} with betting amount ${bet}: ${money + bet}")
        return -bet
    elif (check_e_o == 0 and guess_o_or_e == "Odd"):
        print(f"Money lost on guessing {guess_o_or_e} with betting amount ${bet}: ${money - bet}")
        return -bet
    elif (check_e_o != 0 and guess_o_or_e == "Even"):
        print(f"Money lost on guessing {guess_o_or_e} with betting amount ${bet}: ${money - bet}")
        return -bet
    else:
        print("You have typed wrong. Either choose Odd or Even")
        return False
        
        
# Two players picking a card randomly from a deck of cards. The higher number wins.


def picking_a_card(bet):
    if 0 < bet < money:
        print("The game of playing cards begins....")
    else:
        print(f"Your betting amount is : {bet}")
        print(f"The limit for betting amount is from 1 to 100 dollars only")
        return False
    
    my_card = random.randint(1,13)
    your_card = random.randint(1,13)
    
    print(f"The output of my card and your card is : {my_card} and {your_card}")
    if my_card < your_card:
        print(f"I lost my betting amount of ${bet}. So, total loss is ${money - bet}")
        return -bet
    elif my_card > your_card:
        print(f"I won my betting amount of ${bet}. So, total gain is ${money + bet}")
        return bet
    elif my_card == your_card:
        print("No gain, No loss....It's a tie !!")
        return False


#This is the game of roulette.A random number should be generated that determines which space the ball lands on.        

def game_of_roulette(guess,bet):
    if 0 < bet < money:
        print("The game of roulette begins....")
    else:
        print(f"The betting amount is : {bet}")
        print("The limit for betting is from 1 to 100 dollars only")
        return False
    
    ball_output = random.randint(0,36)
    print(f"The random number out of 0 to 36 is: {ball_output}")
    
    if guess == ball_output:
        print(f"You won big !!: ${bet * 58}")
        return bet
    elif guess == "Even" and ball_output % 2 == 0:
        print(f"You bet on Even, and you won :${money + bet}")
        return bet
    elif guess == "Odd" and ball_output % 2 != 0:
        print(f"You bet on Odd, and you won :${money + bet}")
        return bet
    elif guess == "Even" and ball_output % 2 != 0:
        print(f"You bet on Even, and you loose:${money - bet}")
        return -bet
    elif guess == "Odd" and ball_output % 2 == 0:
        print(f"You bet on Odd, and you loose:${money - bet}")
        return -bet
    elif guess != ball_output:
        print(f"You lost game!!Sorry, You lost everything : ${bet*0}")
        return bet
    else:
        print("Please type Even, Odd or numbers between 0 to 36 only")
        return False


# money += flipping_coin("Head", 40)
# money += flipping_coin("Tail", 50)
# money += flipping_coin("xyr", 99)
# money += flipping_coin("Head", -3)       

       
# money +=rolling_two_dice("Even", 30)
# money +=rolling_two_dice("Odd", 20)
# money +=rolling_two_dice("xyz", 10)
# money +=rolling_two_dice("Odd", 101)

# money +=picking_a_card(20)
# money +=picking_a_card(0)
# money +=picking_a_card(101)
# money +=picking_a_card(1)


# money +=game_of_roulette("Even",101)
# money +=game_of_roulette("Even", 40)       
# money +=game_of_roulette("Odd", 20)
# money +=game_of_roulette(0,80)
# money +=game_of_roulette("Even", 80)




