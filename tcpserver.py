import socket
import threading
import argparse

def message(client, add, ress):
    alias = "Server"
    mess = input(alias + " : ")
    if mess != "":
        msg = alias + " : " + mess
        client.send(msg.encode())

def receive(client, add, ress):
    newmess = client.recv(8192)
    print(newmess.decode())

def startServer(portNumber):
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(("0.0.0.0", portNumber))
    server.listen(10)
    print("[!] Listening locally on port %d " %(portNumber))

    while True:
        client,address = server.accept()
        print("[+] Connected with the client: %s %d" %(address[0], address[1]))
        clientRequest = client.recv(4096)
        print("[!] Received data from the client (%s %d): %s" %(address[0], address[1], clientRequest))
        client.send(b"I am a server response, my version is 3.2.")

        thread_send = threading.Thread(target = message, args = (client, address[0], address[1]))
        thread_recv = threading.Thread(target = receive, args = (client, address[0], address[1]))

        thread_send.start()
        thread_recv.start()

        thread_recv.join()
        thread_send.join()


        server.close()

def main():
    parser = argparse.ArgumentParser("TCP SERVER")
    parser.add_argument("-p", "--port", type = int, help = "The port you wish to connect to", default = 4444)
    args = parser.parse_args()

    portNumber = args.port

    startServer(portNumber)

if __name__ == "__main__":
    main()
