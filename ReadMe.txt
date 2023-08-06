Сначала скомпилировать в приложение следующим образом:
Открыть cmd через проводник(зайти в папку с файлом и ввести в строке адреса cmd)
в cmd вводить последовательно(дожидаясь завершения процесса):
pip install pyinstaller
pyinstaller --noconsole --onefile asist.py
pyinstaller  --onefile Settings.py
После из папки dist в папку с папками audio и cfg перетащить ваши приложения
Выполнить настройку с помошью Settings.exe 
Запустить asist.exe и пользоваться
