from servers import *
from servers import serverA, serverE

a = serverA.serverA()
e = serverE.serverE()

a.create_election('Election présidentielle', e)
e.send_pubkeys(a)
