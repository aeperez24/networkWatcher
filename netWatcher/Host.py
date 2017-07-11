class Host:
    def __init__(self):
        self.ip=""
        self.operativeSystem=""
        self.mac=""
        self.brand=""

    def setIp(self,ip):
        self.ip=ip;

    def setMac(self, ip):
        self.mac = ip;

    def setoperativeSystem(self, operativeSystem):
        self.operativeSystem = operativeSystem;

    def getIp(self):
        return self.ip;


    def getOperativeSystem(self):
        return self.operativeSystem;


    def getMac(self):
        return self.mac;
    def setBrand(self,brand):
        self.brand=brand;
    def getBrand(self):
        return self.brand;


class discoverer:
    def __init__(self,defclassnmap):
        self.nmapClass=defclassnmap;

    def discoverHosts(self,ipToDiscover,arguments):
        nmap=self.nmapClass;
        ip = ipToDiscover;
        var_argument = arguments;
        scanner = nmap.PortScanner()
        scanner.scan(ip, arguments=var_argument)
        hosts = []
        for host in scanner.all_hosts():
            nameHost = host
            stateHost = scanner[host].state()
            macs = scanner[host]['vendor']
            # se muestran todos los hosts con el siguiente print
            # print(scanner[host])
            listMacs = []
            #osclasses=scanner[host]['oslass'];

            # print("{} : state {}".format(nameHost, stateHost))
            hostAux = Host();
            hostAux.setIp(nameHost)
            for mac in macs:
                if 'mac' in scanner[host]['addresses']:
                    listMacs.append(mac);
                    hostAux.setMac(mac)
            # for osclass in osclasses:
            #     host.setoperativeSystem(osclass)

            hosts.append(hostAux)

        return hosts;


