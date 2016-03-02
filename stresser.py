#!/usr/bin/python

# Exploit Title: STRESSER DE LILLE
# Date: 02/03/2016
# Exploit Author: GSOIRES, NFIEVEZ, AVILLAIN 



print"  __  _____ ____  _____ ____ ___   ____  ____"
print"/ ___|_   _|  _ \| ____/ ___/ ___|| ____|  _ \ "
print"\___ \ | | | |_) |  _| \___ \___ \|  _| | |_) |"
print" ___) || | |  _ <| |___ ___) |__) | |___|  _ < "
print"|____/ |_| |_| \_\_____|____/____/|_____|_| \_"                 


from scapy.all import *
import logging
logging.getLogger("scapy.runtime").setLevel(logging.ERROR)
from time import sleep
import thread
import os
import signal
import sys