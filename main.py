import check_input
from puppy import Puppy
from puppy_state import PuppyState


def main():
    print('Congratulations on your new puppy!')
    puppy = Puppy()
    # asks user to feed/play with the puppy until user quits
    while True:
        print('What would you like to do?')
        print('1. Feed the puppy')
        print('2. Play with the puppy')
        print('3. Quit')
        choice = check_input.get_int_range('Enter choice: ',1, 3)

        # calls appropriate function regarding the puppy's state and user's choice
        if choice == 1:
            puppy.give_food()
        elif choice == 2:
            puppy.throw_ball()
        else:
            break
        
        
main()
