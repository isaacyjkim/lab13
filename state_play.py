import puppy_state
import random
from state_eat import StateEat
from state_asleep import StateAsleep

class StatePlay:
    def feed(self, puppy):
        return ('The puppy is too busy playing with the ball to eat right now.')

    def play(self,puppy):
        times = random.choice([3,2])
        add = ""
        if puppy._plays == times:
            puppy.change_state(StateAsleep)
            add = '\n The puppy played so much it fell asleep!'
        return ('You throw the ball again and the puppy excitedly chases it.'+add)
