import os
import netifaces as ni
import nmap

if __name__== "__main__":
    ps = nmap.PortScanner()
    ps.scan('10.0.0.0/24',arguments= '-p 22 --open')
    print(ps.all_hosts())

    ###############################################
    # net = ni.interfaces()

    # for n in net: 
    #     a = ni.ifaddresses(n)
    #     try:
    #         ip = a[ni.AF_INET][0]['addr']
    #         print(ip)
    #     except KeyError as e:
    #         pass
    

    ###############################################
    # for root, dir, file in os.walk(os.path.abspath('.')):
    #     for f in file:
    #         if(f == "infected.txt"):
    #             print('1')

