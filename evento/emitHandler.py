def handlerSynchronous(tasks, params):
    
    for task in tasks:
        task(*params)
