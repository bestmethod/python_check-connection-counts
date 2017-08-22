# python_check-connection-counts
Check connection counts (unique) for a given port

Usage:
```
$ python checkconn.py [port_no]
port_no default: 3001
```

Example:
```
$ python checkconn.py 443

Counting unique established connections for port 443

Source IP	Destination IP	Connection Count
10.0.2.15	192.124.249.9 	1               
10.0.2.15	216.58.206.40 	1               
10.0.2.15	192.229.233.25	1               
10.0.2.15	31.13.90.36   	1               
10.0.2.15	216.58.206.68 	1               
10.0.2.15	216.58.208.142	2               
10.0.2.15	104.16.20.35  	1               
10.0.2.15	216.58.204.66 	2               
10.0.2.15	31.13.90.6    	1               
10.0.2.15	104.16.25.235 	1               
10.0.2.15	216.58.208.138	1               
10.0.2.15	192.0.77.48   	1               
10.0.2.15	216.58.208.129	1               
10.0.2.15	216.58.208.131	2               
```
