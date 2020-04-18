from PPlay.gameimage import *

from PPlay.sprite import *
from PPlay.sound import *
from PPlay.keyboard import *
from PPlay.window import *
teclado = Keyboard()

def receber_nome():
    janela = Window (1024, 768)
    fundo = GameImage("images/fundo_castelo_bas.jpg")
    nome = ""
    timer = 0
    logo = Sprite("images/Logo.png")
    logo.set_position(10, 10)
    while 1:
        fundo.draw()
        logo.draw()
        janela.draw_text("DIGITE SEU NOME", janela.width* (0.15), janela.height*(0.2), 38, (255, 255, 255), "Impact")
        janela.draw_text("NOME: " + nome, janela.width* (0.15), janela.height*(0.25), 28, (255, 255, 255), "Impact")
        janela.draw_text("pressione ESPACO para deletar", janela.width*(0.15), janela.height*(0.3), 15, (255, 255, 255), "Impact")
        timer+=janela.delta_time()
        if teclado.key_pressed("Q") and timer > 0.3:
            nome+='Q'
            timer = 0
        if teclado.key_pressed("W") and timer > 0.3:
            nome+='W'
            timer = 0
        if teclado.key_pressed("E") and timer > 0.3:
            nome+='E'
            timer = 0
        if teclado.key_pressed("R") and timer > 0.3:
            nome+='R'
            timer = 0
        if teclado.key_pressed("T") and timer > 0.3:
            nome+='T'
            timer = 0
        if teclado.key_pressed("Y") and timer > 0.3:
            nome+='Y'
            timer = 0
        if teclado.key_pressed("U") and timer > 0.3:
            nome+='U'
            timer = 0
        if teclado.key_pressed("I") and timer > 0.3:
            nome+='I'
            timer = 0
        if teclado.key_pressed("O") and timer > 0.3:
            nome+='O'
            timer = 0
        if teclado.key_pressed("P") and timer > 0.3:
            nome+='P'
            timer = 0
        if teclado.key_pressed("A") and timer > 0.3:
            nome+='A'
            timer = 0
        if teclado.key_pressed("S") and timer > 0.3:
            nome+='S'
            timer = 0
        if teclado.key_pressed("D") and timer > 0.3:
            nome+='D'
            timer = 0
        if teclado.key_pressed("F") and timer > 0.3:
            nome+='F'
            timer = 0
        if teclado.key_pressed("G") and timer > 0.3:
            nome+='G'
            timer = 0
        if teclado.key_pressed("H") and timer > 0.3:
            nome+='H'
            timer = 0
        if teclado.key_pressed("J") and timer > 0.3:
            nome+='J'
            timer = 0
        if teclado.key_pressed("K") and timer > 0.3:
            nome+='K'
            timer = 0
        if teclado.key_pressed("L") and timer > 0.3:
            nome+='L'
            timer = 0
        if teclado.key_pressed("Z") and timer > 0.3:
            nome+='Z'
            timer = 0
        if teclado.key_pressed("X") and timer > 0.3:
            nome+='X'
            timer = 0
        if teclado.key_pressed("C") and timer > 0.3:
            nome+='C'
            timer = 0
        if teclado.key_pressed("V") and timer > 0.3:
            nome+='V'
            timer = 0
        if teclado.key_pressed("B") and timer > 0.3:
            nome+='B'
            timer = 0
        if teclado.key_pressed("N") and timer > 0.3:
            nome+='N'
            timer = 0
        if teclado.key_pressed("M") and timer > 0.3:
            nome+='M'
            timer = 0
        if teclado.key_pressed("1") and timer > 0.3:
            nome+='1'
            timer = 0
        if teclado.key_pressed("2") and timer > 0.3:
            nome+='2'
            timer = 0
        if teclado.key_pressed("3") and timer > 0.3:
            nome+='3'
            timer = 0
        if teclado.key_pressed("4") and timer > 0.3:
            nome+='4'
            timer = 0
        if teclado.key_pressed("5") and timer > 0.3:
            nome+='5'
            timer = 0
        if teclado.key_pressed("6") and timer > 0.3:
            nome+='6'
            timer = 0
        if teclado.key_pressed("7") and timer > 0.3:
            nome+='7'
            timer = 0
        if teclado.key_pressed("8") and timer > 0.3:
            nome+='8'
            timer = 0
        if teclado.key_pressed("9") and timer > 0.3:
            nome+='9'
            timer = 0
        if teclado.key_pressed("0") and timer > 0.3:
            nome+='0'
            timer = 0

        if teclado.key_pressed("ENTER") and timer > 0.3:
            timer = 0
            retorno = nome
            if retorno == "":
                retorno = "DESCONHECIDO"
            return retorno

        if teclado.key_pressed("SPACE") and timer > 0.3:
            nome = ""
            timer = 0

        janela.update()


def colocar_no_ranking(nome, score):
    arq = open("Arquivos/database.txt", 'r')

    num = arq.readlines()
    arq.close()
    frase = f'{score}  {nome}\n'

    if score == 0:
        num.append(frase)

    else:

        for i in range(len(num)):
            if num[i][0:2] > frase[0:2]:
                continue
            else:
                num.insert(i, frase)
                break

    arq = open("Arquivos/database.txt", 'w')

    for i in num:
        arq.write(i[0:len(i) - 1])
        arq.write('\n')
    arq.close()



def abrir_ranking():
    janela = Window(516, 750)
    fundo = GameImage("images/pergaminho.gif")
    janela.set_title('MATHIAS - RANKING')
    arq = open('Arquivos/database.txt', 'r')
    num = arq.readlines()

    arq.close()
    while True:
        fundo.draw()

        janela.draw_text(" RANKING ", janela.width/10, 80, 50, ([0, 0, 0]), "Papyrus", True)
        janela.draw_text(num[0][0:len(num[0]) - 1], janela.width / 10, 150, 25, ([0, 0, 0]), "Papyrus", True)
        janela.draw_text(num[1][0:len(num[1]) - 1], janela.width / 10, 200, 25, ([0, 0, 0]), "Papyrus", True)
        janela.draw_text(num[2][0:len(num[2]) - 1], janela.width / 10, 250, 25, ([0, 0, 0]), "Papyrus", True)
        janela.draw_text(num[3][0:len(num[3]) - 1], janela.width / 10, 300, 25, ([0, 0, 0]), "Papyrus", True)
        janela.draw_text(num[4][0:len(num[4]) - 1], janela.width / 10, 350, 25, ([0, 0, 0]), "Papyrus", True)

        if teclado.key_pressed("ESC"):
            return 0
        janela.update()


