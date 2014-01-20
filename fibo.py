# -*- coding: utf-8 -*- 
import sys
import codecs
"""
Check
"""
STDCode =   [
                "0":"检测通过",
                "1":"多余的左备注符号",
                "2":"未检测到『？』",
                "3":"检测到多于一个『？』",
                "4":"在补充标识符后未检测到补充事件结束标识符『！』",
                "5":"补充标识符后没有对应的时间。时间标准格式：12.35",
                "6":"补充事项后没有正文内容"
            ]
def     Comma_Exclamatory_Match(Content):
    
def     Interrogation_Check(Content):

def     Content_devide(Content):
    if  Content[0] ==  "," :
        return  
        









"""
"""
def     Print_Log(Line) :
    L   =   Line.split(sep=",")
    if (len(L))>6 :  
        if L[1]=='submit':
            if  L[7][0]=="。":
                return print(L[5][:10],L[5][11:],L[7][1:],sep="\t")
        else    :
            return "None" 



FilePath    =   "C:/Users/Administrator/Desktop/豌豆荚导出的短信2013年12月7日.csv"
print(FilePath)
#f = open(FilePath,"r+")
f = open(FilePath,mode="r",encoding="utf-8")
data = f.readline()

if data[:1] == codecs.BOM_UTF8[:1] :
    print("hello")
else    :
    print(data[1:])
for line in range(10):
    line    =   f.readline()
    Print_Log(line)


