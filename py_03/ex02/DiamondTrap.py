from S1E7 import Baratheon, Lannister


class King(Baratheon, Lannister):
    """Your docstring for King class"""
    def set_eyes(self, color):
        """Your docstring for set_eyes Method"""
        self.eyes = color

    def set_hairs(self, color):
        """Your docstring for set_hair Method"""
        self.hairs = color

    def get_eyes(self):
        """Your docstring for get_eyes Method"""
        return self.eyes

    def get_hairs(self):
        """Your docstring for get_hair Method"""
        return self.hairs
