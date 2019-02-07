import http, sys
from optparse import OptionParser

usageString = "Usage: %prog [options] hostname"
parser = OptionParser(usage=usageString)
parser.add_option("-p", "--port", dest="port", metavar="PORT", default=80, type="int", help="Port to connect to")
(opts,args) = parser.parse_args()

if len(args) < 1:
        parser.error("Hostname is required")
        
host = args[0]

if len(sys.argv) < 3:
        sys.exit("Usage " + sys.argv[0] + "<hostname> <port> /n")

host = sys.argv[1]
port = sys.argv[2]

client = http.HTTPConnection(host, port)
client.request("GET" ,"/")
resp = client.getresponse()
client.close()

if resp.status == 200:
        print(host + " : OK")
        sys.exit

print(host + ": DOWN  (" + resp.status + " . " + resp.reason + ")")


