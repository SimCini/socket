import socket

INDIRIZZO_IP = "127.0.0.1"
PORTA = 65432
DIMENSIONE_BUFFER = 1024

print(f"Server in ascolto su {INDIRIZZO_IP}:{PORTA}...")

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock_server:
    sock_server.bind((INDIRIZZO_IP, PORTA))
    sock_server.listen()

    while True:
        sock_servizio, indirizzo_client = sock_server.accept()
        with sock_servizio as sock_client:
            print(f"Connessione accettata da {indirizzo_client}")
            try:
                dati = sock_client.recv(DIMENSIONE_BUFFER).decode('utf-8')

                print(f"Ricevuto dal client {indirizzo_client}: '{dati}'")

                parti = dati.split() 
                if len(parti) == 3: #tre parti: numero1, operazione, numero2
                    try:
                        num1 = float(parti[0]) 
                        operazione = parti[1] 
                        num2 = float(parti[2]) 

                        risultato = None
                        if operazione == '+':
                            risultato = num1 + num2
                        elif operazione == '-':
                            risultato = num1 - num2
                        elif operazione == '*':
                            risultato = num1 * num2
                        elif operazione == '/':
                            if num2 != 0:
                                risultato = num1 / num2
                            else:
                                risultato = "Errore: Divisione per zero" 
                        else:
                            risultato = "Errore: Operazione non valida"

                    except ValueError:
                        risultato = "Errore: Formato numeri non valido" 
                else:
                    risultato = "Errore: Formato messaggio non valido"

                risposta = str(risultato).encode('utf-8')
                sock_client.sendall(risposta)
                print(f"Inviato risultato a {indirizzo_client}: '{risultato}'")

            except Exception as e:
                print(f"Errore durante la comunicazione con {indirizzo_client}: {e}")
                risposta_errore = f"Errore server: {e}".encode('utf-8')
                sock_client.sendall(risposta_errore)
        print(f"Connessione con {indirizzo_client} chiusa.")
