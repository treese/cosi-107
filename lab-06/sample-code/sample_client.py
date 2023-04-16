# Simple network client demo code. Borrowed from
# https://www.digitalocean.com/community/tutorials/python-socket-programming-server-client
#
# To use: start the server in a terminal window:
#    python3 sample_server.py
# In a separate terminal window, start the client:
#    python3 sample_client.py

# This program prompts for a line of text to send the server, then
# waits for a response. The corresponding sample server prints the
# text and prompts itself for a response, which it then sends back to
# the client. It prints the response, then prompts for another string.
# If the user types the word "bye", the program quits.

import socket

def client_program():
    host = socket.gethostname()  # as both code is running on same pc
    port = 5001  # socket server port number

    client_socket = socket.socket()  # instantiate
    client_socket.connect((host, port))  # connect to the server

    message = input(" -> ")  # take input

    while message.lower().strip() != 'bye':
        client_socket.send(message.encode())  # send message
        data = client_socket.recv(1024).decode()  # receive response

        print('Received from server: ' + data)  # show in terminal

        message = input(" -> ")  # again take input

    client_socket.close()  # close the connection


if __name__ == '__main__':
    client_program()
