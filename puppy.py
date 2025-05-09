import state_asleep

class Puppy: 

    """
    The Puppy class represents a puppy that can be in different states.
    It can be in a sleeping state or an active state. The puppy can be fed
    or played with, and its state will change accordingly.
    """
    def __init__(self): 
        # Initialize the puppy in the sleeping state
        self._state = state_asleep.StateAsleep()
        self._feeds = 0 
        self._plays = 0 

    @property
    def _feed(self): 
        # The number of times the puppy has been fed
        return self._feeds

    @property
    def _play(self): 
        # The number of times the puppy has played
        return self._plays

    def change_state(self, new_state): 
        # Change the state of the puppy
        self._state = new_state

    def throw_ball(self):
        # Throw a ball for the puppy to play with
        self._state.play(self) 
    
    def give_food(self): 
        # Give food to the puppy
        self._state.feed(self)

    def inc_feeds(self): 
        # Increment the feed count
        self._feeds += 1

    def inc_plays(self):
        # Increment the play count
        self._plays += 1    
    
    def reset(self): 
        # Reset the puppy's state and counts
        self._feeds = 0
        self._plays = 0