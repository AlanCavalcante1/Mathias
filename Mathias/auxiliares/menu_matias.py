from PPlay.gameimage import *
from PPlay.window import *
from PPlay.mouse import *
from PPlay.keyboard import *
from PPlay.sprite import *
from PPlay.sound import *


mouse = Mouse()
teclado = Keyboard()

def menu():
    janela = Window(800, 600)
    janela.set_title("MATHIAS")
    fundo_menu = GameImage("images/menubk.jpg")
    modonormal = Sprite("images/jogar.png")
    modonormalv = Sprite("images/jogar_verde.png")
    ranking = Sprite("images/ranking.png")
    rankingv = Sprite("images/ranking_verde.png")
    tutorial_on = Sprite("images/menu_tutorial_on.png")
    tutorial_off = Sprite("images/menu_tutorial_off.png")
    tutorial_onv = Sprite("images/menu_tutorial_on_v.png")
    tutorial_offv = Sprite("images/menu_tutorial_off_v.png")
    sair = Sprite("images/sair.png")
    sairv = Sprite("images/sairc.png")
    logo = Sprite("images/logo_menu.png")


    timer = 0
    modonormal.set_position(janela.width*(0.3)-modonormal.width/2, janela.height*(0.3)-modonormal.height/2)
    modonormalv.set_position(janela.width*(0.3)-modonormalv.width/2, janela.height*(0.3)-modonormalv.height/2)
    ranking.set_position(janela.width*(0.3)-ranking.width/2, janela.height*(0.5)-ranking.height/2)
    rankingv.set_position(janela.width*(0.3)-rankingv.width/2, janela.height*(0.5)-rankingv.height/2)
    tutorial_on.set_position(janela.width*(0.3)-tutorial_on.width/2, janela.height*(0.7)-tutorial_on.height/2)
    tutorial_onv.set_position(janela.width*(0.3)-tutorial_on.width/2, janela.height*(0.7)-tutorial_on.height/2)
    tutorial_off.set_position(janela.width*(0.3)-tutorial_on.width/2, janela.height*(0.7)-tutorial_on.height/2)
    tutorial_offv.set_position(janela.width*(0.3)-tutorial_on.width/2, janela.height*(0.7)-tutorial_on.height/2)
    sair.set_position(janela.width*(0.3)-sair.width/2, janela.height*(0.9)-sair.height/2)
    sairv.set_position(janela.width*(0.3)-sairv.width/2, janela.height*(0.9)-sairv.height/2)
    logo.set_position(janela.width*(0.3)-logo.width/2, janela.height*(0.1)-logo.height/2)


    controle = 1
    controle_tutorial = -1
    tutorial_r = True

    while 1:
        fundo_menu.draw()
        modonormal.draw()
        ranking.draw()
        sair.draw()
        logo.draw()

        if controle == 2:
            rankingv.draw()
            if teclado.key_pressed("ENTER") or (mouse.is_over_object(ranking) and mouse.is_button_pressed(1)):
                return 2

        if controle == 1:
            modonormalv.draw()
            if teclado.key_pressed("ENTER") or (mouse.is_over_object(modonormal) and mouse.is_button_pressed(1)):
                if controle_tutorial == -1:

                    return -1
                else:
                    return 1

        if controle == 3:
            if teclado.key_pressed("LEFT"):
                controle_tutorial = 1
            if teclado.key_pressed("RIGHT"):
                controle_tutorial = -1
            if controle_tutorial == -1:
                if mouse.is_button_pressed(1):
                    controle_tutorial = 1
                    continue
                tutorial_onv.draw()
            if controle_tutorial == 1:
                tutorial_offv.draw()
        else:
            if controle_tutorial == -1:
                tutorial_on.draw()
            if controle_tutorial == 1:
                tutorial_off.draw()

        if controle == 4:
            sairv.draw()
            if teclado.key_pressed("ENTER") or (mouse.is_over_object(sair) and mouse.is_button_pressed(1)):
                return -2

        timer += janela.delta_time()
        if teclado.key_pressed("DOWN") and timer > 0.3:
            controle += 1
            timer = 0
        if teclado.key_pressed("UP") and timer > 0.3:
            controle -= 1
            timer = 0
        if controle < 1:
            controle = 4
        if controle > 4:
            controle = 1

        if mouse.is_over_object(modonormal):
            controle = 1
        if mouse.is_over_object(ranking):
            controle = 2
        if (controle_tutorial == 1 and mouse.is_over_object(tutorial_on)) or (controle_tutorial == -1 and mouse.is_over_object(tutorial_off)):
            controle = 3
        if mouse.is_over_object(sair):
            controle = 4

        janela.update()
def menu_pergaminho():
    per = Window (516, 750)
    fundo_per = GameImage("images/pergaminho_do_mago.gif")

    b_fogo = Sprite ("images/b_fogo.gif")
    b_fogo_v = Sprite ("images/b_fogo_v.gif")
    b_vida = Sprite ("images/b_vida.gif")
    b_vida_v = Sprite ("images/b_vida_v.gif")
    b_fogo.set_position(per.width/2 - b_fogo.width/2, per.height * (0.6))
    b_fogo_v.set_position(per.width/2 - b_fogo.width/2, per.height * (0.6))
    b_vida.set_position(per.width/2 - b_fogo.width/2, b_fogo.y + b_fogo.height + 5)
    b_vida_v.set_position(per.width/2 - b_fogo.width/2, b_fogo.y + b_fogo.height + 5)

    while 1:
        per.update()
        fundo_per.draw()

        b_fogo.draw()
        if mouse.is_over_object(b_fogo):
            b_fogo_v.draw()
            if mouse.is_button_pressed(1):
                return 1

        b_vida.draw()
        if mouse.is_over_object(b_vida):
            b_vida_v.draw()
            if mouse.is_button_pressed(1):
                return -1
