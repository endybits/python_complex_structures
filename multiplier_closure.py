
def make_multiplier(n: int):
    """This function is a closure because:
        - Has a nested function
        - The nested function uses an argument from its superior scope
        - The father function returns the nested function
        

    Args:
        n (int): This value will be multuplied in the nested function
    
    Return: A nested function
    """

    def multiplier(number: int):
        return number * n
    
    return multiplier


def run():
    n = 5
    print('n = ' + str(n))
    mult_by_ten = make_multiplier(10)
    print('n * ten = ' + str(mult_by_ten(n)))

    mult_by_five = make_multiplier(5)
    print('n * five = ' + str(mult_by_five(n)))

    mult_by_twfive = make_multiplier(25)
    print('n * twenty five = ' + str(mult_by_twfive(n)))


if __name__ == '__main__':
    run()