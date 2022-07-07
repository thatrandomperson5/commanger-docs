Tups in commanger
==================

What is tup?
It's a minimal way to call commands without the command line. It may be usefull if you are making your own command line.

*****
Tup setup
*****

You set your function to a tup var so you can have a command line command and a tups command.

.. code:: python

    def com(**kwargs):
        print(kwargs)
    cmd.tup = com

..

****
Tups calling
****
You can call tups via:

.. code:: python
    
    cmd.tups("main.py hi hello -h", u=True) #U is like a U command, default if False
..
.. warning::
 Tups is minimal and does not support ease of use things. You will have to do part of the command breaking in your funtion or to the input string.
****
Tup support
****

Tups is meant to be minimal and will not be worked on unless needed or requested.

.. toktree::
   :hidden:
   
   sub
   tups
