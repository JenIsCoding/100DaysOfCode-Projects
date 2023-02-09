treasure = (r"""right
                 _.--.
                        _.-'_:-'||
                    _.-'_.-::::'||
               _.-:'_.-::::::'  ||
             .'`-.-:::::::'     ||
            /.'`;|:::::::'      ||_
           ||   ||::::::'     _.;._'-._
           ||   ||:::::'  _.-!oo @.!-._'-.
           \'.  ||:::::.-!()oo @!()@.-'_.|
            '.'-;|:.-'.&$@.& ()$%-'o.'\U||
              `>'-.!@%()@'@_%-'_.-o _.|'||
               ||-._'-.@.-'_.-' _.-o  |'||
               ||=[ '-._.-\U/.-'    o |'||
               || '-.]=|| |'|      o  |'||
               ||      || |'|        _| ';
               ||      || |'|    _.-'_.-'
               |'-._   || |'|_.-'_.-'
            jgs '-._'-.|| |' `_.-'
                    '-.||_/.-'
                    
""")

print("Benvenuto nell\'Isola del Tesoro!")
print("Ti è stata affidata una missione delicata: trovare il tesoro!")

direction = input("Decidi di esplorare l\'isola su cui sei atterrato. Dove vuoi andare? Digita \"destra\" or \"sinistra\" ")
if direction == "destra":
  print("Nooooo, sei caduto nelle sabbie mobili :(!!! Il gioco finisce qui. Game over.")
  
else:
  todo = input("L'esplorazione dell\'isola sta continuando a ritmo incessante. Ti trovi davanti ad un laghetto: vuoi immergerti o preferisci continuare a camminare? Digita \"nuotare\" or \"camminare\" ")
  if todo == "nuotare":
    print("Noooooo!! Si trattava di un laghetto avvelenato dalle alghe assassine! Putroppo il tuo gioco finisce qui. Game over.")
  else:
    color = input("Finalmente, dopo tanta natura selvaggia, ti appare un enorme edificio con tre curiose porte colorate in rosso, blu e giallo rispettivamente.\nDecidi di entrare: potrebbe essere l'occasione parlare con qualcuno.\nQuale colore scegli? Digita \"blu\", \"rosso\" or \"giallo\" ")
    if color == "blu" or color == "rosso":
      print("Nooooooooooo! Sei enrtato nella porta dell\'orco! Ti ha mangiato. Il tuo gioco si è concluso. Game over.")
    else:
      print("Hai vinto!")
      print("Hai trovato il tesoro! Sei un campione!!!!!!!!!!!!!!!!!!")
      print(treasure)