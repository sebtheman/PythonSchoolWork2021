#########################################################################
#                                                                       #
# This is TicTacToe, but using python Turtle                            #
# TODO: Listen for screen click to restart when pressing no for restart #
# TODO: Add restart option to skip intro                                #
# Working on right now: Add local multiplayer support                   #
# TODO: Add optional background music                                   #
#                                                                       #
#########################################################################
#Fix allowDrawing variable not stopping glitch from multiplayer when changing spot variable when setting up

from turtle import Turtle, Screen
import time, socket, random, nmap, threading

global loadingStartTitleTurtle
loadingStartTitleTurtle = Turtle()
loadingStartTitleTurtle.hideturtle()
loadingStartTitleTurtle.speed(500)
loadingStartTitleTurtle.penup()
loadingStartTitleTurtle.goto(0, 100)
loadingStartTitleTurtle.write('Loading...', align='center', font=('Arial', 50, 'bold'))

global hostname
global local_ip
hostname = socket.gethostname()
local_ip = socket.gethostbyname(hostname)
print('Hostname is ' + hostname)
print('Local IP adress is ' + local_ip)

global socket_obj_global
socket_obj_global = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

def checkWhatPortIsAvailable():
    resultOfCheck = 0
    timesTriedToGetPort = 0
    while resultOfCheck == 0:
        global port_number
        global local_ip
        socket_obj = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        port_number = random.randint(0, 65535)
        test_location = (local_ip, port_number)
        resultOfCheck = socket_obj.connect_ex(test_location)
        print('Tryed port number ' + str(port_number) + ' and received status ' + str(resultOfCheck))
        timesTriedToGetPort += 1
        if resultOfCheck != 0:
            print('Port ' + str(port_number) + ' is available and will now be used for this game.')
            print('It took ' + str(timesTriedToGetPort) + ' times to get this port number.')
        socket_obj.close()

def checkIfPortIsOpen(IP, Port):
    port_scanner = nmap.PortScanner()
    check_host = socket.gethostbyname(IP)
    port_scanner.scan(check_host, '1', '-v')
    ip_state = port_scanner[check_host].state()
    print("IP Status: ", ip_state)
    resultOfCheck = None
    print('Checking IP: ' + IP)
    if ip_state == 'up':
        socket_obj = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        test_location = (IP, int(Port))
        resultOfCheck = socket_obj.connect_ex(test_location)
        print('Tryed IP ' + str(IP) + ' with port ' + str(Port) + ' and received status ' + str(resultOfCheck))
        if resultOfCheck == 0:
            print('Port ' + str(Port) + ' is available and will now be used for this game.')
            return True
        if resultOfCheck != 0:
            return 'PORT NOT FOUND ERR'
        socket_obj.close()
    else:
        print('IP ' + IP + ' is down!')
        return 'IP DOWN ERR'

global broadcastList
broadcastList = []

global introductionTurtle
introductionTurtle = Turtle()
introductionTurtle.hideturtle()

global introductionStartButton
introductionStartButton = Turtle()
introductionStartButton.hideturtle()

global joinServerButton_introduction, createServerButton_introduction
joinServerbutton_introduction = Turtle()
createServerButton_introduction = Turtle()
joinServerbutton_introduction.hideturtle()
createServerButton_introduction.hideturtle()

global spot1, spot2, spot3, spot4, spot5, spot6, spot7, spot8, spot9
spot1 = Turtle()
spot2 = Turtle()
spot3 = Turtle()
spot4 = Turtle()
spot5 = Turtle()
spot6 = Turtle()
spot7 = Turtle()
spot8 = Turtle()
spot9 = Turtle()
spot1.hideturtle()
spot2.hideturtle()
spot3.hideturtle()
spot4.hideturtle()
spot5.hideturtle()
spot6.hideturtle()
spot7.hideturtle()
spot8.hideturtle()
spot9.hideturtle()

global boardTurtle
boardTurtle = Turtle()
boardTurtle.hideturtle()

global board
board = ['-', '-', '-',
         '-', '-', '-',
         '-', '-', '-']

global boardXAndY
boardXAndY = [[-120, 230], [35, 230], [190, 230],
              [-120, 80], [35, 80], [190, 80],
              [-120, -70], [35, -70], [190, -70]]

global currentTurn
currentTurn = 'X'

global gameWon
gameWon = False

global playerThatWon
playerThatWon = 'No winner yet'

global turnValueTurtle, turnTitle
turnValueTurtle = Turtle()
turnTitle = Turtle()
turnValueTurtle.hideturtle()
turnTitle.hideturtle()

global numOfClicks
numOfClicks = 0

global endGame_lineDrawer
endGame_lineDrawer = [0, 0, 'No type', 0, 0]

global endGame_lineDrawer_turtle
endGame_lineDrawer_turtle = Turtle()
endGame_lineDrawer_turtle.hideturtle()

global restartYesButton, restartNoButton
restartYesButton = Turtle()
restartNoButton = Turtle()
restartYesButton.hideturtle()
restartNoButton.hideturtle()

global gameType
gameType = None

global IPTitle, IPTitleValue, PortTitle, PortTitleValue
IPTitle = Turtle()
IPTitleValue = Turtle()
PortTitle = Turtle()
PortTitleValue = Turtle()
IPTitle.hideturtle()
IPTitleValue.hideturtle()
PortTitle.hideturtle()
PortTitleValue.hideturtle()

global multiplayerStartButton
multiplayerStartButton = Turtle()
multiplayerStartButton.hideturtle()

global isGamePlaying
isGamePlaying = False

global playerXOrO
playerXOrO = None

global otherPlayer
otherPlayer = None

global multiplayerGameHasStarted
multiplayerGameHasStarted = False

global allowDrawing
allowDrawing = True

def introduction():
    loadingStartTitleTurtle.clear()
    drawPlayersInIntroduction(-200, 200, 'Player 1', 'center', ('Arial', 26, 'bold'))
    drawPlayersInIntroduction(200, 200, 'Player 2', 'center', ('Arial', 26, 'bold'))
    createServerButton_IntroductionFunc()
    joinButton_Introduction()
    startButton_Introduction()


def drawPlayersInIntroduction(x, y, message, align, font):
    introductionTurtle.speed(500)
    introductionTurtle.penup()
    introductionTurtle.goto(x, y)
    introductionTurtle.write(message, align=align, font=font)
    introductionTurtle.goto(x, y - 70 if message == 'Player 1' else y - 28)
    introductionTurtle.pendown()
    introductionTurtle.pensize(20)
    if message == 'Player 1':
        introductionTurtle.setheading(45)
        introductionTurtle.forward(50)
        introductionTurtle.backward(100)
        introductionTurtle.forward(50)
        introductionTurtle.setheading(135)
        introductionTurtle.forward(50)
        introductionTurtle.backward(100)
    else: 
        introductionTurtle.setheading(180)
        introductionTurtle.circle(42)

def startButton_Introduction():
    introductionStartButton.penup()
    introductionStartButton.goto(235, 0)
    introductionStartButton.write('Start local multiplayer', align='center', font=('Arial', 18))
    introductionStartButton.goto(260, -30)
    introductionStartButton.turtlesize(3, 5, 1)
    introductionStartButton.fillcolor('green')
    introductionStartButton.pencolor('black')
    introductionStartButton.showturtle()
    introductionStartButton.onclick(handleStartButtonPress)

def joinButton_Introduction():
    joinServerbutton_introduction.penup()
    joinServerbutton_introduction.goto(0, 0)
    joinServerbutton_introduction.write('Join LAN server (WIP)', align='center', font=('Arial', 18))
    joinServerbutton_introduction.goto(15, -30)
    joinServerbutton_introduction.turtlesize(3, 5, 1)
    joinServerbutton_introduction.fillcolor('yellow')
    joinServerbutton_introduction.pencolor('black')
    joinServerbutton_introduction.showturtle()
    joinServerbutton_introduction.onclick(lambda x, y: handleJoinButtonPress())

def createServerButton_IntroductionFunc():
    createServerButton_introduction.penup()
    createServerButton_introduction.goto(-235, 0)
    createServerButton_introduction.write('Create LAN server (WIP)', align='center', font=('Arial', 18))
    createServerButton_introduction.goto(-220, -30)
    createServerButton_introduction.turtlesize(3, 5, 1)
    createServerButton_introduction.fillcolor('red')
    createServerButton_introduction.pencolor('black')
    createServerButton_introduction.showturtle()
    createServerButton_introduction.onclick(lambda x, y: createServerThread())

def createServerThread():
    createServerThread = threading.Thread(target=handleCreateServerButtonPress, daemon=True)
    createServerThread.name = 'Server Thread'
    createServerThread.start()


def handleStartButtonPress(x, y):
    clearIntroduction()
    startGame()
    global gameType
    gameType = 'Local'

def handleJoinButtonPress():
    clearIntroduction()
    global screen
    showTurnTitle('Type in the IP address you wish to join', 'center', ('Arial', 22, 'bold'), 0, 100, 0, 0, 0)
    ip_to_join = screen.textinput("IP Address", "Enter IP address")
    screen.listen()
    while ip_to_join == None or ip_to_join == '':
        ip_to_join = screen.textinput("IP Address", "Enter IP address")
    turnTitle.clear()
    showTurnTitle('Type in the port you wish to join', 'center', ('Arial', 22, 'bold'), 0, 100, 0, 0, 0)
    port_to_join = screen.numinput("Port", "Enter port", minval=0, maxval=65535)
    screen.listen()
    while port_to_join == None or port_to_join == '':
        port_to_join = screen.numinput("Port", "Enter port", minval=0, maxval=65535)
    port_to_join = int(port_to_join)
    turnTitle.clear()
    showTurnTitle('Trying to connect you...', 'center', ('Arial', 26, 'bold'), 0, 100, 0, 0, 0)
    isPortOpen = checkIfPortIsOpen(ip_to_join, port_to_join)
    print('isPortOpen function returned ' + str(isPortOpen))
    if isPortOpen == 'PORT NOT FOUND ERR':
        turnTitle.clear()
        showTurnTitle('Port Not Found. Please make sure you entered the right port number', 'center', ('Arial', 18, 'bold'), 0, 100, 255, 0, 0)
        sendBackToJoinScreenAfterError()
    elif isPortOpen == True:
        turnTitle.clear()
        showTurnTitle('Port found! Connecting to server...', 'center', ('Arial', 26, 'bold'), 0, 100, 0, 0, 0)
        try:
            socket_obj_global.connect((ip_to_join, int(port_to_join)))
            print('Connected to server')
            turnTitle.clear()
            showTurnTitle('Connected to server successfully! Waiting for server to start', 'center', ('Arial', 20, 'bold'), 0, 100, 0, 150, 0)
            thread_receive = threading.Thread(target=thread_receiving, daemon=True)
            thread_receive.name = "Client Receive Thread"
            thread_receive.start()
            print('Client threads created successfully')
            global gameType
            while not gameType:
                time.sleep(0.1)
            print('Choosing whether player is a spectator or a player')
            print(f'gameType is {gameType}')
            if gameType == 'SPECTATOR':
                print('This client will now be a spectator')
                turnTitle.clear()
                showTurnTitle('There are already 2 players connected!', 'center', ('Arial', 24), 0, 100, 0, 0, 0)
                showTurnValue('You will join as a spectator', 'center', ('Arial', 24), 0, 50, 0, 0, 0)
            elif gameType == 'NOT_SPECTATOR':
                print('This client will now be a player')
            else:
                turnTitle.clear()
                showTurnTitle('Error occured while choosing whether you are a player or a spectator', 'center', ('Arial', 16), 0, 100, 255, 0, 0)
        except:
            turnTitle.clear()
            showTurnTitle('Connection failed. Please try again.', 'center', ('Arial', 22, 'bold'), 0, 100, 255, 0, 0)
    elif isPortOpen == 'IP DOWN ERR':
        turnTitle.clear()
        showTurnTitle('IP address cannot be found. Please make sure you entered the correct IP.', 'center', ('Arial', 16, 'bold'), 0, 100, 255, 0, 0)
        sendBackToJoinScreenAfterError()
    else:
        print('Some weird error happened in checking port and joining')
        turnTitle.clear()
        showTurnTitle('An unknown error occured', 'center', ('Arial', 22, 'bold'), 0, 100, 0, 0, 0)
        sendBackToJoinScreenAfterError()

def sendBackToJoinScreenAfterError():
    showTurnValue('Going back to join server screen in...', 'center', ('Arial', 20), 0, 70, 0, 0, 0)
    for i in range(5,0,-1):
        showIPTitle(f'{i}...', 'center', ('Arial', 30, 'bold'), 0, 40, 0, 0, 0)
        time.sleep(1)
        IPTitle.clear()
    turnTitle.clear()
    turnValueTurtle.clear()
    handleJoinButtonPress()

def send_message_to_server(message):
    try:
        socket_obj_global.send(message.encode())
    except:
        print('ERROR OCCURED WHILE CLIENT TRIED TO SEND MESSAGE TO SERVER')
        print(f'MESSAGE WAS: {message}')
        print('Inititing connection lost with server handler')
        connectionLostWithServerHandle()
        return
        
def thread_receiving(): # Thread receiving messages from server
    while True:
        try:
            global gameType
            global board
            global numOfClicks
            message = socket_obj_global.recv(1024).decode()
            print(message)
            if message == '__SPECTATOR__':
                print('Setting game mode to spectator')
                gameType = 'SPECTATOR'
            if message == 'NOT_SPECTATOR':
                print('Setting game mode to player')
                gameType = 'NOT_SPECTATOR'
            if message == 'STARTING_GAME':
                turnValueTurtle.clear()
                turnTitle.clear()
                global playerXOrO
                playerXOrO = 'O'
                startGameThread = threading.Thread(target=startGame, daemon=True)
                startGameThread.name = "Game Thread"
                startGameThread.start()
            if message == 'X' or message == 'O' and gameType == 'SPECTATOR':
                print(f'Received message {message}')
                spotNumber = socket_obj_global.recv(1024).decode()
                print(f'Spot number is {spotNumber}')
                board[int(spotNumber)] = message
                global currentTurn, allowDrawing
                currentTurn = 'O' if message == 'X' else 'X'
                while allowDrawing == False:
                    print('Allow drawing is set to false. Program is now waiting for Turtle to be done for spots to update')
                setupSpot1() if spotNumber == '0' else setupSpot2() if spotNumber == '1' else setupSpot3() if spotNumber == '2' else setupSpot4() if spotNumber == '3' else setupSpot5() if spotNumber == '4' else setupSpot6() if spotNumber == '5' else setupSpot7() if spotNumber == '6' else setupSpot8() if spotNumber == '7' else setupSpot9()
                numOfClicks += 1
                checkIfWon()
                if gameWon == False:
                    turnValueTurtle.clear()
                    showTurnValue(currentTurn, 'center', ('Arial', 60, 'bold'), 0, -260, 0, 0, 0)
                    print(f'Number of clicks is {numOfClicks}')
                    if numOfClicks == 9:
                        turnTitle.clear()
                        turnValueTurtle.clear()
                        showTurnValue('Both players have tied! Congratulations!', 'center', ('Arial', 30, 'bold'), 0, -260, 0, 0, 0)
                        if playerXOrO == 'X':
                            time.sleep(2)
                            turnValueTurtle.clear()
                            showTurnValue('Restart game?', 'center', ('Arial', 35, 'bold'), 0, -200, 100, 200, 100)
                            showRestartNoButton()
                            showRestartYesButton()
                else:
                    spot1.hideturtle()
                    spot2.hideturtle()
                    spot3.hideturtle()
                    spot4.hideturtle()
                    spot5.hideturtle()
                    spot6.hideturtle()
                    spot7.hideturtle()
                    spot8.hideturtle()
                    spot9.hideturtle()
                    endGame_lineDrawer_turtle.pensize(15)
                    endGame_lineDrawer_turtle.pencolor('red')
                    endGame_lineDrawer_turtle.penup()
                    endGame_lineDrawer_turtle.goto(endGame_lineDrawer[0] - 80, endGame_lineDrawer[1] + 50) if endGame_lineDrawer[2] == 'Diagonal' else endGame_lineDrawer_turtle.goto(endGame_lineDrawer[0] - 80, endGame_lineDrawer[1]) if endGame_lineDrawer[2] == 'Horizontal' else endGame_lineDrawer_turtle.goto(endGame_lineDrawer[0] - 30, endGame_lineDrawer[1] + 50) if endGame_lineDrawer[2] == 'Vertical' else endGame_lineDrawer_turtle.goto(endGame_lineDrawer[0] + 20, endGame_lineDrawer[1] + 50)
                    endGame_lineDrawer_turtle.pendown()
                    endGame_lineDrawer_turtle.goto(endGame_lineDrawer[3] + 20, endGame_lineDrawer[4] - 50) if endGame_lineDrawer[2] == 'Diagonal' else endGame_lineDrawer_turtle.goto(endGame_lineDrawer[3] + 20, endGame_lineDrawer[4]) if endGame_lineDrawer[2] == 'Horizontal' else endGame_lineDrawer_turtle.goto(endGame_lineDrawer[3] - 30, endGame_lineDrawer[4] - 50) if endGame_lineDrawer[2] == 'Vertical' else endGame_lineDrawer_turtle.goto(endGame_lineDrawer[3] - 80, endGame_lineDrawer[4] - 50)
                    turnTitle.clear()
                    turnValueTurtle.clear()
                    showTurnValue(playerThatWon + ' won!', 'center', ('Arial', 60, 'bold'), 0, -260, 0, 0, 0)
                    if playerXOrO == 'X':
                        time.sleep(2)
                        turnValueTurtle.clear()
                        showTurnValue('Restart game?', 'center', ('Arial', 35, 'bold'), 0, -200, 100, 200, 100)
                        showRestartNoButton()
                        showRestartYesButton()
            if message == 'GAME_ALREADY_STARTED':
                gameAlreadyStartedhandler()
                return
            if message == 'GAME_NOT_RESTARTING':
                turnTitle.clear()
                turnValueTurtle.clear()
                showTurnValue('Server is not restarting the game', 'center', ('Arial', 35, 'bold'), 0, -260, 255, 0, 0)
                time.sleep(2)
                turnValueTurtle.clear()
                showTurnValue(playerThatWon + ' won!', 'center', ('Arial', 60, 'bold'), 0, -260, 0, 0, 0)
            if message == 'GAME_RESTARTING':
                allowDrawing = False
                clearEverythingAndRestartGame()
        except:
            print('Handling connection lost with server')
            connectionLostWithServerHandle()
            return

def gameAlreadyStartedhandler():
    turnTitle.clear()
    turnValueTurtle.clear()
    showTurnTitle('This game has already started.', 'center', ('Arial', 18), 0, 100, 255, 0, 0)
    showIPTitle('Going back to the game screen in...', 'center', ('Arial', 18), 0, 80, 0, 0, 0)
    for i in range(3,0,-1):
        showTurnValue(f'{i}...', 'center', ('Arial', 30, 'bold'), 0, 30, 0, 0, 0)
        time.sleep(1)
        turnValueTurtle.clear()
    turnTitle.clear()
    IPTitle.clear()
    introduction()
    return
    #
    #
    #
    #
    #
    # MAKE SURE THIS KILLS ALL THREADS RUNNING
    # MULTIPLE HASHTAGS USED TO GET MY ATTENTION

def connectionLostWithServerHandle():
    print('Connection lost')
    turnTitle.clear()
    turnValueTurtle.clear()
    spot1.hideturtle()
    spot2.hideturtle()
    spot3.hideturtle()
    spot4.hideturtle()
    spot5.hideturtle()
    spot6.hideturtle()
    spot7.hideturtle()
    spot8.hideturtle()
    spot9.hideturtle()
    spot1.clear()
    spot2.clear()
    spot3.clear()
    spot4.clear()
    spot5.clear()
    spot6.clear()
    spot7.clear()
    spot8.clear()
    spot9.clear()
    boardTurtle.clear()
    endGame_lineDrawer_turtle.clear()
    restartNoButton.clear()
    restartYesButton.clear()
    restartYesButton.hideturtle()
    restartNoButton.hideturtle()
    showTurnTitle('Connection lost with server. Taking you back to introduction screen in...', 'center', ('Arial', 18), 0, 100, 255, 0, 0)
    for i in range(3,0,-1):
        showTurnValue(f'{i}...', 'center', ('Arial', 30, 'bold'), 0, 50, 0, 0, 0)
        time.sleep(1)
        turnValueTurtle.clear()
    turnTitle.clear()
    introduction()

def handleCreateServerButtonPress():
    clearIntroduction()
    showTurnTitle('Creating server...', 'center', ('Arial', 26, 'bold'), 0, 100, 0, 0, 0)
    checkWhatPortIsAvailableError = True
    bindSocketError = True
    while checkWhatPortIsAvailableError == True:
        try:
            checkWhatPortIsAvailable()
            checkWhatPortIsAvailableError = False
        except:
            print('Restarted port checker because port permission was denied')
            pass
    socket_obj = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    checkForPlayersConnectedThread = threading.Thread(target=checkForPlayersConnected)
    checkForPlayersConnectedThread.name = 'Check players connected'
    checkForPlayersConnectedThread.start()
    global local_ip
    global port_number
    while bindSocketError == True:
        try:
            socket_obj.bind((local_ip, port_number))
            bindSocketError = False
        except:
            checkWhatPortIsAvailable()
            print('Restarting socket_obj binding because permission was denied')
            pass
    turnTitle.clear()
    showIPTitle('IP for server:', 'center', ('Arial', 26, 'bold'), 0, 100, 0, 0, 0)
    showIPTitleValue(local_ip, 'center', ('Arial', 20), 0, 80, 0, 0, 0)
    showPortTitle('Port for server:', 'center', ('Arial', 26, 'bold'), 0, 0, 0, 0, 0)
    showPortTitleValue(port_number, 'center', ('Arial', 20), 0, -20, 0, 0, 0)
    while True:
        socket_obj.listen()
        client, client_address = socket_obj.accept()
        print('Client variable is', client)
        print('Client address variable is', client_address)
        broadcastList.append(client)
        start_listening_thread(client)
        global multiplayerGameHasStarted
        if multiplayerGameHasStarted == True:
            threading.Thread(target=broadcastToIndividualClient, args=(client, 'GAME_ALREADY_STARTED'), name='Game Already Started Sender', daemon=True).start()
        else:
            if len(broadcastList) / 2 == 1 and len(broadcastList) == 2 or len(broadcastList) >= 3:
                print('Connecting client is a spectator')
                print(f'Client that is a spectator: {client}')
                tellClientTheyAreSpectator = threading.Thread(target=broadcastToIndividualClient, args=(client, '__SPECTATOR__'), daemon=True)
                tellClientTheyAreSpectator.name = "Send spectator msg"
                tellClientTheyAreSpectator.start()
            else:
                print('Connecting client is NOT a spectator')
                global otherPlayer
                otherPlayer = client
                tellClientTheyAreNotSpectator = threading.Thread(target=broadcastToIndividualClient, args=(client, 'NOT_SPECTATOR'), daemon=True)
                tellClientTheyAreNotSpectator.name = "Client Not Spectator Send"
                tellClientTheyAreNotSpectator.start()

def checkForPlayersConnected():
    while True:
        print('Running checkForPlayersConnected function')
        time.sleep(1)
        if len(broadcastList) == 0:
            print('No players connected')
            print(f'Len of broadcastList is {len(broadcastList)}')
            multiplayerStartButton.clear()
            multiplayerStartButton.hideturtle()
            global isGamePlaying
            if isGamePlaying == True:
                isGamePlaying = False
                endGame_lineDrawer_turtle.clear()
                restartNoButton.hideturtle()
                restartNoButton.clear()
                restartYesButton.hideturtle()
                restartYesButton.clear()
                turnValueTurtle.clear()
                turnTitle.clear()
                global board, currentTurn
                board = ['-', '-', '-',
                        '-', '-', '-',
                        '-', '-', '-']
                global numOfClicks
                global gameWon
                gameWon = False
                numOfClicks = 0
                currentTurn = 'X'
                boardTurtle.clear()
                spot1.hideturtle()
                spot2.hideturtle()
                spot3.hideturtle()
                spot4.hideturtle()
                spot5.hideturtle()
                spot6.hideturtle()
                spot7.hideturtle()
                spot8.hideturtle()
                spot9.hideturtle()
                spot1.clear()
                spot2.clear()
                spot3.clear()
                spot4.clear()
                spot5.clear()
                spot6.clear()
                spot7.clear()
                spot8.clear()
                spot9.clear()
                showTurnTitle('The other player has lost connection to the server', 'center', ('Arial', 20), 0, 100, 255, 0, 0)
                showTurnValue('Going back to introduction screen in...', 'center', ('Arial', 20, 'bold'), 0, 70, 0, 0, 0)
                for i in range(5, 0, -1):
                    showIPTitle(f'{i}...', 'center', ('Arial', 30), 0, 40, 0, 0, 0)
                    time.sleep(1)
                    IPTitle.clear()
                turnValueTurtle.clear()
                turnTitle.clear()
                introduction()
                #GET ALL SERVER THREADS TO QUIT
                #
                #
                #
                #
                #
                #
                #
                #
                #
                # MULTIPLE HASHTAGS USED TO GET MY ATTENTION
        else:
            drawMultiplayerStartButton()
            while len(broadcastList) > 0:
                time.sleep(1)
                print('Client is connected')
            
def drawMultiplayerStartButton():
    multiplayerStartButton.penup()
    multiplayerStartButton.goto(0, -180)
    multiplayerStartButton.write('Start', align='center', font=('Arial', 26, 'bold'))
    multiplayerStartButton.goto(30, -230)
    multiplayerStartButton.turtlesize(3, 6, 1)
    multiplayerStartButton.pencolor('black')
    multiplayerStartButton.fillcolor('green')
    multiplayerStartButton.showturtle()
    multiplayerStartButton.onclick(lambda x, y: handleStartMultiplayerButton())

def handleStartMultiplayerButton():
    print('Starting multiplayer game...')
    multiplayerStartButton.clear()
    multiplayerStartButton.hideturtle()
    turnTitle.clear()
    turnValueTurtle.clear()
    IPTitle.clear()
    IPTitleValue.clear()
    PortTitle.clear()
    PortTitleValue.clear()
    broadcast('STARTING_GAME')
    global playerXOrO
    playerXOrO = 'X'
    global multiplayerGameHasStarted
    multiplayerGameHasStarted = True
    startGame()

def start_listening_thread(client):
    client_thread = threading.Thread(
            target=listen_thread,
            daemon=True,
            args=(client,) #the list of argument for the function
        )
    client_thread.name = "Listen for msg Thread"
    client_thread.start()

def listen_thread(client): # Server listening for client messages thread
    while True:
        try:
            message = client.recv(4096).decode()
            if message:
                print(f"Received message : {message}")
                if message == 'O':
                    global numOfClicks
                    print('Received O message')
                    spotNumber = client.recv(4096).decode()
                    print(f'Received spot number as {spotNumber}')
                    board[int(spotNumber)] = 'O'
                    global currentTurn
                    currentTurn = 'X'
                    broadcastToEveryoneExceptOtherPlayer(otherPlayer, 'O')
                    broadcastToEveryoneExceptOtherPlayer(otherPlayer, str(spotNumber))
                    setupSpot1() if spotNumber == '0' else setupSpot2() if spotNumber == '1' else setupSpot3() if spotNumber == '2' else setupSpot4() if spotNumber == '3' else setupSpot5() if spotNumber == '4' else setupSpot6() if spotNumber == '5' else setupSpot7() if spotNumber == '6' else setupSpot8() if spotNumber == '7' else setupSpot9()
                    numOfClicks += 1
                    checkIfWon()
                    if gameWon == False:
                        turnValueTurtle.clear()
                        showTurnValue(currentTurn, 'center', ('Arial', 60, 'bold'), 0, -260, 0, 0, 0)
                        print(f'Number of clicks is: {numOfClicks}')
                        if numOfClicks == 9:
                            turnTitle.clear()
                            turnValueTurtle.clear()
                            showTurnValue('Both players have tied! Congratulations!', 'center', ('Arial', 30, 'bold'), 0, -260, 0, 0, 0)
                            if playerXOrO == 'X':
                                time.sleep(2)
                                turnValueTurtle.clear()
                                showTurnValue('Restart game?', 'center', ('Arial', 35, 'bold'), 0, -200, 100, 200, 100)
                                showRestartNoButton()
                                showRestartYesButton()
                    else:
                        spot1.hideturtle()
                        spot2.hideturtle()
                        spot3.hideturtle()
                        spot4.hideturtle()
                        spot5.hideturtle()
                        spot6.hideturtle()
                        spot7.hideturtle()
                        spot8.hideturtle()
                        spot9.hideturtle()
                        endGame_lineDrawer_turtle.pensize(15)
                        endGame_lineDrawer_turtle.pencolor('red')
                        endGame_lineDrawer_turtle.penup()
                        endGame_lineDrawer_turtle.goto(endGame_lineDrawer[0] - 80, endGame_lineDrawer[1] + 50) if endGame_lineDrawer[2] == 'Diagonal' else endGame_lineDrawer_turtle.goto(endGame_lineDrawer[0] - 80, endGame_lineDrawer[1]) if endGame_lineDrawer[2] == 'Horizontal' else endGame_lineDrawer_turtle.goto(endGame_lineDrawer[0] - 30, endGame_lineDrawer[1] + 50) if endGame_lineDrawer[2] == 'Vertical' else endGame_lineDrawer_turtle.goto(endGame_lineDrawer[0] + 20, endGame_lineDrawer[1] + 50)
                        endGame_lineDrawer_turtle.pendown()
                        endGame_lineDrawer_turtle.goto(endGame_lineDrawer[3] + 20, endGame_lineDrawer[4] - 50) if endGame_lineDrawer[2] == 'Diagonal' else endGame_lineDrawer_turtle.goto(endGame_lineDrawer[3] + 20, endGame_lineDrawer[4]) if endGame_lineDrawer[2] == 'Horizontal' else endGame_lineDrawer_turtle.goto(endGame_lineDrawer[3] - 30, endGame_lineDrawer[4] - 50) if endGame_lineDrawer[2] == 'Vertical' else endGame_lineDrawer_turtle.goto(endGame_lineDrawer[3] - 80, endGame_lineDrawer[4] - 50)
                        turnTitle.clear()
                        turnValueTurtle.clear()
                        showTurnValue(playerThatWon + ' won!', 'center', ('Arial', 60, 'bold'), 0, -260, 0, 0, 0)
                        if playerXOrO == 'X':
                            time.sleep(2)
                            turnValueTurtle.clear()
                            showTurnValue('Restart game?', 'center', ('Arial', 35, 'bold'), 0, -200, 100, 200, 100)
                            showRestartNoButton()
                            showRestartYesButton()
            else:
                print(f"client has been disconnected at listen_thread : {client}")
                broadcastList.remove(client)
                print(f'Len of broadcastList is now {len(broadcastList)}')
                return
        except:
            print(f"client has been disconnected at listen_thread : {client}")
            broadcastList.remove(client)
            print(f'Len of broadcastList is now {len(broadcastList)}')
            return

def broadcast(message):
    for client in broadcastList:
        try:
            print(f'Amount of items in broadcastList is: {len(broadcastList)}')
            client.send(message.encode())
        except:
            broadcastList.remove(client)
            print(f"Client removed at broadcast : {client}")

def broadcastToIndividualClient(client, message):
    try:
        client.send(message.encode())
    except:
        broadcastList.remove(client)
        print(f'Client removed at individual broadcast: {client}')

def broadcastToEveryoneExceptOtherPlayer(clientToIgnore, message):
    for client in broadcastList:
        try:
            if client != clientToIgnore:
                client.send(message.encode())
        except:
            broadcastList.remove(client)
            print(f'Client removed at individual broadcast: {client}')

def showIPTitle(message, alignment, font, x, y, r, g, b):
    global screen
    IPTitle.speed(500)
    IPTitle.penup()
    IPTitle.goto(x, y)
    screen.colormode(255)
    IPTitle.pencolor(r, g, b)
    IPTitle.write(message, align=alignment, font=font)

def showIPTitleValue(message, alignment, font, x, y, r, g, b):
    global screen
    IPTitleValue.speed(500)
    IPTitleValue.penup()
    IPTitleValue.goto(x, y)
    screen.colormode(255)
    IPTitleValue.pencolor(r, g, b)
    IPTitleValue.write(message, align=alignment, font=font)

def showPortTitle(message, alignment, font, x, y, r, g, b):
    global screen
    PortTitle.speed(500)
    PortTitle.penup()
    PortTitle.goto(x, y)
    screen.colormode(255)
    PortTitle.pencolor(r, g, b)
    PortTitle.write(message, align=alignment, font=font)

def showPortTitleValue(message, alignment, font, x, y, r, g, b):
    global screen
    PortTitleValue.speed(500)
    PortTitleValue.penup()
    PortTitleValue.goto(x, y)
    screen.colormode(255)
    PortTitleValue.pencolor(r, g, b)
    PortTitleValue.write(message, align=alignment, font=font)

def startGame():
    global allowDrawing
    allowDrawing = False
    size = 450
    startx = -225
    starty = 300
    speed = 500
    global currentTurn
    global isGamePlaying
    isGamePlaying = True
    drawBoard(size=size, startx=startx, starty=starty, speed=speed)
    if gameType != 'SPECTATOR':
        setupSpot1(x=boardXAndY[0][0], y=boardXAndY[0][1])
        setupSpot2(x=boardXAndY[1][0], y=boardXAndY[1][1])
        setupSpot3(x=boardXAndY[2][0], y=boardXAndY[2][1])
        setupSpot4(x=boardXAndY[3][0], y=boardXAndY[3][1])
        setupSpot5(x=boardXAndY[4][0], y=boardXAndY[4][1])
        setupSpot6(x=boardXAndY[5][0], y=boardXAndY[5][1])
        setupSpot7(x=boardXAndY[6][0], y=boardXAndY[6][1])
        setupSpot8(x=boardXAndY[7][0], y=boardXAndY[7][1])
        setupSpot9(x=boardXAndY[8][0], y=boardXAndY[8][1])
    showTurnTitle('Current turn', 'center', ('Arial', 40, 'bold'), 0, -200, 0, 0, 0)
    showTurnValue(currentTurn, 'center', ('Arial', 60, 'bold'), 0, -260, 0, 0, 0)
    allowDrawing = True

def clearIntroduction():
    introductionStartButton.clear()
    introductionTurtle.clear()
    introductionStartButton.hideturtle()
    joinServerbutton_introduction.clear()
    joinServerbutton_introduction.hideturtle()
    createServerButton_introduction.clear()
    createServerButton_introduction.hideturtle()

def drawBoard(size=450, startx=-225, starty=300, speed=500):
    boardTurtle.penup()
    boardTurtle.goto(startx, starty)
    boardTurtle.pendown()
    boardTurtle.pensize(10)
    boardTurtle.setheading(0)
    boardTurtle.speed(speed)
    for i in range(4):
        boardTurtle.forward(size)
        boardTurtle.right(90)
    for i in range(1, 5, 1):
        boardTurtle.penup()
        boardTurtle.goto(startx + size / 3 * i if i < 3 else startx, starty if i < 3 else starty - size / 3 * (i - 2))
        boardTurtle.setheading(270 if i < 3 else 0)
        boardTurtle.pendown()
        boardTurtle.forward(size)

def handleClick(spot=''):
    global gameWon
    global currentTurn
    global board
    global playerThatWon
    global numOfClicks
    global gameType
    if gameType == 'Local':
        numOfClicks += 1
        board[spot] = currentTurn
        currentTurn = 'O' if currentTurn == 'X' else 'X'
        setupSpot1() if spot == 0 else setupSpot2() if spot == 1 else setupSpot3() if spot == 2 else setupSpot4() if spot == 3 else setupSpot5() if spot == 4 else setupSpot6() if spot == 5 else setupSpot7() if spot == 6 else setupSpot8() if spot == 7 else setupSpot9() if spot == 8 else print('Some stupid error happened when choosing what spot function to run')
        checkIfWon()
        if gameWon == False:
            turnValueTurtle.clear()
            showTurnValue(currentTurn, 'center', ('Arial', 60, 'bold'), 0, -260, 0, 0, 0)
            if numOfClicks == 9:
                turnTitle.clear()
                turnValueTurtle.clear()
                showTurnValue('Both players have tied! Congratulations!', 'center', ('Arial', 30, 'bold'), 0, -260, 0, 0, 0)
                time.sleep(2)
                turnValueTurtle.clear()
                showTurnValue('Restart game?', 'center', ('Arial', 35, 'bold'), 0, -200, 100, 200, 100)
                showRestartNoButton()
                showRestartYesButton()
        else:
            spot1.hideturtle()
            spot2.hideturtle()
            spot3.hideturtle()
            spot4.hideturtle()
            spot5.hideturtle()
            spot6.hideturtle()
            spot7.hideturtle()
            spot8.hideturtle()
            spot9.hideturtle()
            endGame_lineDrawer_turtle.pensize(15)
            endGame_lineDrawer_turtle.pencolor('red')
            endGame_lineDrawer_turtle.penup()
            endGame_lineDrawer_turtle.goto(endGame_lineDrawer[0] - 80, endGame_lineDrawer[1] + 50) if endGame_lineDrawer[2] == 'Diagonal' else endGame_lineDrawer_turtle.goto(endGame_lineDrawer[0] - 80, endGame_lineDrawer[1]) if endGame_lineDrawer[2] == 'Horizontal' else endGame_lineDrawer_turtle.goto(endGame_lineDrawer[0] - 30, endGame_lineDrawer[1] + 50) if endGame_lineDrawer[2] == 'Vertical' else endGame_lineDrawer_turtle.goto(endGame_lineDrawer[0] + 20, endGame_lineDrawer[1] + 50)
            endGame_lineDrawer_turtle.pendown()
            endGame_lineDrawer_turtle.goto(endGame_lineDrawer[3] + 20, endGame_lineDrawer[4] - 50) if endGame_lineDrawer[2] == 'Diagonal' else endGame_lineDrawer_turtle.goto(endGame_lineDrawer[3] + 20, endGame_lineDrawer[4]) if endGame_lineDrawer[2] == 'Horizontal' else endGame_lineDrawer_turtle.goto(endGame_lineDrawer[3] - 30, endGame_lineDrawer[4] - 50) if endGame_lineDrawer[2] == 'Vertical' else endGame_lineDrawer_turtle.goto(endGame_lineDrawer[3] - 80, endGame_lineDrawer[4] - 50)
            turnTitle.clear()
            turnValueTurtle.clear()
            showTurnValue(playerThatWon + ' won!', 'center', ('Arial', 60, 'bold'), 0, -260, 0, 0, 0)
            time.sleep(2)
            turnValueTurtle.clear()
            showTurnValue('Restart game?', 'center', ('Arial', 35, 'bold'), 0, -200, 100, 200, 100)
            showRestartNoButton()
            showRestartYesButton()
    else:
        if (playerXOrO == currentTurn):
            if (playerXOrO == 'X'):
                broadcast('X' if currentTurn == 'X' else 'O')
                broadcast(str(spot))
            else:
                send_message_to_server('O')
                send_message_to_server(str(spot))
            numOfClicks += 1
            board[spot] = currentTurn
            currentTurn = 'O' if currentTurn == 'X' else 'X'
            setupSpot1() if spot == 0 else setupSpot2() if spot == 1 else setupSpot3() if spot == 2 else setupSpot4() if spot == 3 else setupSpot5() if spot == 4 else setupSpot6() if spot == 5 else setupSpot7() if spot == 6 else setupSpot8() if spot == 7 else setupSpot9() if spot == 8 else print('Some stupid error happened when choosing what spot function to run')
            checkIfWon()
            if gameWon == False:
                turnValueTurtle.clear()
                showTurnValue(currentTurn, 'center', ('Arial', 60, 'bold'), 0, -260, 0, 0, 0)
                if numOfClicks == 9:
                    turnTitle.clear()
                    turnValueTurtle.clear()
                    showTurnValue('Both players have tied! Congratulations!', 'center', ('Arial', 30, 'bold'), 0, -260, 0, 0, 0)
                    if playerXOrO == 'X':
                        time.sleep(2)
                        turnValueTurtle.clear()
                        showTurnValue('Restart game?', 'center', ('Arial', 35, 'bold'), 0, -200, 100, 200, 100)
                        showRestartNoButton()
                        showRestartYesButton()
            else:
                spot1.hideturtle()
                spot2.hideturtle()
                spot3.hideturtle()
                spot4.hideturtle()
                spot5.hideturtle()
                spot6.hideturtle()
                spot7.hideturtle()
                spot8.hideturtle()
                spot9.hideturtle()
                endGame_lineDrawer_turtle.pensize(15)
                endGame_lineDrawer_turtle.pencolor('red')
                endGame_lineDrawer_turtle.penup()
                endGame_lineDrawer_turtle.goto(endGame_lineDrawer[0] - 80, endGame_lineDrawer[1] + 50) if endGame_lineDrawer[2] == 'Diagonal' else endGame_lineDrawer_turtle.goto(endGame_lineDrawer[0] - 80, endGame_lineDrawer[1]) if endGame_lineDrawer[2] == 'Horizontal' else endGame_lineDrawer_turtle.goto(endGame_lineDrawer[0] - 30, endGame_lineDrawer[1] + 50) if endGame_lineDrawer[2] == 'Vertical' else endGame_lineDrawer_turtle.goto(endGame_lineDrawer[0] + 20, endGame_lineDrawer[1] + 50)
                endGame_lineDrawer_turtle.pendown()
                endGame_lineDrawer_turtle.goto(endGame_lineDrawer[3] + 20, endGame_lineDrawer[4] - 50) if endGame_lineDrawer[2] == 'Diagonal' else endGame_lineDrawer_turtle.goto(endGame_lineDrawer[3] + 20, endGame_lineDrawer[4]) if endGame_lineDrawer[2] == 'Horizontal' else endGame_lineDrawer_turtle.goto(endGame_lineDrawer[3] - 30, endGame_lineDrawer[4] - 50) if endGame_lineDrawer[2] == 'Vertical' else endGame_lineDrawer_turtle.goto(endGame_lineDrawer[3] - 80, endGame_lineDrawer[4] - 50)
                turnTitle.clear()
                turnValueTurtle.clear()
                showTurnValue(playerThatWon + ' won!', 'center', ('Arial', 60, 'bold'), 0, -260, 0, 0, 0)
                if playerXOrO == 'X':
                    time.sleep(2)
                    turnValueTurtle.clear()
                    showTurnValue('Restart game?', 'center', ('Arial', 35, 'bold'), 0, -200, 100, 200, 100)
                    showRestartNoButton()
                    showRestartYesButton()

def setupSpot1(x=-120, y=230):
    spot1.speed(500)
    spot1.penup()
    spot1.hideturtle()
    spot1.goto(x if board[0] == '-' else x - 30 if board[0] == 'X' else x - 30, y if board[0] == '-' else y if board[0] == 'X' else y - 30)
    spot1.hideturtle() if board[0] == 'X' or board[0] == 'O' or gameType == 'SPECTATOR' else spot1.showturtle()
    spot1.pensize(10)
    spot1.pendown() if board[0] == 'X' or board[0] == 'O' else spot1.penup()
    spot1.speed(6 if board[0] == '-' or board[0] == 'X' else 0)
    if board[0] == '-':
        spot1.setheading(0)
        spot1.pencolor('black')
        spot1.fillcolor('green')
        spot1.turtlesize(4,7,1)
        spot1.onclick(lambda x, y: handleClick(spot=0))
    elif board[0] == 'X':
        for i in range(2):
            spot1.setheading(45 if i == 0 else 135)
            spot1.forward(30)
            spot1.backward(60)
            spot1.forward(30)
    elif board[0] == 'O':
        spot1.setheading(0)
        spot1.circle(30)
    else:
        print('Some weird error happened in setupSpot1() when reading board[0]')

def setupSpot2(x = 35, y = 230):
    spot2.speed(500)
    spot2.penup()
    spot2.hideturtle()
    spot2.goto(x if board[1] == '-' else x - 30 if board[1] == 'X' else x - 30, y if board[1] == '-' else y if board[1] == 'X' else y - 30)
    spot2.hideturtle() if board[1] == 'X' or board[1] == 'O' or gameType == 'SPECTATOR' else spot2.showturtle()
    spot2.pensize(10)
    spot2.pendown() if board[1] == 'X' or board[1] == 'O' else spot2.penup()
    spot2.speed(6 if board[1] == '-' or board[1] == 'X' else 0)
    if board[1] == '-':
        spot2.setheading(0)
        spot2.pencolor('black')
        spot2.fillcolor('green')
        spot2.turtlesize(4,7,1)
        spot2.onclick(lambda x, y: handleClick(spot=1))
    elif board[1] == 'X':
        for i in range(2):
            spot2.setheading(45 if i == 0 else 135)
            spot2.forward(30)
            spot2.backward(60)
            spot2.forward(30)
    elif board[1] == 'O':
        spot2.setheading(0)
        spot2.circle(30)
    else:
        print('Some weird error happened in setupSpot2() when reading board[1]')

def setupSpot3(x = 190, y = 230):
    spot3.speed(500)
    spot3.penup()
    spot3.hideturtle()
    spot3.goto(x if board[2] == '-' else x - 30 if board[2] == 'X' else x - 30, y if board[2] == '-' else y if board[2] == 'X' else y - 30)
    spot3.hideturtle() if board[2] == 'X' or board[2] == 'O' or gameType == 'SPECTATOR' else spot3.showturtle()
    spot3.pensize(10)
    spot3.pendown() if board[2] == 'X' or board[2] == 'O' else spot3.penup()
    spot3.speed(6 if board[2] == '-' or board[2] == 'X' else 0)
    if board[2] == '-':
        spot3.setheading(0)
        spot3.pencolor('black')
        spot3.fillcolor('green')
        spot3.turtlesize(4,7,1)
        spot3.onclick(lambda x, y: handleClick(spot=2))
    elif board[2] == 'X':
        for i in range(2):
            spot3.setheading(45 if i == 0 else 135)
            spot3.forward(30)
            spot3.backward(60)
            spot3.forward(30)
    elif board[2] == 'O':
        spot3.setheading(0)
        spot3.circle(30)
    else:
        print('Some weird error happened in setupSpot3() when reading board[2]')
    
def setupSpot4(x = -120, y = 80):
    spot4.speed(500)
    spot4.penup()
    spot4.hideturtle()
    spot4.goto(x if board[3] == '-' else x - 30 if board[3] == 'X' else x - 30, y if board[3] == '-' else y if board[3] == 'X' else y - 30)
    spot4.hideturtle() if board[3] == 'X' or board[3] == 'O' or gameType == 'SPECTATOR' else spot4.showturtle()
    spot4.pensize(10)
    spot4.pendown() if board[3] == 'X' or board[3] == 'O' else spot4.penup()
    spot4.speed(6 if board[3] == '-' or board[3] == 'X' else 0)
    if board[3] == '-':
        spot4.setheading(0)
        spot4.pencolor('black')
        spot4.fillcolor('green')
        spot4.turtlesize(4,7,1)
        spot4.onclick(lambda x, y: handleClick(spot=3))
    elif board[3] == 'X':
        for i in range(2):
            spot4.setheading(45 if i == 0 else 135)
            spot4.forward(30)
            spot4.backward(60)
            spot4.forward(30)
    elif board[3] == 'O':
        spot4.setheading(0)
        spot4.circle(30)
    else:
        print('Some weird error happened in setupSpot4() when reading board[3]')

def setupSpot5(x = 35, y = 80):
    spot5.speed(500)
    spot5.penup()
    spot5.hideturtle()
    spot5.goto(x if board[4] == '-' else x - 30 if board[4] == 'X' else x - 30, y if board[4] == '-' else y if board[4] == 'X' else y - 30)
    spot5.hideturtle() if board[4] == 'X' or board[4] == 'O' or gameType == 'SPECTATOR' else spot5.showturtle()
    spot5.pensize(10)
    spot5.pendown() if board[4] == 'X' or board[4] == 'O' else spot5.penup()
    spot5.speed(6 if board[4] == '-' or board[4] == 'X' else 0)
    if board[4] == '-':
        spot5.setheading(0)
        spot5.pencolor('black')
        spot5.fillcolor('green')
        spot5.turtlesize(4,7,1)
        spot5.onclick(lambda x, y: handleClick(spot=4))
    elif board[4] == 'X':
        for i in range(2):
            spot5.setheading(45 if i == 0 else 135)
            spot5.forward(30)
            spot5.backward(60)
            spot5.forward(30)
    elif board[4] == 'O':
        spot5.setheading(0)
        spot5.circle(30)
    else:
        print('Some weird error happened in setupSpot5() when reading board[4]')

def setupSpot6(x = 190, y = 80):
    spot6.speed(500)
    spot6.penup()
    spot6.hideturtle()
    spot6.goto(x if board[5] == '-' else x - 30 if board[5] == 'X' else x - 30, y if board[5] == '-' else y if board[5] == 'X' else y - 30)
    spot6.hideturtle() if board[5] == 'X' or board[5] == 'O' or gameType == 'SPECTATOR' else spot6.showturtle()
    spot6.pensize(10)
    spot6.pendown() if board[5] == 'X' or board[5] == 'O' else spot6.penup()
    spot6.speed(6 if board[5] == '-' or board[5] == 'X' else 0)
    if board[5] == '-':
        spot6.setheading(0)
        spot6.pencolor('black')
        spot6.fillcolor('green')
        spot6.turtlesize(4,7,1)
        spot6.onclick(lambda x, y: handleClick(spot=5))
    elif board[5] == 'X':
        for i in range(2):
            spot6.setheading(45 if i == 0 else 135)
            spot6.forward(30)
            spot6.backward(60)
            spot6.forward(30)
    elif board[5] == 'O':
        spot6.setheading(0)
        spot6.circle(30)
    else:
        print('Some weird error happened in setupSpot6() when reading board[5]')

def setupSpot7(x = -120, y = -70):
    spot7.speed(500)
    spot7.penup()
    spot7.hideturtle()
    spot7.goto(x if board[6] == '-' else x - 30 if board[6] == 'X' else x - 30, y if board[6] == '-' else y if board[6] == 'X' else y - 30)
    spot7.hideturtle() if board[6] == 'X' or board[6] == 'O' or gameType == 'SPECTATOR' else spot7.showturtle()
    spot7.pensize(10)
    spot7.pendown() if board[6] == 'X' or board[6] == 'O' else spot7.penup()
    spot7.speed(6 if board[6] == '-' or board[6] == 'X' else 0)
    if board[6] == '-':
        spot7.setheading(0)
        spot7.pencolor('black')
        spot7.fillcolor('green')
        spot7.turtlesize(4,7,1)
        spot7.onclick(lambda x, y: handleClick(spot=6))
    elif board[6] == 'X':
        for i in range(2):
            spot7.setheading(45 if i == 0 else 135)
            spot7.forward(30)
            spot7.backward(60)
            spot7.forward(30)
    elif board[6] == 'O':
        spot7.setheading(0)
        spot7.circle(30)
    else:
        print('Some weird error happened in setupSpot7() when reading board[6]')

def setupSpot8(x = 35, y = -70):
    spot8.speed(500)
    spot8.penup()
    spot8.hideturtle()
    spot8.goto(x if board[7] == '-' else x - 30 if board[7] == 'X' else x - 30, y if board[7] == '-' else y if board[7] == 'X' else y - 30)
    spot8.hideturtle() if board[7] == 'X' or board[7] == 'O' or gameType == 'SPECTATOR' else spot8.showturtle()
    spot8.pensize(10)
    spot8.pendown() if board[7] == 'X' or board[7] == 'O' else spot8.penup()
    spot8.speed(6 if board[7] == '-' or board[7] == 'X' else 0)
    if board[7] == '-':
        spot8.setheading(0)
        spot8.pencolor('black')
        spot8.fillcolor('green')
        spot8.turtlesize(4,7,1)
        spot8.onclick(lambda x, y: handleClick(spot=7))
    elif board[7] == 'X':
        for i in range(2):
            spot8.setheading(45 if i == 0 else 135)
            spot8.forward(30)
            spot8.backward(60)
            spot8.forward(30)
    elif board[7] == 'O':
        spot8.setheading(0)
        spot8.circle(30)
    else:
        print('Some weird error happened in setupSpot8() when reading board[7]')

def setupSpot9(x = 190, y = -70):
    spot9.speed(500)
    spot9.penup()
    spot9.hideturtle()
    spot9.goto(x if board[8] == '-' else x - 30 if board[8] == 'X' else x - 30, y if board[8] == '-' else y if board[8] == 'X' else y - 30)
    spot9.hideturtle() if board[8] == 'X' or board[8] == 'O' or gameType == 'SPECTATOR' else spot9.showturtle()
    spot9.pensize(10)
    spot9.pendown() if board[8] == 'X' or board[8] == 'O' else spot9.penup()
    spot9.speed(6 if board[8] == '-' or board[8] == 'X' else 0)
    if board[8] == '-':
        spot9.setheading(0)
        spot9.pencolor('black')
        spot9.fillcolor('green')
        spot9.turtlesize(4,7,1)
        spot9.onclick(lambda x, y: handleClick(spot=8))
    elif board[8] == 'X':
        for i in range(2):
            spot9.setheading(45 if i == 0 else 135)
            spot9.forward(30)
            spot9.backward(60)
            spot9.forward(30)
    elif board[8] == 'O':
        spot9.setheading(0)
        spot9.circle(30)
    else:
        print('Some weird error happened in setupSpot9() when reading board[8]')

def showTurnValue(message, alignment, font, x, y, r, g, b):
    global screen
    turnValueTurtle.speed(500)
    turnValueTurtle.penup()
    turnValueTurtle.goto(x, y)
    screen.colormode(255)
    turnValueTurtle.pencolor(r, g, b)
    turnValueTurtle.write(message, align=alignment, font=font)

def showTurnTitle(message, alignment, font, x, y, r, g, b):
    global screen
    turnTitle.speed(500)
    turnTitle.penup()
    turnTitle.goto(x, y)
    screen.colormode(255)
    turnTitle.pencolor(r, g, b)
    turnTitle.write(message, align=alignment, font=font)

def checkIfWon():
    global board
    global gameWon
    global playerThatWon
    global endGame_lineDrawer
    #Check if X has won in either diagonal direction
    if board[0] == 'X' and board[4] == 'X' and board[8] == 'X' or board[2] == 'X' and board[4] == 'X' and board[6] == 'X':
        gameWon = True
        playerThatWon = 'X'
        print('X has won. They got 3 diagonally')
        if board[0] == 'X' and board[4] == 'X' and board[8] == 'X':
            endGame_lineDrawer = [boardXAndY[0][0], boardXAndY[0][1], 'Diagonal', boardXAndY[8][0], boardXAndY[8][1]]
        else:
            endGame_lineDrawer = [boardXAndY[2][0], boardXAndY[2][1], 'Diagonal-Left', boardXAndY[6][0], boardXAndY[6][1]]
    
    #Check if O has won in either diagonal direction
    if board[0] == 'O' and board[4] == 'O' and board[8] == 'O' or board[2] == 'O' and board[4] == 'O' and board[6] == 'O':
        gameWon = True
        playerThatWon = 'O'
        print('O has won. They got 3 diagonally')
        if board[0] == 'O' and board[4] == 'O' and board[8] == 'O':
            endGame_lineDrawer = [boardXAndY[0][0], boardXAndY[0][1], 'Diagonal', boardXAndY[8][0], boardXAndY[8][1]]
        else:
            endGame_lineDrawer = [boardXAndY[2][0], boardXAndY[2][1], 'Diagonal-Left', boardXAndY[6][0], boardXAndY[6][1]]

    #Check if X has won in either vertical directions
    if board[0] == 'X' and board[3] == 'X' and board[6] == 'X' or board[1] == 'X' and board[4] == 'X' and board[7] == 'X' or board[2] == 'X' and board[5] == 'X' and board[8] == 'X':
        gameWon = True
        playerThatWon = 'X'
        print('X has won. They got 3 vertically')
        if board[0] == 'X' and board[3] == 'X' and board[6] == 'X':
            endGame_lineDrawer = [boardXAndY[0][0], boardXAndY[0][1], 'Vertical', boardXAndY[6][0], boardXAndY[6][1]]
        elif board[1] == 'X' and board[4] == 'X' and board[7] == 'X':
            endGame_lineDrawer = [boardXAndY[1][0], boardXAndY[1][1], 'Vertical', boardXAndY[7][0], boardXAndY[7][1]]
        else:
            endGame_lineDrawer = [boardXAndY[2][0], boardXAndY[2][1], 'Vertical', boardXAndY[8][0], boardXAndY[8][1]]

    #Check if O has won in either vertical directions
    if board[0] == 'O' and board[3] == 'O' and board[6] == 'O' or board[1] == 'O' and board[4] == 'O' and board[7] == 'O' or board[2] == 'O' and board[5] == 'O' and board[8] == 'O':
        gameWon = True
        playerThatWon = 'O'
        print('O has won. They got 3 vertically')
        if board[0] == 'O' and board[3] == 'O' and board[6] == 'O':
            endGame_lineDrawer = [boardXAndY[0][0], boardXAndY[0][1], 'Vertical', boardXAndY[6][0], boardXAndY[6][1]]
        elif board[1] == 'O' and board[4] == 'O' and board[7] == 'O':
            endGame_lineDrawer = [boardXAndY[1][0], boardXAndY[1][1], 'Vertical', boardXAndY[7][0], boardXAndY[7][1]]
        else:
            endGame_lineDrawer = [boardXAndY[2][0], boardXAndY[2][1], 'Vertical', boardXAndY[8][0], boardXAndY[8][1]]

    #Check if X has won in either horizontal directions
    if board[0] == 'X' and board[1] == 'X' and board[2] == 'X' or board[3] == 'X' and board[4] == 'X' and board[5] == 'X' or board[6] == 'X' and board[7] == 'X' and board[8] == 'X':
        gameWon = True
        playerThatWon = 'X'
        print('X has won. They got 3 horizontally')
        if board[0] == 'X' and board[1] == 'X' and board[2] == 'X':
            endGame_lineDrawer = [boardXAndY[0][0], boardXAndY[0][1], 'Horizontal', boardXAndY[2][0], boardXAndY[2][1]]
        elif board[3] == 'X' and board[4] == 'X' and board[5] == 'X':
            endGame_lineDrawer = [boardXAndY[3][0], boardXAndY[3][1], 'Horizontal', boardXAndY[5][0], boardXAndY[5][1]]
        else:
            endGame_lineDrawer = [boardXAndY[6][0], boardXAndY[6][1], 'Horizontal', boardXAndY[8][0], boardXAndY[8][1]]

    
    #Check if O has won in either horizontal directions
    if board[0] == 'O' and board[1] == 'O' and board[2] == 'O' or board[3] == 'O' and board[4] == 'O' and board[5] == 'O' or board[6] == 'O' and board[7] == 'O' and board[8] == 'O':
        gameWon = True
        playerThatWon = 'O'
        print('O has won. They got 3 horizontally')
        if board[0] == 'O' and board[1] == 'O' and board[2] == 'O':
            endGame_lineDrawer = [boardXAndY[0][0], boardXAndY[0][1], 'Horizontal', boardXAndY[2][0], boardXAndY[2][1]]
        elif board[3] == 'O' and board[4] == 'O' and board[5] == 'O':
            endGame_lineDrawer = [boardXAndY[3][0], boardXAndY[3][1], 'Horizontal', boardXAndY[5][0], boardXAndY[5][1]]
        else:
            endGame_lineDrawer = [boardXAndY[6][0], boardXAndY[6][1], 'Horizontal', boardXAndY[8][0], boardXAndY[8][1]]

def showRestartYesButton():
    restartYesButton.speed(500)
    restartYesButton.penup()
    restartYesButton.goto(-200, -240)
    restartYesButton.write('Yes', align='center', font=('Arial', 30, 'bold'))
    restartYesButton.goto(-160, -270)
    restartYesButton.turtlesize(5, 9, 1)
    restartYesButton.fillcolor('green')
    restartYesButton.pencolor('black')
    restartYesButton.showturtle()
    restartYesButton.onclick(lambda x, y: restartYesButtonHandleClick())

def showRestartNoButton():
    restartNoButton.speed(500)
    restartNoButton.penup()
    restartNoButton.goto(200, -240)
    restartNoButton.write('No', align='center', font=('Arial', 30, 'bold'))
    restartNoButton.goto(160, -270)
    restartNoButton.setheading(180)
    restartNoButton.turtlesize(5, 9, 1)
    restartNoButton.fillcolor('red')
    restartNoButton.pencolor('black')
    restartNoButton.showturtle()
    restartNoButton.onclick(lambda x, y: restartNoButtonHandleClick())

def restartYesButtonHandleClick():
    if gameType == 'Local':
        global isGamePlaying
        isGamePlaying = False
        endGame_lineDrawer_turtle.clear()
        restartNoButton.hideturtle()
        restartNoButton.clear()
        restartYesButton.hideturtle()
        restartYesButton.clear()
        turnValueTurtle.clear()
        turnTitle.clear()
        global board, currentTurn
        board = ['-', '-', '-',
                '-', '-', '-',
                '-', '-', '-']
        global numOfClicks
        global gameWon
        global multiplayerGameHasStarted
        multiplayerGameHasStarted = False
        gameWon = False
        numOfClicks = 0
        currentTurn = 'X'
        boardTurtle.clear()
        spot1.clear()
        spot2.clear()
        spot3.clear()
        spot4.clear()
        spot5.clear()
        spot6.clear()
        spot7.clear()
        spot8.clear()
        spot9.clear()
        introduction()
    else:
        broadcast('GAME_RESTARTING')
        clearEverythingAndRestartGame()
        

def restartNoButtonHandleClick():
    global playerThatWon
    global numOfClicks
    restartNoButton.hideturtle()
    restartNoButton.clear()
    restartYesButton.hideturtle()
    restartYesButton.clear()
    turnValueTurtle.clear()
    turnTitle.clear()
    broadcast('GAME_NOT_RESTARTING')
    showTurnValue('Restart will not happen', 'center', ('Arial', 30, 'bold'), 0, -260, 255, 0, 0)
    time.sleep(1)
    turnValueTurtle.clear()
    if numOfClicks != 9:
        showTurnValue(playerThatWon + ' won!', 'center', ('Arial', 60, 'bold'), 0, -260, 0, 0, 0)
    else:
        showTurnValue('Both players have tied! Congratulations!', 'center', ('Arial', 30, 'bold'), 0, -260, 0, 0, 0)

def clearEverythingAndRestartGame():
    global board, currentTurn, numOfClicks, gameWon, endGame_lineDrawer, playerThatWon, allowDrawing
    allowDrawing = False
    board = ['-', '-', '-',
            '-', '-', '-',
            '-', '-', '-']
    currentTurn = 'X'
    numOfClicks = 0
    gameWon = False
    endGame_lineDrawer = None
    playerThatWon = None
    boardTurtle.clear()
    endGame_lineDrawer_turtle.clear()
    spot1.clear()
    spot2.clear()
    spot3.clear()
    spot4.clear()
    spot5.clear()
    spot6.clear()
    spot7.clear()
    spot8.clear()
    spot9.clear()
    spot1.hideturtle()
    spot2.hideturtle()
    spot3.hideturtle()
    spot4.hideturtle()
    spot5.hideturtle()
    spot6.hideturtle()
    spot7.hideturtle()
    spot8.hideturtle()
    spot9.hideturtle()
    restartNoButton.hideturtle()
    restartNoButton.clear()
    restartYesButton.hideturtle()
    restartYesButton.clear()
    turnValueTurtle.clear()
    turnTitle.clear()
    startGame()


introduction()
global screen
screen = Screen()
screen.mainloop()