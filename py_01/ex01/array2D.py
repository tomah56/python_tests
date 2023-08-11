import numpy as np


def checker(givelist: list[int | float]) -> bool:
    """
This function checks the validity of input
"""
    if not isinstance(givelist, list):
        raise TypeError("Only lists are valid arguments")
    terunt_value = True
    for sublist in givelist:
        if isinstance(sublist, list):
            for num in sublist:
                if not isinstance(num, (int, float)):
                    raise TypeError("Wrong type of vlaues in list")
        else:
            if not isinstance(sublist, (int, float)):
                raise TypeError("Wrong type of vlaues in list")
            terunt_value = False
    return terunt_value


def shapedefiner(family: list[int | float]) -> list:
    """
This function returns the shape of a givven list.
"""
    if not isinstance(family, list):
        raise TypeError("Only lists are valid arguments")
    shape_x = len(family)
    shape_y = 1
    if checker(family):
        shape_y = len(family[0])
        if not all(len(sublist) == shape_y for sublist in family):
            raise ValueError("Missmaching size of array")
    return [shape_x, shape_y]


def slice_me(family: list, start: int, end: int) -> list:
    """
This function return a new shape checks the input.
"""
    try:
        list_manipulate = np.array(family, dtype=np.float64)
        print(f"My Shape is : {list_manipulate.shape}")
        newshape = list_manipulate[start:end]
        print(f"My New Shape is : {newshape.shape}")
    except (ValueError, TypeError) as e:
        print("Error:", e)
        return []
    # old version
    # myshape_before = shapedefiner(family)
    # print(f"My shape is : ({myshape_before[0]}, {myshape_before[1]})")
    # new_shape = family[start:end]
    # myshape_after = shapedefiner(new_shape)
    # print(f"My new shape is : ({myshape_after[0]}, {myshape_after[1]})")
    return newshape.tolist()
