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
    #main.py
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

Lets call it now with:

.. code:: bash

    python main.py hello world
..

With your current code you should get this result:

.. code:: python

    {"1": "hello", "1": "world", "b": False, "c": False}
..

If you run this: ``python main.py hello world -b``,
you get:

.. code:: python

    {"1": "hello", "1": "world", "b": True, "c": False}
..

And if you run this: ``python main.py helloworld``,
you should get the error:

.. code:: python

   commanger.commanger.ArgumentError: Arg number 2 not in ["main.py","helloworld"]
..

You can do what you want with the args in the main function, it's up to you. Thats it for basic usage!

.. note::
 In the future I will add more tools to help you manage arguments
..
.. 
 Future note. remove later
.. 

------------------------------------------------------------------------------------------------------------------------
------------------------------------------------------------------------------------------------------------------------
------------------------------------------------------------------------------------------------------------------------
 
*********************
Tool usage
*********************
          ===========================
commanger.ppconfig(self, config=None):
          ============================
