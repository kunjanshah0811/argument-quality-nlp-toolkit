import math
import os
import random
import xml.etree.ElementTree as ET
import json


def listDirectory():
    Basepath = '.data/dagstuhl-15512-argquality-corpus-annotated-xmi'
    Issue_List = os.listdir(Basepath)

    if (".DS_Store" in Issue_List):
        Issue_List.remove(".DS_Store")
    
    IssuesDict = {}

    for Issue in Issue_List:
        stance_List = os.listdir(Basepath + '/' + Issue)
        temp_Aray = []
        for stance in stance_List:
            arg_List = os.listdir(Basepath + '/' + Issue + '/' + stance)
            temp_DictObj = {}
            temp_DictObj[stance] = arg_List
            temp_Aray.append(temp_DictObj)

        IssuesDict[Issue] = temp_Aray

    return IssuesDict


def readXmi(Filepath):

    filePath = Filepath
    tree = ET.parse(filePath)
    root = tree.getroot()
    ArgumentDict = {}
    for child in root:
        if('ArgumentationQuality' in child.tag):
            ArgumentDict['argument_quality_score'] = child.attrib['allScores']   
        elif('Appropriateness' in child.tag):
            list1 = child.attrib['allScores'].split()
            for i in range(len(list1)):
                if  float(list1[i])>1.0 and float(list1[i])<3.0:
                    list1[i]="n"
                else:
                    list1[i]="y"
            ArgumentDict['argumentative']=list1
        elif('Effectiveness' in child.tag):
             ArgumentDict['effectiveness_scores'] = child.attrib['allScores']
        elif('Sofa' in child.tag):
            ArgumentDict['text'] = child.attrib['sofaString']

       
    return ArgumentDict
           
    
def createJsonG ():
     Basepath = '.data/dagstuhl-15512-argquality-corpus-annotated-xmi'
     DirectoryList = listDirectory()
     ListOfObjects = []
     SingleDictionary = {}
     for Issue in DirectoryList:
    
         for stance in DirectoryList[Issue]:
    
             ArgList= []
             stance_on_topic = ''
             for key in stance:
                 stance_on_topic = key
                 ArgList = stance[key]
             for arg in ArgList:
    
                 path = Basepath + '/' + Issue + '/' + stance_on_topic + '/' + arg
                 SingleDictionary['id'] = arg.replace('.xmi', '')
                 SingleDictionary['issue'] = Issue
                 SingleDictionary['stance_on_topic'] = stance_on_topic
                 argDictionary = readXmi(path)   
                 SingleDictionary = SingleDictionary | argDictionary
                 ListOfObjects.append(SingleDictionary)
                 SingleDictionary = {}
     
    
     return ListOfObjects


def SplitData ():
    ListtoSplit = createJsonG()
    TrainList = []
    TestList = []
    ValList = []

    RandomList= []

    Range= len(ListtoSplit)
    
    RangeForTrainData =  round(Range*0.70)
    RangeForTestData = round(Range*0.20)
    RangeForValData = round(Range*0.10)
    print("Total::",Range)
    while len(TrainList) < RangeForTrainData:
        index = random.randint(0, Range-1)
        if(index in RandomList):
            continue
        else:
            RandomList.append(index)
            TrainList.append(ListtoSplit[index])

    while len(TestList) < RangeForTestData:
        index=random.randint(0,Range-1)
        if(index in RandomList):
            continue
        else:
            RandomList.append(index)
            TestList.append(ListtoSplit[index])
        
    while len(ValList) < RangeForValData:
        index = random.randint(0, Range-1)
        if(index in RandomList):
            continue
        else:
            RandomList.append(index)
            ValList.append(ListtoSplit[index])

    jsonData = json.dumps(TrainList)
    with open('train.json', 'w') as f:
        json.dump(jsonData, f)

    jsonData = json.dumps(TestList)
    with open('test.json', 'w') as f:
        json.dump(jsonData, f)

    jsonData = json.dumps(ValList)
    with open('val.json', 'w') as f:
        json.dump(jsonData, f)
    print('Success..!!')


def main():
    SplitData()
    print("it works!")
    pass


if __name__ == '__main__':
    main()