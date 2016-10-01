import os


def controller(response=""):
    if response is not "":
        print(response)

    car_models = ['Ford', 'Dodge', 'Chevy', 'None']

    reply = input("Sir, what type of car do you own? {} > ".format(car_models))

    if not checker(reply):
        os.system('clear')  # on linux / os x
        return controller("That choice isn't a string, try again!")

    for x in car_models:
        if reply == x:
            print(x)
            return True

    reset()
    return controller("That's not in the list, try again")


def reset():
    os.system('clear')  # on linux / os x


def checker(x):
    if x.isalpha():
        return x

    elif int(x):
        print("I'm a integer")
        return False

    else:
        return False


print(controller())
