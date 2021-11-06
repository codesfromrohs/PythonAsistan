# PythonAsistan

Konuşma tanıma ve metin okuma kullanan Python uygulaması
Bu uygulama başlangıçta Google metin okuma API'sini kullanıyordu, ancak pyttsx3 ile çevrimdışı metin okuma kullanacak şekilde güncellendi.

### Kurulması Gereken Bazı Python Tool'ları

```
pip install speechrecognition
pip install pyttsx3
pip install pyaudio
pip install playsound
pip install PyObjC
```
```
pip install PyAudio
```
(PyAudio kurulumunda bir sorun varsa bu bağlantıdan .whl dosyasını kullanacaz. [https://www.lfd.uci.edu/~gohlke/pythonlibs/#pyaudio](https://www.lfd.uci.edu/~gohlke/pythonlibs/#pyaudio))  

### Ses Komutları

Şimdilik eklediğim bazı komutlar. Başka komutlarda eklenebilir. Komutların ingilizce olmasının nedeni konuşma tanıma ve metin okumayı google translate üzerinden almamızdır.

- What is your name?
- What time is it
- Search
- Find Location
- Exit

### Apple Mac OS X (Homebrew & PyAudio)
Önkoşul olan portaudio kitaplığını kurmak için Homebrew'i kullanın, ardından pip kullanarak PyAudio'yu kurun:

`brew install portaudio`
`pip install pyaudio`

Notlar:

Henüz kurulmadıysa, Homebrew'i indirin.
pip, PyAudio kaynağını indirecek ve Python sürümünüz için oluşturacaktır.
Homebrew ve PyAudio'yu oluşturmak için Xcode için Komut Satırı Araçlarının da yüklenmesi gerekir (daha fazla bilgi).

https://people.csail.mit.edu/hubert/pyaudio/
