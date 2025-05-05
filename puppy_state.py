
import abc
import state_asleep 
import state_eat
import state_play

class PuppyState(abc.ABC): 

    @abc.abstractmethod
    def feed(self,puppy): 
        pass 

    @abc.abstractmethod
    def play(self,puppy): 
        pass



