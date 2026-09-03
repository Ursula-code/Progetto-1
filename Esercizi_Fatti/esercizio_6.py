# Esercizio 6 
# Autore: Sechi Ursula 
# Data: 30/04/2026


import json
import os


# Una 'classe' è come uno schema o un progetto per creare oggetti.
class Rubrica:              #La classe Rubrica gestisce le informazioni sui contatti (dizionario)

# INIZIALIZZAZIONE DEL DIZIONARIO 
    def __init__(self, dati_rubrica=None):
        """
        Il metodo __init__ viene eseguito automaticamente quando creiamo un oggetto Rubrica.
        - 'self' rappresenta l'oggetto stesso che stiamo creando.
        - 'dati_rubrica' è il dizionario contenente i contatti. Se non viene fornito,
          viene impostato a None (cioè 'nessun valore').
        """
        # Se viene passato un dizionario, usiamo quello; altrimenti la rubrica parte 'vuota' (None).
        if dati_rubrica is not None:
            self.contatti = dati_rubrica
        else:
            self.contatti = None

    @classmethod                        #serve per inizializzare da file JSON o Testo 
    def da_json(cls, percorso_file):

        """
        Un @classmethod è un metodo speciale che lavora sulla classe intera 'cls'
        invece che sul singolo oggetto 'self'. Serve qui come 'costruttore alternativo'.
        Legge un file JSON e crea direttamente un oggetto Rubrica con quei dati.
        """

        # Verifichiamo se il file esiste sul computer
        if not os.path.exists(percorso_file):
            print(f"Errore: Il file '{percorso_file}' non esiste.")
            return cls(None)

        # Apriamo il file JSON in modalità lettura ('r' = read)
        with open(percorso_file, 'r', encoding='utf-8') as file:                    #encoding='utf-8' indica a python con quale "dizionario di codifica" deve tradurre i bite salvati sul disco fisso in lettere e caratteri  
            # json.load prende il testo JSON dal file e lo trasforma in un dizionario Python
            dati = json.load(file)

        # Restituisce una nuova istanza della classe Rubrica popolata con i dati letti
        return cls(dati)

    @classmethod
    def da_testo(cls, percorso_file):
        
        """
        Legge un file di testo (formato txt) dove ogni riga rappresenta un contatto.
        Formato atteso: Nome;giorno;mese;anno;età;sesso;mail
        """

        if not os.path.exists(percorso_file):
            print(f"Errore: Il file '{percorso_file}' non esiste.")
            return cls(None)

        dati = {}
        with open(percorso_file, 'r', encoding='utf-8') as file:
            for riga in file:
                # .strip() rimuove gli spazi vuoti e i caratteri di a capo '\n' a fine riga
                riga_pulita = riga.strip()
                if not riga_pulita:
                    continue  # Salta le righe vuote

                # .split(';') divide la stringa ogni volta che trova un punto e virgola ';'
                parti = riga_pulita.split(';')
                
                # Ci assicuriamo che la riga contenga tutti e 7 i campi necessari
                if len(parti) == 7:
                    nome, giorno, mese, anno, eta, sesso, mail = parti
                    dati[nome] = {
                        'giorno': int(giorno),
                        'mese': mese,
                        'anno': int(anno),
                        'età': int(eta),
                        'sesso': sesso,
                        'mail': mail
                    }

        return cls(dati)

# AZIONE APRI 
    def apri(self, percorso_file):
        
        """
        Apre un file esistente (JSON o Testo) e carica i contatti nell'oggetto corrente.
        L'estensione del file (.json o .txt) determina come verrà letto.
        """

        # Controlliamo l'estensione del file trasformandola in minuscolo
        if percorso_file.endswith('.json'):
            # Usiamo il metodo da_json creato in precedenza
            nuova_rubrica = Rubrica.da_json(percorso_file)
            self.contatti = nuova_rubrica.contatti
        elif percorso_file.endswith('.txt'):
            # Usiamo il metodo da_testo creato in precedenza
            nuova_rubrica = Rubrica.da_testo(percorso_file)
            self.contatti = nuova_rubrica.contatti
        else:
            print("Formato non supportato! Usa un file .json o .txt")

#AZIONE AGGIUNGI 
    # Requisito: Prima bisogna aver aperto una rubrica, altrimenti errore "Prima apri una rubrica"
    def aggiungi(self, nome, giorno, mese, anno, eta, sesso, mail):
        
        """
        Aggiunge un nuovo contatto al dizionario della rubrica.
        """

        # la rubrica deve essere stata inizializzata/aperta
        if self.contatti is None:
            print("Prima apri una rubrica")
            return

        # Aggiungiamo o aggiorniamo la chiave 'nome' nel dizionario dei contatti
        self.contatti[nome] = {
            'giorno': giorno,
            'mese': mese,
            'anno': anno,
            'età': eta,
            'sesso': sesso,
            'mail': mail
        }
        print(f"Contatto '{nome}' aggiunto con successo.")

# AZIONE RIMUOVI 
    #Deve esserci almeno un elemento (altrimenti "La rubrica è vuota").
        #Se l'elemento non esiste allora "Il contatto NOME non esiste in rubrica"
    def rimuovi(self, nome):

        """
        Rimuove un contatto cercando il suo nome all'interno della rubrica.
        """

        # Controllo vincolo: rubrica non aperta o vuota
        if self.contatti is None or len(self.contatti) == 0:
            print("La rubrica è vuota")
            return

        # verifica se il nome esiste tra le chiavi del dizionario
        if nome not in self.contatti:
            print(f"Il contatto {nome} non esiste in rubrica")
            return

        # del   è un comando che rimuove una chiave e il relativo valore da un dizionario
        del self.contatti[nome]
        print(f"Contatto '{nome}' rimosso con successo.")

# AZIONE SALVA
    # La rubrica non deve essere vuota 
    def salva(self, percorso_file):

        """
        Salva i dati della rubrica in un file .json o .txt basandosi sull'estensione.
        """

        # Controllo se la rubrica non è stata aperta aperta oppure se è vuota
        if self.contatti is None or len(self.contatti) == 0:
            print("La rubrica è vuota")
            return

        if percorso_file.endswith('.json'):
            # json.dump scrive il dizionario Python nel file in formato JSON
            # indent=4 serve per formattare il testo rendendolo ben leggibile
            with open(percorso_file, 'w', encoding='utf-8') as file:
                json.dump(self.contatti, file, indent=4, ensure_ascii=False)
            print(f"Rubrica salvata con successo in '{percorso_file}'.")

        elif percorso_file.endswith('.txt'):
            # Scriviamo un file di testo salvando ogni contatto su una riga separata
            with open(percorso_file, 'w', encoding='utf-8') as file:
                for nome, info in self.contatti.items():
                    riga = f"{nome};{info['giorno']};{info['mese']};{info['anno']};{info['età']};{info['sesso']};{info['mail']}\n"
                    file.write(riga)
            print(f"Rubrica salvata con successo in '{percorso_file}'.")

        else:
            print("Formato non supportato! Usa un file .json o .txt")

# AZIONE STAMPA 
    #Deve esserci almeno un elemento in rubrica
    # Formattazione come nell'Esercizio 3
    def stampa(self, nome):

        """
        Stampa le informazioni dettagliate di un contatto.
        """

        # Controllo se la rubrica è vuota
        if self.contatti is None or len(self.contatti) == 0:
            print("La rubrica è vuota")
            return

        # Controllo se il contatto è in rubrica 
        if nome not in self.contatti:
            print(f"Il contatto {nome} non esiste in rubrica")
            return

        # Recuperiamo i dati del contatto
        info = self.contatti[nome]

        # Costruiamo e stampiamo la stringa formattata richiesta nell'Esercizio 3
        stampa_formattata = (
            f"'{nome}', 'giorno' {info['giorno']}, 'mese' '{info['mese']}', "
            f"'anno' {info['anno']}, 'età' {info['età']}, 'sesso' '{info['sesso']}', "
            f"'mail' '{info['mail']}'"
        )
        print(stampa_formattata)