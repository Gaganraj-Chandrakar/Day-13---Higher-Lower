import random
from game_data import data
from art import logo, vs


# No of items in data list = 50
def select_A():
    return random.randint(0, 49)


def select_B():
    return random.randint(0, 49)


guess = True
score = 0
print(logo)
while guess:
    A = select_A()
    B = select_B()
    if A != B:
        account_a = data[A]
        account_b = data[B]
    else:
        print(logo)
        continue

    print(
        f"Compare A: {account_a['name']}, a {account_a['description']}, from  {account_a['country']}."
    )

    print(vs)

    print(
        f"Against B: {account_b['name']}, a {account_b['description']}, from  {account_b['country']}."
    )

    user_input = input("Who has more followers? Type 'A' or 'B': ").lower()

    if ((user_input == 'a'
         and account_a['follower_count'] > account_b['follower_count'])
            or (user_input == 'b'
                and account_b['follower_count'] > account_a['follower_count'])):
        print(logo)
        score += 1
        print(f"You're right! Current score: {score}.")


        def select_A():
            return B
    else:
        guess = False

        print(logo)
        print(f"Sorry, that's wrong. Final score: {score}.")
