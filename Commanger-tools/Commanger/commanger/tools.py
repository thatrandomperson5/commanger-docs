import sys
import colorama as cr
from commanger.NoneVar import NoneVar
cr.init(autoreset=True)
class subCommanger:
    def __init__(self, parent, name, depth):
        self.parent = parent
        if type(name) != list:
            self.name = [name]
        else:
            self.name = name
        self.depth = depth
        self.cfig = {}
        self.tup =None
        
        self.argv = sys.argv
    class ArgumentError(Exception):
        def __init__(self, msg):
            
            be = sys.argv[1]+": "
            super().__init__(be+msg)
    class ArgumentTypeError(Exception):
        def __init__(self, msg):
            be = sys.argv[1]+": "
            super().__init__(be+msg)
    def eval(self, val):
 
        a = NoneVar(val)
        return a
    def evalArgs(self, args):
        """
        Dev funct evalArgs:
        Evaluates args.
        """
        
        def findRange(f: str, b: str, rng: slice, *, bump=slice(0,None)):
                look = aargs[rng]
                

                
                if not f in look[0]:
                    error = "Range start not in start"
                    raise self.ArgumentError(error)
                if not self.sliceList(look, b):
                    error = "Range end does not exist"
                    raise self.ArgumentError(error)
                out = look[0][bump]
                out = out[out.rfind(f)+len(f):]
                for x in look[1:]:
                    if not b in x:
                        out = out+" "+x
                    else:
                        out = out+" "+x[:x.rfind(b)]
                        break
                return out
        def indexExists(list,index):
            if 0 <= index < len(list):
                return True
            else:
                return False
        o = {}
        i = 1
        c = self.cfig
        covered = []
        for k in c.keys():
            ck = c[k]
            rtype = ck["type"]
            aargs = args[i:]
            if rtype == "pos":
                if not indexExists(args, c[k]["pos"]):
                    error = f"Arg number {c[k]['pos']} is not in {args}"
                    raise self.ArgumentError(error)
                if not c[k]["in"] == [None]:
                    if not type(self.eval(args[i])) in c[k]["in"]:
                        error = f"Expected type {c[k]['in']}, got type {type(self.eval(args[i]))}"
                        raise self.ArgumentTypeError(error)
                
                o[str(i)] = self.eval(args[i])
                i += 1
            elif rtype == "tg":
                if f"-{k}" in args[i:]:
                    o[k] = not c[k]["base"]
                else:
                    o[k] = c[k]["base"]
                covered.append(f"-{k}")
            elif rtype == "ltg":
                if f"--{k}" in args[i:]:
                    o[k] = not c[k]["base"]
                else:
                    o[k] = c[k]["base"]
                covered.append(f"--{k}")
            elif rtype == "char": #c: in
                if f"-{k}" in aargs:
                    dex = aargs.index(f"-{k}")
                    find = self.eval(aargs[dex+1])
                    
                    if not None in ck["in"]:
                        
                        if not type(find) in ck["in"]:
                            error = f"Expected type {ck['in']}, got type {type(find)}"
                            raise self.ArgumentTypeError(error)
                    o[k] = find
                    covered.append(aargs[dex+1])
                
                else:
                    o[k] = None  
                covered.append(f"-{k}")
            elif rtype == "long": #c: in
                if f"--{k}" in aargs:
                    dex = aargs.index(f"--{k}")
                    find = self.eval(aargs[dex+1])
                    if not None in ck["in"]:
                        if not type(find) in ck["in"]:
                            error = f"Expected type {ck['in']}, got type {type(find)}"
                            raise self.ArgumentTypeError(error)
                    o[k] = find
                    covered.append(aargs[dex+1])
                
                else:
                    o[k] = None
                covered.append(f"--{k}")  
            elif rtype == "sticky": #c: in
                
                if self.sliceList(aargs, f"-{k}"):
       
                    dex = self.sliceList(aargs, f"-{k}", True)
                    find = self.eval(aargs[dex][2:])
                    if not None in ck["in"]:
                        if not type(find) in ck["in"]:
                            error = f"Expected type {ck['in']}, got type {type(find)}"
                            raise self.ArgumentTypeError(error)
                    o[k] = find                   
                    covered.append(aargs[dex])
                else:
                    o[k] = None
            elif rtype == "range": #c: in, quote, bquote
                if f"-{k}" in aargs:
                    dex = aargs.index(f"-{k}")
                    dex = dex+1
                    find = self.eval(findRange(ck["quote"],ck["bquote"],slice(dex,None)))
                    if not None in ck["in"]:
                        if not type(find) in ck["in"]:
                            error = f"Expected type {ck['in']}, got type {type(find)}"
                            raise self.ArgumentTypeError(error)
                    o[k] = find    
                    ffind = ck["quote"]+find+ck["bquote"]
                    for x in ffind.split(" "):
                        covered.append(x)
                    covered.append(f"-{k}")
                else:
                    o[k] = None
            elif rtype == "lrange": #^
                if f"--{k}" in aargs:
                    dex = aargs.index(f"--{k}")
                    dex = dex+1
                    find = self.eval(findRange(ck["quote"],ck["bquote"],slice(dex,None)))
                    if not None in ck["in"]:
                        if not type(find) in ck["in"]:
                            error = f"Expected type {ck['in']}, got type {type(find)}"
                            raise self.ArgumentTypeError(error)
                    o[k] = find 
                    ffind = ck["quote"]+find+ck["bquote"]
                    for x in ffind.split(" "):
                        covered.append(x)
                    covered.append(f"--{k}")
                else:
                    o[k] = None
            elif rtype == "srange": #^
                
                if self.sliceList(aargs, f"-{k}"):
                    
                    dex = self.sliceList(aargs, f"-{k}", True)
                    find = self.eval(findRange(ck["quote"],ck["bquote"],slice(dex,None),bump=slice(2,None)))
                    if not None in ck["in"]:
                        if not type(find) in ck["in"]:
                            error = f"Expected type {ck['in']}, got type {type(find)}"
                            raise self.ArgumentTypeError(error)
                    
                    o[k] = find 
                    ffind = f"-{k}"+ck["quote"]+find+ck["bquote"]
                    for x in ffind.split(" "):
                        covered.append(x)
                else:
                    o[k] = None
            elif rtype == "hard": #c: in
                if f"-*{k}" in aargs:
                    dex = aargs.index(f"-*{k}")
                    find = self.eval(aargs[dex+1])
                    
                    if not None in ck["in"]:
                        
                        if not type(find) in ck["in"]:
                            error = f"Expected type {ck['in']}, got type {type(find)}"
                            raise self.ArgumentTypeError(error)
                    o[k] = find
                    covered.append(f"-*{k}")
                    covered.append(aargs[dex+1])
                    
                else:
                    error=f"Missing Required Keyword Argument -{k}, Arg type is hard"
                    raise self.ArgumentError(error)

        return [o, [i, covered]]
            
    def command(self, funct):
        args = self.argv
        if len(args) >= 2:

            if args[1] == self.name[0]:
                args2 = args[2:]
                args2.insert(0, args[0])
                
                e = self.evalArgs(args2)

                self.parent._cArgs(args2, e[1])

                unct(e[0])
                sys.exit()
    def commandU(self, funct):
        args =self.argv
        
        if len(args) >= 2:

            if args[1] == self.name[0]:
                
                args2 = args[2:]
                args2.insert(0, args[0])
                e = self.evalArgs(args2)

                self.parent._cArgs(args2, e[1])

                funct(**e[0])
                sys.exit()
    def basicCfig(self, l):
        """
        Same as parent
        """
        self.cfig = self.parent.basicCfig(l, False)
class commanger:
    def __init__(self, globe=__name__):
        self.name = globe
        self.cfig = {}
        self.tup = None
        self.commandDepth = 0
    class ArgumentError(Exception):
        pass
    class ArgumentTypeError(ArgumentError):
        pass
    def basicCfig(self, l: list, bl=True):
        """
        Form a basic config and set commanger.cfig to the output unless bl = False.
        
        Returns: config dict
        
        Example:
        `cmd.basicCfig([1, 2, '3', 'four'])`
        Goes to:
        ```python
        {1: {'type': 'pos', 'in': [None], 'pos': 1, 'base': None}, 2: {'type': 'pos', 'in': [None], 'pos': 2, 'base': None}, '3': {'type': 'tg', 'base': False}, 'four': {'type': 'ltg', 'base': False}}
        ```
        """
        if type(l) != list:
            error = "Arg is not list"
            raise TypeError(error)
        ps = 1
        cfigg = {}
        
        l = sorted(l, key=lambda val: str(val))
        for x in l:
            
            if type(x) is int:
                cfigg[x] = {
                    "type": "pos",
                    "in": [None],
                    "pos": ps,
                    "base": None
                }
            elif type(x) is str and len(x) == 1:
                cfigg[x] = {
                    "type": "tg",
                    
                    "base": False
                }
            elif type(x) is str:
                cfigg[x] = {
                    "type": "ltg",
                    
                    "base": False
                }
            ps += 1
        if bl:
            self.cfig = cfigg
        return cfigg
    def __enter__(self):
        raise NotImplementedError(" ")
    def __exit__(self, exc_type, exc_val, exc_tb):
        raise NotImplementedError(" ")
    def ppconfig(self, config=None):
        """
        Get a pretty version of commanger.cfig or supplied config
        
        Returns: string
        """
        if config==None:
            n = self.cfig
        else:
            n = config
        out = "{\n"
        for x in n.keys():
            out = out + f"\n\t{cr.Fore.LIGHTGREEN_EX}" + str(x) + cr.Fore.WHITE+": {\n"
            for y in n[x].keys():
                out = out + f"\t\t{cr.Fore.LIGHTGREEN_EX}" + str(y) + f"{cr.Fore.WHITE}: {cr.Fore.LIGHTBLUE_EX}" + str(n[x][y]) +f"{cr.Fore.WHITE},\n"
            out = out + "\t}, \n"
        out = out+"\n}\n"
        return out
    def sliceList(self, list, i, val=False):
        index = 0
        for x in list:
            
            if i in x:
                if val:
                    return index
                return True
            index += 1
        return False
    def eval(self, val):
 
        a = NoneVar(val)
        return a
    def evalArgs(self, args):
        """
        Dev funct evalArgs:
        Evaluates args.
        """
        
        def findRange(f: str, b: str, rng: slice, *, bump=slice(0,None)):
                look = aargs[rng]
                

                
                if not f in look[0]:
                    error = "Range start not in start"
                    raise self.ArgumentError(error)
                if not self.sliceList(look, b):
                    error = "Range end does not exist"
                    raise self.ArgumentError(error)
                out = look[0][bump]
                out = out[out.rfind(f)+len(f):]
                for x in look[1:]:
                    if not b in x:
                        out = out+" "+x
                    else:
                        out = out+" "+x[:x.rfind(b)]
                        break
                return out
        def indexExists(list,index):
            if 0 <= index < len(list):
                return True
            else:
                return False
        o = {}
        i = 1
        c = self.cfig
        covered = []
        for k in c.keys():
            
            ck = c[k]
            rtype = ck["type"]
            aargs = args[i:]
            if rtype == "pos":
                if not indexExists(args, c[k]["pos"]):
                    error = f"Arg number {c[k]['pos']} is not in {args}"
                    raise self.ArgumentError(error)
                if not c[k]["in"] == [None]:
                    if not type(self.eval(args[i])) in c[k]["in"]:
                        error = f"Expected type {c[k]['in']}, got type {type(self.eval(args[i]))}"
                        raise self.ArgumentTypeError(error)
                
                o[str(i)] = self.eval(args[i])
                i += 1
            elif rtype == "tg":
                if f"-{k}" in args[i:]:
                    o[k] = not c[k]["base"]
                else:
                    o[k] = c[k]["base"]
                covered.append(f"-{k}")
            elif rtype == "ltg":
                if f"--{k}" in args[i:]:
                    o[k] = not c[k]["base"]
                else:
                    o[k] = c[k]["base"]
                covered.append(f"--{k}")
            elif rtype == "char": #c: in
                if f"-{k}" in aargs:
                    dex = aargs.index(f"-{k}")
                    find = self.eval(aargs[dex+1])
                    
                    if not None in ck["in"]:
                        
                        if not type(find) in ck["in"]:
                            error = f"Expected type {ck['in']}, got type {type(find)}"
                            raise self.ArgumentTypeError(error)
                    o[k] = find
                    covered.append(aargs[dex+1])
                
                else:
                    o[k] = None  
                covered.append(f"-{k}")
            elif rtype == "long": #c: in
                if f"--{k}" in aargs:
                    dex = aargs.index(f"--{k}")
                    find = self.eval(aargs[dex+1])
                    if not None in ck["in"]:
                        if not type(find) in ck["in"]:
                            error = f"Expected type {ck['in']}, got type {type(find)}"
                            raise self.ArgumentTypeError(error)
                    o[k] = find
                    covered.append(aargs[dex+1])
                
                else:
                    o[k] = None
                covered.append(f"--{k}")  
            elif rtype == "sticky": #c: in
                
                if self.sliceList(aargs, f"-{k}"):
       
                    dex = self.sliceList(aargs, f"-{k}", True)
                    find = self.eval(aargs[dex][2:])
                    if not None in ck["in"]:
                        if not type(find) in ck["in"]:
                            error = f"Expected type {ck['in']}, got type {type(find)}"
                            raise self.ArgumentTypeError(error)
                    o[k] = find                   
                    covered.append(aargs[dex])
                else:
                    o[k] = None
            elif rtype == "range": #c: in, quote, bquote
                if f"-{k}" in aargs:
                    dex = aargs.index(f"-{k}")
                    dex = dex+1
                    find = self.eval(findRange(ck["quote"],ck["bquote"],slice(dex,None)))
                    if not None in ck["in"]:
                        if not type(find) in ck["in"]:
                            error = f"Expected type {ck['in']}, got type {type(find)}"
                            raise self.ArgumentTypeError(error)
                    o[k] = find    
                    ffind = ck["quote"]+find+ck["bquote"]
                    for x in ffind.split(" "):
                        covered.append(x)
                    covered.append(f"-{k}")
                else:
                    o[k] = None
            elif rtype == "lrange": #^
                if f"--{k}" in aargs:
                    dex = aargs.index(f"--{k}")
                    dex = dex+1
                    find = self.eval(findRange(ck["quote"],ck["bquote"],slice(dex,None)))
                    if not None in ck["in"]:
                        if not type(find) in ck["in"]:
                            error = f"Expected type {ck['in']}, got type {type(find)}"
                            raise self.ArgumentTypeError(error)
                    o[k] = find 
                    ffind = ck["quote"]+find+ck["bquote"]
                    for x in ffind.split(" "):
                        covered.append(x)
                    covered.append(f"--{k}")
                else:
                    o[k] = None
            elif rtype == "srange": #^
                
                if self.sliceList(aargs, f"-{k}"):
                    
                    dex = self.sliceList(aargs, f"-{k}", True)
                    find = self.eval(findRange(ck["quote"],ck["bquote"],slice(dex,None),bump=slice(2,None)))
                    if not None in ck["in"]:
                        if not type(find) in ck["in"]:
                            error = f"Expected type {ck['in']}, got type {type(find)}"
                            raise self.ArgumentTypeError(error)
                    
                    o[k] = find 
                    ffind = f"-{k}"+ck["quote"]+find+ck["bquote"]
                    for x in ffind.split(" "):
                        covered.append(x)
                else:
                    o[k] = None
            elif rtype == "hard": #c: in
                if f"-*{k}" in aargs:
                    dex = aargs.index(f"-*{k}")
                    find = self.eval(aargs[dex+1])
                    
                    if not None in ck["in"]:
                        
                        if not type(find) in ck["in"]:
                            error = f"Expected type {ck['in']}, got type {type(find)}"
                            raise self.ArgumentTypeError(error)
                    o[k] = find
                    covered.append(f"-*{k}")
                    covered.append(aargs[dex+1])
                    
                else:
                    error=f"Missing Required Keyword Argument -{k}, Arg type is hard"
                    raise self.ArgumentError(error)

        return [o, [i, covered]]
    def  _cArgs(self, args, comp):
        i = 1
        print(comp[1])
        for x in args:
            if i > comp[0]:

                if not x in comp[1]:
                    error = f"Unexpected Argument: {x}"
                    raise self.ArgumentError(error)
            i+=1
    def command(self, funct):
        """
        Funct that runs on command. Key function. It is recommended to have only one of commanger.command and commanger.commandU
        
        Returns: None
        
        Expect: A dict as the single argument

        Example:
        ```python
        @commanger.command
        def main(args):
            #do stuff
        ```
        """
       
 #       for x in self.cfig.keys():
 #           if x["type"] == "pos":
 #               x["pos"] += self.depth
        
        
        e = self.evalArgs(sys.argv)

        self._cArgs(sys.argv, e[1])
        funct(e[0])
    def commandU(self, funct):
        """
        Funct that runs on command. Key function. It is recommended to have only one of commanger.command and commanger.commandU
        
        Returns: None
        
        Expect: **kwargs as arguments.

        Examples:
        ```python
        @commanger.commandU
        def main(**kwargs): #get as dict
            #do stuff
        ```
        ```python
        @commanger.commandU
        def main(*, hi, bye, hello): #get as individual args
            #do stuff
        ```        
        """
 
        e = self.evalArgs(sys.argv)

        self._cArgs(sys.argv, e[1])
        
        funct(**e[0])
    def tups(self, args, u=False):
        """
        Run a tup command.

        How to set a tup command:
        ```py
        cmd = commanger("cmd")
        def tup(**kwargs):
            #do something
        cmd.tup = tup
        ```
        Run:
        
        `cmd.tups("command like string", True)`
        """
        a= args.split(" ")
        
        e = self.evalArgs(a)
        
        
        if u:
            self.tup(**e[0])
        else:
            self.tup(e[0])
    def subCommand(self, name, depth=1):
        if depth > self.commandDepth:
            odepth = depth
        else:
            odepth = self.commandDepth
        self.commandDepth = odepth
        return subCommanger(self, name, depth)
        