class calculator:
    """Description of Calculator class"""
    def __init__(self, number_list):
        """Description of constructore"""
        self.number_list = number_list

    @staticmethod
    def dotproduct(V1: list[float], V2: list[float]) -> None:
        """Description of dodtproduct method
        creates scalar out of vectors.
        """
        temp = sum(x * y for x, y in zip(V1, V2))
        print("Dot product is:", temp)

    @staticmethod
    def add_vec(V1: list[float], V2: list[float]) -> None:
        """Description of adding vectors"""
        temp = [x + y for x, y in zip(V1, V2)]
        print("Add Vector is:", temp)

    @staticmethod
    def sous_vec(V1: list[float], V2: list[float]) -> None:
        """Description of deviding vectors"""
        temp = [x - y for x, y in zip(V1, V2)]
        print("Sous Vector is:", temp)
