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

from distutils.core import setup
import codecs

setup (

    name = "asyncEvento",
    version = "0.1.7",
    author = "Akshit Grover",
    author_email = "akshit.grover2016@gmail.com",
    description = "Fully asynhronous python library to listen and emit events like in nodejs",
    packages = ["asyncEvento"],
    long_description = open("Readme.rst").read(),
    license = "LICENSE",
    url = "https://github.com/akshitgrover/asyncEvento",
    keywords = "events asynchronous emit on once listen",
    classifiers = [

        "Development Status :: 2 - Pre-Alpha",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7"
    
    ]

)