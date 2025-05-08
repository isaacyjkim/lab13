import puppy_state
import random
import state_play
import state_asleep 

class StateEat:
    # feeds the puppy until it is too full to eat. Changes to asleep state after it's full.
    def feed(self, puppy):
        puppy.inc_feeds()
        if puppy._feeds == 3:
            puppy.change_state(state_asleep.StateAsleep())
            puppy.reset()
            print('The puppy continues to eat as you add another scoop of kibble to its bowl.\nThe puppy ate so much it fell asleep!')
        else:
            print ('The puppy continues to eat as you add another scoop of kibble to its bowl.')

    # plays with puppy and changes its state from eating to playing.
    def play(self,puppy):
        puppy.change_state(state_play.StatePlay())
        print ('The puppy looks up from its food and chases the ball you threw.')
