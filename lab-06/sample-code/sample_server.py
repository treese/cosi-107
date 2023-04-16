# Simple network server demo code. Borrowed from
# https://www.digitalocean.com/community/tutorials/python-socket-programming-server-client
#
# To use: start the server in a terminal window:
#    python3 sample_server.py
# In a separate terminal window, start the client:
#    python3 sample_client.py
#
# This program listens on a network port (usually 5001, shown below).
# When it receives a line of text from a client, it prints the message
# and prompts for a message to send back to the client. It runs until
# terminated with ^C.

import socket


def server_program():
    # get the hostname
    host = socket.gethostname()
    port = 5001  # initiate port no above 1024

    server_socket = socket.socket()  # get instance
    # look closely. The bind() function takes tuple as argument
    server_socket.bind((host, port))  # bind host address and port together

    # configure how many client the server can listen simultaneously
    server_socket.listen(2)
    conn, address = server_socket.accept()  # accept new connection
    print("Connection from: " + str(address))
    while True:
        # receive data stream. it won't accept data packet greater than 1024 bytes
        data = conn.recv(1024).decode()
        if not data:
            # if data is not received break
            break
        print("from connected user: " + str(data))
        data = input(' -> ')
        conn.send(data.encode())  # send data to the client

    conn.close()  # close the connection


if __name__ == '__main__':
    server_program()
