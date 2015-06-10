import glob
import os
import time

os.chdir("/home/pjh7/Dropbox/print")
f = open('active')

activestr = f.read(1);

if activestr == '1':

    pdfs = glob.glob("*.pdf")

    while len(pdfs)>0:
        activefile = pdfs[0]
        pdfs = pdfs[1:len(pdfs)]
        print "printing " + activefile
        newfile = "printing_" + activefile
        rencmd = "mv \"" + activefile + "\" \"" + newfile + "\""
        os.system(rencmd)
        time.sleep(1)
        printcmd = "lpr -P xerox-d \"" + newfile + "\""
        os.system(printcmd)
        mvcmd = "mv \"" + newfile + "\" completed/\"" + activefile + "\""
        os.system(mvcmd)
