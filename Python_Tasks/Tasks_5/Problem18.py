# Problem: The Minion Game
# HackerRank: https://www.hackerrank.com/challenges/the-minion-game/problem

def minion_game(string):
    vowels = 'AEIOU'
    stuart = 0
    kevin = 0
    length = len(string)

    for i in range(length):
        if string[i] in vowels:
            kevin += length - i
        else:
            stuart += length - i

    if stuart > kevin:
        print("Stuart", stuart)
    elif kevin > stuart:
        print("Kevin", kevin)
    else:
        print("Draw")

if __name__ == '__main__':
    s = input()
    minion_game(s)
