###
#Lucky Sevens

# Start With $10, every game costs $1 to play
# Roll two dice
# If the result is seven, win $5 (+$4 overall after the $1 cost)
# The game continuously plays until you run out of money.
# At the end, it tells you how many rounds were played.

import sys
import random
money = 10
rounds = 0
top = 10
deal = 'quit'
deal = raw_input ("Say 'Roll' to play manualy, say 'auto' to skip to the end: ")
if deal == 'auto':
    while money > 0:
        die1 = random.randint(1,6)
        die2 = random.randint(1,6)
        if die1+die2 == 7:
            money += 4
            rounds += 1
        if money > top:
            top = money   
        else:
            money -=1
            rounds +=1
        
    if money == 0:
        print "Your top money was: " + str(top)+'$'
        print "Your total rounds was: " + str(rounds)
        sys.exit(0)
    if deal in ['q','quit','exit']:
        sys.exit(0)

elif deal == 'r':
    while money > 0:   
        deal = raw_input ("Say 'Roll' to play manualy, say 'auto' to skip to the end:")
        if deal in ['Roll','roll','r']: 
            die1 = random.randint(1,6)
            die2 = random.randint(1,6)
            print "Your number is " + str(die1+die2)
        if die1+die2 == 7:
            money +=4
            print "Your money is now..."
            print str(money) + "$"
            rounds+=1
            print 'Turn ' + str(rounds)
        else:
            money -=1
            print "Your money is now..."
            print str(money) + "$"
            rounds += 1
            print 'Turn ' + str(rounds)
        if money == 0:
            print "You ran out of money, you lost"
            print "Total turns: " + str(rounds)
        if deal in ['q','quit','exit']:
            sys.exit(0)

