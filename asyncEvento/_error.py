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

class ListenerCountReached(Exception):
    
    def __init__(self, count = 0, event = ""):
        self.__listenerCount = count
        self.__eventName = event

    def string(self):
        return "\nListenerCountReached: Maximum Listener count '{}' reached for event '{}'\n".format(self.__listenerCount, self.__eventName)

    pass


def errorHandler(err):
    
    print(err.string())
