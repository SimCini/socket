import socket
import json

SERVER_IP = "127.0.0.1"
SERVER_PORT = 5005
BUFFER_SIZE = 1024

# Create a UDP socket
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind((SERVER_IP, SERVER_PORT))
print(f"Server {SERVER_IP} ascolta su: {SERVER_PORT}...")

while True:
    try:
        data, addr = s.recvfrom(BUFFER_SIZE)

        data = data.decode("UTF-8")
        richiesta = json.loads(data)

        primoNumero = richiesta["primoNumero"]
        operazione = richiesta["operazione"]
        secondoNumero = richiesta["secondoNumero"]

        print(f"ricevuta richiesta da {addr}: {primoNumero} {operazione} {secondoNumero}")

        risultato = None
        if operazione == '+':
            risultato = primoNumero + secondoNumero
        elif operazione == '-':
            risultato = primoNumero - secondoNumero
        elif operazione == '*':
            risultato = primoNumero * secondoNumero
        elif operazione == '/':
            if secondoNumero != 0:
                risultato = primoNumero / secondoNumero
            else:
                risultato = "Errore: Divisione per zero"
        else:
            risultato = "Errore: operazione non valida"

        risposta = {"risultato": risultato}
        risposta_json = json.dumps(risposta)

        s.sendto(risposta_json.encode("UTF-8"), addr)
        print(f"invio risultati a {addr}: {risultato}")

    except Exception as e:
        print(f"{e}")