import json
class LastStatusRegisterManager:
    lastReadUserHosts=[]
    listJson=""
    nameFile="lastStatus.txt"
    def __init__(self):
        print("In Building")
    def getidsConnected(self):
        ids=[]
        for readUserHost in self.lastReadUserHosts:
            ids.append(int(readUserHost))
        return ids

    def reload(self):
        self.lastReadUserHosts=[]
        archvio = open(self.nameFile, 'r')
        salida = archvio.read().replace("\'","\"").replace("True","true").replace("False","false")
        archvio.close()
        varjson = json.loads(salida)
        # print("-------------------------------------archivo leido es {}".format(salida))
        for varX in varjson:
          self.lastReadUserHosts.append(varX['userInfo']['id'])
        print ("reloading")
        self.listJson=salida;


    def save(self,UsersHosts):
        # print("saving next")
        fout = open(self.nameFile, 'w')
        fout.write("[")
        size=UsersHosts.__len__()
        counter=0
        for userHost in UsersHosts:
            fout.write("{\'userInfo\':"+str(userHost.userInfo.__dict__)+",\'host\':"+str(userHost.host.__dict__)+"}")
            counter=counter+1
            # print(userHost.__dict__)
            if counter<size:
                fout.write(",")
        fout.write("]")
        fout.close()

#TEST
# rmanager=LastStatusRegisterManager()
# rmanager.reload()
# print(rmanager.lastReadUserHosts)