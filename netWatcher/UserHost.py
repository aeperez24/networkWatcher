class UserHost:
    def __init__(self,userInfo,host):
        self.userInfo=userInfo;
        self.host=host;

class UserHostRelator:
    macsToIgnore=[]
    idsToIgnore=[]
    usersInfo=[]
    hosts=[]
    def relateKnownHosts(self):
        result=[]
        for host in self.hosts:
            for userInfo in self.usersInfo:
                if userInfo.mac==host.mac and not (host.mac in self.macsToIgnore) and not (userInfo.id in self.idsToIgnore):
                    userHost=UserHost(userInfo,host)
                    result.append(userHost)
        return result
