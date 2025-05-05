import puppy_state
import random
from state_play import StatePlay
from state_asleep import StateAsleep


class StateEat:
    def feed(self, puppy):
        times = random.choice([3,2])
        add = ""
        if puppy._feeds == times:
            puppy.change_state(StateAsleep)
            add = '\n The puppy ate so much it fell asleep!'
        return ('The puppy continues to eat as you add another scoop of kibble to its bowl.'+add)

    def play(self,puppy):
        puppy.change_state(StatePlay)
        return ('The puppy looks up from its food and chases the ball you threw.')
