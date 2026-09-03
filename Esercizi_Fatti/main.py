# Esercizio 6 - Punto 2
# Autore: Sechi Ursula 
# Data: 30/04/2026


# Importiamo la classe Rubrica dal file rubrica_module.py creato prima
from esercizio_6 import Rubrica

def esegui_programma():
    # Creiamo un'istanza della rubrica (inizialmente non aperta/vuota)
    rubrica = Rubrica()

    while True:
        # Chiediamo all'utente quale azione vuole svolgere
        azione = input("\nInserisci un'azione (APRI, AGGIUNGI, RIMUOVI, SALVA, STAMPA, EXIT): ").strip().upper()

        # Uscita dal programma
        if azione == "EXIT":
            print("Programma terminato.")
            break

        # Azione APRI
        elif azione == "APRI":
            nome_file = input("Inserisci il nome del file da aprire (es. rubrica.json o rubrica.txt): ")
            rubrica.apri(nome_file)

        # Azione AGGIUNGI
        elif azione == "AGGIUNGI":
            nome = input("Nome e Cognome: ")
            giorno = input("Giorno di nascita: ")
            mese = input("Mese di nascita: ")
            anno = input("Anno di nascita: ")
            eta = input("Età: ")
            sesso = input("Sesso (M/F): ")
            mail = input("Email: ")
            rubrica.aggiungi(nome, giorno, mese, anno, eta, sesso, mail)

        # Azione RIMUOVI
        elif azione == "RIMUOVI":
            nome = input("Inserisci il nome del contatto da rimuovere: ")
            rubrica.rimuovi(nome)

        # Azione SALVA
        elif azione == "SALVA":
            nome_file = input("Inserisci il nome con cui salvare il file (es. nuova_rubrica.json): ")
            rubrica.salva(nome_file)

        # Azione STAMPA
        elif azione == "STAMPA":
            nome = input("Inserisci il nome del contatto da stampare: ")
            rubrica.stampa(nome)

        # Se l'azione non esiste, il ciclo ricomincia e richiede l'input
        else:
            print("Azione non valida! Riprova.")

if __name__ == "__main__":
    esegui_programma()