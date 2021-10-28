#!/usr/bin/python
import sys
from mininet.node import Controller
from mininet.log import setLogLevel, info
from mn_wifi.cli import CLI_wifi
from mn_wifi.net import Mininet_wifi
from mn_wifi.link import wmediumd, adhoc
from mn_wifi.wmediumdConnector import interference
from mn_wifi.link import wmediumd, mesh

def topology(plot):
    "Create a network."
  
    net = Mininet_wifi(link=wmediumd, wmediumd_mode=interference, controller=Controller)

    info("*** Creating nodes\n")    
    #creating mobile stations
    sta1 = net.addStation('sta1', mac='00:00:00:00:00:02', ip='10.0.0.2/8', position='30,40,0' , passwd= '19066506')
    sta2 = net.addStation('sta2', mac='00:00:00:00:00:03', ip='10.0.0.3/8', position='30,40,0' , passwd= '19066506')
    sta3 = net.addStation('sta3', mac='00:00:00:00:00:04', ip='10.0.0.4/8', position='30,40,0' , passwd= '19066506')
    sta4 = net.addStation('sta4', mac='00:00:00:00:00:05', ip='10.0.0.5/8', position='30,40,0' , passwd= '19066506')  
    

    
    #Ad-hoc networks
    sta4ad = net.addStation('sta4ad', position='150,150,0', range=30 , mac='00:00:00:00:00:06', ipv6='fe80::4' , antenna_height=1 , antenna_gain=5 ) 
          
    sta5ad = net.addStation('sta5ad', position='175,150,0', range=30 , mac='00:00:00:00:00:07', ipv6='fe80::5' , antenna_height=2 , antenna_gain=6)
	
    sta6ad = net.addStation('sta6ad', position='200,150,0', range=30 , mac='00:00:00:00:00:08', ipv6='fe80::6' , antenna_height=3 , antenna_gain=7)


    #Mesh networks
    sta7M = net.addStation('sta7M', position='25,150,0', range=30 , mac='00:00:00:00:00:09', ipv6='fe80::7' , antenna_height=3 , antenna_gain=7 )

    sta8M = net.addStation('sta8M', position='50,150,0', range=30 , mac='00:00:00:00:00:10', ipv6='fe80::8' , antenna_height=3 , antenna_gain=7 )
	
    sta9M = net.addStation('sta9M', position='70,150,0', range=30 , mac='00:00:00:00:00:11', ipv6='fe80::9' , antenna_height=3 , antenna_gain=7 )

   


    #Access Points
    ap1 = net.addAccessPoint('ap1', mac ='00:00:00:00:10:02', ssid='ssid-ap1', mode='g',channel='1',position='50,50,0', band='5',  range=25 , passwd= '19065506')
    ap2 = net.addAccessPoint('ap2', mac ='00:00:00:00:10:03', ssid='ssid-ap2', mode='g',channel='6', position='100,50,0', band='5',  range=25 , passwd= '19065506')
    ap3 = net.addAccessPoint('ap3', mac ='00:00:00:00:10:04', ssid='ssid-ap3', mode='g',channel='2',position='150,50,0', band='5',  range=25 , passwd= '19065506')
    ap4 = net.addAccessPoint('ap4', mac ='00:00:00:00:10:05', ssid='ssid-ap4', mode='g',channel='3', position='150,90,0', band='5', range=25 ,  passwd= '19065506')
 
    net.setPropagationModel(model="logDistance", exp=4)

    
    c1 = net.addController('c1')



    info("*** Configuring wifi nodes\n")
    net.configureWifiNodes()

    info("*** Creating links\n")

    net.plotGraph(min_x=0, min_y=0, max_x=230, max_y=230)
    net.startMobility(time=0)

    net.addLink(ap1, ap2)
    net.addLink(ap3, ap2)
    net.addLink(ap3, ap4)
   
    #Ad-hoc links
    net.addLink(sta4ad, cls=adhoc, ssid='adhocUH', mode='g',  proto='olsr', channel=5, ht_cap='HT40+')
    net.addLink(sta5ad, cls=adhoc, ssid='adhocUH', mode='g',  proto='olsr', channel=5, ht_cap='HT40+')
    net.addLink(sta6ad, cls=adhoc, ssid='adhocUH', mode='g',  proto='olsr', channel=5, ht_cap='HT40+')


    #Mesh Network
    net.addLink(sta7M, cls=mesh, ssid='meshNet', mode='g', channel=5, ht_cap='HT40+')
    net.addLink(sta8M, cls=mesh, ssid='meshNet', mode='g', channel=5, ht_cap='HT40+')
    net.addLink(sta9M, cls=mesh, ssid='meshNet', mode='g', channel=5, ht_cap='HT40+')
     
    
    

    #TODO set mobility to random 
    net.startMobility(time=0)
    net.mobility(sta1,'start', time=10, position='30,40,0')
    net.mobility(sta2,'start', time=15, position='30,40,0')
    net.mobility(sta3,'start', time=16, position='30,40,0')
    net.mobility(sta4,'start', time=3, position='30,40,0')
    net.mobility(sta1,'stop', time=20, position='100,40,0')
    net.mobility(sta2,'stop', time=21, position='150,60,0')
    net.mobility(sta3,'stop', time=22, position='150,100,0')
    net.mobility(sta4,'stop', time=10, position='50,100,0')
    net.stopMobility(time=25)




    net.stopMobility(time=30)
    
    info("*** Starting network\n")
    net.build()
    c1.start()
    ap1.start([c1])
    ap2.start([c1])
    ap3.start([c1])
    ap4.start([c1])

    
	

    info("*** Running CLI\n")
    CLI_wifi(net)

    info("*** Stopping network\n")
    net.stop()

if __name__ == '__main__':
    setLogLevel('info')
    plot = False if '-p' in sys.argv else True
    topology(plot)
