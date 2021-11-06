import speech_recognition as sr # konuşmayı tanımak
import playsound # bir ses dosyası çalmak için
from gtts import gTTS # google metin okuma
import random
from time import ctime # zaman ayrıntılarını al
import webbrowser # Tarayıcı aç
import yfinance as yf # finansal verileri almak için
import ssl
import certifi
import time
import os # oluşturulan ses dosyalarını kaldırmak için

class person:
    name = ''
    def setName(self, name):
        self.name = name

def there_exists(terms):
    for term in terms:
        if term in voice_data:
            return True

r = sr.Recognizer() # tanıyıcıyı başlatmak
# sesi dinleyin ve metne dönüştürün:
def record_audio(ask=False):
    with sr.Microphone() as source: # kaynak olarak mikrofon
        if ask:
            speak(ask)
        audio = r.listen(source)  # sesi kaynak üzerinden dinle
        voice_data = ''
        try:
            voice_data = r.recognize_google(audio)  # sesi metne dönüştür
        except sr.UnknownValueError: # hata: tanıyıcı anlamıyor
            speak('I did not get that')
        except sr.RequestError:
            speak('Sorry, the service is down') # hata: tanıyıcı bağlı değil
        print(f">> {voice_data.lower()}") # kullanıcının söylediğini yazdır
        return voice_data.lower()

# dizgi alın ve çalınacak bir ses dosyası oluşturun
def speak(audio_string):
    tts = gTTS(text=audio_string, lang='en') # metin okuma (ses)
    r = random.randint(1,20000000)
    audio_file = 'audio' + str(r) + '.mp3'
    tts.save(audio_file) # mp3 olarak kaydet
    playsound.playsound(audio_file) # ses dosyasını çal
    print(f"kiri: {audio_string}") # uygulamanın ne dediğini yazdır
    os.remove(audio_file) # ses dosyasını kaldır

def respond(voice_data):
    # 1: selamlama
    if there_exists(['hey','hi','hello']):
        greetings = [f"hey, how can I help you {person_obj.name}", f"hey, what's up? {person_obj.name}", f"I'm listening {person_obj.name}", f"how can I help you? {person_obj.name}", f"hello {person_obj.name}"]
        greet = greetings[random.randint(0,len(greetings)-1)]
        speak(greet)

    # 2: isim
    if there_exists(["what is your name","what's your name","tell me your name"]):
        if person_obj.name:
            speak("my name is Alexis")
        else:
            speak("my name is Alexis. what's your name?")

    if there_exists(["my name is"]):
        person_name = voice_data.split("is")[-1].strip()
        speak(f"okay, i will remember that {person_name}")
        person_obj.setName(person_name) # kişi nesnesindeki adı hatırla

    # 3: hal-hatır sorma
    if there_exists(["how are you","how are you doing"]):
        speak(f"I'm very well, thanks for asking {person_obj.name}")

    # 4: saat sorma
    if there_exists(["what's the time","tell me the time","what time is it"]):
        time = ctime().split(" ")[3].split(":")[0:2]
        if time[0] == "00":
            hours = '12'
        else:
            hours = time[0]
        minutes = time[1]
        time = f'{hours} {minutes}'
        speak(time)

    # 5: Google'da ara
    if there_exists(["search for"]) and 'youtube' not in voice_data:
        search_term = voice_data.split("for")[-1]
        url = f"https://google.com/search?q={search_term}"
        webbrowser.get().open(url)
        speak(f'Here is what I found for {search_term} on google')

    # 6: youtube'da ara
    if there_exists(["youtube"]):
        search_term = voice_data.split("for")[-1]
        url = f"https://www.youtube.com/results?search_query={search_term}"
        webbrowser.get().open(url)
        speak(f'Here is what I found for {search_term} on youtube')

    # 7: hisse senedi fiyatı al
    if there_exists(["price of"]):
        search_term = voice_data.lower().split(" of ")[-1].strip() #şerit, dizedeki bir terimden sonraki / önceki beyaz boşluğu kaldırır
        stocks = {
            "apple":"AAPL",
            "microsoft":"MSFT",
            "facebook":"FB",
            "tesla":"TSLA",
            "bitcoin":"BTC-USD"
        }
        try:
            stock = stocks[search_term]
            stock = yf.Ticker(stock)
            price = stock.info["regularMarketPrice"]

            speak(f'price of {search_term} is {price} {stock.info["currency"]} {person_obj.name}')
        except:
            speak('oops, something went wrong')
    if there_exists(["exit", "quit", "goodbye"]):
        speak("going offline")
        exit()


time.sleep(1)

person_obj = person()
while(1):
    voice_data = record_audio() # ses girdisini al
    respond(voice_data) # cevap verme

