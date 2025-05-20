import socket

HOST = '127.0.0.1'  # Indirizzo IP del server
PORTA = 65432        # Porta usata dal server
DIMENSIONE_BUFFER = 1024

while True: # Ciclo infinito per permettere più calcoli
    try:
        # Richiedi all'utente i numeri e l'operazione
        primo_numero = float(input("Inserisci il primo numero: "))
        operazione = input("Inserisci l'operazione (+, -, *, /): ")
        secondo_numero = float(input("Inserisci il secondo numero: "))

        # Costruisci il messaggio da inviare al server
        messaggio = f"{primo_numero} {operazione} {secondo_numero}"

        # Creazione della socket del client usando il costrutto 'with'
        # Questo assicura che la socket venga chiusa automaticamente una volta usciti dal blocco 'with'
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock_servizio:
            # Connettiti al server
            sock_servizio.connect((HOST, PORTA))
            print(f"Connesso al server {HOST}:{PORTA}")

            # Invia il messaggio al server, codificato in byte (UTF-8)
            sock_servizio.sendall(messaggio.encode('utf-8'))
            print(f"Inviato al server: '{messaggio}'")

            # Ricevi la risposta dal server
            dati = sock_servizio.recv(DIMENSIONE_BUFFER)

            # Decodifica i byte ricevuti in una stringa e stampa il risultato
            print('Risultato ricevuto:', dati.decode('utf-8'))

        # A questo punto, sock_servizio viene automaticamente chiusa

    except ValueError:
        print("Input non valido. Assicurati di inserire numeri validi.")
    except ConnectionRefusedError:
        print(f"Errore: Connessione rifiutata. Assicurati che il server sia in esecuzione su {HOST}:{PORTA}.")
    except Exception as e:
        print(f"Si è verificato un errore inatteso: {e}")

    # Chiedi all'utente se desidera eseguire un'altra operazione
    altra_operazione = input("\nVuoi eseguire un'altra operazione? (sì/no): ").lower()
    if altra_operazione != 'sì' and altra_operazione != 'si':
        break # Esce dal ciclo se l'utente non vuole continuare

print("Client chiuso.")