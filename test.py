import unittest
import asyncEvento
import asyncio

class TestSynchronousEmit(unittest.TestCase):

    def test(self):
        
        emitter = asyncEvento.EventoEmitter()

        def hello():
            print("\nHello World (Synchronous)\n")
            emitter.emit("stop", True)
        
        emitter.on("hello", hello)
        emitter.once("stop", asyncEvento.EventoEmitter.stop)
        emitter.emit("hello")

        emitter.listen()

class TestAsynchronousEmit(unittest.TestCase):

    def test(self):
        
        emitter = asyncEvento.EventoEmitter()

        async def hello():
            await asyncio.sleep(1)
            print("\nHello World (Asynchronous)\n")
            emitter.emit("stop", True)
        
        emitter.on("hello", hello)
        emitter.once("stop", asyncEvento.EventoEmitter.stop)
        emitter.emit("hello", True)

        emitter.listen()

if __name__ == "__main__":
    unittest.main()
