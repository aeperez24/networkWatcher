class statusProcesed:
    id=0
    st=0
class LastStatusProcessor:
    def __init__(self,actuals,lasts):
        self.actuals=actuals;
        self.lasts=lasts;
    def getStatus(self):
        procesed=[]
        for actualConected in self.actuals:
            nstatus = statusProcesed()
            nstatus.id=actualConected
            if not actualConected in self.lasts:
                nstatus.st=1
                procesed.append(nstatus)
            else:
                procesed.append(nstatus)
        for lastConected in self.lasts:
            if not( lastConected in self.actuals):
                nstatus=statusProcesed()
                nstatus.id=lastConected
                nstatus.st=2
                procesed.append(nstatus)
        return procesed



#testing
# varActual=[1,2,3,4]
# varLast=[1,2,5]
# procesor=LastStatusProcessor(varActual,varLast)
# varProcesed=procesor.getStatus()
#
# for varProcesedx in varProcesed:
#     print(str(varProcesedx.id)+":"+str(varProcesedx.st))