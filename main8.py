from AirportClass import airport
from HarborClass import harbor
from TrainstationClass import trainstasion
from TruckClass import truck
from WarehouseClass import warehouse
from ItemClass import item
from OrderClass import order
import math
import sys

###SetupList
AirportDict={}
HarborDict={}
TrainstationDict={}
TruckDict={}
WarehouseDict={}
ItemDict={}
GraphOfPath={}
#...
TransactionList=[]
OrderDict={}
SortLog=[]
Nation = ["USA", "UK", "Italy", "Wakanda", "Germany", "USSR", "Brazil", "Argentina", "Ireland", "India",
              "Indonesia", "Hong Kong", "Philipine", "Singapore", "Sri Lanka", "Egypt", "Congo", "Madagascer",
              "Vietnam", "China", "Laos", "Hungary", "Austria", "Myanmar", "Bulgaria", "Poland", "Latvia"]

def num(s):
    s = str(s)
    try:
        return int(s)
    except ValueError:
        if float(s)-math.ceil(float(s))==0:
            return int(float(s))
        else:
            return round(float(s),2)

def ReadInputFile(filename):
    try:
        file = open(filename, encoding="utf8")
        inputfile = file.readlines()
        #print('utf8')
    except:
        file = open(filename, encoding="utf16")
        inputfile = file.readlines()
        #print('utf16')
    #print(inputfile)
    n=0
    length=len(inputfile)
    while n<length:
    #for i in inputfile:
        if inputfile[n]=='\n':
            inputfile.remove(inputfile[n])
            length=length-1
            continue
        n+=1
    #print(inputfile)
    inputlist = []
    inputlistline = []
    ListOfTextbuffer = []
    ListOfTextbufferLower=[]
    for i in inputfile:
        i=i.strip('\n')
        i = i.strip('\t')
        i = i.strip(' :')
        inputlistsplit = []
        inputlistline.append(i)
        i=i.replace(',',' ')
        i=i.replace('  ',' ')
        i = i.replace('“ ', '"')
        i = i.replace(' ”', '"')
        i=i.replace('“','"')
        i=i.replace('”', '"')
        #print(i)
        inputlistsplit = i.split(' ')
        buffer = []
        textbuffer = ''
        j = 0
        ch = False
        Specialbuffer = []

        for j in range(len(inputlistsplit)):
            inputlistsplit[j] = inputlistsplit[j].strip('(')
            inputlistsplit[j] = inputlistsplit[j].strip(')')
            inputlistsplit[j] = inputlistsplit[j].strip(':')
            inputlistsplit[j] = inputlistsplit[j].replace(' ', '')
            if ch == False:
                if inputlistsplit[j][0] == '"':
                    textbuffer = textbuffer + inputlistsplit[j]
                    ch = True
                else:
                    buffer.append(inputlistsplit[j])
                if inputlistsplit[j][-1] == '"':
                    textbuffer=textbuffer.strip('"')
                    textbuffer = textbuffer.strip('"')
                    buffer.append(textbuffer)
                    ListOfTextbuffer.append(textbuffer)
                    ch = False
            else:
                if inputlistsplit[j][-1] == '"':
                    textbuffer = textbuffer + ' ' + inputlistsplit[j]
                    textbuffer = textbuffer.strip('"')
                    textbuffer = textbuffer.strip('"')
                    buffer.append(textbuffer)
                    ListOfTextbuffer.append(textbuffer)
                    ch = False
                else:
                    textbuffer = textbuffer + ' ' + inputlistsplit[j]
        #print(buffer)
        for j in ListOfTextbuffer:
            ListOfTextbufferLower.append(j.lower())
        if buffer[0] == "Set_path":
            Namebuffer = ""
            Checkname = False
            Specialbuffer.append(buffer[0])
            fristplacebufferlist = []
            countCheckname=0
            while countCheckname<len(buffer)-3:
                fristplace = ''
                seconplace = ''
                checkfristplace = False
                #print(countCheckname)
                for j in range(1,len(buffer)-1):
                    if checkfristplace==False:
                        fristplace = fristplace +buffer[j].lower()+ " "
                    else:
                        seconplace = seconplace +buffer[j].lower()+ " "
                    if fristplace.lower().strip(" ") in ListOfTextbufferLower and fristplace.lower().strip(' ') not in fristplacebufferlist:
                        checkfristplace = True
                #print(fristplace.strip(" "))
                #print(seconplace.strip(" "))
                if fristplace.lower().strip(" ") in ListOfTextbufferLower and seconplace.lower().strip(" ") in ListOfTextbufferLower:
                    for j in ListOfTextbuffer:
                        if fristplace.lower().strip(' ')==j.lower():
                            fristplace=j
                        if seconplace.lower().strip(' ')==j.lower():
                            seconplace=j
                    Specialbuffer.append(fristplace)
                    Specialbuffer.append(seconplace)
                    break
                else:
                    fristplacebufferlist.append(fristplace.strip(' '))
                    countCheckname+=1
                #print(fristplacebufferlist)
            Specialbuffer.append(buffer[-1])
            inputlistsplit = Specialbuffer
        elif buffer[0] == "Import" or buffer[0] == "Export" or buffer[0] == "Transfer":
            Namebuffer = ""
            Specialbuffer.append(buffer[0])
            Specialbuffer.append(buffer[1])
            for j in range(2,len(buffer)):
                if buffer[j] == "from":
                    for k in Nation:
                        if Namebuffer.lower().strip(" ") == k.lower():
                            Namebuffer = k
                    for k in ListOfTextbuffer:
                        if Namebuffer.lower().strip(" ") == k.lower():
                            Namebuffer = k
                    Specialbuffer.append(Namebuffer.strip(" "))
                    Specialbuffer.append(buffer[j])
                    Namebuffer = ""
                #elif buffer[j] in ListOfTextbufferLower or buffer[j] in Nation:
                #    Namebuffer = Namebuffer + buffer[j] + " "
                    #Specialbuffer.append(buffer[j])
                elif buffer[j] == "to":
                    for k in Nation:
                        if Namebuffer.lower().strip(" ") == k.lower():
                            Namebuffer = k
                    for k in ListOfTextbuffer:
                        if Namebuffer.lower().strip(" ") == k.lower():
                            Namebuffer = k
                    Specialbuffer.append(Namebuffer.strip(" "))
                    Specialbuffer.append(buffer[j])
                    Namebuffer = ""
                else:
                    Namebuffer=Namebuffer+buffer[j]+" "
                #if Namebuffer.strip(" ") in ListOfTextbuffer or Namebuffer.strip(" ") in Nation:
                #    Specialbuffer.append(Namebuffer.strip(" "))
                #    Namebuffer=""
            for k in Nation:
                if Namebuffer.lower().strip(" ") == k.lower():
                    Namebuffer = k
            for k in ListOfTextbuffer:
                if Namebuffer.lower().strip(" ") == k.lower():
                    Namebuffer = k
            Specialbuffer.append(Namebuffer.strip(" "))
            inputlistsplit = Specialbuffer
        else:
            inputlistsplit = buffer
        inputlist.append(inputlistsplit)

    file.close()
    return inputlist

def CreateObject(filelist):
    AirportCount=0
    HarborCount=0
    TrainstationCount=0
    AirportNameList=[]
    HarborNameList=[]
    TrainstationNameList=[]
    WarehouseNameList=[]
    for i in filelist:
        ###Set up Environment
        if i[0]=="Create":
            if i[1]=="Airport":
                AirportDict[i[2]]=airport(name=i[2],Count=AirportCount)
                AirportNameList.append(i[2])
                SortLog.append(i[2])
                AirportCount+=1
            elif i[1]=="Harbor":
                HarborDict[i[2]]=harbor(name=i[2],Count=HarborCount)
                HarborNameList.append(i[2])
                SortLog.append(i[2])
                HarborCount+=1
            elif i[1]=="Train_Station":
                TrainstationDict[i[2]]=trainstasion(name=i[2],Count=TrainstationCount)
                TrainstationNameList.append(i[2])
                SortLog.append(i[2])
                TrainstationCount+=1
            elif i[1]=="Truck":
                TruckDict[i[2]]=truck(name=i[2],minload=num(i[3]),maxload=num(i[4]))
            elif i[1]=="Warehouse":
                WarehouseDict[i[2]]=warehouse(name=i[2],temp=num(i[3]),capacity=num(i[4]))
                WarehouseNameList.append(i[2])
        elif i[0]=="Set_path":
            if i[1] in AirportNameList:
                if i[2] in AirportNameList:
                    AirportDict[i[1]].pathlist.append([AirportDict[i[2]],num(i[3])])
                    AirportDict[i[2]].pathlist.append([AirportDict[i[1]],num(i[3])])
                    if i[1] not in list(GraphOfPath.keys()):
                        GraphOfPath[i[1]]=set([i[2]])
                    else:
                        GraphOfPath[i[1]] = GraphOfPath[i[1]]|set([i[2]])
                    if i[2] not in list(GraphOfPath.keys()):
                        GraphOfPath[i[2]]=set([i[1]])
                    else:
                        GraphOfPath[i[2]] = GraphOfPath[i[2]]|set([i[1]])
                elif i[2] in HarborNameList:
                    AirportDict[i[1]].pathlist.append([HarborDict[i[2]],num(i[3])])
                    HarborDict[i[2]].pathlist.append([AirportDict[i[1]],num(i[3])])
                    if i[1] not in list(GraphOfPath.keys()):
                        GraphOfPath[i[1]]=set([i[2]])
                    else:
                        GraphOfPath[i[1]] = GraphOfPath[i[1]]|set([i[2]])
                    if i[2] not in list(GraphOfPath.keys()):
                        GraphOfPath[i[2]]=set([i[1]])
                    else:
                        GraphOfPath[i[2]] = GraphOfPath[i[2]]|set([i[1]])
                elif i[2] in TrainstationNameList:
                    AirportDict[i[1]].pathlist.append([TrainstationDict[i[2]],num(i[3])])
                    TrainstationDict[i[2]].pathlist.append([AirportDict[i[1]],num(i[3])])
                    if i[1] not in list(GraphOfPath.keys()):
                        GraphOfPath[i[1]]=set([i[2]])
                    else:
                        GraphOfPath[i[1]] = GraphOfPath[i[1]]|set([i[2]])
                    if i[2] not in list(GraphOfPath.keys()):
                        GraphOfPath[i[2]]=set([i[1]])
                    else:
                        GraphOfPath[i[2]] = GraphOfPath[i[2]]|set([i[1]])
                else:
                    AirportDict[i[1]].pathlist.append([WarehouseDict[i[2]], num(i[3])])
                    WarehouseDict[i[2]].pathlist.append([AirportDict[i[1]], num(i[3])])
                    if i[1] not in list(GraphOfPath.keys()):
                        GraphOfPath[i[1]]=set([i[2]])
                    else:
                        GraphOfPath[i[1]] = GraphOfPath[i[1]]|set([i[2]])
                    if i[2] not in list(GraphOfPath.keys()):
                        GraphOfPath[i[2]]=set([i[1]])
                    else:
                        GraphOfPath[i[2]] = GraphOfPath[i[2]]|set([i[1]])
            elif i[1] in HarborNameList:
                if i[2] in AirportNameList:
                    HarborDict[i[1]].pathlist.append([AirportDict[i[2]],num(i[3])])
                    AirportDict[i[2]].pathlist.append([HarborDict[i[1]],num(i[3])])
                    if i[1] not in list(GraphOfPath.keys()):
                        GraphOfPath[i[1]]=set([i[2]])
                    else:
                        GraphOfPath[i[1]] = GraphOfPath[i[1]]|set([i[2]])
                    if i[2] not in list(GraphOfPath.keys()):
                        GraphOfPath[i[2]]=set([i[1]])
                    else:
                        GraphOfPath[i[2]] = GraphOfPath[i[2]]|set([i[1]])
                elif i[2] in HarborNameList:
                    HarborDict[i[1]].pathlist.append([HarborDict[i[2]],i[3]])
                    HarborDict[i[2]].pathlist.append([HarborDict[i[1]],i[3]])
                    if i[1] not in list(GraphOfPath.keys()):
                        GraphOfPath[i[1]]=set([i[2]])
                    else:
                        GraphOfPath[i[1]] = GraphOfPath[i[1]]|set([i[2]])
                    if i[2] not in list(GraphOfPath.keys()):
                        GraphOfPath[i[2]]=set([i[1]])
                    else:
                        GraphOfPath[i[2]] = GraphOfPath[i[2]]|set([i[1]])
                elif i[2] in TrainstationNameList:
                    HarborDict[i[1]].pathlist.append([TrainstationDict[i[2]],num(i[3])])
                    TrainstationDict[i[2]].pathlist.append([HarborDict[i[1]],num(i[3])])
                    if i[1] not in list(GraphOfPath.keys()):
                        GraphOfPath[i[1]]=set([i[2]])
                    else:
                        GraphOfPath[i[1]] = GraphOfPath[i[1]]|set([i[2]])
                    if i[2] not in list(GraphOfPath.keys()):
                        GraphOfPath[i[2]]=set([i[1]])
                    else:
                        GraphOfPath[i[2]] = GraphOfPath[i[2]]|set([i[1]])
                else:
                    HarborDict[i[1]].pathlist.append([WarehouseDict[i[2]], num(i[3])])
                    WarehouseDict[i[2]].pathlist.append([HarborDict[i[1]], num(i[3])])
                    if i[1] not in list(GraphOfPath.keys()):
                        GraphOfPath[i[1]]=set([i[2]])
                    else:
                        GraphOfPath[i[1]] = GraphOfPath[i[1]]|set([i[2]])
                    if i[2] not in list(GraphOfPath.keys()):
                        GraphOfPath[i[2]]=set([i[1]])
                    else:
                        GraphOfPath[i[2]] = GraphOfPath[i[2]]|set([i[1]])
            elif i[1] in TrainstationNameList:
                if i[2] in AirportNameList:
                    TrainstationDict[i[1]].pathlist.append([AirportDict[i[2]],num(i[3])])
                    AirportDict[i[2]].pathlist.append([TrainstationDict[i[1]],num(i[3])])
                    if i[1] not in list(GraphOfPath.keys()):
                        GraphOfPath[i[1]]=set([i[2]])
                    else:
                        GraphOfPath[i[1]] = GraphOfPath[i[1]]|set([i[2]])
                    if i[2] not in list(GraphOfPath.keys()):
                        GraphOfPath[i[2]]=set([i[1]])
                    else:
                        GraphOfPath[i[2]] = GraphOfPath[i[2]]|set([i[1]])
                elif i[2] in HarborNameList:
                    TrainstationDict[i[1]].pathlist.append([HarborDict[i[2]],num(i[3])])
                    HarborDict[i[2]].pathlist.append([TrainstationDict[i[1]],num(i[3])])
                    if i[1] not in list(GraphOfPath.keys()):
                        GraphOfPath[i[1]]=set([i[2]])
                    else:
                        GraphOfPath[i[1]] = GraphOfPath[i[1]]|set([i[2]])
                    if i[2] not in list(GraphOfPath.keys()):
                        GraphOfPath[i[2]]=set([i[1]])
                    else:
                        GraphOfPath[i[2]] = GraphOfPath[i[2]]|set([i[1]])
                elif i[2] in TrainstationNameList:
                    TrainstationDict[i[1]].pathlist.append([TrainstationDict[i[2]],num(i[3])])
                    TrainstationDict[i[2]].pathlist.append([TrainstationDict[i[1]],num(i[3])])
                    if i[1] not in list(GraphOfPath.keys()):
                        GraphOfPath[i[1]]=set([i[2]])
                    else:
                        GraphOfPath[i[1]] = GraphOfPath[i[1]]|set([i[2]])
                    if i[2] not in list(GraphOfPath.keys()):
                        GraphOfPath[i[2]]=set([i[1]])
                    else:
                        GraphOfPath[i[2]] = GraphOfPath[i[2]]|set([i[1]])
                else:
                    TrainstationDict[i[1]].pathlist.append([WarehouseDict[i[2]], num(i[3])])
                    WarehouseDict[i[2]].pathlist.append([TrainstationDict[i[1]], num(i[3])])
                    if i[1] not in list(GraphOfPath.keys()):
                        GraphOfPath[i[1]]=set([i[2]])
                    else:
                        GraphOfPath[i[1]] = GraphOfPath[i[1]]|set([i[2]])
                    if i[2] not in list(GraphOfPath.keys()):
                        GraphOfPath[i[2]]=set([i[1]])
                    else:
                        GraphOfPath[i[2]] = GraphOfPath[i[2]]|set([i[1]])
            elif i[1] in WarehouseNameList:
                if i[2] in AirportNameList:
                    WarehouseDict[i[1]].pathlist.append([AirportDict[i[2]],num(i[3])])
                    AirportDict[i[2]].pathlist.append([WarehouseDict[i[1]],num(i[3])])
                    if i[1] not in list(GraphOfPath.keys()):
                        GraphOfPath[i[1]]=set([i[2]])
                    else:
                        GraphOfPath[i[1]] = GraphOfPath[i[1]]|set([i[2]])
                    if i[2] not in list(GraphOfPath.keys()):
                        GraphOfPath[i[2]]=set([i[1]])
                    else:
                        GraphOfPath[i[2]] = GraphOfPath[i[2]]|set([i[1]])
                elif i[2] in HarborNameList:
                    WarehouseDict[i[1]].pathlist.append([HarborDict[i[2]],num(i[3])])
                    HarborDict[i[2]].pathlist.append([WarehouseDict[i[1]],num(i[3])])
                    if i[1] not in list(GraphOfPath.keys()):
                        GraphOfPath[i[1]]=set([i[2]])
                    else:
                        GraphOfPath[i[1]] = GraphOfPath[i[1]]|set([i[2]])
                    if i[2] not in list(GraphOfPath.keys()):
                        GraphOfPath[i[2]]=set([i[1]])
                    else:
                        GraphOfPath[i[2]] = GraphOfPath[i[2]]|set([i[1]])
                elif i[2] in TrainstationNameList:
                    WarehouseDict[i[1]].pathlist.append([TrainstationDict[i[2]],num(i[3])])
                    TrainstationDict[i[2]].pathlist.append([WarehouseDict[i[1]],num(i[3])])
                    if i[1] not in list(GraphOfPath.keys()):
                        GraphOfPath[i[1]]=set([i[2]])
                    else:
                        GraphOfPath[i[1]] = GraphOfPath[i[1]]|set([i[2]])
                    if i[2] not in list(GraphOfPath.keys()):
                        GraphOfPath[i[2]]=set([i[1]])
                    else:
                        GraphOfPath[i[2]] = GraphOfPath[i[2]]|set([i[1]])
                else:
                    WarehouseDict[i[1]].pathlist.append([WarehouseDict[i[2]],num(i[3])])
                    WarehouseDict[i[2]].pathlist.append([WarehouseDict[i[1]],num(i[3])])
                    if i[1] not in list(GraphOfPath.keys()):
                        GraphOfPath[i[1]]=set([i[2]])
                    else:
                        GraphOfPath[i[1]] = GraphOfPath[i[1]]|set([i[2]])
                    if i[2] not in list(GraphOfPath.keys()):
                        GraphOfPath[i[2]]=set([i[1]])
                    else:
                        GraphOfPath[i[2]] = GraphOfPath[i[2]]|set([i[1]])
        elif i[0]=="Create_item":
            ItemDict[i[1]]=item(name=i[1],mintemp=num(i[2]),maxtemp=num(i[3]),weight=num(i[4]))
        else:
            TransactionList.append(i)

def EventObject(TransactionList):
    OrderNow = ""
    countEvent = 0
    for i in TransactionList:
        if i[0] == "Order":
            OrderDict[i[1]]=order(name=i[1])
            OrderNow=i[1]
            countEvent = 0
        else:
            OrderDict[OrderNow].listevent.append([])
            for j in i:
                if j == 'from' or j == 'to':
                    pass
                else:
                    OrderDict[OrderNow].listevent[countEvent].append(j)
            countEvent += 1

def dfs_path(graph, start, goal):
    stack = [(start, [start])]
    listofpath=[]
    while stack:
        (vertex, path) = stack.pop()
        for next in graph[vertex] - set(path):
            if next == goal:
                listofpath.append(path + [next])
                #yield path + [next]
            else:
                stack.append((next, path + [next]))
    return listofpath

def distanceOfEvent(listofpath):
    distance=0
    for i in range(len(listofpath)-1):
        if listofpath[i] in list(AirportDict.keys()):
            for j in AirportDict[listofpath[i]].pathlist:
                if j[0].name == listofpath[i+1]:
                    distance+=num(j[1])
        if listofpath[i] in list(HarborDict.keys()):
            for j in HarborDict[listofpath[i]].pathlist:
                if j[0].name == listofpath[i+1]:
                    distance+=num(j[1])
        if listofpath[i] in list(TrainstationDict.keys()):
            for j in TrainstationDict[listofpath[i]].pathlist:
                if j[0].name == listofpath[i+1]:
                    distance+=num(j[1])
        if listofpath[i] in list(WarehouseDict.keys()):
            for j in WarehouseDict[listofpath[i]].pathlist:
                if j[0].name == listofpath[i+1]:
                    distance+=num(j[1])
    return distance

def processOrder():
    fristairport = ["USA", "UK", "Italy"]
    secondairport = ["Wakanda", "Germany", "USSR"]
    thirdairport = ["Brazil", "Argentina", "Ireland"]
    fristharbor = ["India","Indonesia", "Hong Kong"]
    secondharbor = ["Philipine", "Singapore", "Sri Lanka"]
    thirdharbor = ["Egypt", "Congo", "Madagascer"]
    fristtrainstation = ["Vietnam", "China", "Laos"]
    secondtrainstation = ["Hungary", "Austria", "Myanmar"]
    thirdtrainstation = ["Bulgaria", "Poland", "Latvia"]
    orderNum=0
    ProcessNum=0
    SuccessNum=0
    FailNum=0
    keyOrderList=list(OrderDict.keys())
    for i in list(AirportDict.keys()):
        if AirportDict[i].count == 0:
            for j in list(TruckDict.keys()):
                TruckDict[j].lastplacename = AirportDict[i].name
    for i in keyOrderList:
        orderNum=OrderDict[i].name
        ProcessNum=len(OrderDict[i].listevent)
        SuccessNum = 0
        FailNum = 0
        TruckName=''
        TruckNamelist=[]
        Rejectbool = False
        FailBool = {}
        countevent =0
        minload = num(OrderDict[i].listevent[0][1]) * num(ItemDict[OrderDict[i].listevent[0][2]].weight)
        maxload = num(OrderDict[i].listevent[0][1]) * num(ItemDict[OrderDict[i].listevent[0][2]].weight)
        print("Order "+str(orderNum)+':')
        #logfile.write("Order "+str(orderNum)+':\r\n')

        # check weight ,truck
        countevent = 0
        #check truck1
        for j in OrderDict[i].listevent:
            countevent += 1
            weight = num(j[1]) * ItemDict[j[2]].weight
            if weight <= minload:
                minload = weight
            if weight >= maxload:
                maxload = weight
        for k in list(TruckDict.keys()):
            # print(k)
            # print(TruckDict[k].minload)
            # print(TruckDict[k].maxload)
            if maxload >= int(TruckDict[k].minload) and maxload <= int(TruckDict[k].maxload):
                TruckName = k
        if TruckName == '':
            Rejectbool = True
        else:
            Rejectbool = False
        #check truck2
        '''for j in OrderDict[i].listevent:
            countevent += 1
            weight = num(j[1]) * ItemDict[j[2]].weight
            for k in list(TruckDict.keys()):
                if weight >= TruckDict[k].minload and weight <= TruckDict[k].maxload:
                    TruckName = k
                    TruckNamelist.append(TruckName)
            if TruckName == '':
                Rejectbool = True
                FailBool[countevent] = True
                FailNum += 1
            else:
                FailBool[countevent] = False
                Rejectbool = False'''
        if Rejectbool == True:
            print('Reject')
            print('')
            continue
        else:
            for j in TruckNamelist:
                if TruckDict[TruckName].maxload<TruckDict[j].maxload:
                    TruckName=j
        #check name
        countevent = 0
        for j in OrderDict[i].listevent:
            countevent += 1
            if j[0] == 'Import':
                if j[2] not in list(ItemDict.keys()) or j[3] not in Nation or j[4] not in list(WarehouseDict.keys()):
                    FailBool[countevent] = True
                    FailNum += 1
                    #print("name fail")
                else:
                    FailBool[countevent] = False
            elif j[0] == 'Export':
                if j[2] not in list(ItemDict.keys()) or j[4] not in Nation or j[3] not in list(WarehouseDict.keys()):
                    FailBool[countevent] = True
                    FailNum += 1
                    #print("name fail")
                else:
                    FailBool[countevent] = False
            elif j[0] == 'Transfer':
                if j[2] not in list(ItemDict.keys()) or j[3] not in list(WarehouseDict.keys()) or j[4] not in list(WarehouseDict.keys()):
                    FailBool[countevent] = True
                    FailNum += 1
                    #print("name fail")
                else:
                    FailBool[countevent] = False
            else:
                FailBool[countevent] = False

        #check temp
        countevent = 0
        for j in OrderDict[i].listevent:
            countevent+=1
            if FailBool[countevent] == False:
                if j[0]=='Import' or j[0]=='Transfer':
                    if WarehouseDict[j[4]].temp < ItemDict[j[2]].mintemp or WarehouseDict[j[4]].temp > ItemDict[j[2]].maxtemp:
                        FailBool[countevent]=True
                        FailNum+=1
                        #print("temp fail")
                    else:
                        FailBool[countevent]=False
                else:
                    FailBool[countevent] = False

        #check slot & add,delete in object
        countevent = 0
        for j in OrderDict[i].listevent:
            countevent += 1
            fail=False
            #print(j)
            if FailBool[countevent] == False:
                if j[0] == 'Import':
                    if WarehouseDict[j[4]].capacity<len(WarehouseDict[j[4]].log)+num(j[1]):
                        FailBool[countevent]=True
                        FailNum += 1
                        #print("slot fail")
                    else:
                        for l in range(num(j[1])):
                            if j[3] in fristairport:
                                WarehouseDict[j[4]].importProduct(j[2])
                                for k in list(AirportDict.keys()):
                                    if AirportDict[k].count == 0:
                                        AirportDict[k].importlist.append(j[2])
                            elif j[3] in secondairport:
                                WarehouseDict[j[4]].importProduct(j[2])
                                for k in list(AirportDict.keys()):
                                    if AirportDict[k].count == 1:
                                        AirportDict[k].importlist.append(j[2])
                            elif j[3] in thirdairport:
                                WarehouseDict[j[4]].importProduct(j[2])
                                for k in list(AirportDict.keys()):
                                    if AirportDict[k].count == 2:
                                        AirportDict[k].importlist.append(j[2])
                            elif j[3] in fristharbor:
                                WarehouseDict[j[4]].importProduct(j[2])
                                for k in list(HarborDict.keys()):
                                    if HarborDict[k].count == 0:
                                        HarborDict[k].importlist.append(j[2])
                            elif j[3] in secondharbor:
                                WarehouseDict[j[4]].importProduct(j[2])
                                for k in list(HarborDict.keys()):
                                    if HarborDict[k].count == 1:
                                        HarborDict[k].importlist.append(j[2])
                            elif j[3] in thirdharbor:
                                WarehouseDict[j[4]].importProduct(j[2])
                                for k in list(HarborDict.keys()):
                                    if HarborDict[k].count == 2:
                                        HarborDict[k].importlist.append(j[2])
                            elif j[3] in fristtrainstation:
                                WarehouseDict[j[4]].importProduct(j[2])
                                for k in list(TrainstationDict.keys()):
                                    if TrainstationDict[k].count == 0:
                                        TrainstationDict[k].importlist.append(j[2])
                            elif j[3] in secondtrainstation:
                                WarehouseDict[j[4]].importProduct(j[2])
                                for k in list(TrainstationDict.keys()):
                                    if TrainstationDict[k].count == 1:
                                        TrainstationDict[k].importlist.append(j[2])
                            elif j[3] in thirdtrainstation:
                                WarehouseDict[j[4]].importProduct(j[2])
                                for k in list(TrainstationDict.keys()):
                                    if TrainstationDict[k].count == 2:
                                        TrainstationDict[k].importlist.append(j[2])
                            else:
                                fail=True
                    if fail==True:
                        FailBool[countevent] = True
                        FailNum += 1
                        #print("name fail")
                        #print("++++++++++++++++++++++++++++++++++++++++")
                        #print(AirportDict[j[3]].importlist)
                elif j[0] == 'Export':
                    countiteminwarehouse=0
                    for k in WarehouseDict[j[3]].log:
                        if k == j[2]:
                            countiteminwarehouse+=1
                    if countiteminwarehouse<num(j[1]):
                        FailBool[countevent]=True
                        FailNum += 1
                        #print("slot fail")
                    else:
                        for l in range(num(j[1])):
                            if j[4] in fristairport:
                                WarehouseDict[j[3]].exportProduct(j[2])
                                for k in list(AirportDict.keys()):
                                    if AirportDict[k].count == 0:
                                        AirportDict[k].exportlist.append(j[2])
                            elif j[4] in secondairport:
                                WarehouseDict[j[3]].exportProduct(j[2])
                                for k in list(AirportDict.keys()):
                                    if AirportDict[k].count == 1:
                                        AirportDict[k].exportlist.append(j[2])
                            elif j[4] in thirdairport:
                                WarehouseDict[j[3]].exportProduct(j[2])
                                for k in list(AirportDict.keys()):
                                    if AirportDict[k].count == 2:
                                        AirportDict[k].exportlist.append(j[2])
                            elif j[4] in fristharbor:
                                WarehouseDict[j[3]].exportProduct(j[2])
                                for k in list(HarborDict.keys()):
                                    if HarborDict[k].count == 0:
                                        HarborDict[k].exportlist.append(j[2])
                            elif j[4] in secondharbor:
                                WarehouseDict[j[3]].exportProduct(j[2])
                                for k in list(HarborDict.keys()):
                                    if HarborDict[k].count == 1:
                                        HarborDict[k].exportlist.append(j[2])
                            elif j[4] in thirdharbor:
                                WarehouseDict[j[3]].exportProduct(j[2])
                                for k in list(HarborDict.keys()):
                                    if HarborDict[k].count == 2:
                                        HarborDict[k].exportlist.append(j[2])
                            elif j[4] in fristtrainstation:
                                WarehouseDict[j[3]].exportProduct(j[2])
                                for k in list(TrainstationDict.keys()):
                                    if TrainstationDict[k].count == 0:
                                        TrainstationDict[k].exportlist.append(j[2])
                            elif j[4] in secondtrainstation:
                                WarehouseDict[j[3]].exportProduct(j[2])
                                for k in list(TrainstationDict.keys()):
                                    if TrainstationDict[k].count == 1:
                                        TrainstationDict[k].exportlist.append(j[2])
                            elif j[4] in thirdtrainstation:
                                WarehouseDict[j[3]].exportProduct(j[2])
                                for k in list(TrainstationDict.keys()):
                                    if TrainstationDict[k].count == 2:
                                        TrainstationDict[k].exportlist.append(j[2])
                            else:
                                fail = True
                    if fail == True:
                        FailBool[countevent] = True
                        FailNum += 1
                        #print("name fail")
                elif j[0] == 'Transfer':
                    if WarehouseDict[j[3]].name==WarehouseDict[j[4]].name:
                        pass
                    elif WarehouseDict[j[4]].capacity<len(WarehouseDict[j[4]].log)+num(j[1]):
                        FailBool[countevent]=True
                        FailNum += 1
                        #print("slot fail")
                    else:
                        countiteminwarehouse = 0
                        for k in WarehouseDict[j[3]].log:
                            if k == j[2]:
                                countiteminwarehouse += 1
                        if countiteminwarehouse < num(j[1]):
                            FailBool[countevent]=True
                            FailNum += 1
                            #print("slot fail")
                        else:
                            for l in range(num(j[1])):
                                WarehouseDict[j[3]].transferProduct(j[2], WarehouseDict[j[4]])

        # check distence
        countevent = 0
        for j in OrderDict[i].listevent:
            countevent += 1
            fromname = ''
            toname = ''

            #print(j)
            if FailBool[countevent] == False:
                if j[0]=='Import':
                    if j[3] in fristairport:
                        for k in list(AirportDict.keys()):
                            if AirportDict[k].count==0:
                                fromname=AirportDict[k].name
                    elif j[3] in secondairport:
                        for k in list(AirportDict.keys()):
                            if AirportDict[k].count==1:
                                fromname=AirportDict[k].name
                    elif j[3] in thirdairport:
                        for k in list(AirportDict.keys()):
                            if AirportDict[k].count==2:
                                fromname=AirportDict[k].name
                    elif j[3] in fristharbor:
                        for k in list(HarborDict.keys()):
                            if HarborDict[k].count==0:
                                fromname=HarborDict[k].name
                    elif j[3] in secondharbor:
                        for k in list(HarborDict.keys()):
                            if HarborDict[k].count==1:
                                fromname=HarborDict[k].name
                    elif j[3] in thirdharbor:
                        for k in list(HarborDict.keys()):
                            if HarborDict[k].count==2:
                                fromname=HarborDict[k].name
                    elif j[3] in fristtrainstation:
                        for k in list(TrainstationDict.keys()):
                            if TrainstationDict[k].count==0:
                                fromname=TrainstationDict[k].name
                    elif j[3] in secondtrainstation:
                        for k in list(TrainstationDict.keys()):
                            if TrainstationDict[k].count==1:
                                fromname=TrainstationDict[k].name
                    elif j[3] in thirdtrainstation:
                        for k in list(TrainstationDict.keys()):
                            if TrainstationDict[k].count==2:
                                fromname=TrainstationDict[k].name
                    toname=WarehouseDict[j[4]].name
                elif j[0]=='Export':
                    fromname=WarehouseDict[j[3]].name
                    if j[4] in fristairport:
                        for k in list(AirportDict.keys()):
                            if AirportDict[k].count==0:
                                toname=AirportDict[k].name
                    elif j[3] in secondairport:
                        for k in list(AirportDict.keys()):
                            if AirportDict[k].count==1:
                                toname=AirportDict[k].name
                    elif j[3] in thirdairport:
                        for k in list(AirportDict.keys()):
                            if AirportDict[k].count==2:
                                toname=AirportDict[k].name
                    elif j[3] in fristharbor:
                        for k in list(HarborDict.keys()):
                            if HarborDict[k].count==0:
                                toname=HarborDict[k].name
                    elif j[3] in secondharbor:
                        for k in list(HarborDict.keys()):
                            if HarborDict[k].count==1:
                                toname=HarborDict[k].name
                    elif j[3] in thirdharbor:
                        for k in list(HarborDict.keys()):
                            if HarborDict[k].count==2:
                                toname=HarborDict[k].name
                    elif j[3] in fristtrainstation:
                        for k in list(TrainstationDict.keys()):
                            if TrainstationDict[k].count==0:
                                toname=TrainstationDict[k].name
                    elif j[3] in secondtrainstation:
                        for k in list(TrainstationDict.keys()):
                            if TrainstationDict[k].count==1:
                                toname=TrainstationDict[k].name
                    elif j[3] in thirdtrainstation:
                        for k in list(TrainstationDict.keys()):
                            if TrainstationDict[k].count==2:
                                toname=TrainstationDict[k].name
                elif j[0]=='Transfer':
                    fromname=WarehouseDict[j[3]].name
                    toname=WarehouseDict[j[4]].name
                    #if fromname==toname:

                #print(fromname)
                #print(toname)
                #print(TruckDict[TruckName].lastplacename)
                #print(dfs_path(GraphOfPath,fromname,toname))
                if j[0]=='Transfer' and fromname==toname:
                    pass
                elif dfs_path(GraphOfPath,TruckDict[TruckName].lastplacename,fromname)==[] and TruckDict[TruckName].lastplacename!=fromname:
                    FailBool[countevent] = True
                    FailNum += 1
                    #print("path fail")
                elif dfs_path(GraphOfPath,fromname,toname)==[]:
                    FailBool[countevent] = True
                    FailNum += 1
                    #print("path fail")
                else:
                    if TruckDict[TruckName].lastplacename!=fromname:
                        TruckDict[TruckName].distance += distanceOfEvent(dfs_path(GraphOfPath, TruckDict[TruckName].lastplacename, fromname)[0])
                    TruckDict[TruckName].distance += distanceOfEvent(dfs_path(GraphOfPath,fromname,toname)[0])
                    TruckDict[TruckName].lastplacename=toname

        print("Process:", ProcessNum)
        print('Success:', ProcessNum - FailNum)
        print('Fail:', FailNum)

        #print log
        for j in list(WarehouseDict.keys()):
            WarehouseDict[j].log.sort()
            print(WarehouseDict[j].name,'('+str(len(WarehouseDict[j].log))+','+str(WarehouseDict[j].capacity)+'):',str(WarehouseDict[j].log).replace("'",''))
        print("")
    #Summary
    print('Summary:')
    for i in list(WarehouseDict.keys()):
        WarehouseDict[i].log.sort()
        print(WarehouseDict[i].name, '(' + str(len(WarehouseDict[i].log)) + ',' + str(WarehouseDict[i].capacity) + '):',str(WarehouseDict[i].log).replace("'", ''))
    for i in list(TruckDict.keys()):
        print(TruckDict[i].name,'has traveled',TruckDict[i].printDistance(),'km.')
    for i in SortLog:
        if i in list(HarborDict.keys()):
            HarborDict[i].importlist.sort()
            HarborDict[i].exportlist.sort()
            print(HarborDict[i].name, 'has imported', len(HarborDict[i].importlist), 'items:',str(HarborDict[i].importlist).replace("'", ''))
            print(HarborDict[i].name, 'has exported', len(HarborDict[i].exportlist), 'items:',str(HarborDict[i].exportlist).replace("'", ''))
        elif i in list(AirportDict.keys()):
            AirportDict[i].importlist.sort()
            AirportDict[i].exportlist.sort()
            print(AirportDict[i].name, 'has imported', len(AirportDict[i].importlist), 'items:', str(AirportDict[i].importlist).replace("'", ''))
            print(AirportDict[i].name, 'has exported', len(AirportDict[i].exportlist), 'items:', str(AirportDict[i].exportlist).replace("'", ''))
        elif i in list(TrainstationDict.keys()):
            TrainstationDict[i].importlist.sort()
            TrainstationDict[i].exportlist.sort()
            print(TrainstationDict[i].name, 'has imported', len(TrainstationDict[i].importlist), 'items:', str(TrainstationDict[i].importlist))
            print(TrainstationDict[i].name, 'has exported', len(TrainstationDict[i].exportlist), 'items:', str(TrainstationDict[i].exportlist))

def Main():
    #log = open("testLog.txt", 'w')
    #sys.stdout = log
    #print(ReadInputFile("test_input_5.txt"))
    #InputFileList = ReadInputFile("test_input_5.txt")
    #print(ReadInputFile("input01.txt"))
    InputFileList = ReadInputFile("input04.txt")
    CreateObject(InputFileList)
    EventObject(TransactionList)
    print(GraphOfPath)
    processOrder()

    #log.close()

if __name__ == '__main__':
    Main()