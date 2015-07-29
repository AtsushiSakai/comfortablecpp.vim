#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys

def GenerateShowStructFunction(structstr, separater="\\n"):
    structname, memberlist=GenerateStructMetaData(structstr)
    #print structname
    #print memberlist

    showCode=[]
    showCode.append("void Show"+structname+"struct(const "+structname+" &obj){")
    showCode.append('\tprintf("__func__");')

    for member in memberlist:
        code='\tprintf("'
        code+=member[1]+":%"
        typename=member[0]
        code+=GetValueFormat(typename)
        code+=separater+'");'
        showCode.append(code)

    showCode.append('}')
    #print showCode
    return showCode

def GetValueFormat(typename):
    valueformat=""
    if typename.find("float")!=-1:
        valueformat="f"
    elif typename.find("double")!=-1:
        valueformat="lf"
    elif typename.find("char")!=-1 and typename.find("*")!=-1:
        valueformat="s"
    elif typename.find("char")!=-1:
        valueformat="c"
    elif typename.find("uint16")!=-1 and typename.find("uint8")!=-1:
        valueformat="u"
    elif typename.find("unsigned")!=-1 and typename.find("int")!=-1:
        valueformat="u"
    elif typename.find("unsigned")!=-1 and typename.find("short")!=-1:
        valueformat="u"
    elif typename.find("short")!=-1 or typename.find("int")!=-1:
        valueformat="d"
    elif typename.find("int16")!=-1 and typename.find("int8")!=-1:
        valueformat="d"
    elif typename.find("unsigned")!=-1 and typename.find("long")!=-1:
        valueformat="lu"
    elif typename.find("uint32")!=-1:
        valueformat="lu"
    elif typename.find("long")!=-1 or typename.find("int32")!=-1:
        valueformat="ld"
    else:
        valueformat="UNKNOWN"

    return valueformat

def GenerateStructMetaData(structstr):
    # search space
    headerind=structstr.find(" ");
    header=structstr[0:headerind];
    #print header

    # header shoud be "struct"
    if header!="struct":
        print "Unknown header:"+header
        return ""

    body=structstr[headerind+1:];
    #print body

    #get struct name
    structnameind=body.find("{");
    structname=body[0:structnameind]
    structname=structname.strip()

    #get content
    contentind=body.rfind("}");
    content=body[structnameind+1:contentind]
    #print structname
    #print content

    #get struct menber
    members=content.split(";")
    while members.count("") > 0:
        members.remove("")
    while members.count("\n") > 0:
        members.remove("\n")

    #print members
    
    #Get memberlist
    memberlist=[];
    for member in members:
        valueid=member.rfind(" ")
        typename=member[0:valueid]
        value=member[valueid+1:]
        memberlist.append((typename,value))

    #print memberlist
    return (structname,memberlist)


if __name__ == '__main__':
    #============Main Function============
    #print __file__+" start!!"
    #structstr="struct Sample{int a;unsigned int b;float c;double d;char e;char* fg;short comcom};"
    structstr=sys.argv
    #print structstr

    #GenerateShowStructFunction(structstr,',')
    result=GenerateShowStructFunction(structstr)
    #print result

    #Yank Code
    import vim
    code=""
    for line in result:
        code+=line+"\n"

    vim.command(":let @*='"+code+"'")
    print "Yank ShowStructFunction!"


