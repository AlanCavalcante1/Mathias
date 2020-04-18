from PPlay.sprite import *


def barra_de_vida_vi(vida_inimigo, inimigo):
    barras = []
    Vi3= Sprite("images/vi_verde.png")
    Vi2= Sprite("images/vi_amarelo.png")
    Vi1= Sprite("images/vi_vermelho.png")
    if vida_inimigo == 9:
        barras = [Vi3, Vi3, Vi3]
    if vida_inimigo == 8:
        barras = [Vi3, Vi3, Vi2]
    if vida_inimigo == 7:
        barras = [Vi3, Vi3, Vi1]
    if vida_inimigo == 6:
        barras = [Vi3, Vi3]
    if vida_inimigo == 5:
        barras = [Vi3, Vi2]
    if vida_inimigo == 4:
        barras = [Vi3, Vi1]
    if vida_inimigo == 3:
        barras = [Vi3]
    if vida_inimigo == 2:
        barras = [Vi2]
    if vida_inimigo == 1:
        barras = [Vi1]

    for i in range(len(barras)):
        barras[i].set_position(inimigo.x, inimigo.y-(i*8)-5)
        barras[i].draw()


def barra_de_vida(Vida_Mathias):
    V10= Sprite("images/10.png")
    V9= Sprite("images/9.png")
    V8= Sprite("images/8.png")
    V7= Sprite("images/7.png")
    V6= Sprite("images/6.png")
    V5= Sprite("images/5.png")
    V4= Sprite("images/4.png")
    V3= Sprite("images/3.png")
    V2= Sprite("images/2.png")
    V1= Sprite("images/1.png")


    if Vida_Mathias == 10:
        V10.draw()
    if Vida_Mathias == 9:
        V9.draw()
    if Vida_Mathias == 8:
        V8.draw()
    if Vida_Mathias == 7:
        V7.draw()
    if Vida_Mathias == 6:
        V6.draw()
    if Vida_Mathias == 5:
        V5.draw()
    if Vida_Mathias == 4:
        V4.draw()
    if Vida_Mathias == 3:
        V3.draw()
    if Vida_Mathias == 2:
        V2.draw()
    if Vida_Mathias == 1:
        V1.draw()



def pontuacao(pontos, janela):

    janela.draw_text(str(pontos), janela.width*(0.15), janela.height*(0.08), 30, (3, 250, 235), "Arial", True)







