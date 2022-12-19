import pygame,random,time

def aggiornaSchermo():
    global FPS
    pygame.display.update() #aggiorno il display
    pygame.time.Clock().tick(FPS) #frame di aggiornamento

    
def moviment():
    global screen,rectX,rectY,snake
    color=(68, 155, 172) #scelgo il colore dello sfondo
    screen.fill(color) #imposto il colore allo sfondo

    for cube in snake:  
        pygame.draw.rect(screen,(0,255,0),[cube[0],cube[1],dimRX,dimRY]) #disegno un rettangolo (dove,colore,[posx,posy,width,heitgth)
        pygame.draw.rect(screen,(255,0,0),[pallX,pallY,dimRX-4,dimRY-4]) #disegno il cerchio (dove,colore,[posizione],raggio,colore interno)
    punteggio = text.render("POINT: "+str((lungehzza-1)*3), True, (0,0,255)) #stampo a video il punteggio
    punteggio = pygame.transform.scale(punteggio, (100, 30)) #ridimensiono il testo
    screen.blit(punteggio, (width-140, 10))#posizione testo
    


def pallinoRand():
    global screen,pallX,pallY,rectX,rectY
    pallX=random.randint(20,width-20) #genero una x casuale
    pallY=random.randint(20,heigth-20) #genero una y casuale
    
    
def collision():
    global pallX,pallY,rectX,rectY,genera,lungehzza,snake,eatSound
        
    if pallX+10>=rectX and pallX<=rectX and pallY+10>=rectY and pallY<=rectY or pallX-10<=rectX and pallX>=rectX and pallY-10<=rectY and pallY>=rectY: #se il rettangolo si trova vicino al pallino
        if musica=="si":
            collisionSound()
        genera="si" #genero un nuovo pallino
        lungehzza+=4

           
def gameOver():
    global snake,rectX,rectY

    for cube in snake[:-1]: # se i cubi del serpente si toccano (a parte la testa)
        if rectX==cube[0] and rectY==cube[1]: #se la coordinata di almeno un cubo coincide con la testa
            loser() #perdi

def loser():
    global gameover,pausa
    screen.blit(gameover,(150,65)); #stampo l'immagine di pausa
    if musica=="si":
        gameoverSound() #suoni di gameover
    pausa="pausa" #blocco i prossimi aggiornamenti
    aggiornaSchermo() #faccio vedere l'immagine
    azzera() #torno allo start del gioco
    time.sleep(3)
    pausa="start"
    if musica=="si":
        music()


def pausaG():
    global pause,pausa,gameover,musica
    pygame.mixer.music.stop() #pausa
    if musica=="si":
        pauseOnSound()
    screen.blit(pause,(140,70)); #stampo l'immagine di pausa
    pausa="pausa" #blocco i prossimi aggiornamenti
    aggiornaSchermo() #faccio vedere l'immagine
    time.sleep(1)
    
    
def azzera():
    global rectX,rectY,genera,lungehzza,snake,muovi,dimRX,dimRY
    rectX=310 #posizione iniziale rettangolo
    rectY=250 
    dimRX=13 #dimensioni iniziali larghezza rettangolo
    dimRY=13 #dimensione iniziali altezza rettangolo
    lungehzza=1 #dim iniziale
    snake=[] #azzero il serpente
    genera="no" #all'avvio genera il pallino
    muovi="su" #all'avvio si muove verso l'alto
    

def music():
    global musica
    musica="si" #flag attiva
    pygame.mixer.pre_init(44100,16,2,4096) #inizializzo la musica (frequenza,ampiezza,canale,buffer)
    pygame.mixer.music.load("music/colonna.mp3") #colonna musicale
    pygame.mixer.music.set_volume(0.8)
    pygame.mixer.music.play(-1) #avvio in loop


def gameoverSound():
    global overSound
    pygame.mixer.music.stop() #stop loop
    musica="no" #flag musica disattivata
    pygame.mixer.Sound.play(overSound) #riproduci il gameover
    time.sleep(3) #dopo 3 sec compare la scritta di game over

   
def collisionSound():
    global eatSound
    pygame.mixer.Sound.play(eatSound) #riproduci

def pauseOnSound():
    global pauseOn
    pygame.mixer.Sound.play(pauseOn) #quando si mette pausa

def pauseOffSound():
    global pauseOff
    pygame.mixer.Sound.play(pauseOff) #quando si esce dalla pausa

def musiControll():
    global pausa
    if pausa=="pausa": #qualsiasi tasto che non sia p toglie la pausa
        if musica=="si": #se la musica è attiva fa gli effeti audio
            pauseOffSound()
            time.sleep(1)
            music() #e parte la musica
        else:
            time.sleep(1)
            

pygame.init() #inizializzo pygame e i suoi metodi
    
width=540 #larghezza schermo
heigth=400 #altezza schermo

screen = pygame.display.set_mode((width, heigth))#dimensione finestra
pygame.display.set_caption("SNAKE!") #titolo della finestra



FPS=60 #frame di aggioramento

rectX=310 #posizione iniziale rettangolo
rectY=250 
dimRX=13 #dimensioni iniziali larghezza rettangolo
dimRY=13 #dimensione iniziali altezza rettangolo

snake=[] #lista che conterrà tutto il serpente
lungehzza=1 #lunghezza iniziale del serpente

text = pygame.font.SysFont(None, 48)



pause = pygame.image.load("image/pause.png") #carico l'immagine di pausa
pause = pygame.transform.scale(pause, (250, 250))
gameover = pygame.image.load("image/gameover.png") #carico l'immagine di pausa
gameover = pygame.transform.scale(gameover, (250, 250))

eatSound = pygame.mixer.Sound("music/collision.wav") #suono di collisione
eatSound.set_volume(0.2) #livello volume
pauseOn = pygame.mixer.Sound("music/pauseOn.wav")
eatSound.set_volume(0.3) #livello volume
pauseOff = pygame.mixer.Sound("music/pauseOff.wav")
eatSound.set_volume(0.3) #livello volume
overSound = pygame.mixer.Sound("music/overSound.wav") #suono di gameover

genera="no" #all'avvio genera il pallino
muovi="su" #all'avvio si muove verso l'alto

speed=5

pallinoRand() #genero il pallino iniziale
moviment()#faccio disegnare il rettangolo insieme allo schermo
music() #avio la colonna musicale
pausaG()#metto in pausa all'avvio del gioco

ascolta=True #ciclo sempre vero

while ascolta: #while in cui ascolto qualsiasi evento
    
    if rectX>width: #se va oltre la larghezza schermo
        rectX=0 
    if rectX<0:
        rectX=width
    if rectY>heigth: #se va oltre l' altezza schermo
        rectY=0
    if rectY<0: 
        rectY=heigth
        
    
    
    for event in pygame.event.get(): #scorro tutti gli eventi che accadono
        if event.type == pygame.KEYDOWN: #alla pressione di un tasto della tastiera

            if event.key == pygame.K_RIGHT and muovi!="sinistra": #se il tasto è uguale a
                muovi="destra"
                musiControll()
                pausa="start"#quando viene premuto un tasto mette start
                
            if event.key == pygame.K_DOWN and muovi!="su": #se il tasto è uguale a
                muovi="giu"
                musiControll()
                pausa="start"#quando viene premuto un tasto mette start
                
            if event.key == pygame.K_UP and muovi!="giu": #se il tasto è uguale a
                muovi="su"
                musiControll()
                pausa="start"#quando viene premuto un tasto mette start
              
            if event.key == pygame.K_LEFT and muovi!="destra": #se il tasto è uguale a
                muovi="sinistra"
                musiControll()
                pausa="start"#quando viene premuto un tasto mette start
                
            
            if event.key == pygame.K_m and musica=="si": #se il tasto è uguale a
                pygame.mixer.music.stop() #muto
                musica="no"

            elif event.key == pygame.K_m and musica=="no": #se il tasto è uguale a
                music()  #avvio il loop
            
   
            if event.key == pygame.K_p and pausa=="start": #se il tasto è uguale a p e il gioco è in movimento
                pausaG()#metti in pausa
                
                         
                
        if event.type == pygame.QUIT:#se viene premuta la x 
            ascolta=False #interrompo il ciclo
    
    if pausa=="start": #se il gioco non è messo in pausa

        collision() #indivdua le collisioni tra palla e serpente
        aggiornaSchermo() #aggiornamento dello schermo
        snakeXY=[] #prendo le coordinate del serpente e le salvo in questa lista
        snakeXY.append(rectX)
        snakeXY.append(rectY)
        snake.append(snakeXY) #nel serpente salvo ogni movimento che ha fatto fino adesso
        moviment() #disegna gli oggetti
        if len(snake) > lungehzza: #cancello il primo cubo disegnato
            del snake[0]
            
        gameOver() # controllo se c'è stato il gameover
        
        
        if genera=="si": #se deve generare il pallino
            pallinoRand() #lo genera
            genera="no" #non genera altri pallini

        if muovi=="destra":
            rectX+=speed #velocità destra
        elif muovi=="giu":
            rectY+=speed #velocità basso
        elif muovi=="su":
            rectY-=speed #velocità alto
        elif muovi=="sinistra":
            rectX-=speed #velocità sinistra




pygame.quit() # chiudo tutto



    











