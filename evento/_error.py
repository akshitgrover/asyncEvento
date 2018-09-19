class ListenerCountReached(Exception):
    
    def string(self, event):
        return "ListenerCountReached: Maxium Listener count for '{}' reached".format(event)

    pass


def errorHandler(self,err):
    
    print(err.string(self.eventName))
