# parent class
class Bird:

    def __init__(self):
        print("Bird is ready")

    def whoisThis(self):
        print("Bird")

    def swim(self):
        print("swim faster")

class penguin(Bird):


    def __init__(self):

        super().__init__()
        print("Penguin is ready")

    def whoisThis(self):
        print("Penguin")

    def run(self):
        print("run faster")

peggy = penguin()
peggy.whoisThis()
peggy.swim()
peggy.run()