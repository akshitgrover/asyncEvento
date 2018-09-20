===========
asyncEvento
===========

.. image:: https://travis-ci.org/akshitgrover/asyncEvento.svg?branch=master
    :target: https://travis-ci.org/akshitgrover/asyncEvento

Fully asynchronous python library to listen and emit events like in nodejs

Installation
============

::

    `pip install asyncEvento`

Compatibilty
============

py36, py37


Usage
=====

Read docs at: Docs_

.. _Docs: https://akshitgrover.github.io/asyncEvento/docs/index.html


Why asyncEvento
===============
Handling asynchronous coroutines can be painful at times, using asyncEvento one can register a function with a certain event and later can fire the event on completion of some asynchronous tasks, which will in turn lead to execute all the functions registered to the event which was fired. 

Read the Docs for more info_

.. _info: https://akshitgrover.github.io/asyncEvento/docs/index.html


Scope
=====

asyncEvento can be used in many areas where asynchronous tasks are to be handled with much ease.

For eg: **Asynchronous file handling**

Copyright
=========

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