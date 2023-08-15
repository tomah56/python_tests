from S1E7 import Baratheon, Lannister


class King(Baratheon, Lannister):
    def set_eyes(self, color):
        self.eyes = color
    def set_hairs(self, color):
        self.hairs = color
    def get_eyes(self):
        return self.eyes
    def get_hairs(self):
        return self.hairs
