import state_asleep

class Puppy: 


    def __init__(self): 
        self._state = state_asleep.StateAsleep()
        self._feeds = 0 
        self._plays = 0 

    @property
    def _feed(self): 
        return self._feeds

    @property
    def _play(self): 
        return self._plays

    def change_state(self, new_state): 
        self._state = new_state

    def throw_ball(self):
        self._state.play(self) 
    
    def give_food(self): 
        self._state.feed(self)

    def inc_feeds(self): 
        self._feeds += 1

    def inc_plays(self):
        self._plays += 1    
    
    def reset(self): 
        self._feeds = 0
        self._plays = 0