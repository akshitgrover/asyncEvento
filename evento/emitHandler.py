import asyncio

def handlerSynchronous(tasks, params):
    
    for task in tasks:
        task(*params)

async def handlerAsynchronous(tasks, params):

    sem = asyncio.Semaphore(3)
    
    async def wrap(task, args):

        await sem.acquire()
        await task(*args)
        sem.release()
    
    await asyncio.gather(*[wrap(task, params) for task in tasks])
    