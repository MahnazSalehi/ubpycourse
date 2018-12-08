import sys
import os

tempwheel = []
for i in sys.argv[1:]:
	tempwheel.append(i)
for part in tempwheel:
    os.system("potrace -b svg -b pdf {0} -o {1}.pdf".format(part,part[:-4]))
    
#replace wheel temp pic and get path and run
