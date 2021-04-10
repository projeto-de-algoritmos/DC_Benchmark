def random_generator(size: int):
    """Create a list of random numbers 

            Parameters:
                    size (int): the size of the list

            Returns:
                    numbers (list): the new list with random numbers
    """
    import random
    numbers = []
    for i in range(size):
        n = random.randint(1,100000)
        numbers.append(n)
    return numbers

def ascending_generator(size: int) -> list:
    """Create a ascending list

            Parameters:
                    size (int): the size of the list

            Returns:
                    numbers (list): the new list with random numbers
    """
    numbers = []
    for i in range(size):
        numbers.append(i)
    return numbers

def descending_generator(size: int) -> list:
    """Create a descending list

            Parameters:
                    size (int): the size of the list

            Returns:
                    numbers (list): the new list with random numbers
    """
    numbers = []
    aux = 1000000
    for i in range(size):
        numbers.append(aux)
        aux = aux - 1
    return numbers

def equal_generator(size: int) -> list:
    """Create a list with the same element

            Parameters:
                    size (int): the size of the list

            Returns:
                    numbers (list): the new list with random numbers
    """
    numbers = []
    for i in range(size):
        numbers.append(5)
    return numbers
