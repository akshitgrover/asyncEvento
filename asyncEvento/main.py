"""
   Copyright 2018 Akshit Grover

   Licensed under the Apache License, Version 2.0 (the "License");
   you may not use this file except in compliance with the License.
   You may obtain a copy of the License at

       http://www.apache.org/licenses/LICENSE-2.0

   Unless required by applicable law or agreed to in writing, software
   distributed under the License is distributed on an "AS IS" BASIS,
   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
   See the License for the specific language governing permissions and
   limitations under the License.
"""

import  asyncio

from ._error import errorHandler, ListenerCountReached
from .emitHandler import handlerSynchronous, handlerAsynchronous

class EventoEmitter():

    __defaultMaxListeners = 11
    __loop = None

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
    
    @classmethod
    def listen(cls):
        cls.__loop = asyncio.get_event_loop()
        cls.__loop.run_forever()
    
    @classmethod
    async def stop(cls):

        if(cls.__loop is not None):
            cls.__loop.stop()

    def setMaxListeners(self, n):
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
    
    def emit(self, eventName, asynchronous = False, *params):

        tasks = []

        if(eventName in self.__onceListeners):
            tasks += self.__onceListeners[eventName]
            del self.__onceListeners[eventName]
        
        if(eventName in self.__onListeners):
            tasks += self.__onListeners[eventName]

        if(asynchronous == False):
            handlerSynchronous(tasks, params)
        else:
            asyncio.ensure_future(handlerAsynchronous(tasks, params))
            
