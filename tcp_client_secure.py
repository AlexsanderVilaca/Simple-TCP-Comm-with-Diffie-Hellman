from socket import *
serverName = "10.1.70.23"
serverPort = 1300

def shifttext(text, shift):
    data = list(text)
    for i, char in enumerate(data):
        print(i, char)
        data[i] = chr((ord(char) + shift))
        print(i, data[i], '\n')
    output = ''.join(data)
    return output

#chaves
A_public_key = 43
A_private_key = 4
M_public_key = 23

while True:
    #computando chave pública computada
    computed_public_values = pow(A_public_key, A_private_key) % M_public_key

    clientSocket = socket(AF_INET, SOCK_STREAM) 
    clientSocket.connect((serverName,serverPort))
    print("Enviando chave pública computada", computed_public_values)
    clientSocket.send(bytes(str(computed_public_values), 'utf-8'))

    M_chave_publica_computada = clientSocket.recv(65000)
    # print("M chave pubvlica:", int(M_chave_publica))
    converted_M_public_key = int(M_chave_publica_computada)
    print("Chave pública computada do Marcus é: ", converted_M_public_key)

    ka = pow(converted_M_public_key, A_private_key) % M_public_key
    print("Chave simétrica: ", ka)

    #fazendo a cifra de César
    message_to_send = input("Soldado! Precisamos que você envie a mensagem secreta (ou o mundo vai acabar): ")
    message_to_send = shifttext(message_to_send, ka)

    #enviando a mensagem
    print("Endendidido soldado, a mensagem cifrada é: ", message_to_send)
    clientSocket.send(bytes(message_to_send, 'utf-8'))

    desejo_supremo = input("Soldado, deseja continuar? (s/n)")
    if desejo_supremo.lower() != 's':
        clientSocket.send(bytes("CLOSE_CONNECTION", 'utf-8'))
        clientSocket.close()
        break