# Unimibex
one-click UniMiB Webex link opener

### Installazione
É necessario solo scaricare il programma dal seguente link (valido per 1° anno Informatica T2): [Scarica](https://github.com/BrockDeveloper/unimibex/releases/download/v1.0/unimibex.exe)  
***Importante:*** Windows presenterà il programma come pericoloso, per ignorare il warning ed eseguirlo cliccare _Ulteriori Informazioni_ e poi _Esegui Comunque_.

### Funzionalità e Utilizzo
Apertura automatica dei link dei meet Webex UniMiB.  
Con un doppio click il link della lezione viene aperto in modo automatico. La lezione aperta sarà quella corrispondente all'ora in cui viene effettuata la richiesta.

### Sezione Development
***Struttura:*** i link sono ottenuti da un file Json condiviso online, è necessario configurarne uno per poter usare il programma. Una volta configurato e compilato, l'eseguibile potrà essere usato da chiunque necessiti di quei link (e.g. quello distribuito da questa pagina apre i link del Primo Anno di Informatica T2).  
  
***Configurazione:*** per configurare i file in modo da ottenere un eseguibile collegato ai propri link (eventualmente distribuibile):  
1. Prerequisiti: Python 3
2. Installare tutte le dipendenze necessarie con "pip install -r requirements.pip"
3. Scrivere un json blob (https://jsonblob.com/) seguendo l'esempio del file json_example.json e salvarlo. Conserva il link, sarà necessario ogni qual volta ci sia la necessità di modificare il file
4. Aggiungere al link SHARED_DATA nel file unimibex.py l'id del file (serie di numeri alla fine del link copiato al punto precedente)
5. Generare una chiave di crittografia con lo script crypto/generate.py
6. Copiare la chiave generata in KEY nel file unimibex.py
7. Ora è possibile generare l'eseguibile con il comando da cmd "pyinstaller --one-file unimibex.py"
8. I link salvati nel json blob sono esposti pubblicamente, usare lo script crypto/crypto.py per generarli crittografati e inserirli nel file json.
