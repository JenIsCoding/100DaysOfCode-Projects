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

print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")

direction = input("Where do you want to go? Type \"left\" or \"right\" ")
if direction == "right":
  print("Game over.")
  
else:
  todo = input("Do you feel like going for a swim or would you rather wait? Type \"swim\" or \"wait\" ")
  if todo == "swim":
    print("Game over.")
  else:
    color = input("While waiting, you see three doors in front of you. Which color do you choose? Type \"blue\", \"red\" or \"yellow\" ")
    if color == "blue" or color == "red":
      print("Game over.")
    else:
      print("You win!")
      print("You have found the treasure!")
      print(treasure)