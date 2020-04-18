from auxiliares.fases_matias import *

teclado = Keyboard()
mouse = Mouse()


def movimentacao_Mathias(janela, Mathias, Mathias_A, buff):

    if buff:
        vel_Mathias = 300 * janela.delta_time()
    else:
        vel_Mathias = 175 * janela.delta_time()


    if teclado.key_pressed("RIGHT"):
        Mathias.x += vel_Mathias


    elif teclado.key_pressed("LEFT"):
        Mathias.x -= vel_Mathias

    elif teclado.key_pressed("SPACE"):
        Mathias_A.set_position(Mathias.x, Mathias.y)
        Mathias_A.draw()




    #para matias n sair da tela
    if Mathias.x <= 0:
        Mathias.x += vel_Mathias

    elif Mathias.x >= (janela.width - Mathias.width):
        Mathias.x -= vel_Mathias






def movimentacao_inimigo(janela, inimigo):
    vel_inimigo = 150 * janela.delta_time()
    inimigo.x -= vel_inimigo
    if inimigo.x < 0:
        inimigo.x = janela.height


def ataque_Mathias(permissao):
    if permissao:
        retorno = 1
    else:
        retorno = 0

    return retorno


def ataque_Illinois(Vida_Illinois):
    if Vida_Illinois < 3:
        return 5
    else:
        return 4

def combate_c(janela, imagem, Mathias, Mathias_A, inimigo, Vida_Illinois):

    inimigo.draw()


    dano = ataque_Illinois(Vida_Illinois)
    if imagem == 0:
        golpe = ataque_Mathias()
        if golpe == 1:
            Mathias_A.set_position(Mathias.x, Mathias.y)
            Mathias_A.draw()
            if Mathias_A.collided(inimigo):
                inimigo.x = janela.width
                if Mathias.x < janela.width/2:
                    Mathias.x = 0
                else:
                    Mathias.x = janela.width*(0.5)

                return 1
        else:
            Mathias.draw()
            if Mathias.collided(inimigo):
                inimigo.x = janela.width
                if Mathias.x >= janela.width/2:
                    Mathias.x = janela.width*(0.5)
                else:
                    Mathias.x = 0
                return dano

def combate(janela, imagem, Mathias, Mathias_A, inimigo, novo_combate, permissao):

    inimigo.draw()

    if imagem == 0:
        golpe = ataque_Mathias(permissao)
        if golpe == 1:
            Mathias_A.set_position(Mathias.x, Mathias.y)
            Mathias_A.draw()
            if Mathias_A.collided(inimigo):
                if novo_combate:
                    inimigo.x = janela.width - inimigo.width
                else:
                    inimigo.x += 300
                if Mathias.x < janela.width/2:
                    Mathias.x -= 50
                else:
                    Mathias.x -= 100

                return 1
        else:
            Mathias.draw()
            if Mathias.collided(inimigo):
                inimigo.x = janela.width
                if Mathias.x >= janela.width/2:
                    Mathias.x = janela.width*(0.5)
                else:
                    Mathias.x = 0
                return -2


def movimentacao_inimigo2(janela, inimigo, Mathias, vel_inimigo):


    if inimigo.x > Mathias.x:
        if abs(Mathias.x - inimigo.x) >= 40:
            inimigo.x -= vel_inimigo * janela.delta_time()

    elif inimigo.x < Mathias.x:
        if abs(Mathias.x - inimigo.x) >= 40:
            inimigo.x += vel_inimigo * janela.delta_time()

def animacao_vit():
    janela = Window(1180, 800)
    fundo = GameImage("images/fundo_animacao-1.gif")

    princesad = Sprite("images/princesa.gif")
    princesae = Sprite("images/princesa_e.gif")
    princesad.set_position(janela.width*(0.7), janela.height*(0.65))
    princesae.set_position(janela.width*(0.7), janela.height*(0.65))
    princesa = princesad

    MatD = Animation("images/mathias_d.png", 5, True)
    MatE = Animation("images/mathias_e.png", 5, True)
    MatD.set_sequence_time(0, 5, 100, True)
    MatE.set_sequence_time(0, 5, 100, True)
    Mat = [MatD, MatE]

    Mathias = Mat[0]
    Mathias.set_position(0, janela.height*(0.7))
    vel_Mathias = 75
    vel_princesa = 0
    troca = True
    while 1:
        fundo.draw()


        if janela.delta_time() < 1:
            for i in Mat:
                i.set_position(Mathias.x, Mathias.y)
            if vel_Mathias > 0:
                Mathias = Mat[0]
                Mathias.play()
            if vel_Mathias < 0:
                Mathias = Mat[1]
                Mathias.play()
            Mathias.x += vel_Mathias * janela.delta_time()
            Mathias.draw()
            Mathias.update()

            if Mathias.x + Mathias.width >= princesa.x - 50 and Mathias.x + Mathias.width < princesa.x and troca:
                vel_Mathias *= -1
                vel_princesa = -75*janela.delta_time()
                troca = False
                princesa = princesae
            princesa.x += vel_princesa
            princesa.draw()

            if princesa.x + princesa.width < 0:
                return 1

        janela.update()
