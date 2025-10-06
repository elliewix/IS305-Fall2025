# raffle system or something
# odds are (1/463) for the big win
# odds are (1/32) for a small win

import random
def determine_wins(chance):
    if chance <= (1/463):
        return 100
    elif chance <= (1/32):
        return 10
    else:
        return 0

bank = 0
while bank <=0:
    bank -=.5 # costs $1 to play
    prob = random.random()
    result = determine_wins(prob)
    bank += result
    print(bank)

