from mininet.topo import Topo  
from mininet.node import CPULimitedHost, Host, Node
from mininet.node import OVSSwitch
from mininet.topo import Topo


class VLANHost( Host ):
        def config( self, vlan=100, **params ):
                """Configure VLANHosts """
                r = super( Host, self ).config( **params )
                intf = self.defaultIntf()
                self.cmd( 'ifconfig %s inet 0' % intf )
                self.cmd( 'vconfig add %s %d' % ( intf, vlan ) )
                self.cmd( 'ifconfig %s.%d inet %s' % ( intf, vlan, params['ip'] ) )
                newName = '%s.%d' % ( intf, vlan )
                intf.name = newName
                self.nameToIntf[ newName ] = intf
                return r

class MyTopo( Topo ):  
    "Simple topology example."
    def __init__( self ):
        "Create custom topo."

        # Initialize topology
        Topo.__init__( self )

        # Add hosts and switches TODO
	h1 = self.addHost( 'H1' , mac='00:00:00:00:00:01', ip='147.197.29.1/24', cls=VLANHost, vlan=300)
	h2 = self.addHost( 'H2' , mac='00:00:00:00:00:02', ip='147.197.29.2/24', cls=VLANHost, vlan=400)
	h3 = self.addHost( 'H3' , mac='00:00:00:00:00:03', ip='147.197.29.3/24', cls=VLANHost, vlan=300)
	h4 = self.addHost( 'H4' , mac='00:00:00:00:00:04', ip='147.197.29.4/24', cls=VLANHost, vlan=400)
	h5 = self.addHost( 'H5' , mac='00:00:00:00:00:01', ip='147.197.29.5/24', cls=VLANHost, vlan=300)
	h6 = self.addHost( 'H6' , mac='00:00:00:00:00:02', ip='147.197.29.6/24', cls=VLANHost, vlan=400)
	h7 = self.addHost( 'H7' , mac='00:00:00:00:00:03', ip='147.197.29.7/24', cls=VLANHost, vlan=300)
	h8 = self.addHost( 'H8' , mac='00:00:00:00:00:04', ip='147.197.29.8/24', cls=VLANHost, vlan=400)
	
	#SERVER = self.addHost( 'SERVER' , mac='02:00:00:00:20:03',ip='192.168.1.5/24')
	#CLIENT = self.addHost( 'CLIENT' , mac='02:00:00:00:20:04',ip='192.168.1.6/24')

	Switch1 = self.addSwitch( 'Switch1' , cls=OVSSwitch)
        Switch2 = self.addSwitch( 'Switch2' , cls=OVSSwitch)
	Switch3 = self.addSwitch( 'Switch3' , cls=OVSSwitch)
	Switch4 = self.addSwitch( 'Switch4' , cls=OVSSwitch)
	Switch5 = self.addSwitch( 'Switch5' , cls=OVSSwitch)
        Switch6 = self.addSwitch( 'Switch6' , cls=OVSSwitch)
	Switch7 = self.addSwitch( 'Switch7' , cls=OVSSwitch)
	Switch8 = self.addSwitch( 'Switch8' , cls=OVSSwitch)
	Switch9 = self.addSwitch( 'Switch9' , cls=OVSSwitch)
        Switch10 = self.addSwitch( 'Switch10' , cls=OVSSwitch)
	Switch11 = self.addSwitch( 'Switch11' , cls=OVSSwitch)



        
        
        # Add links TODO 
	self.addLink( h1, Switch1,Bandwidth='1000', delay='0', Loss='0' )
	self.addLink( h2, Switch2,Bandwidth='1000', delay='0', Loss='0' )
	self.addLink( h3, Switch3,Bandwidth='1000', delay='0', Loss='0' )
	self.addLink( h4, Switch4,Bandwidth='1000', delay='0', Loss='0' )
	self.addLink( h5, Switch5,Bandwidth='1000', delay='0', Loss='0' )
	self.addLink( h6, Switch6,Bandwidth='1000', delay='0', Loss='0' )
	self.addLink( h7, Switch7,Bandwidth='1000', delay='0', Loss='0' )
	self.addLink( h8, Switch8,Bandwidth='1000', delay='0', Loss='0' )
	

	self.addLink( Switch1, Switch2,Bandwidth='1000', delay='1', Loss='0.5' )
	self.addLink( Switch1, Switch9, Bandwidth='1000', delay='1', Loss='0.5' )

	self.addLink( Switch2, Switch1,Bandwidth='1000', delay='1', Loss='0.5' )
	self.addLink( Switch2, Switch9,Bandwidth='1000', delay='1', Loss='0.5' )
	self.addLink( Switch2, Switch5,Bandwidth='1000', delay='1', Loss='0.5' )
	self.addLink( Switch2, Switch10,Bandwidth='1000', delay='1', Loss='0.5' )
	
	self.addLink( Switch3, Switch4,Bandwidth='1000', delay='1', Loss='0.5' )
	self.addLink( Switch3, Switch9,Bandwidth='1000', delay='1', Loss='0.5' )
	
	
	self.addLink( Switch4, Switch3,Bandwidth='1000', delay='1', Loss='0.5' )
	self.addLink( Switch4, Switch7,Bandwidth='1000', delay='1', Loss='0.5' )
	self.addLink( Switch4, Switch9,Bandwidth='1000', delay='1', Loss='0.5' )
	self.addLink( Switch4, Switch10,Bandwidth='1000', delay='1', Loss='0.5' )

	self.addLink( Switch5, Switch2,Bandwidth='1000', delay='1', Loss='0.5' )
	self.addLink( Switch5, Switch6,Bandwidth='1000', delay='1', Loss='0.5' )
	self.addLink( Switch5, Switch10,Bandwidth='1000', delay='1', Loss='0.5' )
	self.addLink( Switch5, Switch11,Bandwidth='1000', delay='1', Loss='0.5' )

	self.addLink( Switch6, Switch5,Bandwidth='1000', delay='1', Loss='0.5' )
	self.addLink( Switch6, Switch11,Bandwidth='1000', delay='1', Loss='0.5' )

	self.addLink( Switch7, Switch4,Bandwidth='1000', delay='1', Loss='0.5' )
	self.addLink( Switch7, Switch8,Bandwidth='1000', delay='1', Loss='0.5' )
	self.addLink( Switch7, Switch10,Bandwidth='1000', delay='1', Loss='0.5' )
	self.addLink( Switch7, Switch11,Bandwidth='1000', delay='1', Loss='0.5' )
	
	self.addLink( Switch8, Switch11,Bandwidth='1000', delay='1', Loss='0.5' )
	self.addLink( Switch8, Switch7,Bandwidth='1000', delay='1', Loss='0.5')

	self.addLink( Switch9, Switch3,Bandwidth='1000', delay='1', Loss='0.5' )
	self.addLink( Switch9, Switch4,Bandwidth='1000', delay='1', Loss='0.5' )
	self.addLink( Switch9, Switch1,Bandwidth='1000', delay='1', Loss='0.5' )
	self.addLink( Switch9, Switch2,Bandwidth='1000', delay='1', Loss='0.5' )
	self.addLink( Switch9, Switch10,Bandwidth='1000', delay='1', Loss='0.5' )

	self.addLink( Switch10, Switch2,Bandwidth='1000', delay='1', Loss='0.5' )
	self.addLink( Switch10, Switch5,Bandwidth='1000', delay='1', Loss='0.5' )
	self.addLink( Switch10, Switch11,Bandwidth='1000', delay='1', Loss='0.5' )
	self.addLink( Switch10, Switch7,Bandwidth='1000', delay='1', Loss='0.5' )
	self.addLink( Switch10, Switch4,Bandwidth='1000', delay='1', Loss='0.5' )
	self.addLink( Switch10, Switch9,Bandwidth='1000', delay='1', Loss='0.5' )

	self.addLink( Switch11, Switch6,Bandwidth='1000', delay='1', Loss='0.5' )
	self.addLink( Switch11, Switch5 ,Bandwidth='1000', delay='1', Loss='0.5')
	self.addLink( Switch11, Switch10,Bandwidth='1000', delay='1', Loss='0.5' )
	self.addLink( Switch11, Switch7,Bandwidth='1000', delay='1', Loss='0.5' )
	self.addLink( Switch11, Switch8 ,Bandwidth='1000', delay='1', Loss='0.5')
	


	


	
	
	
        
topos = { 'mytopo': ( lambda: MyTopo() ) } 
