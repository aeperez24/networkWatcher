from Host import *;
from infoReader import *;
from UserInfo import *;
from UserHost import *
from LastStatusRegister import *;
from LastStatusProcessor import *;
from Messager import *;
from MailConfig import mailPassword;
from MailConfig import mailUsername
import time
import nmap
user=mailUsername
pwd=mailPassword
while True:
    vardisc=discoverer(nmap)
    hosts=vardisc.discoverHosts("192.168.0.1/24","-sP")
    infoRead=InfoReader();
    infoUsers=infoRead.readUserInfor();
    userHostRelator=UserHostRelator();
    userHostRelator.idsToIgnore=[3,4,5,6,7,9,10,11]#TODO:move to an external file and read it!!
    userHostRelator.hosts=hosts
    userHostRelator.usersInfo=infoUsers
    relations=userHostRelator.relateKnownHosts()
    #for relation in relations:
    #    print("{} esta conectad@".format(relation.userInfo.nombre))

    register=LastStatusRegisterManager()
    register.reload()

    idsConecteds=[]
    for relation in relations:
        idsConecteds.append(relation.userInfo.id)
    print("id conectadas: {}".format(idsConecteds))

    idsConectedRegister=register.getidsConnected()
    lastStatusProcesor=LastStatusProcessor(idsConecteds,idsConectedRegister)
    statusProcesed=lastStatusProcesor.getStatus()

    register.save(relations)
    for statusAux in statusProcesed:
        print("statusAux id:{} y st:{}".format(statusAux.id,statusAux.st))
        if statusAux.st!=0:
            msj=createMessage(statusAux,infoUsers)
            send_email(user,pwd,msj.recipent,"sistema de monitoreo de andres",msj.text)

    print("fin de la ejecucion")

    time.sleep(5)