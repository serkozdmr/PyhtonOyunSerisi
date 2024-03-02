import random
import  pygame
pygame.init()
GENISLIK, YUKSEKLIK = 780,640
pencere = pygame.display.set_mode((GENISLIK, YUKSEKLIK))
#Sınıflar
class oyun():
    def __init__(self,balikci,balik_grup):
        self.balikci = balikci
        self.balik_grup = balik_grup
        #Oyun Değişkenleri
        self.sure = 0
        self.fps_degeri_sayac = 0
        self.bolum_no = 0
        #Balıklar
        balik1 = pygame.image.load("balik1.png")
        balik2 = pygame.image.load("balik2.png")
        balik3 = pygame.image.load("balik3.png")
        balik4 = pygame.image.load("balik4.png")
        self.balik_liste = [balik1,balik2,balik3,balik4]
        self.balik_liste_index_no = random.randint(0,3)
        self.hedef_balik_goruntu = self.balik_liste[self.balik_liste_index_no]
        self.hedef_balik_konum = self.hedef_balik_goruntu.get_rect()
        self.hedef_balik_konum.top = 40
        self.hedef_balik_konum.centerx = GENISLIK//2
        # Oyun fontu
        self.oyun_fontu = pygame.font.Font("oyun_font.ttf",40)
        # Oyun Arka Plan
        #self.oyun_arka_plan = pygame.image.load("arka_plan.jpg")
        self.oyun_bitti = pygame.image.load("oyun_sonu.jpg")

    def update(self):
        self.fps_degeri_sayac += 1
        if self.fps_degeri_sayac  == FPS:
            self.sure += 1
            self.fps_degeri_sayac = 0
        self.temas()

    def cizdir(self):
        metin1 = self.oyun_fontu.render("Süre: "+str(self.sure),True,(255,255,255) )
        metin1_konum = metin1.get_rect()
        metin1_konum.top = 30
        metin1_konum.left = 30
        pencere.blit(metin1,metin1_konum)
        pencere.blit(self.hedef_balik_goruntu, self.hedef_balik_konum)

        metin2 = self.oyun_fontu.render("can: " +str(self.balikci.can),True,(255,255,255) )
        metin2_konum = metin2.get_rect()
        metin2_konum.top = 20
        metin2_konum.left = GENISLIK - 125
        pencere.blit(metin2,metin2_konum)
        pygame.draw.rect(pencere,(255,255,255),(360,30,50,50),5)
        pygame.draw.rect(pencere,(255,0,255),(0,100,780,YUKSEKLIK-150),5)

        #pencere.blit(self.oyun_arka_plan, (0,0))
    def temas(self):
        temas_oldumu = pygame.sprite.spritecollideany(self.balikci, self.balik_grup)
        if temas_oldumu:
            if temas_oldumu.type == self.balik_liste_index_no:
                temas_oldumu.remove(self.balik_grup)
                if self.balik_grup :
                    self.hedef_yenile()
                else:
                    self.hedefle()

            else :
                self.balikci.can -=1
                self.guvenli_alan()
                if self.balikci.can == 0:
                    self.durdurma()



    def durdurma(self):
        pass
    def reset(self):
        pass
    def guvenli_alan(self):
        pass
    def hedef_yenile(self):
        hedef_balik = random.choice(self.balik_grup.sprites())
        self.hedef_balik_goruntu = hedef_balik.image
        self.balik_liste_index_no = hedef_balik.tip

    def hedefle(self):
        pass

class balik(pygame.sprite.Sprite):
    def __init__(self,x,y,resim,tip):
        super().__init__()
        self.image = resim
        self.rect = self.image.get_rect()
        self.rect.topleft = (x,y)
        self.tip = tip
        self.hiz = random.randint(1,5)
        self.yonx = random.choice([-1,1])
        self.yony = random.choice([-1,1])



    def update(self):
        self.rect.x += self.hiz * self.yonx
        self.rect.y += self.hiz * self.yony
        if self.rect.left <= 0 or self.rect.right >= GENISLIK:
            self.yonx *= -1
        if self.rect.top <= 0 or self.rect.bottom >= YUKSEKLIK:
            self.yony *= -1

class Balikci(pygame.sprite.Sprite):
    def __init__(self,x,y):
        super().__init__()
        self.image = pygame.image.load("balikci.png")
        self.rect = self.image.get_rect()
        self.rect.center = (x,y)
        self.can = 3
        self.hiz = 20
    def update(self):
        self.hareket()
    def hareket(self):
        tus = pygame.key.get_pressed()
        if tus[pygame.K_LEFT] and self.rect.left > 0:
            self.rect.x -= self.hiz
        elif tus[pygame.K_RIGHT] and self.rect.right < 760:
            self.rect.x += self.hiz
        elif tus[pygame.K_UP] and self.rect.top > 0:
            self.rect.y -= self.hiz
        elif tus[pygame.K_DOWN] and self.rect.bottom < 620:
            self.rect.y += self.hiz

#Ana karakter grup işlemleri
Balikci.grup =pygame.sprite.Group()
balikci = Balikci(GENISLIK//2, YUKSEKLIK//2)
Balikci.grup.add(balikci)
#Balık test
balik_grup = pygame.sprite.Group()
balik1 = pygame.image.load("balik1.png")
balik = balik(random.randint(0,GENISLIK-32), random.randint(0,YUKSEKLIK-32),balik1,0)
balik_grup.add(balik)
balik2 = pygame.image.load("balik2.png")
#balik = balik(random.randint(0,GENISLIK-32), random.randint(0,YUKSEKLIK-32),balik2,0)
balik_grup.add(balik)
#Oyun Sınıfı
oyun = oyun(balikci,balik_grup)

#FPS Ayarları
FPS = 20
saat = pygame.time.Clock()

durum = True
while durum:
    for etkinlik in pygame.event.get():
        if etkinlik.type == pygame.QUIT:
            durum = False
    pencere.fill((0,0,0))
    #Balıkçı çizdirme ve güncelleme
    balikci.grup.update()
    balikci.grup.draw(pencere)
    #Oyun güncelleme
    oyun.update()
    oyun.cizdir()
    oyun.oyun_fontu
    #balık Test
    balik_grup.update()
    balik_grup.draw(pencere)
    pygame.display.update()
    #hedef balık test

    saat.tick(FPS)
pygame.quit()

