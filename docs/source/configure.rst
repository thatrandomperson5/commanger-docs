#####
Configure Commanger: configure all the way!
#####

How to configure commanger!

*****
Configuration tutorial
*****

As you might have seen, there is a nice tool I made called ``basicCfig()``. Which generates and sets the config with simple settings. You can check the actual config with this code:

.. code:: python

  from commanger import commanger
  comm = commanger("cmd")
  comm.basicCfig([1,2,"a","be"])
  print(comm.ppconfig()) #Pretty print the config
..
You should get this output in your console:

.. code:: python

  {

      1: {
          type: pos,
          in: [None],
          pos: 1,
          base: None, #Gen error, will be patched
      }, 

      2: {
          type: pos,
          in: [None],
          pos: 2,
          base: None, #Gen error, will be patched
      }, 

      a: {
          type: tg,
          base: False,
      }, 

      be: {
          type: ltg,
          base: False,
      }, 

  }
..

But as you go on you will realize that the `basicCfig()` function is very limited. So you will need to set it manually as a dict:

First more Advanced cfig
==========

.. code:: python

  comm.cfig = {
      "a": {
          "type": "toggle", #Part 1
          "base": True #Part 2
      },
      1: { #Part 3
          "type": "pos",
          "in": [str, int], #Part 4
          "pos": 1 #Part 5
      }
  }
..

.. note::

 These can get very big. You might want to move it to it's own file then import it
..
Below are the parts as they are marked in the code block.

Part 1 - The type setting
^^^^^^^^^
Here is the type of the arg. There are alot of types with different config settings but there will always be the `"type"` config setting. If you have a invalid type your config branch will be ignored. As shown above the type is set to `"tg"` or toggle.

---------------

Part 2 - Toggle base setting
^^^^^^^^^
The toggle `"base"` setting is default value of a toggle or long toggle. For example (With a's `"base"` as ``True``) if did not have the ``-a`` arg then it will go to the default value, if the arg is there it will be the opposite. So true and false.

---------------

Part 3 - Positinal argument naming
^^^^^^^^^

.. note:: 

 Positinal arguments names do not matter. More info in part 5.
..

------------------

Part 4 - The In setting
^^^^^^^^^

The in setting it to regulate what kind of input the arguments can receive. You use type objects like ``str, int, list, tuple, set, dict`` (All of those work), You can also accept any with ``[None]``. If the user gives a wrong type it throws an ``ArgumentTypeError``.

.. note::

 The `"in"` setting is used by alot of arg types.
..

-------------------

Part 5 - The position
^^^^^^^^^

The pos setting is what position the positional argument will be called at. It is also the name (in string form) of the output argument. Setting the pos to 0 won't work becuase the name of the file takes that position, so always start with ``pos:1``

------------------

Types: introduction
==========

A list of the other types below:

 * Toggle
 * Char
 * Long
 * Sticky
 * Range
 * Hard

------------------

*****
Types:
*****

Toggle
======

A char that can be True or False depending on settings(Above) and if it exists. example of calling:

.. code:: console

 python main.py -t
..

Example config:

.. code:: python

    "t": {
        "type": "tg", #Char toggle, eg. -t
        "base": False #Without -t arg it is false
    },
..

Long Toggle
^^^^^^
A toggle which is a string. example of calling:

.. code:: console

 python main.py --toggle
..

Example config:

.. code:: python

    "toggle": {
        "type": "ltg", #Long string toggle, eg. --toggle
        "base": True #Without --toggle arg it is true
    },
..

Char
======
A char argument with a value after it. example:

.. code:: console

 python main.py -c hello
                ^   ^
                1   2
..

Now the char "c"[1] has the value of hello[2]. If char "c" does not exist the value will return None. If c does not have a value an error should be thrown.

Example config:

.. code:: python

    "c": {
        "type": "char", #Called like: commandname -c int/str_value --next_arg
        "in": [str, int]
    },
..

Long
=====

Longs are basically chars but with a string name:

.. code:: console

 python main.py --long hello
..

Now long is set to hello.

Example config:

.. code:: python

    "long": {
        "type": "long", #Called like: commandname --long (tupe, list) -n
        "in": [list, tuple] 
    },
..

Sticky
=====

A sticky is a sticky char. instead of the name and the value being 2 arguments, they are one. Example:

.. code:: console

 python main.py -Shello
                ^  ^
                1  2
..

Now S[1] has the value of hello[2]. Notice how they look like they are sticking to eachother, that is why they are "sticky".

Example config:

.. code:: python

    "S": {
        "type": "sticky", #Called like: commandname -S{dict} --next_arg
        "in": [dict]
    },
..

Range
=====

Ranges are chars with start quotes and end quotes to contain a value. The quotes are defined in the config with ``"quote":`` and ``"bquote":``. Example with quotes as "<" and ">":

.. code:: console

 python main.py -r <hello world haha lol>

..

Now r will be set to "hello world haha lol"

Example config:

.. code:: python

    "R": {
       "type": "range", #Called like: commandname -R ::hi hello lol hehe:: --next_arg
        "in": [str],
        "quote": "::",
        "bquote": "::"
    },
..

Sticky Range
^^^^^
A range except there is no space between the char and the front quote. Example:

.. code:: console

 python main.py -R<hello world>
..

R is now "hello world"

Example config:

.. code:: python

    "r": {
        "type": "srange", #Called like: commandname -r(hi hello tehe) -n
        "in": [str],
        "quote": "(",
        "bquote": ")"       
    },
..

Long Range
^^^^^
A range but has a string instead of a char as a name. Example:

.. code:: console

 python main.py --lrange <hi hello>
..

lrange is now set to "hi hello".

Example config:

.. code:: python

    "longR": {
        "type": "lrange", #Called like: commandname --longR +<hello world>+ -n
        "in": [str],
        "quote": "+<",
        "bquote": ">+"
    },
..

Hard
=====

Like a long except it is required. If you don't have it it will throw an error. Example!

.. code:: console

 python main.py -*hard hello
..

The hard is now set to hello.

Example config:

.. code:: python

    "hard": {
        "type": "hard", #A long that is required
        "in": [int]
    }
..
