def shifttext(text, shift):
    data = list(text)
    for i, char in enumerate(data):
        print(i, char)
        data[i] = chr((ord(char) + shift))
    output = ''.join(data)
    return output

from socket import *
serverPort = 1300
serverSocket = socket(AF_INET,SOCK_STREAM)
serverSocket.bind(("",serverPort))
serverSocket.listen(5) # o argumento “listen” diz à biblioteca de soquetes que queremos enfileirar no máximo 5 requisições de conexão (normalmente o máximo) antes de recusar começar a recusar conexões externas. Caso o resto do código esteja escrito corretamente, isso deverá ser o suficiente.
print ("TCP Server\n")

M_publicKeyOne = 11
A_publicKey = 43
M_privateKey = 4

computedPublicValues = pow (A_publicKey, M_privateKey) % M_publicKeyOne

while True:

    connectionSocket, addr = serverSocket.accept()
    A_chavePublicaComputada = connectionSocket.recv(65000)

    print('Enviando minha chave pública computada: ', computedPublicValues)
    connectionSocket.send(bytes(str(computedPublicValues), 'utf-8'))

    x = pow (int(A_chavePublicaComputada), M_privateKey) % M_publicKeyOne
    #received = str(sentence,"utf-8")

    print ("Received From Client: ", str(A_chavePublicaComputada, 'utf-8'))


    print ("Chave simétrica: ", x)

    #Fazendo cifra de César
    receivedText = connectionSocket.recv(65000)
    decriptedText = shifttext(str(receivedText.decode('utf-8')), -x)

    print('Texto descriptografado: ', decriptedText)

    receivedMessage = connectionSocket.recv(65000)
    print('Aguardando comando supremo...')

    connectionSocket.close()
    print(receivedMessage.decode('utf-8'))

    
    if str(receivedMessage.decode('utf-8')) == 'CLOSE_CONNECTION':
        break