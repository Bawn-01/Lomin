#!/usr/bin/env python3

# imports

# lomin

# ting

# init



maxmem = 1000
mem = [0] * maxmem
memcount = 0

def __init__():
    with open("VARSTOR.Vln", "w") as f:
        f.write("")
        f.close()

__init__()

# /init

# idk

def writeVar(inp, type):
    global mem
    global memcount
    with open("VARSTOR.Vln", "a") as f:
        if type == "nil":
            if "\"" in inp:
                f.write("string " + inp + "\n")
            else:
                f.write("integer " + inp + "\n")
        else:
            f.write("inp " + inp + "\n")
    f.close()

lienupA = ""
lineupB = ""

def readVar(name, printable=True):
    global lienupA
    global lineupB
    global mem
    global memcount
    with open("VARSTOR.Vln", "r") as f:
        for line in f.readlines():
            if name in line:
                fn = line.rstrip()
                fin = fn.replace(name, "")
                finn = fin.replace(" = ", "")
                if "\"" in finn:
                    fnn = finn.replace("\"", "")
                    fnnn = fnn.replace("string ", "")
                    if not printable:
                        if lienupA != "":
                            if lineupB != "":
                                exit("ERROR: lib unable to find open lineup")
                            else: lineupB = fnnn
                        else: lienupA = fnnn
                        continue
                    else:
                        print(fnnn)
                elif "inp" in finn:
                    fnn = finn.replace("inp ", "")
                    fni = fnn.replace(" ", "")
                    if not printable:
                        if lienupA != "":
                            if lineupB != "":
                                exit("ERROR: lib unable to find open lineup")
                            else: lineupB = fni
                        else: lienupA = fni
                        continue
                    else:
                        print(fni)
                else:
                    fnn = finn.replace("integer ", "")
                    if not printable:
                        if lienupA != "":
                            if lineupB != "":
                                exit("ERROR: lib unable to find open lineup")
                            else: lineupB = fnn
                        else: lienupA = fnn 
                        continue
                    else:
                        print(fnn)
            f.close()

lienupA = ""
lineupB = ""

def ifState(FILE):
    with open(FILE, "r") as f:
        for line in f.readlines():
            if "end" in line: break
            if "var" in line:
                fin = line.rstrip()
                finn = fin.replace("var ", "")
                mem[memcount] = finn
                if "input" in finn:
                    inp = input()
                    fian = fin.replace("var ", "")
                    fni = fian.replace("input", "")
                    fn = fni + " " + inp
                    writeVar(fn, "wda")
                    continue
                else:
                    writeVar(finn, "nil")
            if "println" in line:
                fin = line.rstrip()
                finn = fin.replace("println", "")
                fnn = finn.replace("(", "")
                fni = fnn.replace(")", "")
                if "\"" not in fni:
                    readVar(fni)
                else:
                    fn = fni.replace("\"", "")
                    println(fn)
            if "input" in line:
                input()
        f.close()

# /idk


def println(text):
    print(text)


def ifstate():
    pass

ifstatem = False

def compile(FILE):
    global ifstatem
    global maxmem
    global mem
    global memcount
    global lienupA
    global lineupB
    with open(FILE, "r") as f:
        for line in f.readlines():
            if not ifstatem:
                if "var" in line:
                    fin = line.rstrip()
                    finn = fin.replace("var ", "")
                    mem[memcount] = finn
                    if "input" in finn:
                        inp = input()
                        fian = fin.replace("var ", "")
                        fni = fian.replace("input", "")
                        fn = fni + " " + inp
                        writeVar(fn, "wda")
                        continue
                    else:
                        writeVar(finn, "nil")
                if "println" in line:
                    fin = line.rstrip()
                    finn = fin.replace("println", "")
                    fnn = finn.replace("(", "")
                    fni = fnn.replace(")", "")
                    if "\"" not in fni:
                        readVar(fni)
                    else:
                        fn = fni.replace("\"", "")
                        println(fn)
                if "input" in line:
                    input()
                if "if" in line:
                    po = line.rstrip()
                    pt = po.replace("if ", "")
                    if "==" in pt:
                        lineupB = ""
                        lienupA = ""
                        fin, _, fni = pt.partition('==')
                        proA = fin.replace(" ", "")
                        proB = fni.replace(" ", "")
                        readVar(proA, False)
                        readVar(proB, False)
                        ifstatem = True
            else:
                if lienupA == lineupB:
                    if "end" in line: ifstatem = False
                    if "var" in line:
                        fin = line.rstrip()
                        finn = fin.replace("var ", "")
                        mem[memcount] = finn
                        if "input" in finn:
                            inp = input()
                            fian = fin.replace("var ", "")
                            fni = fian.replace("input", "")
                            fn = fni + " " + inp
                            writeVar(fn, "wda")
                            continue
                        else:
                            writeVar(finn, "nil")
                    if "println" in line:
                        fin = line.rstrip()
                        finn = fin.replace("println", "")
                        fnn = finn.replace("(", "")
                        fni = fnn.replace(")", "")
                        if "\"" not in fni:
                            readVar(fni)
                        else:
                            fn = fni.replace("\"", "")
                            println(fn)
                    if "input" in line:
                        input()
        f.close()

compile("test.ln")
