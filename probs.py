
a = 0.95
b = 0.75
c = 0.55

# assume every wizard attacks the strongest remaining opponent
# turns go a->b->c->a... for two rounds, starting with whoever player 1 chooses

def win_probabilities(player_1):
    if player_1 == 'a':
        prob_a_wins = a*a*(1-c)
        prob_b_wins = ((1-a)*b*b*(1-c))+((1-a)*(1-b)*c*b)
        prob_c_wins = (a*c)+(a*(1-c)*(1-a)*c)+((1-a)*b*c)+((1-a)*b*(1-c)*(1-b)*c)+((1-a)*(1-b)*c*c*(1-b))+((1-a)*(1-b)*(1-c)*a*c)+((1-a)*(1-a)*(1-b)*(1-c)*b*c)
    elif player_1 == 'b':
        prob_a_wins = (1-b)*(1-c)*(1-c)*a*a
        prob_b_wins = (b*b*(1-c))+((1-b)*c*b)
        prob_c_wins = (b*c)+(b*(1-c)*(1-b)*c)+((1-b)*(1-b)*c*c)+((1-b)*(1-c)*a*c)+((1-b)*(1-c)*(1-a)*b*c)
    elif player_1 == 'c':
        prob_a_wins = (1-c)*(1-c)*a*a
        prob_b_wins = (c*b)+(c*(1-b)*(1-c)*b)+((1-c)*(1-c)*(1-a)*b*b)+((1-c)*(1-a)*(1-b)*c*b)
        prob_c_wins = (c*c*(1-b))+((1-c)*a*c)+((1-c)*(1-a)*b*c)
    print('Player 1 is {}'.format(player_1))
    print('Probability of wizard A winning: {}'.format(prob_a_wins))
    print('Probability of wizard B winning: {}'.format(prob_b_wins))
    print('Probability of wizard C winning: {}'.format(prob_c_wins))

win_probabilities(player_1='a')
win_probabilities(player_1='b')
win_probabilities(player_1='c')
