import nmap;
ip="192.168.0.1/28";
var_argument="-sP";
scanner=nmap.PortScanner()
scanner.scan(ip,arguments=var_argument)

for host in scanner.all_hosts():
    nameHost=host
    stateHost=scanner[host].state()
    macs=scanner[host]['vendor']
    addresses=scanner[host]['addresses']
    listMacs=[]
    # for mac in macs:
        # print(mac)



