import puppy_state

class Puppy: 


    def __init__(self): 
        self._state = puppy_state.state_asleep.StateAsleep()
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
        self._state.play() 
    
    def give_food(self): 
        self._state.feed()

    def inc_feeds(self): 
        self._feeds += 1

    def inc_plays(self):
        self._plays += 1    
    
    def reset(self): 
        self._feeds = 0
        self._plays = 0