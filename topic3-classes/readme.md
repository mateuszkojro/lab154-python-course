# Sources for today

1. Python classes: <https://www.w3schools.com/python/python_classes.asp>
2. Python inheritance: <https://www.w3schools.com/python/python_inheritance.asp>

# Execercise

Convert the the game from topic2 to the object oriented style e.g:

```python

game = TicTackToe('X', 'O')

while !game.check_winner():
    print(game)
    x = input()
    y = input()
    game.set(x,y)

print("Game ended, player:" + game.winner()+ " won")
```