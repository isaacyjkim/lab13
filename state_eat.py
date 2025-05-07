import puppy_state
import random
import state_play
import state_asleep 

#from state_play import StatePlay
#from state_asleep import StateAsleep


class StateEat:
    def feed(self, puppy):
        puppy.inc_feeds()
        if puppy._feeds == 3:
            puppy.change_state(state_asleep.StateAsleep())
            puppy.reset()
            print('The puppy continues to eat as you add another scoop of kibble to its bowl.\n The puppy ate so much it fell asleep!')
        else:
            print ('The puppy continues to eat as you add another scoop of kibble to its bowl.')

    def play(self,puppy):
        puppy.change_state(state_play.StatePlay())
        print ('The puppy looks up from its food and chases the ball you threw.')
