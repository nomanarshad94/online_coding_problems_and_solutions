from functools import cmp_to_key


class Player:
    def __init__(self, name, score):
        self.name = name
        self.score = score

    def __repr__(self):
        return 'Player(x=%s, y=%s)' % (self.name, self.score)

    def comparator(a, b):
        if a > b:
            return 1
        elif a == b:
            return 0
        else:
            return -1

    def __gt__(self, other):
        if self.score < other.score:
            return True
        elif self.score == other.score:
            if self.name > other.name:
                return True
        return False


n = int(input())
data = []
for i in range(n):
    name, score = input().split()
    score = int(score)
    player = Player(name, score)
    data.append(player)

data = sorted(data, key=cmp_to_key(Player.comparator))
for i in data:
    print(i.name, i.score)
