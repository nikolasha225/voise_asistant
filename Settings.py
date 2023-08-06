import os
import time
from tkinter import filedialog
import speech_recognition as sr
import keyboard
import sys
import tkinter as tk


key_names = [
    "backspace", "tab", "return", "enter", "pause", "scroll_lock", "print_screen",
    "escape", "home", "end", "page_up", "page_down", "insert", "delete",
    "up", "down", "left", "right", "menu", "num_lock", "caps_lock", "shift",
    "ctrl", "alt", "alt_gr", "win", "space", "decimal", "subtract", "add",
    "multiply", "divide", "f1", "f2", "f3", "f4", "f5", "f6", "f7", "f8", "f9",
    "f10", "f11", "f12", "num_0", "num_1", "num_2", "num_3", "num_4", "num_5",
    "num_6", "num_7", "num_8", "num_9", "a", "b", "c", "d", "e", "f", "g", "h",
    "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w",
    "x", "y", "z", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9"
]
def sluh(dl=1):
    recognizer = sr.Recognizer()
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
            print("Проверьте Интернет соединение")
            return ''
        except sr.WaitTimeoutError:
            print("Вы ничего не сказали")
            return ''

        return text
def file():
    root = tk.Tk()
    tk.Frame(root, width=0, height=0).pack()
    a = filedialog.askopenfilename()
    root.destroy()
    return a
def cfg_list(fname = "cfg"):
    return os.listdir(os.path.join(os.path.dirname(os.path.abspath(__file__)), fname))
print("Вы открыли настройки асистента")
print("F2 для продолжения")

def gl ():
    print("========================Удерживать===========================")
    print("F3 - добавить реплику для запуска приложения")
    print("F4 - добавить приложение и реплику для него")
    print("F5 - добавить сайт и реплику для него")
    print("F6 - добавить реплику для запуска голосового ввода")
    print("F7 - добавить реплику для завершения работы")
    print("F8 - добавить реплику для голосового запроса")
    print("F9 - добавить реплику для запуска плеера")
    print("F11 - задать расположение плеера")
    print("F12 - сменить горячую клавишу")
    print("Alt - сброс всех настроек")
    print("Backspace - выход")
    print("===========================================================")
    while 1:
        if(keyboard.read_key() == "backspace"):
            sys.exit()
        if (keyboard.read_key() == "f3"):
            print("Нажмите Shift, когда будете готовы")
            print("Ctrl - выход")
            while not(keyboard.is_pressed("shift") or keyboard.is_pressed("ctrl")):
                continue
            if 1:
                if (keyboard.read_key() == "shift"):
                    while 1:
                        txt = ''
                        while txt == '':
                            txt = sluh(2)
                            time.sleep(1)
                        print("подтвердить добавление - Backspace")
                        print("заново - Shift")
                        while 1:
                            if(keyboard.read_key() == "backspace"):
                                #open("cfg/test.txt", mode="a", encoding="utf-8").writelines(txt+"\n")
                                open("cfg/wrd_run.txt", mode="a", encoding="utf-8").writelines(txt+"\n") #=========================================================================================
                                print("Успешно")
                                time.sleep(0.5)
                                gl()
                            if keyboard.read_key() == "shift":
                                break

                if (keyboard.read_key() == "ctrl"):
                    gl()
            time.sleep(0.5)
        if (keyboard.read_key() == 'f4'):
            add_fl = ''
            add_repl = ''
            print("Выберите расположение файла")
            add_fl = file()
            print(add_fl)
            print("Shift - добавить реплику")
            while not(keyboard.is_pressed("shift")):
                continue
            if(1):
                if (keyboard.is_pressed("shift")):
                    while 1:
                        txt = ''
                        while txt == '':
                            txt = sluh(2)
                        print("Ctrl - добавить ещё реплику")
                        print("Shift - заново (эта реплика)")
                        print("Backspace - завершить")
                        while(1):
                            if(keyboard.is_pressed('shift')):
                                break
                            if(keyboard.is_pressed("ctrl")):
                                if(add_repl == ''):
                                    add_repl += txt
                                    break
                                else:
                                    add_repl+="_"+txt
                                    break
                            if(keyboard.is_pressed("backspace")):
                                add_repl+="_"+txt
                                #open("cfg/test.txt", mode="a", encoding="utf-8").writelines(add_repl+"%%%" + '"' + add_fl + '"' + "\n")
                                open("cfg/gm.txt", mode="a", encoding="utf-8").writelines(add_repl + "%%%" + '"' + add_fl + '"' + "\n")#=================================================
                                print("Успешно")
                                time.sleep(1)
                                gl()
        if (keyboard.read_key() == 'f5'):
            add_wb_rp = ''
            print("Введите ссылку")
            add_url = input()
            print("Shift - добавить реплику(например: Включи ютуб")
            while not (keyboard.is_pressed("shift")):
                continue
            if (1):
                if (keyboard.is_pressed("shift")):
                    while 1:
                        txt = ''
                        while txt == '':
                            txt = sluh(2)
                        print("Ctrl - добавить ещё реплику")
                        print("Shift - заново (эта реплика)")
                        print("Backspace - завершить")
                        while (1):
                            if (keyboard.is_pressed('shift')):
                                break
                            if (keyboard.is_pressed("ctrl")):
                                if (add_wb_rp == ''):
                                    add_wb_rp += txt
                                    break
                                else:
                                    add_wb_rp += "___" + txt
                                    break
                            if (keyboard.is_pressed("backspace")):
                                add_wb_rp += "___" + txt
                                #open("cfg/test.txt", mode="a", encoding="utf-8").writelines(add_wb_rp + "%%%" + '"' + add_url + '"' + "\n")
                                open("cfg/wb.txt", mode="a", encoding="utf-8").writelines(add_wb_rp + "%%%%%" + '"' + add_url + '"' + "\n")
                                print("Успешно")
                                time.sleep(1)
                                gl()
        if (keyboard.read_key() == "f6"):
            print("Нажмите Shift, когда будете готовы")
            print("Ctrl - выход")
            while not (keyboard.is_pressed("shift") or keyboard.is_pressed("ctrl")):
                continue
            if 1:
                if (keyboard.read_key() == "shift"):
                    while 1:
                        txt = ''
                        while txt == '':
                            txt = sluh(2)
                            time.sleep(1)
                        print("подтвердить добавление - Backspace")
                        print("заново - Shift")
                        while 1:
                            if (keyboard.read_key() == "backspace"):
                                #open("cfg/test.txt", mode="a", encoding="utf-8").writelines(txt + "\n")
                                open("cfg/wrd_gvvod.txt", mode="a", encoding="utf-8").writelines(txt+"\n") #=========================================================================================
                                print("Успешно")
                                time.sleep(0.5)
                                gl()
                            if keyboard.read_key() == "shift":
                                break

                if (keyboard.read_key() == "ctrl"):
                    gl()
            time.sleep(0.5)
        if (keyboard.read_key() == "f7"):
            print("Нажмите Shift, когда будете готовы")
            print("Ctrl - выход")
            while not (keyboard.is_pressed("shift") or keyboard.is_pressed("ctrl")):
                continue
            if 1:
                if (keyboard.read_key() == "shift"):
                    while 1:
                        txt = ''
                        while txt == '':
                            txt = sluh(2)
                            time.sleep(1)
                        print("подтвердить добавление - Backspace")
                        print("заново - Shift")
                        while 1:
                            if (keyboard.read_key() == "backspace"):
                                #open("cfg/test.txt", mode="a", encoding="utf-8").writelines(txt + "\n")
                                open("cfg/wrd_off.txt", mode="a", encoding="utf-8").writelines(txt+"\n") #=========================================================================================
                                print("Успешно")
                                time.sleep(0.5)
                                gl()
                            if keyboard.read_key() == "shift":
                                break

                if (keyboard.read_key() == "ctrl"):
                    gl()
            time.sleep(0.5)
        if (keyboard.read_key() == "f8"):
            print("Нажмите Shift, когда будете готовы")
            print("Ctrl - выход")
            while not (keyboard.is_pressed("shift") or keyboard.is_pressed("ctrl")):
                continue
            if 1:
                if (keyboard.read_key() == "shift"):
                    while 1:
                        txt = ''
                        while txt == '':
                            txt = sluh(2)
                            time.sleep(1)
                        print("подтвердить добавление - Backspace")
                        print("заново - Shift")
                        while 1:
                            if (keyboard.read_key() == "backspace"):
                                #open("cfg/test.txt", mode="a", encoding="utf-8").writelines(txt + "\n")
                                open("cfg/wrd_rd.txt", mode="a", encoding="utf-8").writelines(txt+"\n") #=========================================================================================
                                print("Успешно")
                                time.sleep(0.5)
                                gl()
                            if keyboard.read_key() == "shift":
                                break

                if (keyboard.read_key() == "ctrl"):
                    gl()
            time.sleep(0.5)
        if (keyboard.read_key() == "f9"):
            print("Нажмите Shift, когда будете готовы")
            print("Ctrl - выход")
            while not (keyboard.is_pressed("shift") or keyboard.is_pressed("ctrl")):
                continue
            if 1:
                if (keyboard.read_key() == "shift"):
                    while 1:
                        txt = ''
                        while txt == '':
                            txt = sluh(2)
                            time.sleep(1)
                        print("подтвердить добавление - Backspace")
                        print("заново - Shift")
                        while 1:
                            if (keyboard.read_key() == "backspace"):
                                #open("cfg/test.txt", mode="a", encoding="utf-8").writelines(txt + "\n")
                                open("cfg/wrd_muz.txt", mode="a", encoding="utf-8").writelines(txt+"\n") #=========================================================================================
                                print("Успешно")
                                time.sleep(0.5)
                                gl()
                            if keyboard.read_key() == "shift":
                                break

                if (keyboard.read_key() == "ctrl"):
                    gl()
            time.sleep(0.5)
        if (keyboard.read_key() == "f11"):
            print("Выберите расположение плеера")
            mz = file()
            print(mz)
            #open("cfg/test.txt",encoding="utf-8",mode="w").write('"'+str(mz)+'"')
            open("cfg/muz.txt", encoding="utf-8", mode="w").write('"' + str(mz) + '"')
            print("Успешно")
            gl()
        if (keyboard.read_key() == 'f12'):
            print("Если не знаете такой клавиши - загуглите")
            print("Скопируйте название нужной клавиши и вставьте его(без пробелов)")
            print("Список клавиш:")
            for i in range(len(key_names)):
                print(key_names[i],end="  ")
                if(i%6 == 5):print()
                hk = ''
            while 1:
                hk = input()
                if hk != '':
                    if(hk in key_names):
                        #open('cfg/test.txt', encoding="utf-8", mode="w").write(hk)
                        open('cfg/hkey.txt',encoding="utf-8",mode="w").write(hk)
                        print("Успешно")
                        time.sleep(1)
                        gl()
                    else:
                        print("Нет такой клавиши")
        if (keyboard.read_key() == 'alt'):
            open("cfg/hkey.txt",encoding="utf-8",mode="w").write('f10')
            open("cfg/gm.txt", encoding="utf-8", mode="w").write('')
            open("cfg/muz.txt", encoding="utf-8", mode="w").write('')
            open("cfg/wb.txt", encoding="utf-8", mode="w").write('что посмотреть___открой ютуб___открой YouTube___открой видосы___Что посмотреть___Открой ютуб___Открой YouTube___Открой видосы%%%%%"https://www.youtube.com"\n')
            open("cfg/wrd_gvvod.txt", encoding="utf-8", mode="w").write("голосовой ввод\nввод голосом\nголосовой вод\nвод голосом\nактивируй голосовой ввод\nактивируй голосовой вод\nактивируй вод голосом\nактивируй ввод голосом\nГолосовой ввод\nВвод голосом\nГолосовой вод\nВод голосом\nАктивируй голосовой ввод\nАктивируй голосовой вод\nАктивируй вод голосом\nАктивируй ввод голосом\nАктивировать голосовой ввод\nАктивировать голосовой вод\nАктивировать вод голосом\nАктивировать ввод голосом\n")
            open("cfg/wrd_muz.txt", encoding="utf-8", mode="w").write('музыку\nвруби музыку\nвключи музыку\nпоставь пластинку\nМузыку\nВруби музыку\nВключи музыку\nПоставь пластинку\n')
            open("cfg/wrd_off.txt", encoding="utf-8", mode="w").write('завершение работы\nвырубай\nзакругляйся\nЗавершение работы\nВырубай\nЗакругляйся\n')
            open("cfg/wrd_rd.txt", encoding="utf-8", mode="w").write('Расскажи о\nРасскажи об\nРасскажи про\nрасскажи о\nрасскажи об\nрасскажи про\nназови\nНазови\nГолосовой запрос\nголосовой запрос\n')
            open("cfg/wrd_run.txt", encoding="utf-8", mode="w").write('запусти\nпогнали в\nго в\nЗапусти\nПогнали в\nГо в\ngo в\nGo в\nоткрой\nОткрой\nгов\nГов\n')
            open("cfg/wrd_wb.txt", encoding="utf-8", mode="w").write('Загугли\nНайди\nБраузер\nзагугли\nнайди\nбраузер\n')
            print("Всё сброшено до заводских настроек")
            time.sleep(1)
            gl()
if (keyboard.read_key()) == "f2":#============================================================================================
    gl()