from pygame import mixer
#import playsound
#playsound.playsound(nome do arquivo.mp3) [MUITO FÁCIL]
#print('Deixe uma mensagem, torna o programa mais interessante!')

mixer.init()
mixer.music.load('ex021.1.mp3')
mixer.music.play()
input()

print('Espero que tenha gostado!')