
#print [1,2], '\n', [3,4]
# CUPS' API
import sys
sys.path.insert(0,'../app/print')
from pkipplib import pkipplib

# Create a CUPS client instance 
# cups = pkipplib.CUPS(url="http://server:631, \
#                      username="john", \
#                      password="5.%!oyu")
cups = pkipplib.CUPS()

# High level API : retrieve info about job 3 :
answer = cups.getJobAttributes(3)
#print answer.job["document-format"]
# That's all folks !


# Lower level API :
request = cups.newRequest(pkipplib.IPP_GET_PRINTER_ATTRIBUTES)
request.operation["printer-uri"] = ("uri", 
                                    cups.identifierToURI("printers", "HP2100"))
for attribute in ("printer-uri-supported",                                     
                  "printer-type",
                  "member-uris") :
    # IMPORTANT : here, despite the unusual syntax, we append to              
    # the list of requested attributes :
    request.operation["requested-attributes"] = ("nameWithoutLanguage", attribute)
    
# Sends this request to the CUPS server    
answer = cups.doRequest(request)    

# Print the answer as a string of text
print answer