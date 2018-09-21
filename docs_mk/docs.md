# How to Use asyncEvento

asyncEvento lib follows a singleton pattern, A base class is used to extend or create emitter instances which are are further used to add as well as listen to certain events.

## EventoEmitter Class
***
### Base emitter class, Can be used both as extension and parent class.

Usage:

```python

from asyncEvento import EventoEmitter

emitter = EventoEmitter() # Single entrypoint of emitter methods

```
***
<br>

## < class >.setDefaultMaxListeners(n)
***
### {n:"integer"} <br><br>

### Set number of listeners allowed on a all the event of every class instance, By default it is set to 11.

Usage:

```python

from asyncEvento import EventoEmitter

emitter1 = EventoEmitter() # Will have 11 listeners allowed for each event

EventoEmitter.setMaxListeners(16) # Will set default listeners count to 16

emitter2 = EventoEmitter() # Will have 16 listeners allowed for each event

emitter3 = EventoEmitter() # Will have 16 listeners allowed for each event

```
***
<br>


## < class >.listen()
***
Start the event loop, You can choose no to use this method, by running your own loop instead.


> ***Note:***

> This event loop will be common for all the emitter instances created.

Usage:

```python

from asyncEvento import EventoEmitter

emitter = EventoEmitter() # Single entrypoint of emitter methods

```
***
<br>

## < instance >.setMaxListeners(n)
***
### {n:"integer"} <br><br>

### This method is used to setMaxListener for a specific instance of emitter class.

Usage:

```python

from asyncEvento import EventoEmitter

emitter = EventoEmitter() # Single entrypoint of emitter methods

emitter.setMaxListener(16)

```
***
<br>

## < instance >.getEvents()
***
Return an array of all the events having a listener attached.

> ***Note:***
> Will include 'error' by default.

Usage:

```python

from asyncEvento import EventoEmitter

emitter = EventoEmitter() # Single entrypoint of emitter methods

print(emitter.getEvents()) # ["error"]

```
***
<br>

## < instance >.on(eventName, func)
***
### {eventName:"string", func:"function"} <br><br>

### Attaches a listener to an event.

> ***Note:***
> Everytime an event is fired the listener attached will run.

Usage:

```python

from asyncEvento import EventoEmitter

emitter = EventoEmitter() # Single entrypoint of emitter methods

async def hello():
    print("Hello node")

emitter.on("hello", hello)

```
***
<br>

## < instance >.once(eventName, func)
***
### {eventName:"string", func:"function"} <br><br>

### Attaches a listener to an event.

> ***Note:***
> This function ran only once no matter how many times an event is emitted.

Usage:

```python

from asyncEvento import EventoEmitter

emitter = EventoEmitter() # Single entrypoint of emitter methods

async def hello():
    print("Hello node")

emitter.once("hello", hello)

```
***
<br>

## < instance >.removeListener(eventName, func)
***
### {eventName:"string", func:"function"}<br><br>

### Removes a previosly attached listener.

Usage:

```python

from asyncEvento import EventoEmitter

emitter = EventoEmitter() # Single entrypoint of emitter methods

async def hello():
    print("Hello node")

emitter.on("hello", hello)

emitter.removeListener("hello", hello)

```
***
<br>

## < instance >.getMaxListeners()
***
### Returns the number of listeners allowed for this instance per event.

Usage:

```python

from asyncEvento import EventoEmitter

emitter = EventoEmitter()

print(emitter.getMaxListeners()) # 11 (Default, see setMaxListeners)

```
***
<br>

## < instance >.listenerCount(eventName)
***
### {eventName:"string"} <br><br>

### Returns the number of listeners allowed for this instance on a certain event.

Usage:

```python

from asyncEvento import EventoEmitter

emitter = EventoEmitter()

async def hello():
    print("Hello node")

emitter.on("hello", hello)

emitter.on("hello", hello)

print(emitter.listenerCount("hello")) # 2

```
***
<br>

## < instance >.listeners(eventName)
***
### {eventName:"string"} <br><br>

### Returns underlying functions registers as listeners on a particular event.

Usage:

```python

from asyncEvento import EventoEmitter

emitter = EventoEmitter()

async def hello():
    print("Hello node")

emitter.on("hello", hello)

emitter.on("hello", hello)

print(emitter.listeners("hello")) # <function> object

```
***
<br>

## < instance >.emit(eventName, asynchronous = False, *params)
***
### {eventName:"string", params:"argumentsto be passed in registered functions", asynchronous:"flag to control if registered functions are to be executed asynchronously or not"}

Usage:

> Synchronous

```python

from asyncEvento import EventoEmitter

emitter = EventoEmitter()

async def hello():
    print("Hello node")

async def helloV2():
    print("Hello world")

emitter.on("hello", hello)
emitter.on("hello", helloV2)
emitter.once("hello", helloV2)

emitter.emit("hello") 

emitter.listen() # Start the event loop

"""
Output:

Hello node
Hello world
Hello world
"""

```

> Asynchronous

```python

from asyncEvento import EventoEmitter
import asyncio

emitter = EventoEmitter()

async def hello():
    print("Hello node")

async def helloV2():
    await asyncio.sleep(1)
    print("Hello world")

emitter.on("hello", helloV2)
emitter.once("hello", helloV2)
emitter.on("hello", hello)

emitter.emit("hello", True) 

emitter.listen() #Start the event loop

"""
Output:

Hello node
Hello world
Hello world
"""

```