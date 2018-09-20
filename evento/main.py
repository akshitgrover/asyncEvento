from _error import errorHandler, ListenerCountReached
from emitHandler import handlerSynchronous

class EventoEmitter:

    __defaultMaxListeners = 11

    def __init__(self):
        
        self.__maxListeners = self.__defaultMaxListeners
        self.__events = []
        self.__onceListeners = {}
        self.__onListeners = {}
        self.__events.append("error")
        self.__onListeners["error"] = [errorHandler]
    
    @classmethod
    def setDefaultMaxListeners(cls, n):
        cls.defaultMaxListeners = n

    def setMaxListener(self, n):
        self.__maxListeners = n

    def __addListener(self, eventName, func, once = False):

        try:
            _ = self.__events.index(eventName)
        
        except(ValueError):
            self.__events.append(eventName)

        count = len(self.__onListeners[eventName]) if (eventName in self.__onListeners) else 0
        count += len(self.__onceListeners[eventName]) if (eventName in self.__onceListeners) else 0

        if(count >= self.__maxListeners):
            listenerError = ListenerCountReached(self.__maxListeners, eventName)
            self.emit("error", listenerError)
            return

        if(once == False):
            if(eventName in self.__onListeners):
                self.__onListeners[eventName].append(func)
            else:
                self.__onListeners[eventName] = [func]
        else:
            if(eventName in self.__onceListeners):
                self.__onceListeners[eventName].append(func)
            else:
                self.__onceListeners[eventName] = [func]

    def getEvents(self):

        return self.__events

    def on(self, eventName, func):
        
        self.__addListener(eventName, func)
    
    def once(self, eventName, func):

        self.__addListener(eventName, func, True)
    
    def removeListener(self, eventName, func):

        def checkLength(eventName):
            
            flag = 0
            if(eventName not in self.__onListeners or eventName not in self.__onceListeners):
                flag += 1

            if(eventName in self.__onListeners and len(self.__onListeners[eventName]) == 0):
                flag += 1
                del self.__onListeners[eventName]
            if(eventName in self.__onceListeners and len(self.__onceListeners[eventName]) == 0):
                flag += 1
                del self.__onceListeners[eventName]

            if(flag == 2):
                index = self.__events.index(eventName)
                self.__events = self.__events[0:index] + self.__events[index + 1:]

        if(eventName in self.__onListeners and func in self.__onListeners[eventName]):

            index = self.__onListeners[eventName].index(func)
            self.__onListeners[eventName] = self.__onListeners[eventName][0:index] + self.__onListeners[eventName][index + 1:]
            checkLength(eventName)

        if(eventName in self.__onceListeners and func in self.__onceListeners[eventName]):
            
            index = self.__onceListeners[eventName].index(func)
            self.__onceListeners[eventName] = self.__onceListeners[eventName][0:index] + self.__onceListeners[eventName][index + 1:]
            checkLength(eventName)
    
    def getMaxListeners(self):

        return self.__maxListeners
    
    def listenerCount(self, eventName):

        count = 0
        
        if(eventName in self.__onListeners):
            count += len(self.__onListeners[eventName])

        if(eventName in self.__onceListeners):
            count += len(self.__onceListeners[eventName])

        return count
    
    def listeners(self, eventName):

        listenersList = {}

        if(eventName in self.__onListeners):
            listenersList["on"] = self.__onListeners[eventName]

        if(eventName in self.__onceListeners):
            listenersList["once"] = self.__onceListeners[eventName]
    
    def emit(self, eventName, synchronous = True, *params):

        tasks = []

        if(eventName in self.__onceListeners):
            tasks += self.__onceListeners[eventName]
            del self.__onceListeners[eventName]
        
        if(eventName in self.__onListeners):
            tasks += self.__onListeners[eventName]

        if(synchronous):
            handlerSynchronous(tasks, params)
