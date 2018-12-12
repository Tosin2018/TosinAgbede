secret_word2 = "TOSMAN"
guess = ""
guess_count = 0
guess_limit = 3
out_of_guesses = False

while guess != secret_word2 and not(out_of_guesses):
    if guess_count < guess_limit:
        guess = input("Enter guess: ")
        guess_count += 1
    else:
        out_of_guesses = True

if out_of_guesses:
    print("Out of Guesses, GAME OVER!")
else:
    print("YOU WIN! NEXT LEVEL")
