##https://edabit.com/challenge/dLnZLi8FjaK6qKcvv
class Shiritori:
    def __init__(self):
        self.game_over = False
        self.words = []
    def play(self, word):
        if len(self.words) == 0 or self.words[-1][-1] == word[0]  and word not in self.words :
            self.words.append(word)
            return self.words
        self.game_over = True
        return 'game over'
    def restart(self):
        self.words = []
        self.game_over = False
        return 'game restarted'
my_shiritori = Shiritori()
print(my_shiritori.words)
print(my_shiritori.play("rhino"))
print(my_shiritori.play("apple"))
print(my_shiritori.game_over)