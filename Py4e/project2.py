password = int(000)
count = 0
while True:
    try:
        guess = int(input("Guess my password. Hint: A three digit number. "))
    except:
        print("Use numbers instead.")
        continue
    while guess == password:
        print("HOORAY!! You guessed the password!")
        quit()
    else:
        print("WRONG! Try again.")
        count += 1
        if count > 4:
            compaw = input("Do you give up? Type: Yes or No.")
            if compaw == "Yes" or "yes":
                print("The password is","000")
                quit()
            elif compaw == "No" or "no":
                print(guess)
                count = 0
                break
           

