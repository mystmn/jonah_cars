import os


class master_lesson(object):
    def __init__(self):
        self.car_models = ['', 'Ford', 'Dodge', 'Chevy', 'None']
        self.test = False

    def controller(self, response=""):
        if response is not "":
            print(response)

        self.screen_display(self.car_models)

        try:
            reply = int(input("Sir, what type of car do you own? > "))
        except:
            self.reset()
            return self.controller("You entered a string not an integer")

        validate = self.list_checker(self.car_models, reply)

        if self.test:
            print(" validate == {}, type{}".format(validate, type(validate)))

        if not validate:
            self.reset()
            return self.controller("That choice wasn't an option, try again!")
        else:
            self.reset()
            return "Completed, returned {}".format(self.car_models[validate])

        self.reset()
        return controller("That's not in the list, try again")

    @staticmethod
    def screen_display(list_car):

        for x, each in enumerate(list_car):
            if x is 0:
                pass
            else:
                print("{}) {}".format(x, each))

        print("9) Exit")

    def reset(self):
        if not self.test:
            os.system('clear')  # on linux / os x

    def list_checker(self, list_x, user_answer):

        if user_answer == int(9):
            exit()

        for position, each in enumerate(list_x):
            if self.test:
                print("{}, {}".format(type(position), type(user_answer)))

            if position == user_answer:
                if self.test:
                    print("answer passed")
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

print(master_lesson().controller())
