import os


def controller(response=""):
    if response is not "":
        print(response)

    car_models = ['Ford', 'Dodge', 'Chevy', 'None']

    display(car_models)

    reply = int(input("Sir, what type of car do you own? > "))

    validate = list_checker(car_models, reply)
    if not validate:
        reset()
        return controller("That choice wasn't an option, try again!")
    else:
        reset()
        return "Completed, returned {}".format(car_models[validate])

    reset()
    return controller("That's not in the list, try again")


def display(list_car):
    for x, each in enumerate(list_car):
        print("{}) {}".format(x, each))


def reset():
    os.system('clear')  # on linux / os x


def list_checker(list_x, user_answer):

    for position, each in enumerate(list_x):
        # print("{}, {}".format(type(position), type(user_answer)))
        if position == user_answer:
            return position

    return False


def checker(x):
    if x.isalpha():
        return x

    elif int(x):
        print("I'm a integer")
        return False

    else:
        return False


print(controller())
