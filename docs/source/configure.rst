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

Part 1
^^^^^^^^^
Here is the type of the arg. There are alot of types with different config settings but there will always be the `"type"` config setting.

*****
Types:
*****

Toggle
======

Long Toggle
^^^^^^

Char
======

Long
=====

Sticky
=====

Range
=====

Sticky Range
^^^^^

Long Range
^^^^^

Hard
=====


