class calculator:
    """Description of Calculator class"""
    def __init__(self, number_list):
        """Description of constructore"""
        self.number_list = number_list

    def __add__(self, object) -> None:
        """Description of + overload"""
        self.number_list = [x + object for x in self.number_list]
        print(self.number_list)

    def __mul__(self, object) -> None:
        """Description of * overload"""
        self.number_list = [x * object for x in self.number_list]
        print(self.number_list)

    def __sub__(self, object) -> None:
        """Description of - overload"""
        self.number_list = [x - object for x in self.number_list]
        print(self.number_list)

    def __truediv__(self, object) -> None:
        """Description of / overload"""
        if not object == 0:
            self.number_list = [x / object for x in self.number_list]
            print(self.number_list)
        else:
            print("Only Chack Norris can divide with 0")
            print("Are you Chack Norris??")
            print("That's what I thougth...")
