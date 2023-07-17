# Topic 2 - Tick tack toe

## Exercise description

Write a program allowing for a 2 player game of tick tack toe, board should be
displayed in the console and the application should be able to determine 
if the game has ended and who was the winner (if there was one).

### Example game

This is just the suggestion you can change the design in any way you want.

Program startup screen:
```
Current board

   1 2 3
1 | | | |
2 | | | |
3 | | | |

It's 'X' turn, enter position:
```

followed by the player 1 input:
```
1
1
```
(this means that player enters `1` and presses `enter` two times)

output:
```
Current board

   1 2 3
1 |X| | |
2 | | | |
3 | | | |

It's 'O' turn, enter position:
```

and player 2 input:

```
2
1
```

output:
```
Current board

   1 2 3
1 |X|O| |
2 | | | |
3 | | | |

It's 'X' term, enter position:
```

After some time:

```
Current board

   1 2 3
1 |X|O| |
2 | |X| |
3 | |O| |

It's 'X' turn, enter position:
```

Player 2 input:
```
3
3
```

output:

```
Current board

   1 2 3
1 |X|O| |
2 | |X| |
3 | |O|X|

GAME OVER!
Player 'X' won!
```
