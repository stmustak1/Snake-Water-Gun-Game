import time
import random
# Code By Mustak Ahmed
# Timestrap : 11 April 2021 at 8.10 p.m
# Snake Water Gun Game Using Python


print("<<<-------- Welcome to Snake-Gun-Water-Game --------->>>\n")
match_no = 1
print(" Type :\n \ts for snake\n \tw for water\n \tg for gun\n")
human = input("Enter Your Name : ")


while(1):
    print()
    print(f' <<------ Match 0{match_no} ------->>\n')
    match_no = match_no + 1
    time.sleep(1.2)
    print(" Match Starting...")
    print()
    time.sleep(1)
    print(f" {human} Vs Computer\n")
    time.sleep(1)
    print(" Your Current Score 0   ||   Computers Current Score 0.\n")
    time.sleep(1)

    list = ['s', 'w', 'g']
    n = 0
    choice = int(input('How many Level You Want to Play?  : '))
    comp_score = 0
    inp_score = 0
    level = 1

    snake_human = 0
    gun_human = 0
    water_human = 0
    snake_comp = 0
    gun_comp = 0
    water_comp = 0

    f = open(f"{human}.txt", 'a')
    exact_time = time.asctime(time.localtime(time.time()))
    f.write(
        f'\n\n\n\n\t\t\t\t\t\t<<<[ {exact_time} ]>>>\nMatch Details::\nPlayer : {human}      Match 0{match_no-1}\n')

    #  <<<<-------------main Game Start from here -------------->>>>

    while(n < choice):

        print()
        print(f'>>>  Level 0{level} ::\n')

        Inp = input("Choose :: Snake  Water  Gun :  ")
        inp = Inp.lower()
        comp = random.choice(list)
        print()

        if inp == 's' and comp == 'w':
            inp_score = inp_score + 1
            snake_human = snake_human + 1
            water_comp = water_comp + 1

            print(
                f"\t\t{human}, You have --Won-- level 0{level}  ||  Computer lose.")
            print()
            print(
                f"\t\tYour score : {inp_score}   ||   Computer's Score : {comp_score}")

            f.write(
                f"Level 0{level}  ::  You Enter {inp}   ||   Computer Taken {comp}   || Status : You Won\n")
            time.sleep(.8)

        elif inp == 's' and comp == 'g':
            comp_score = comp_score + 1
            snake_human = snake_human + 1
            gun_comp = gun_comp + 1
            print(
                f"\t\tComputer -Won-  ||  {human}, You have lose level 0{level}.")
            print()
            print(
                f"\t\tYour score : {inp_score}   ||   Computer's Score : {comp_score}")

            f.write(
                f"Level 0{level}  ::  You Enter {inp}   ||   Computer Taken {comp}   ||    Status : You lose\n")
            time.sleep(.8)

        elif inp == 'w' and comp == 's':
            comp_score = comp_score + 1
            water_human = water_human + 1
            snake_comp = snake_comp + 1
            print(
                f"\t\tComputer -Won-  ||  {human}, You have lose level 0{level}.")
            print()
            print(
                f"\t\tYour score : {inp_score}   ||   Computer's Score : {comp_score}")

            f.write(
                f"Level 0{level}  ::  You Enter {inp}   ||   Computer Taken {comp}   ||    Status : You lose\n")
            time.sleep(.8)

        elif inp == 'w' and comp == 'g':
            inp_score = inp_score + 1
            water_human = water_human + 1
            gun_comp = gun_comp + 1
            print(
                f"\t\t{human}, You have --Won-- level 0{level} ||  Computer lose.")
            print()
            print(
                f"\t\tYour score : {inp_score}   ||   Computer's Score : {comp_score}")

            f.write(
                f"Level 0{level}  ::  You Enter {inp}   ||   Computer Taken {comp}   ||    Status : You Won\n")
            time.sleep(.8)

        elif inp == 'g' and comp == 's':
            inp_score = inp_score + 1
            gun_human = gun_human + 1
            snake_comp = snake_comp + 1
            print(
                f"\t\t{human}, You have --Won-- level 0{level} ||  Computer lose.")
            print()
            print(
                f"\t\tYour score : {inp_score}   ||   Computer Score : {comp_score}")

            f.write(
                f"Level 0{level}  ::  You Enter {inp}   ||   Computer Taken {comp}   ||    Status : You Won\n")
            time.sleep(.8)

        elif inp == 'g' and comp == 'w':
            comp_score = comp_score + 1
            gun_human = gun_human + 1
            water_comp = water_comp + 1
            print(
                f"\t\tComputer -Won-  ||  {human}, You have lose level 0{level}.")
            print()
            print(
                f"\t\tYour score : {inp_score}   ||   Computer Score : {comp_score}")

            f.write(
                f"Level 0{level}  ::  You Enter {inp}   ||   Computer Taken {comp}   ||    Status : You lose\n")
            time.sleep(.8)

        elif inp == comp:
            if inp == 's':
                snake_human = snake_human + 1
                snake_comp = snake_comp + 1
            elif inp == 'g':
                gun_human = gun_human + 1
                gun_comp = gun_comp + 1
            else:
                water_human = water_human + 1
                water_comp = water_comp + 1
            print('\t\tMatch Draw')
            print()
            print(
                f"\t\tYour score : {inp_score}   ||   Computer Score : {comp_score}")

            f.write(
                f"Level 0{level}  ::  You Enter {inp}   ||   Computer Taken {comp}   ||    Status : Match Draw\n")
            time.sleep(.8)

        else:        # <-----If Wrong Enter among 's''g''w'  game will be stop here ------->
            print(" Invalid Enter. Please Try Again by following above instruction.\n")
            break

        n = n+1
        level = level + 1

    # <<------Condition for checking all level done or not ------->>

    if level == (choice + 1):
        print('\n\n>>> Level Up! ')
        print('\nFinal Results :', end=' ')
        if inp_score > comp_score:
            result = f'Hurry! {human}, You have Won'
            print(f"{result} the Match.")
        elif inp_score < comp_score:
            result = 'Computer won'
            print(f"Oops! {result} the Match. Try again Later")
        else:
            result = 'Match Tied Up.'
            print(f'{result} Try again Now.')

        store = f"Total Level Played : 0{level-1}\nFinal Status :: {result}\nYou Entered :   Snake 0{snake_human}   Gun 0{gun_human}   Water 0{water_human}\nComputer Taken : Snake 0{snake_comp}   Gun 0{gun_comp}     Water 0{water_comp}"
        f.write(f'\n{store}')
        f.close()

        print()
        Y_N = input('Are you want to Play again? (y or n) : ')
        y_n = Y_N.lower()
        if y_n == 'y':
            continue
        elif y_n == 'n':
            break
        else:
            print('Invalid Enter')
            break
    else:                # <--------If all level not done , the game quit -------->
        break
