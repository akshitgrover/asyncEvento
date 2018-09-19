from _error import errorHandler, ListenerCountReached
import methods

class EventoEmitter:
    
    __events = []
    __onceListeners = {}
    __onListeners = {}

    def __init__(self):
        
        self.__events.append("error")
        self.__onListeners["error"] = errorHandler

    def __addListener(self, eventName, func):

        self.__events.append(eventName)
        
        if(eventName in self.__onListeners):
            self.__onListeners[eventName].append(func)
        elif(len(self.__onListeners) == 11):
            raise ListenerCountReached
        else:
            self.__onListeners[eventName].append(func)

    def on(self, eventName, func):
        
        methods.on(self, eventName, func)    
