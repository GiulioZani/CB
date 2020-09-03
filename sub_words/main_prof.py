# subWords.py
from sys import argv, exit

def main() :
   if len(argv) != 3 :
      exit("Specificare il nome del file e la parola da cercare")
   word = argv[2]
   if not word.isalpha() :
      exit("La parola deve contenere soltanto lettere")
   word = word.lower()
   filename = argv[1]
   isURL1 = "http://"
   isURL2 = "https://"
   if filename.startswith(isURL1) or filename.startswith(isURL2) :
      from urllib.request import urlopen
      webPage = urlopen(filename)
      text = str(webPage.read(), "utf-8")
      webPage.close()
   else :
      f = open(filename, "r")
      text = f.read()
      f.close()
   text = text.lower()
   from re import split
   words = split("[^a-z]+", text) # ci sono solo minuscole...
   # creo un dizionario di insiemi, usando come chiavi le lettere presenti
   # in word e come valori i sottoinsiemi di words che contengono la chiave
   d = dict()
   for w in words :
      for c in w:
         d[c] = d.get(c, set())
         d[c].add(w)

   foundWords = d.get(word[0], set()) # insieme di parole che contengono il primo carattere
   for c in word[1:]: # tutti i caratteri di word tranne il primo
      justFound = d.get(c, set()) # insieme di parole che contengono il carattere c
      foundWords = foundWords.intersection(justFound)

   for w in sorted(foundWords) :
      print(w)

main()

