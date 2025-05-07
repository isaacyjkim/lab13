import puppy_state
import random
import state_asleep
# from state_eat import StateEat
#from state_asleep import StateAsleep

class StatePlay:
    def feed(self, puppy):
        print ('The puppy is too busy playing with the ball to eat right now.')

    def play(self,puppy):
        times = random.choice([3,2])
        puppy.change_state(state_asleep.StateAsleep())
        puppy.inc_plays()
        if puppy._plays == times:
            print('You throw the ball again and the puppy excitedly chases it. \n The puppy played so much it fell asleep!')
        print ('You throw the ball again and the puppy excitedly chases it.')
