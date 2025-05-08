import puppy_state
import random
import state_asleep

class StatePlay:
    # doesn't let user feel the puppy when puppy is in play state. 
    def feed(self, puppy):
        print ('The puppy is too busy playing with the ball to eat right now.')

    # plays with puppy until it's tired and changes state to asleep.
    def play(self,puppy):
        puppy.inc_plays()
        if puppy._plays == 3:
            puppy.change_state(state_asleep.StateAsleep())
            puppy.reset()
            print('You throw the ball again and the puppy excitedly chases it. \nThe puppy played so much it fell asleep!')
        else:
            print ('You throw the ball again and the puppy excitedly chases it.')
