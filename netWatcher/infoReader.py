from UserInfo import *

class InfoReader:
    fileName="userInfo.txt"
    splitterCharacter="|"




    def readFile(self,x):

        archvio=open(x,'r')
        salida=archvio.readlines()
        archvio.close()
        return salida



    def readUserInfor(self):

        content= self.readFile(self.fileName)
        content.remove(content.__getitem__(0))
        listaInfo=[]
        for line  in content:
            parameters=line.split(self.splitterCharacter)
            id              = int(parameters.__getitem__(1))
            tipo            = parameters.__getitem__(2).strip()
            nombre          = parameters.__getitem__(3).strip()
            desc            = parameters.__getitem__(4).strip()
            notificar       = bool(parameters.__getitem__(5))
            email           = parameters.__getitem__(6).strip()
            mac             = parameters.__getitem__(7).strip()

            userInfo=UserInfo(id,nombre,desc,mac,tipo,notificar,email)
            listaInfo.append(userInfo)
        return listaInfo;
    