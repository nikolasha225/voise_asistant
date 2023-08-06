import keyboard
import datetime
import pyperclip
import webbrowser
import speech_recognition as sr
from gtts import gTTS
import pygame
import os
import time
from pymystem3 import Mystem
import requests
from bs4 import BeautifulSoup
#pyinstaller --noconsole --onefile asist.py
pygame.mixer.init()
def fpar(url,txt):
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        fp = soup.find('p').get_text()
        if (len(list(fp))<len(list(txt))+10):
            first_paragraph = soup
            #(first_paragraph.get_text())
            if 1:
                # Найдем первый список в абзаце
                flist = first_paragraph.find_all('ul')
                fp = flist[2].find('li').text
        fp = list(fp)
        k = 0
        for i in range(len(fp)):
            if (k == 1):
                break
            if (fp[i] == "("):
                for j in range(i, len(fp)):
                    if (fp[j] == ')'):
                        fp = fp[:i] + fp[j + 2:]
                        k = 1
                        break
        ar = []
        for i in range(len(fp)):
            if (fp[i] == "["):
                ar.append(i)
        ar.reverse()
        for i in ar:
            fp.pop(i)
            fp.pop(i)
            fp.pop(i)
        fp2 = ''
        for i in fp:
            fp2 += i
        return fp2

    else:
        print(f"Ошибка: {response.status_code}")
        return None
def wurl(title):
    base_url = "https://ru.wikipedia.org/w/api.php"
    params = {
        "action": "query",
        "titles": title,
        "format": "json",
        "prop": "info",
        "inprop": "url"
    }
    response = requests.get(base_url, params=params)
    data = response.json()

    page_id = next(iter(data["query"]["pages"]))
    page_info = data["query"]["pages"][page_id]

    if "missing" in page_info:
        return None  # Страница не найдена
    else:
        return page_info["fullurl"]


def g_zapr(txt):
    ur = wurl(txt)
    fp2 = fpar(ur,txt)
    if(fp2 == ''):
        fp2= 'Ошибка запроса, попробуйте переформулировать'
    zv2(fp2)

def zv (nm):
    pygame.mixer.init()
    pygame.mixer.music.load(nm)
    pygame.mixer.music.play()
    time.sleep(0.2)
    #while pygame.mixer.music.get_busy():
     #   continue
def zv2 (text):
    tts = gTTS(text, lang="ru", slow=0)
    tts.save("text.mp3")
    sound = pygame.mixer.Sound("text.mp3")
    sound.play()
    if (keyboard.read_key()):
        sound.stop()
    #pygame.mixer.music.load("text.mp3")
    #pygame.mixer.music.play()
    #while pygame.mixer.music.get_busy():
       # continue

recognizer = sr.Recognizer()
def sluh(dl=1):
    with sr.Microphone() as source:
        print("Скажите что-нибудь:")
        try:
            audio = recognizer.listen(source, timeout=dl)
            text = recognizer.recognize_google(audio, language="ru-RU")
            print("Вы сказали:", text)
        except sr.UnknownValueError:
            print("Извините, не удалось распознать речь.")
            return ''
        except sr.RequestError as e:
            print("Произошла ошибка при запросе к Google Speech Recognition: {0}".format(e))
            return ''
        except sr.WaitTimeoutError:
            print("timeout")
            return ''

        return text
def wb(url):
    webbrowser.open(url)
atmp = 0
#os.system("cmd")

def word(text):
    m = Mystem()
    lemmas = m.lemmatize(text)
    lemmas = [lemma.strip() for lemma in lemmas if lemma.strip()]
    if(lemmas[0] == ' ' ):
        lemmas.pop(0)
        rt = lemmas[0]
    else:
        rt = lemmas[0]

    for i in range(1,len(lemmas)):
        rt+=' '+lemmas[i]
    return rt
fnd_wb = open("cfg/wrd_wb.txt", encoding="utf-8").readlines()
for i in range(len((fnd_wb))):
    fnd_wb[i] = fnd_wb[i].rstrip()


fnd_gv = open("cfg/wrd_gvvod.txt", encoding="utf-8").readlines()
for i in range(len((fnd_gv))):
    fnd_gv[i] = fnd_gv[i].rstrip()


fnd_run = open("cfg/wrd_run.txt", encoding="utf-8").readlines()
for i in range(len((fnd_run))):
    fnd_run[i] = fnd_run[i].rstrip()


fnd_muz = open("cfg/wrd_muz.txt", encoding="utf-8").readlines()
for i in range(len((fnd_muz))):
    fnd_muz[i] = fnd_muz[i].rstrip()


fnd_off = open("cfg/wrd_off.txt", encoding="utf-8").readlines()
for i in range(len((fnd_off))):
    fnd_off[i] = fnd_off[i].rstrip()


fnd_rd = open("cfg/wrd_rd.txt", encoding="utf-8").readlines()
for i in range(len((fnd_rd))):
    fnd_rd[i] = fnd_rd[i].rstrip()


fnd_wb2 = open("cfg/wb.txt", encoding="utf-8").readlines()
for i in range(len(fnd_wb2)):
    fnd_wb2[i] = fnd_wb2[i].split('%%%%%')
    fnd_wb2[i][0] = fnd_wb2[i][0].split('___')
    fnd_wb2[i][1] = fnd_wb2[i][1].rstrip()

fnd_gm = open("cfg/gm.txt", encoding="utf-8").readlines()
for i in range(len(fnd_gm)):
    fnd_gm[i] = fnd_gm[i].split('%%%')
    fnd_gm[i][0] = fnd_gm[i][0].split('_')
    fnd_gm[i][1] = fnd_gm[i][1].rstrip()
def chk_web(txt):
    for i in fnd_wb:
        if i in txt:
            txt = txt.replace(i,'')
            zv("audio/answ_zapros.mp3")
            wb("https://ya.ru/search/?text="+word(txt))

            return 1
    for i in fnd_wb2:
        for j in i[0]:
            if j in txt:
                zv("audio/answ_zapros.mp3")
                wb(i[1])
                return 1

    return 0
def chk_gvvod(txt):
    for i in fnd_gv:
        if i in txt:
            zv("audio/load.mp3")
            t = sluh(2)
            keyboard.write(t)
            pyperclip.copy(t)
            zv('audio/new_element.mp3')
            return 1
    return 0
def chk_game(txt):
    for i in fnd_run:
        if(i in txt):
            zv("audio/answ_sps.mp3")
            txt = txt.replace(i, '')
            for j in range(len(fnd_gm)):
                for k in range(len(fnd_gm[j][0])):
                    if(fnd_gm[j][0][k] in txt):
                        if(fnd_gm[j][1][1] == ":"):
                            os.system(fnd_gm[j][1])
                        else:
                            wb(fnd_gm[j][1])
                        return 1

    return 0
def chk_muz(txt):
    for i in fnd_muz:
        if(i in txt):
            zv("audio/load.mp3")
            os.system(str(open("cfg/muz.txt").readline()))
            return 1
    return 0
def chk_off(txt):
    for i in fnd_off:
        if(i in txt):
            zv("audio/shutdown.mp3")
            os.system("shutdown /s /t 3")
            return 1
    return 0
def chk_gzapr(txt):
    for i in fnd_rd:
        if i in txt:
            txt = txt.replace(i,"")
            txt2 = word(txt)
            g_zapr(str(txt2))
            return 1
    return 0
while 1:
    if 1:#keyboard.is_pressed("ctrl"):
        if 1:#keyboard.is_pressed("shift"):
            if keyboard.is_pressed(open('cfg/hkey.txt',encoding="utf-8").readline()):#keyboard.is_pressed("f3"):
                if(atmp == 0):
                    if(datetime.datetime.now().hour < 13):
                        zv("audio/hi2.mp3")
                        time.sleep(0.7)
                        txt = sluh(2)
                    else:
                        zv("audio/hi.mp3")
                        time.sleep(0.3)
                        txt = sluh(2)
                else:
                    zv("audio/da_ser.mp3")
                    time.sleep(0.2)
                    txt = sluh(1)
                atmp+=1

                if not(chk_web(str(txt)) or chk_gvvod(str(txt)) or chk_game(str(txt)) or chk_muz(str(txt)) or chk_off(str(txt)) or chk_gzapr(str(txt))):
                    zv("audio/mi_reboot.mp3")


#keyboard.write(message) голосовой ввод
