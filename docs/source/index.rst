Welcome to Commanger's documentation!
===================================

**Commanger** (/com-manger/) A easy to use, extremely configurable shell/terminal command manager for
python.

.. note::

   This project is under active development.

At first it may just look like any other command line parser but it has
so much more! You don’t have to ever configure the parsing yourself, you
can just tell it what you wan’t. It also deals with stray non specfied
arguments and I am always adding more!

Basic example:
--------------


.. code:: py
   

   from commanger import commanger #Setup
   cmd = commanger("cmd")

..

      
.. code:: py


   cmd.basicConfig([1,2,"b"]) #set a basic config

   @cmd.command #Attach the main func
   def main(args): #Take in the args
       print(args)
..

Contents
--------

.. toctree::
   :maxdepth: 2
   usage
   configure
   Beta
       Beta/sub
       Beta/tups
   

