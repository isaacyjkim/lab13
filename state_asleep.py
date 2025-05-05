import puppy_state
from state_play import StatePlay
from state_eat import StateEat

class StateAsleep:
    def feed(self, puppy):
        puppy.change_state(StateEat())
        return ('The puppy wakes up and comes running to eat.')
        

    def play(self,puppy):
        return ('The puppy is asleep right now. It doesn\'t want to play right now.')
