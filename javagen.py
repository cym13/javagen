#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Usage: javagen [-h] [-g] [-s] [-t] [-c classname] (TYPE ATT)...

Arguments:
    TYPE    Attribute type
    ATT     Attribute name

Options:
    -g, --getters           Generate getters
    -s, --setters           Generate setters
    -t, --tostring          Generate toString method
    -c, --class classname   Name of the class
"""

from docopt import docopt


def gen_class(classname):
    return "public class %s {" % classname

def constructor(classname, att_list):
    text = "    public %s(" % classname

    for att, att_type in att_list[:-1]:
        text += att_type + " " + att + ", "
    text += att_list[-1][1] + " " + att_list[-1][0]

    text += ") {\n"
    for each in [x[0] for x in att_list]:
        text += "        this.%s = %s;\n" % (each, each)
    text += "    }\n"
    return text

def definition(att, att_type):
    return "    private %s %s;" % (att_type, att)


def getter(att, att_type):
    text = "    public %s get%s() {\n" % (att_type, att[0].upper() + att[1:])
    text+= "        return %s;\n" % att
    text+= "    }\n"
    return text


def setter(att, att_type):
    text = "    public void set%s(%s %s) {\n" % (att[0].upper()+att[1:],
                                                    att_type, att)
    text+= "        this.%s = %s;\n" % (att, att)
    text+= "    }\n"
    return text


def tostring(classname, attributes):
    text      = '    public String toString() {\n'
    text     += '        return "%s("\n' % classname

    for att in attributes[:-1]:
        text += '             + "%s=" + this.%s + ", "\n' % (att, att)

    text     += '             + "%s=" + this.%s + ")";\n' % (attributes[-1],
                                                             attributes[-1])
    text     += "    }\n"
    return text


def main():
    args = docopt(__doc__)

    if args["--class"]:
        print(gen_class(args["--class"]))

    for att, att_type in zip(args["ATT"], args["TYPE"]):
        print(definition(att, att_type))

    print()

    if args["--class"]:
        print(constructor(args["--class"], list(zip(args["ATT"],args["TYPE"]))))

    for att, att_type in zip(args["ATT"], args["TYPE"]):
        if args["--getters"]:
            print(getter(att, att_type))
        if args["--setters"]:
            print(setter(att, att_type))

    if args["--tostring"]:
        print(tostring(args["--class"], args["ATT"]))

    if args["--class"]:
        print("}")

if __name__ == "__main__":
    main()
