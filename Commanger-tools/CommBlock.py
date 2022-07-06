class CommFunctBlock:
    def __init__(self):
        self.funct = None
        self.tupe = ()
        self.kwargs = {}
    def __push(self, val):
        if type(val) is tuple:
            self.tupe = val
        elif type(val) is dict:
            self.kwargs = dict
        elif callable(val):
            self.funct = val
    def __ilshift__(self, val):
        self.__push(val)
    
        return self
    class EmptyKeyArgumentError(Exception):
        pass

    def __call__(self, *args, **kwargs):
        if self.funct == None:
            error = "Function has not yet been pushed"
            raise self.EmptyKeyArgumentError(error)
            self.funct(*self.tupe, *args, **self.kwargs, **kwargs) 
class RecCommBlock:
    def __init__(self):
        self.funct=None
        self.maxRecs=None
    def __push(self, funct):
        self.funct = funct
    def __call__(self):
        self.funct()
    def __ilshift__(self, val):
        self.__push(val)
def CommBlock(*, type):
    if type in ["funct","func","function"]:
        return CommFunctBlock()
    elif type in ["rec", 'recursive']:
        return RecCommBlock
















        
