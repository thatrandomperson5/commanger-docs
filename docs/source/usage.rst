Usage of Commanger
=================


*************
Installation
*************

Pip is the best way to install Commanger, you can do it with the command below

.. code:: bash

    pip install commanger

..
but if you don't want to you can install is `here <https://pypi.org/project/commanger/#files>`_ on pypi.


******************
Setup
******************
Once you install commanger the next step is preparing the file with basic code:

.. code:: python
    
    from commanger import commanger
    cmd = commanger("cmd")
..

.. note::
 commanger should only be called once per process
..
As shown above you need to import the class then init it with ``commanger(name)``, name is not yet used. Now lets get started!

************************
Basic Example: Continued
************************


We start where we left off:

.. code:: python

cmd.basicConfig([1,2,"b"]) #set a basic config

@cmd.command #Attach the main func
def main(args): #Take in the args
    print(args)

..
Now lets change the config abit:

.. code:: python

cmd.basicConfig([1,2,"b","c"])

..

.. note::
Nums in the basic config are positional arguments and strings are toggle arguments.
..

Now we should have a config with 2 positional arguments and 2 toggles, one named "b" and the other named "c"
