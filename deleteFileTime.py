import os
from datetime import date

file_path = '/Users/'+os.getlogin()+'/Downloads/'
files = os.listdir(file_path)
daysToday = (date.today().month*30) + (date.today().year*365)

for item in files:
    statusInfo = os.stat(os.path.join(file_path, item))
    lastModificationInDays = (date.fromtimestamp(statusInfo[8]).month*30) + (date.fromtimestamp(statusInfo[8]).year*365)
    if abs((daysToday - lastModificationInDays)) > 120:
        if os.path.isfile(os.path.join(file_path, item)):
                try:
                    os.remove(os.path.join(file_path, item))
                    print('Arquivo(s) removido(s)!')
                except:
                    print(f'Arquivo "{item}" nao pode ser apagado.')
        if os.path.isdir(os.path.join(file_path, item)):
            try:
                os.rmdir(os.path.join(file_path, item))
            except:
                print(f'A pasta "{item}" contem arquivo(s)!')
