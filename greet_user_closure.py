
def greet_funct(user: str):
    """This function is a closure because:
        - Has a nested function
        - The nested function uses an argument from its superior scope
        - The father function returns the nested function
        

    Args:
        user (str): Username 
    
    Return: A nested function
    """

    def greet():
        print(f'Hi {user}, nice to meet you!')
    
    return greet


def run():
    greet_person = greet_funct('Endy')
    print(greet_person())

if __name__ == '__main__':
    run()