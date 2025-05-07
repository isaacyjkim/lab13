import puppy_state
import state_eat
# from state_play import StatePlay
# from state_eat import StateEat

class StateAsleep:
    def feed(self, puppy):
        puppy.change_state(state_eat.StateEat())
        print ('The puppy wakes up and comes running to eat.')
        

    def play(self,puppy):
        print ('The puppy is asleep right now. It doesn\'t want to play right now.')
