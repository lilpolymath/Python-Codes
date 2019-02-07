import argparse
import time
from socket import *
import threading

def message(server):
    mess = input(alias + " : ")
    if mess != "":
        msg = alias + " : " + mess
        server.send(msg.encode())

def receive(server):
    newmess = server.recv(8192)
    print(newmess.decode())

def connscan(tgtHost, tgtPort):
    try:
        server = socket(AF_INET, SOCK_STREAM)
        server.connect((tgtHost, tgtPort))
        print("[+] {} TCP open".format(tgtPort))
        print("[!] Connection to Server was successfully.")
        time.sleep(2)
        # print("[!] Sending Welcome message to server.")
        # time.sleep(2)
        global alias
        alias = input("[+] Enter your preferred name: ")

        server.send(b"Hello there this is a client server comms.")
        server_resp = server.recv(8192)
        print("[!] Recieving message.")
        time.sleep(2)
        print("[+] Server Response : {}".format(server_resp))
        print("*[!] **************************************\n")

        thread_send = threading.Thread(target = message, args = (server, ))
        thread_recv = threading.Thread(target = receive, args = (server, ))

        thread_recv.start()
        thread_send.start()

        thread_send.join()
        thread_recv.join()

        server.close()

    except:
        print("[+] {} TCP closed.".format(tgtPort))
        server.close()

def scan(tgtHost, tgtPorts):
    try:
        tgtIP = gethostbyname(tgtHost)
    except:
        print("[-] Error: Unknown Host.")
        exit(0)

    try:
        tgtName = gethostbyaddr(tgtIP)
        print("[+] --- Scan result for: " + tgtName[0] + " ---")
    except:
        print("[+] --- Scan result for: " + tgtIP + " ---")

    setdefaulttimeout(100)

    #connscan(tgtHost, int(tgtPorts))
    for tgtPort in tgtPorts:
        connscan(tgtHost, int(tgtPort))

def main():
    parser = argparse.ArgumentParser("Smart TCP Client to Server Connection.")
    parser.add_argument("-a", "--address", type = str, help = "The Target IP Address", default = "localhost")
    parser.add_argument("-p", "--port", type = str, help = "The Port(s) number to connect to")
    args = parser.parse_args()

    ipaddress =  args.address
    port = args.port.split(",")

    scan(ipaddress, port)

if __name__ == "__main__":
    main()
