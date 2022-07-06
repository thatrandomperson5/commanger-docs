from pyparsing import *

class RecCommBlock:
    def __init__(self):
        self.funct=None
        self.maxRecs=None
    def __push(self, funct):
        self.funct = funct
    def __call__(self, *args, **kwargs):
        
        a = self.funct(*args, **kwargs)
  
        return a
    def __ilshift__(self, val):
        self.__push(val)
        return self


pr = printables.replace("]","").replace("[","").replace(",","").replace(":","").replace("}","").replace("{","").replace("(","").replace(")","")+" "
string = Word(pr).setResultsName("str")
integer = (Optional(Char("-"))+ OneOrMore(Char(nums)+Optional(Char(".")))).setResultsName("int")
tuple_ = Forward()
set_= Forward()
list_ = Forward()
dict_ = Forward()
object=integer|tuple_|set_|list_|dict_|string
tuple2 = Suppress(Literal("+t["))+Group(delimited_list(Group(object), delim=','))+Suppress("]")
tuple_ <<= ((Suppress("(")+delimited_list(Group(object), delim=',')+Suppress(")"))|tuple2).setResultsName("tuple")
set2 = (Suppress(Literal("+e["))+Group(delimited_list(Group(object), delim=','))+Suppress("]"))
set_ <<= ((Suppress("{")+delimited_list(Group(object), delim=',')+Suppress("}"))|set2).setResultsName("set")
list_ <<= (Suppress("[")+delimited_list(Group(object), delim=',')+Suppress("]")).setResultsName("list")
dict2 = Suppress(Word("+d["))+delimited_list(Group(Group(object)+Suppress(":")+Group(object)), delim=",")+Suppress("]")
dict_ <<= Group((Suppress("{")+delimited_list(Group(Group(object)+Suppress(":")+Group(object)), delim=",")+Suppress("}"))|dict2).setResultsName("dict")
evalChunck = RecCommBlock()
def evalChunck_(chunk):
    o = chunk

    out = None
    def unique(sequence):
        seen = set()
        return [x for x in sequence if not (x in seen or seen.add(x))]       
    if list(o.keys())[0] == "dict":
        out = {}
        for x, y in o['dict']:
            x = evalChunck(x)
            y = evalChunck(y)
            out[x] = y
    elif list(o.keys())[0] == "list":
        out = []
        for x in o["list"]:
            x = evalChunck(x)
            out.append(x)

    elif list(o.keys())[0] == "set":
        out = []
        
        for x in o["set"]:
            
            x = evalChunck(x)
            out.append(x)
        tup = tuple(out)
        
        out = unique(tup)
        
    elif list(o.keys())[0] == "tuple":
        out = []
        for x in o["tuple"]:
            x = evalChunck(x)
            out.append(x)
        out = tuple(out)
    elif list(o.keys())[0] == "str":
        out = str(o["str"])
    elif list(o.keys())[0] == "int":
        try:
            out = int("".join(o["int"]))
        except ValueError:
            out = float("".join(o["int"]))
    return out
evalChunck <<= evalChunck_
def NoneVar(sttr):
    
    ck = object.parse_string(sttr).as_dict()
    
    ck = evalChunck(ck)
    return ck