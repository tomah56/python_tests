def give_bmi(height: list[int | float], weight: list[int | float]) -> list[int | float]:
    bmi = []
    if len(height) != len(weight):
        raise ValueError("lists doen't have the same number of values")
    for num in height:
        if not isinstance(num, (int, float)):
            raise TypeError("Wrong type of vlaues in height")
    for num in weight:
        if not isinstance(num, (int, float)):
            raise TypeError("Wrong type of vlaues in weight")
    for h, w in zip(height, weight):
        temp = w / (h * h)
        bmi.append(temp)
    return bmi


def apply_limit(bmi: list[int | float], limit: int) -> list[bool]:
    for num in bmi:
        if not isinstance(num, (int, float)):
            raise TypeError("Wrong type of vlaues in list")
    return [limit < num for num in bmi]
