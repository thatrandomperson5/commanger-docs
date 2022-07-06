# Commanger for python
A easy to use, extremely configurable shell/terminal command manager for python.

At first it may just look like any other command line parser but it has so much more!
You don't have to ever configure the parsing yourself, you can just tell it what you wan't.
It also deals with stray non specfied arguments and I am always adding more!
## Basic example:
>#### Importation and initialization
```py
from commanger import commanger
cmd = commanger("cmd")
```
>#### The main Function and config
```py
cmd.basicConfig([1,2,"b"]) #set a basic config

@cmd.command #Attach the main func
def main(args): #Take in the args
    print(args)
```
### Places:
* #### [Docs](https://python-commanger-docs.readthedocs.io/en/latest/)
* #### [Github](https://github.com/thatrandomperson5/commanger-docs)