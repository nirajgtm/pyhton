# def display_board(board):
import sys
a=['   ','   ','   ','   ','   ','   ','   ','   ','   ', '   ']
def display_board():
  print ('  |   |   |   |')
  print ("  |{}|{}|{}|".format(a[1],a[2], a[3]))
  print ('-----------------')
  print ('  |   |   |   |')
  print ("  |{}|{}|{}|".format(a[4],a[5], a[6]))
  print ('-----------------')
  print ('  |   |   |   |')
  print ("  |{}|{}|{}|".format(a[7],a[8], a[9]))

player1=input('Please enter symbol for Player 1 : X or O').upper()
if player1 !='O' and player1 != 'X':
  while True:
    player1= input('You did not enter valid option, Please enter X or O \n or you can Press Q to quit the game').upper()
    if (player1 =='O' or player1 == 'X' or player1 == 'Q'):
      break
if player1== 'Q':
  sys.exit()  
if player1== 'X':
  player2= 'O'
elif player1== 'O':
  player2= 'X'
print('Player 1 goes First')
display_board()
def moves():
  notused= [1,2,3,4,5,6,7,8,9]
  for move in range(1,10):
    if move %2 == 0:
        turn='2'
    else:
      turn='1'
    place= int(input("Player{}:".format(turn)))
    while place not in range (1,10):
      print('invalid input')
      place= int(input("Player{}:".format(turn)))
    while place not in notused:
      print('The place is already taken , please chhose another')
      place= int(input("Player{}:".format(turn)))
    if move %2 == 0:
      a[place]= ' ' + player2 + ' '
    else:
      a[place]= ' ' + player1 + ' '
    if place in notused:
      notused[place-1]= ''
    display_board()
    if a[1]==a[2]==a[3]!='   ' or a[1]==a[5]==a[9]!='   ' or a[3]==a[9]==a[7]!='   ' or a[2]==a[5]==a[8]!='   ' or a[3]==a[6]==a[9]!='   ' or a[3]==a[5]==a[7]!='   ' or a[4]==a[5]==a[6]!='   ' or a[7]==a[8]==a[9]!='   ' :
      print ('Player {} won the game! Congratulations.'.format(turn))
      sys.exit()
    
moves()
display_board()

    
    