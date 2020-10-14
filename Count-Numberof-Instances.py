###https://edabit.com/challenge/rprukfcGWqnvKZR9g
class User:
    user_count = 0
    def __init__(self, username):
        self.username = username
        User.user_count += 1
u1 = User("johnsmith10")
print(User.user_count)
u2 = User("marysue1989")
print(User.user_count)
u3 = User("milan_rodrick")
print(User.user_count)
print(u1.username)
print(u2.username)
print(u3.username)