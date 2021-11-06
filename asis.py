import speech_recognition as sr # konuşmayı tanımak
import playsound # bir ses dosyası çalmak için
from gtts import gTTS # google metin okuma
import random
from time import ctime # zaman ayrıntılarını al
import webbrowser # Tarayıcı aç
import ssl
import certifi
import time
import os # oluşturulan ses dosyalarını kaldırmak için
from PIL import Image
import subprocess
import pyautogui # ekran görüntüsü
import pyttsx3
import bs4 as bs
import urllib.request
import requests

class person:
    name = ''
    def setName(self, name):
        self.name = name

class asis:
    name = ''
    def setName(self, name):
        self.name = name



def there_exists(terms):
    for term in terms:
        if term in voice_data:
            return True

def engine_speak(text):
    text = str(text)
    engine.say(text)
    engine.runAndWait()

r = sr.Recognizer() # tanıyıcıyı başlatmak
# sesi dinleyin ve metne dönüştürün:
def record_audio(ask=""):
    with sr.Microphone() as source: # kaynak olarak mikrofon
        if ask:
            engine_speak(ask)
        audio = r.listen(source, 5, 5)  #sesi kaynak üzerinden dinle
        print("Dinleme Bitti")
        voice_data = ''
        try:
            voice_data = r.recognize_google(audio)  # sesi metne dönüştür
        except sr.UnknownValueError: # hata: tanıyıcı anlamıyor
            engine_speak('Ne demek istediğini anlamadım.')
        except sr.RequestError:
            engine_speak('Maalesef hizmet çalışmıyor') # hata: tanıyıcı bağlı değil
        print(">>", voice_data.lower()) # kullanıcının söylediğini yazdır
        return voice_data.lower()

# dizgi alın ve çalınacak bir ses dosyası oluşturun
def engine_speak(audio_string):
    audio_string = str(audio_string)
    #ASİSTAN DİLİNİ DEĞİŞTİRMEK İÇİN KULLANILACAK SATIR ALTTADIR ---------------------------
    
    tts = gTTS(text=audio_string, lang='tr') # metin okuma (ses)

    #ASİSTAN DİLİNİ DEĞİŞTİRMEK İÇİN KULLANILACAK SATIR ÜSTTEDİR ---------------------------
    r = random.randint(1,20000000)
    audio_file = 'audio' + str(r) + '.mp3'
    tts.save(audio_file) # mp3 olarak kaydet
    playsound.playsound(audio_file) # ses dosyasını çal
    print(asis_obj.name + ":", audio_string) # uygulamanın ne dediğini yazdır
    os.remove(audio_file) # ses dosyasını kaldır

def respond(voice_data):
    # 1: selamlama
    if there_exists(['selam','merhaba','hey']):
        greetings = ["hey, Size nasıl yardım edebilirim?" + person_obj.name, "hey, naber?" + person_obj.name, "dinliyorum" + person_obj.name, "size nasıl yardım edebilirim?" + person_obj.name, "merhaba" + person_obj.name]
        greet = greetings[random.randint(0,len(greetings)-1)]
        engine_speak(greet)

    # 2: isim
    if there_exists(["adın ne","adınız ne","bana adını söyle"]):

        if person_obj.name:
            engine_speak(f"benim ismim {asis_obj.name}, {person_obj.name}") # kullanıcıların adını ses girişinden alır.
        else:
            engine_speak(f"benim ismim {asis_obj.name}. adınız ne?") # ismini vermediysen.

    if there_exists(["benim ismim"]):
        person_name = voice_data.split("is")[-1].strip()
        engine_speak("okay, i will remember that " + person_name)
        person_obj.setName(person_name) # kişi nesnesindeki adı hatırla
    
    if there_exists(["benim adım ne"]):
        engine_speak("senin adın sanırım " + person_obj.name + " olmalı")
    
    if there_exists(["hay aksi senin adın neydi, hatırlamaya çalışayım."]):
        asis_name = voice_data.split("be")[-1].strip()
        engine_speak("heh sonunda, senin adın sanırım" + asis_name)
        asis_obj.setName(asis_name) # asis nesnesindeki adı hatırla

    # 3: Hal-Hatır sorma
    if there_exists(["nasilsin","naber"]):
        engine_speak("çok iyiyim sorduğun için teşekkürler " + person_obj.name)

    # 4: saat
    if there_exists(["saat kaç","bana zamanı söyle","saat kaç","saat kaç"]):
        time = ctime().split(" ")[3].split(":")[0:2]
        if time[0] == "00":
            hours = '12'
        else:
            hours = time[0]
        minutes = time[1]
        time = hours + " saat ve " + minutes + "dakika"
        engine_speak(time)

    # 5: Google'da ara
    if there_exists(["bunu arat"]) and 'youtube' not in voice_data:
        search_term = voice_data.split("for")[-1]
        url = "https://google.com/search?q=" + search_term
        webbrowser.get().open(url)
        engine_speak("işte google'da " + search_term + "için bulduklarım.")
    
    if there_exists(["bunu arat"]) and 'youtube' not in voice_data:
        search_term = voice_data.replace("search","")
        url = "https://google.com/search?q=" + search_term
        webbrowser.get().open(url)
        engine_speak("işte google'da " + search_term + "için bulduklarım.")

    # 6: youtube'da ara Kullanımı = Aratmak istediğin kavram + youtube
    if there_exists(["youtube"]):
        search_term = voice_data.split("for")[-1]
        search_term = search_term.replace("on youtube","").replace("search","")
        url = "https://www.youtube.com/results?search_query=" + search_term
        webbrowser.get().open(url)
        engine_speak("işte YouTube'da " + search_term + "için bulduklarım.")

     #7: hisse senedi fiyatı al
    if there_exists(["fiyat söyle"]):
        search_term = voice_data.split("for")[-1]
        url = "https://google.com/search?q=" + search_term
        webbrowser.get().open(url)
        engine_speak("işte google'da " + search_term + "için bulduklarım.")
    
     #8 Duvar Kağıdı
    if there_exists(["duvar kağıdımı göster"]):
        im = Image.open(r"C:\Kullanıcılar\yusuf\Walpapers\walpaper.jpg")
        im.show()
    
     #9 weather
    if there_exists(["hava durumu"]):
        search_term = voice_data.split("for")[-1]
        url = "https://www.google.com/search?sxsrf=ACYBGNSQwMLDByBwdVFIUCbQqya-ET7AAA%3A1578847393212&ei=oUwbXtbXDN-C4-EP-5u82AE&q=weather&oq=weather&gs_l=psy-ab.3..35i39i285i70i256j0i67l4j0i131i67j0i131j0i67l2j0.1630.4591..5475...1.2..2.322.1659.9j5j0j1......0....1..gws-wiz.....10..0i71j35i39j35i362i39._5eSPD47bv8&ved=0ahUKEwiWrJvwwP7mAhVfwTgGHfsNDxsQ4dUDCAs&uact=5"
        webbrowser.get().open(url)
        engine_speak("hava durumu için google'da bunları buldum")
     

     #10 stone paper scisorrs
    if there_exists(["let's play"]):
        voice_data = record_audio("taş, kağıt veya makas arasından seçim yapın")
        moves=["taş", "kağıt", "makas"]
    
        cmove=random.choice(moves)
        pmove=voice_data
        

        engine_speak("Bilgisayar " + cmove + "ı seçti")
        engine_speak("Senin seçimin " + pmove)
        #engine_speak("hi")
        if pmove==cmove:
            engine_speak("maç berabere bitti")
        elif pmove== "taş" and cmove== "makas":
            engine_speak("sen kazandın")
        elif pmove== "taş" and cmove== "kağıt":
            engine_speak("ben kazandım haha")
        elif pmove== "kağıt" and cmove== "taş":
            engine_speak("sen kazandın")
        elif pmove== "kağıt" and cmove== "makas":
            engine_speak("ben kazandım haha")
        elif pmove== "makas" and cmove== "kağıt":
            engine_speak("sen kazandın")
        elif pmove== "makas" and cmove== "taş":
            engine_speak("ben kazandım haha")

     # 11 Bir yazı tura at
    if there_exists(["para","çevir","yazı tura"]):
        moves=["Yazi", "Tura"]   
        cmove=random.choice(moves)
        engine_speak("bilgisayar " + cmove +"yı seçti")

     # 12 hesap makinesi
    if there_exists(["artı","eksi","çarp","böl","üs","+","-","*","/"]):
        opr = voice_data.split()[1]

        if opr == '+':
            engine_speak(int(voice_data.split()[0]) + int(voice_data.split()[2]))
        elif opr == '-':
            engine_speak(int(voice_data.split()[0]) - int(voice_data.split()[2]))
        elif opr == 'çarp' or 'x':
            engine_speak(int(voice_data.split()[0]) * int(voice_data.split()[2]))
        elif opr == 'böl':
            engine_speak(int(voice_data.split()[0]) / int(voice_data.split()[2]))
        elif opr == 'üs':
            engine_speak(int(voice_data.split()[0]) ** int(voice_data.split()[2]))
        else:
            engine_speak("Yanlış Operatör")
        
     # 13 ekran görüntüsü
    if there_exists(["yakala","ss","ekran görüntüsü","benim ekranım"]):
        engine_speak("ekran görüntüsü screenshot klasörüne kaydedildi")
        myScreenshot = pyautogui.screenshot()
        myScreenshot.save('D:/screenshot/screen.png')
    
    
     # 14 Tanım için Wikipedia'da Arama Yapmak İçin
    if there_exists(["tanım"]):
        definition=record_audio("neyin tanımına ihtiyacın var")
        url=urllib.request.urlopen('https://en.wikipedia.org/wiki/'+definition)
        soup=bs.BeautifulSoup(url,'lxml')
        definitions=[]
        for paragraph in soup.find_all('p'):
            definitions.append(str(paragraph.text))
        if definitions:
            if definitions[0]:
                engine_speak('üzgünüm bu tanımı bulamadım, lütfen bir web araması yapmayı deneyin')
            elif definitions[1]:
                engine_speak('işte '+definitions[1] + "için bulduğum şey")
            else:
                engine_speak ('işte '+definitions[2] + "hakkında bulduklarım")
        else:
                engine_speak("üzgünüm ama "+definition + "hakkında bir tanım bulamadım")


    if there_exists(["çıkış", "çıkmak", "güle güle", "goodbye"]):
        engine_speak("uygulama durduruluyor. görüşmek üzere..")
        exit()

    # Mevcut şehir veya bölge
    if there_exists(["neredeyim"]):
        Ip_info = requests.get('https://api.ipdata.co?api-key=test').json()
        loc = Ip_info['region']
        engine_speak(f"sanırım şu anda {loc}'ın içinde bir yerde olmalısın")    
   
   # Google haritalarına göre mevcut konum
    if there_exists(["tam konumum nedir"]):
        url = "https://www.google.com/maps/search/Where+am+I+?/"
        webbrowser.get().open(url)
        engine_speak("google haritalarına göre, buraya yakın bir yerde olmalısınız")    



time.sleep(1)

person_obj = person()
asis_obj = asis()
asis_obj.name = 'kiki'
person_obj.name = ""
engine = pyttsx3.init()


while(1):
    voice_data = record_audio("dinliyorum") #ses girdisini al
    print("Bitti")
    print("Q:", voice_data)
    respond(voice_data) #cevap verme
