from commanger import commanger


cmd = commanger("cmd")
l={
    "t": {
        "type": "tg", #Char toggle, eg. -t
        "base": False #Without -t arg it is false
    },
    "toggle": {
        "type": "ltg", #Long string toggle, eg. --toggle
        "base": True #Without --toggle arg it is true
    },
    1: { #name does not matter for positional arguments. The outtput name is the pos number in str form
        "type": "pos", #Positional argument
        "in": [None], #Input types, [None] is any. can be like: [str, int, list]
        "pos": 1 #Position of the arg
    },
    "c": {
        "type": "char", #Called like: commandname -c int/str_value --next_arg
        "in": [str, int]
    },
    "long": {
        "type": "long", #Called like: commandname --long (tupe, list) -n
        "in": [list, tuple] 
    },
    "S": {
        "type": "sticky", #Called like: commandname -S{dict} --next_arg
        "in": [dict]
    },
    "R": {
       "type": "range", #Called like: commandname -R ::hi hello lol hehe:: --next_arg
        "in": [str],
        "quote": "::",
        "bquote": "::"
    },
    "r": {
        "type": "srange", #Called like: commandname -r(hi hello tehe) -n
        "in": [str],
        "quote": "(",
        "bquote": ")"       
    },
    "longR": {
        "type": "lrange", #Called like: commandname --longR +<hello world>+ -n
        "in": [str],
        "quote": "+<",
        "bquote": ">+"
    },
    "hard": {
        "type": "hard", #A long that is required
        "in": [int]
    }
}

#hello = cmd.subCommand("hello")
cmd.basicCfig(["h",1,2])

#print(cmd.config(
#@hello.commandU
#def hello(**kwargs):
#    print(kwargs)


    
#@cmd.commandU
def com(**kwargs):
    print(kwargs)
cmd.tup = com
cmd.tups("main.py hi hello -h", u=True)

