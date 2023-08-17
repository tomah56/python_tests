def callLimit(limit: int):
    count = 0

    def callLimiter(function):
        nonlocal count

        def limit_function(*args: any, **kwds: any):
            nonlocal count
            if count < limit:
                count += 1
                return function(*args, **kwds)
            else:
                print(f"<function '{function.__name__}' ", end='')
                print(f"at {hex(id(function))}> call too many times")
                # raise RuntimeError("Too many function call!")
                return None

        return limit_function

    return callLimiter
