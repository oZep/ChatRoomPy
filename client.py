import threading
import socket

alias = input('Choose an alias >>>')
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client.connect(('127.0.0.1', 6789))

def client_recieve():
    '''
    recieve messages from the server
    '''
    while True:
        try:
            message = client.recv(1024).decode('utf-8')
            if message == 'alias?':
                client.send(alias.encode('utf-8'))
            else:
                print(message) # print the message that is sent from the server
        except:
            print("Error")
            client.close()
            break

def client_send():
    '''
    send messages to the server
    '''
    while True:
        message = f'{alias}: {input("")}'
        client.send(message.endcode('utf-8'))

# make threads for receiving and sending
receive_thread = threading.Thread(target=client_recieve)
receive_thread.start()
send_thread = threading.Thread(target=client_send)
send_thread.start()