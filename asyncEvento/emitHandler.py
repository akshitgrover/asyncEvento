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

import asyncio

async def handlerSynchronous(tasks, params):

    for task in tasks:
        await asyncio.ensure_future(task(*params))

async def handlerAsynchronous(tasks, params):

    sem = asyncio.Semaphore(3)
    
    async def wrap(task, args):

        await sem.acquire()
        await task(*args)
        sem.release()
    
    await asyncio.gather(*[wrap(task, params) for task in tasks])
    