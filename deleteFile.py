import os

file_path = '/Users/'+os.getlogin()+'/Downloads/'
files = os.listdir(file_path)

for item in files:
    if os.path.isfile(os.path.join(file_path, item)):
        if not(item.endswith(".pdf") or item.endswith(".jpeg")):
            try:
                os.remove(os.path.join(file_path, item))
                print(f'Arquivo "{item}" removido!')
            except:
                print(f'Arquivo "{item}" nao pode ser apagado.')
    if os.path.isdir(os.path.join(file_path, item)):
        try:
            os.rmdir(os.path.join(file_path, item))
        except:
            print(f'A pasta "{item}" contem arquivo(s)!')
# print(os.listdir(file_path))    
