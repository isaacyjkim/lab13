import puppy_state
import state_eat

class StateAsleep:
    # puppy wakes up to eat, changes to eat state.
    def feed(self, puppy):
        puppy.change_state(state_eat.StateEat())
        print ('The puppy wakes up and comes running to eat.')
        
    # doesn't let user play with puppy when it is asleep.
    def play(self,puppy):
        print ('The puppy is asleep right now. It doesn\'t want to play right now.')
