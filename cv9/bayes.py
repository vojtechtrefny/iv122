import random


dice = [lambda num : (1/6, 1/6, 1/6, 1/6, 1/6, 1/6)[num - 1],   # fair dice
        lambda num : (1/6, 0, 1/6, 1/6, 2/6, 1/6)[num - 1],     # 2 -> 5
        lambda num : (1/7, 1/7, 1/7, 1/7, 1/7, 2/7)[num - 1],]  # twice 6

seq = [1, 3, 4, 5, 1, 4, 6, 5, 1, 5, 4, 5]

prior1 = [1/3, 1/3, 1/3]
prior2 = [0.05, 0.05, 0.90]


def seq_p(seq, die, die_prob):
    # probability of sequence with selected die
    p = 1
    for num in seq:
        p *= die(num)
    return p * die_prob

def bayes(prior, seq):

    for i in range(len(dice)):
        p_die = seq_p(seq, dice[i], prior[i]) / sum([seq_p(seq, dice[j], prior[j]) for j in range(len(dice))])
        print("P(H_%d | seq) = %f" %(i + 1, p_die))


bayes(prior1, seq)
print("----------")
bayes(prior2, seq)
