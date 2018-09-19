from _error import errorHandler

class EventoEmitter:
    
    __events = []
    __onceListeners = {}
    __onListerners = {}

    def __init__(self):
        
        self.__events.append("error")
        self.__onListerners["error"] = errorHandler    
