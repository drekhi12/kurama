import os
a=os.system("ping www.google.com")
if  a==0:
    print "The site's up"
else:
    print "The site's not up"
