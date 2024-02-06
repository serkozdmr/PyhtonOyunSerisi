import random
import pygame
#Paketleri baslattık
pygame.init()
GENISLIK = 640
YUKSEKLIK = 780

pencere = pygame.display.set_mode((GENISLIK, YUKSEKLIK))
#penceremizi olusturduk

#pygame.mixer.music.load("oyunarkaplanmp3")
#pygame.mixer.music.play(-1,0,0)

#FPS ayarlama
HIZ = 10
FPS = 27
saat = pygame.time.Clock()

#Karakter ve yem tanımlama
canavar1 = pygame.image.load("monster.png")
canavar_koordinat = canavar1.get_rect()
canavar_koordinat.topleft = (320,390)
#canavar2 = pygame.image.load("monster2.png")
yem = pygame.image.load("dollar.png")
yem_koordinat = yem.get_rect()
yem_koordinat.topleft = (150,150)

arkaplan = pygame.image.load("arkaplan1.jpg")
arkaplan = pygame.transform.scale(arkaplan,(GENISLIK, YUKSEKLIK))
#Font ayarları
FONT = pygame.font.SysFont("consolas", 64)
#Skor
Skor = 0
#Oyun Döngüsü
durum = True
while durum:
    for etkinlik in pygame.event.get():
        if etkinlik.type == pygame.QUIT:
            durum = False
    pencere.blit(arkaplan,(0,0))

    pencere.blit(canavar1, canavar_koordinat)
    pencere.blit(yem, yem_koordinat)
    YAZI = FONT.render("skor: "+str(Skor),(255,255,255),(0,0,0))
    yazi_koordinat = YAZI.get_rect()
    yazi_koordinat.topleft = (20,20)
    pygame.draw.line(pencere,(255,0,255), (0,100),(640,100),3)
    pencere.blit(YAZI, yazi_koordinat)

    tus = pygame.key.get_pressed()
    if tus[pygame.K_LEFT] and canavar_koordinat.x > 0:
        canavar_koordinat.x -= HIZ
    elif tus[pygame.K_RIGHT] and canavar_koordinat.x < 620:
        canavar_koordinat.x += HIZ
    elif tus[pygame.K_UP] and canavar_koordinat.y > 100:
        canavar_koordinat.y -= HIZ
    elif tus[pygame.K_DOWN] and canavar_koordinat.y < 755:
        canavar_koordinat.y += HIZ
    if canavar_koordinat.colliderect(yem_koordinat):
        Skor += 1
        yem_koordinat.x = random.randint(0,GENISLIK)
        yem_koordinat.y = random.randint(100,YUKSEKLIK)


    pygame.display.update()
    saat.tick(FPS)