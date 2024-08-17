# Simple-TCP-Comm-with-Diffie-Hellman

## Sumário

- [Descrição](#descrição)
- [O que é Diffie-Hellman?](#o-que-é-diffie-hellman)
- [Processo de Comunicação](#processo-de-comunicação)
- [Funcionalidades](#funcionalidades)
- [Configuração](#configuração)
- [Uso](#uso)
- [Licença](#licença)

## Descrição

Este projeto demonstra um comunicação simples de cliente-servidor TCP com um mecanismo básico de criptografia. Ele utiliza o protocolo de **troca de valores Diffie-Hellman** para estabelecer um segredo compartilhado entre o cliente e o servidor. Este segredo compartilhado é então usado para cifrar e decifrar mensagens utilizando a cifra de César.

- O cliente se conecta ao servidor, troca valores e envia uma mensagem criptografada.
- O servidor descriptografa a mensagem utilizando o segredo compartilhado.

## O que é Diffie-Hellman?

A **troca de valores Diffie-Hellman** é um método utilizado para gerar um segredo compartilhado de forma segura através de um canal de comunicação público. Esse protocolo permite que duas partes, mesmo em uma rede pública, compartilhem um valor secreto que pode ser usado para criptografar e descriptografar mensagens, sem a necessidade de transmitir o segredo em si pela rede.

O processo funciona da seguinte forma:
1. Tanto o cliente quanto o servidor concordam com um valor base (`g`) e um módulo (`p`), conhecidos como valores públicos.
2. Cada parte gera um valor privado secreto (`a` para o cliente e `b` para o servidor).
3. O cliente calcula `A = g^a mod p` e envia ao servidor, enquanto o servidor calcula `B = g^b mod p` e envia ao cliente.
4. O cliente então calcula o valor compartilhado `S = B^a mod p`, e o servidor calcula `S = A^b mod p`.
5. Ambas as partes agora possuem o mesmo segredo compartilhado `S`, que pode ser usado para criptografar e descriptografar mensagens.

A vantagem desse sistema está no fato de que, embora os valores `A` e `B` sejam transmitidos pela rede, os valores privados nunca são expostos, e o segredo compartilhado não pode ser facilmente deduzido por um interceptador.

## Processo de Comunicação

1. **Conexão Inicial**: 
   - O servidor inicia e espera por uma conexão em uma porta específica.
   - O cliente se conecta ao servidor.

2. **Troca de Valores**: 
   - O cliente e o servidor utilizam a troca de valores Diffie-Hellman para estabelecer um segredo compartilhado (`ka`).
   - Esse segredo compartilhado será utilizado para criptografar e descriptografar as mensagens.

3. **Criptografia da Mensagem**:
   - Após a troca de valores, o cliente criptografa uma mensagem secreta utilizando a cifra de César. A cifra de César desloca cada letra da mensagem por um número de posições no alfabeto com base no valor compartilhado (`ka`).

4. **Transmissão da Mensagem**:
   - O cliente envia a mensagem criptografada para o servidor.

5. **Descriptografia da Mensagem**:
   - O servidor recebe a mensagem criptografada e a descriptografa utilizando o valor compartilhado.
   - A mensagem descriptografada é então exibida no lado do servidor.

6. **Repetir ou Encerrar**:
   - O cliente decide se deseja enviar outra mensagem ou encerrar a conexão através do terminal.

## Funcionalidades

- **Troca de Valores**: O cliente e o servidor calculam e trocam valores utilizando o protocolo Diffie-Hellman para o estabelecimento de uma chave comum sem que esta seja passada pela rede.
- **Geração de Segredo Compartilhado**: Um segredo compartilhado é calculado em ambos os lados.
- **Criptografia com Cifra de César**: O cliente criptografa as mensagens utilizando o segredo compartilhado, e o servidor as descriptografa com o mesmo valor.
- **Protocolo de Comunicação**: Comunicação segura via sockets TCP.

## Configuração

### Requisitos

- Python 3.x
- Módulo de programação com sockets (já incluído na biblioteca padrão do Python)

### Instruções

1. Clone o repositório ou faça o download dos arquivos `tcp_client_secure.py` e `tcp_server_secure.py`.

2. Execute o servidor:
   ```bash
   python3 tcp_server_secure.py
   ```

3. Em outro terminal, execute o cliente:
   ```bash
   python3 tcp_client_secure.py
   ```

## Uso

1. **Execute o servidor**:
   - O servidor ficará escutando por conexões do cliente e irá lidar com a troca de valores e a comunicação criptografada.
   - Ele descriptografará e exibirá as mensagens recebidas.

2. **Execute o cliente**:
   - O cliente se conectará ao servidor e realizará a troca de valores Diffie-Hellman para calcular o segredo compartilhado.
   - O cliente solicitará ao usuário que insira uma mensagem, criptografará a mensagem usando o valor compartilhado e enviará ao servidor.

3. **Continuar ou Sair**:
   - Após enviar uma mensagem, o cliente pode optar por continuar enviando mensagens ou encerrar a conexão enviando o comando 's'(sim) ou 'n'(não).
