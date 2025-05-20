import socket
import json

SERVER_IP = "127.0.0.1"
SERVER_PORT = 5005
BUFFER_SIZE = 1024

# Create a UDP socket
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

while True:
    try:
        primoNumero = float(input("Inserisci il primo numero: "))
        operazione = input("Inserisci l'operazione (+, -, *, /): ")
        secondoNumero = float(input("Inserisci il secondo numero: "))

        message = {
            "primoNumero": primoNumero,
            "operazione": operazione,
            "secondoNumero": secondoNumero
        }

        json_message = json.dumps(message)
        s.sendto(json_message.encode("UTF-8"), (SERVER_IP, SERVER_PORT))

        # Receive the response from the server
        data, addr = s.recvfrom(BUFFER_SIZE)

        # Decode bytes to string, then load JSON
        risposta_json = data.decode("UTF-8")
        risposta = json.loads(risposta_json)

        print(f"Risultati ricevuti da {addr}: {risposta['risultato']}")

    except Exception as e:
        print(f"Errore: {e}")

    controllo = input("vuoi fare un altra operazione? (si/no): ")
    if controllo != 'si':
        break
s.close()