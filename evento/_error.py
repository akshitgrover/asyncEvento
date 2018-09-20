class ListenerCountReached(Exception):
    
    def __init__(self, count = 0, event = ""):
        self.__listenerCount = count
        self.__eventName = event

    def string(self):
        return "\nListenerCountReached: Maximum Listener count '{}' reached for event '{}'\n".format(self.__listenerCount, self.__eventName)

    pass


def errorHandler(err):
    
    print(err.string())
