from PPlay.gameimage import *
from PPlay.window import *
from PPlay.mouse import *
from PPlay.keyboard import *
from PPlay.sprite import *
from PPlay.sound import *
from PPlay.animation import *

from auxiliares.ranking import *
from auxiliares.menu_matias import *
from PPlay.sound import *
import time
import random

from auxiliares.move_and_atack_matias import *
from auxiliares.life_points_matias import *
teclado = Keyboard()

def floresta(tutorial, pontos, Vida_Mathias, buff_damage, buff_armor, nome):
    if tutorial and pontos == 0:
        mouse = Mouse()
        leitura = True
        janela = Window (539, 700)
        botao = Sprite("images/botao.png")
        botao.set_position(janela.width-botao.width, 0)
        pergaminho_missao = GameImage("images/pergaminho_da_missao.png")
        pergaminho_mapa = GameImage("images/mapa_da_missao.png")
        pergaminho_mecanica = GameImage("images/pergaminho_de_mecanicas.png")
        pergaminho_mecanica_2 = GameImage("images/pergaminho_dos_itens.png")

        botao_cinza = GameImage('images/botao_cinza.png')
        botao_cinza.set_position(botao.x, botao.y)
        while leitura:
            pergaminho_missao.draw()
            botao.draw()
            if teclado.key_pressed("ENTER") :
                leitura = False
            if mouse.is_over_object(botao):
                botao_cinza.draw()
                if mouse.is_button_pressed(1):
                    leitura = False
            janela.update()
        leitura = True
        janela = Window(750, 610)
        botao.set_position(janela.width-botao.width, 0)
        botao_cinza.set_position(botao.x, botao.y)
        while leitura:
            pergaminho_mapa.draw()
            botao.draw()
            if teclado.key_pressed("ENTER"):
                leitura = False
            if mouse.is_over_object(botao):
                botao_cinza.draw()
                if mouse.is_button_pressed(1):
                    leitura = False
            janela.update()
        leitura = True
        janela = Window (750, 610)
        botao.set_position(janela.width-botao.width, 0)
        botao_cinza.set_position(botao.x, botao.y)
        while leitura:
            pergaminho_mecanica.draw()
            botao.draw()
            if teclado.key_pressed("ENTER"):
                leitura = False
            if mouse.is_over_object(botao):
                botao_cinza.draw()
                if mouse.is_button_pressed(1):
                    leitura = False
            janela.update()
        leitura = True
        janela = Window(750, 610)
        botao.set_position(janela.width-botao.width, 0)
        botao_cinza.set_position(botao.x, botao.y)
        while leitura:
            pergaminho_mecanica_2.draw()
            botao.draw()
            if teclado.key_pressed("ENTER"):
                leitura = False
            if mouse.is_over_object(botao):
                botao_cinza.draw()
                if mouse.is_button_pressed(1):
                    leitura = False
            janela.update()



    janela = Window(1280, 650)
    janela.set_title('Floresta do Abismo')
    fundo = GameImage("images/florestabk.png")
    som = Sound('music/floresta.ogg')
    som.play()

    chao = janela.height*(0.7)

    MatD = Animation("images/mathias_d.png", 5, True)
    MatE = Animation("images/mathias_e.png", 5, True)
    MatD.set_sequence_time(0, 5, 100, True)
    MatE.set_sequence_time(0, 5, 100, True)
    Mat = [MatD, MatE]

    MatE.set_position(janela.width/15 - MatE.width/15, chao)
    MatD.set_position(janela.width/15 - MatD.width/15, chao)

    MatAD = Animation("images/mathias_atack.png", 4, False)
    MatAE = Animation("images/mathias_atack2.png", 4, False)
    MatAD.set_sequence_time(0, 4, 50, False)
    MatAE.set_sequence_time(0, 4, 50, False)
    MatA = [MatAD, MatAE]

    plat_1 = Sprite("images/plat_f.png")

    plat_1.set_position(600, chao - 95)

    orc_d = Animation("images/ini_d.png", 9, True)
    orc_e = Animation("images/ini_e.png", 9, True)
    orc_d.set_sequence_time(0, 9, 100, True)
    orc_e.set_sequence_time(0, 9, 100, True)
    orc_d.set_position(1040, janela.height*(0.7))
    orc_e.set_position(1040, janela.height*(0.7))
    orc = [orc_d, orc_e]

    quest_open = False
    if pontos == 10:
        quest_open = True

    fps = 0
    fr = 0
    contagem = 0

    jumping = False
    gravidade = 100
    pulo = 0
    vida_orc = 2
    damage_orc = 1
    atack1 = 0
    if buff_armor:
        damage_orc = 0

    atack = False
    jumping_orc = False
    Mathias = MatD
    M_anterior = Mat[0]
    platm = plat_1
    golpe = 0
    segue = False
    damage = 1
    orc_floresta = orc[1]
    vel_Orc = 110
    permissao = 0
    pulo_orc = 0
    chao_orc = janela.height*(0.7)
    habilita = False
    habilita2 = False
    while True:
        fundo.draw()
        if janela.delta_time() < 1:
            for i in range (2):
                Mat[i].set_position(Mathias.x, Mathias.y)
                MatA[i].set_position(Mathias.x, Mathias.y)
            if quest_open:
                quest = Sprite("images/quest.png")
                quest.set_position(platm.x + platm.width - quest.width, platm.y - quest.height)
                quest.draw()
                if quest.collided(Mathias):
                    quest_open = False
                    h_buff=random.randint(0,1)
                    if h_buff == 0:
                        buff_damage = True
                    elif h_buff == 1:
                        buff_armor = True



            if (Mathias.x + Mathias.width >= platm.x and Mathias.x <= platm.x + platm.width) and Mathias.y + Mathias.height >= platm.y-20 and Mathias.y <= platm.y and habilita2 == True:
                chao = platm.y - Mathias.height + 9
            if chao == platm.y - Mathias.height + 9 and (Mathias.x <= platm.x - Mathias.width/2 or Mathias.x + Mathias.width/2 >= platm.x + platm.width):
                chao = janela.height*(0.7)
                jumping = True

            golpe += janela.delta_time()
            if golpe > 1 and teclado.key_pressed("space"):
                atack = True
                golpe = 0
                M_anterior = Mathias
            if atack:
                if M_anterior == Mat[0]:
                    Mathias = MatA[0]
                elif M_anterior == Mat[1]:
                    Mathias = MatA[1]
                Mathias.play()
                M = Mathias.get_curr_frame()
                if M == 3:
                    atack = False
                    MatA[0].set_curr_frame(0)
                    MatA[1].set_curr_frame(0)
                    Mathias = M_anterior
            else:

                if teclado.key_pressed("RIGHT"):
                    Mathias = Mat[0]
                    if Mathias.x + Mathias.width <= janela.width:
                        Mathias.x += 100 * janela.delta_time()
                    Mathias.play()
                elif teclado.key_pressed("LEFT"):
                    Mathias = Mat[1]
                    if Mathias.x >= 0:
                        Mathias.x -= 100 * janela.delta_time()
                    Mathias.play()
                else:
                    Mathias.set_curr_frame(0)

            if habilita == False:
                if Mathias.y <= 400:
                    pulo += 100

            elif habilita2 == False:
                if Mathias.y <= 400:
                    pulo += 30
            if teclado.key_pressed("UP") and jumping == False:
                if chao == platm.y - Mathias.height + 9:
                    pulo = -350
                else:
                    pulo = -400
                if Mathias.y >= platm.y and 535 <= Mathias.x <= 828:
                    habilita = False

                elif Mathias.y >= platm.y and 828 < Mathias.x <= 873:
                    habilita2 = False
                else:
                    habilita2 = True
                    habilita = True

                jumping = True

            if jumping == True:
                if not atack:
                    Mathias.set_curr_frame(4)
                Mathias.y += pulo * janela.delta_time() + gravidade * janela.delta_time()
                pulo += 300 * janela.delta_time()

                if Mathias.y >= chao:
                    Mathias.y = chao
                    jumping = False

            Mathias.draw()
            Mathias.update()
            if buff_armor:
                buff_image = GameImage("images/buff_armor.gif")
                buff_image.set_position(100, janela.height*(0.15))
                buff_image.draw()
            if buff_damage:
                buff_image = GameImage("images/buff_damage.gif")
                buff_image.set_position(0, janela.height*(0.15))
                buff_image.draw()


            if len(orc)!=0:
                orc[0].set_position(orc_floresta.x, orc_floresta.y)
                orc[1].set_position(orc_floresta.x, orc_floresta.y)
                if vel_Orc < 0:
                    orc_floresta = orc[1]
                    orc_floresta.play()

                if vel_Orc > 0:
                    orc_floresta = orc[0]
                    orc_floresta.play()
                orc_floresta.update()
                orc_floresta.draw()

            barra_de_vida(Vida_Mathias)
            barra_de_vida_vi(vida_orc, orc_floresta)
            pontuacao(pontos, janela)

            contagem += janela.delta_time()
            fps += 1

            if contagem >= 1:
                fr = fps
                fps = 0
                contagem = 0



            if (orc_floresta.x + orc_floresta.width >= platm.x and orc_floresta.x <= platm.x + platm.width) and orc_floresta.y + orc_floresta.height >= platm.y-20:
                 chao_orc = platm.y - orc_floresta.height + 9
            if chao_orc == platm.y - orc_floresta.height + 9 and (orc_floresta.x <= platm.x - orc_floresta.width/3 or orc_floresta.x + orc_floresta.width/2 >= platm.x + platm.width):
                 chao_orc = janela.height*(0.7)
                 jumping_orc = True



            if (Mathias.x > orc_floresta.x - 150 and Mathias.x < orc_floresta.x) and int(Mathias.y) == int(orc_floresta.y):
                 vel_Orc = 110
                 segue = True


            elif Mathias.x < orc_floresta.x + 150 and orc_floresta.x < Mathias.x and int(Mathias.y) == int(orc_floresta.y):
                 vel_Orc = -110
                 segue = True

            else:
               if orc_floresta.x < platm.x - 200:
                    vel_Orc = -110
                    segue = False
               if orc_floresta.x > janela.width - orc_floresta.width:
                    vel_Orc = 110
                    segue = False
            orc_floresta.x -= vel_Orc*janela.delta_time()

            if not segue and ((int(orc_floresta.x) >= 460 and int(orc_floresta.x) < 470 and vel_Orc < 0) or (int(orc_floresta.x) >= 990 and int(orc_floresta.x) < 1000 and vel_Orc > 0)):
                 permissao = random.randint(0, 2)


            if permissao == 1 or permissao == 2 and jumping_orc == False:
                 pulo_orc = -400
                 jumping_orc = True
                 permissao = 0

            if jumping_orc == True:
                 orc_floresta.y += pulo_orc * janela.delta_time() + gravidade * janela.delta_time()
                 pulo_orc += 300 * janela.delta_time()

                 if orc_floresta.y >= chao_orc:
                    orc_floresta.y = chao_orc
                    jumping_orc = False


            if Mathias.collided(orc_floresta) and len(orc) != 0:
                if atack and ((vel_Orc > 0 and Mathias == MatA[0]) or (vel_Orc < 0 and Mathias == MatA[1])) :
                    atack1 = 0
                    vida_orc -= damage
                    if vel_Orc > 0:
                        orc_floresta.x += 120
                    elif vel_Orc < 0:
                        orc_floresta.x -= 120
                else:
                    atack1 += janela.delta_time()
                if atack1 >= 0.2:
                    Vida_Mathias -= damage_orc
                    atack1 = 0
                    if vel_Orc > 0:
                        orc_floresta.x += 120
                    elif vel_Orc < 0:
                        orc_floresta.x -= 120
                if vida_orc == 0:
                    pontos += 10
                    orc.clear()
            if Vida_Mathias <= 0:
                colocar_no_ranking(nome, pontos)
                return [-1, Vida_Mathias, buff_damage, buff_armor]
            platm.draw()



        if Mathias.x + Mathias.width >= janela.width*(0.95) and vida_orc <= 0:
            if pontos == 20:
                som.pause()
            return [pontos, Vida_Mathias, buff_damage, buff_armor]

        janela.update()
        if teclado.key_pressed("ESC"):
            som.stop()
            colocar_no_ranking(nome, pontos)
            return [-1, Vida_Mathias]




def deserto(tempo, pontos, Vida_Mathias, buff_damage, buff_speed, buff_armor, nome):
    if pontos == 20:
        janela = Window(516, 750)
        janela.set_title('Deserto do Sol Eterno')
        leitura = True
        botao = Sprite("images/botao.png")
        botao.set_position(janela.width-botao.width, 0)
        pergaminho_missao = GameImage("images/pergaminho_do_deserto.gif")
        botao.set_position(janela.width-botao.width, 0)
        botao_cinza = GameImage('images/botao_cinza.png')
        botao_cinza.set_position(botao.x, botao.y)
        while leitura:
            pergaminho_missao.draw()
            botao.draw()
            if teclado.key_pressed("ENTER"):
                leitura = False
            if mouse.is_over_object(botao):
                botao_cinza.draw()
                if mouse.is_button_pressed(1):
                    leitura = False
            janela.update()

    janela = Window(1280, 650)
    fundo = GameImage("images/deserto3.png")

    som = Sound('music/deserto.ogg')


    chao = janela.height*(0.7)

    MatD = Animation("images/mathias_d.png", 5, True)
    MatE = Animation("images/mathias_e.png", 5, True)
    MatD.set_sequence_time(0, 5, 100, True)
    MatE.set_sequence_time(0, 5, 100, True)
    Mat = [MatD, MatE]

    MatE.set_position(janela.width/15 - MatE.width/15, chao)
    MatD.set_position(janela.width/15 - MatD.width/15, chao)

    MatAD = Animation("images/mathias_atack.png", 4, False)
    MatAE = Animation("images/mathias_atack2.png", 4, False)
    MatAD.set_sequence_time(0, 4, 50, False)
    MatAE.set_sequence_time(0, 4, 50, False)
    MatA = [MatAD, MatAE]

    plat_1 = Sprite("images/plat.png")
    plat_2 = Sprite("images/plat.png")
    plat_1.set_position(400, chao - 95)
    plat_2.set_position(900, chao - 180)

    orc_d = Animation("images/deserto_d.png", 6, True)
    orc_e = Animation("images/deserto_e.png", 6, True)
    orc_d.set_sequence_time(0, 6, 100, True)
    orc_e.set_sequence_time(0, 6, 100, True)
    orc_d.set_position(1040, janela.height*(0.7))
    orc_e.set_position(1040, janela.height*(0.7))

    orc_d2 = Animation("images/deserto2_d.png", 7, True)
    orc_e2 = Animation("images/deserto2_e.png", 7, True)
    orc_d2.set_sequence_time(0, 7, 100, True)
    orc_e2.set_sequence_time(0, 7, 100, True)
    orc_d2.set_position(1040, janela.height*(0.7))
    orc_e2.set_position(1040, janela.height*(0.7))


    orc = [orc_d, orc_e]
    orc2 = [orc_d2, orc_e2]

    fps = 0
    fr = 0
    contagem = 0

    jumping = False
    gravidade = 100

    pulo = 0
    vida_orc = 3
    vida_orc2 = 3
    atack = False

    jumping_orc = False
    jumping_orc2 = False
    golpe = 0

    Mathias = MatD
    Mathias_A = MatAD
    M_anterior = Mat[0]

    plath = plat_2
    platm = plat_1

    segue = False
    segue2 = False

    quest_open = False
    if pontos == 20:
        quest_open = True

    damage = 1
    damage_orc = 2
    if buff_armor:
        damage_orc = 1

    orc_deserto = orc[1]
    orc_deserto2 = orc2[0]

    atack1 = 0
    atack2 = 0
    vel_Orc = 110
    vel_Orc2 = -110

    permissao = 0
    permissao2 = 0

    pulo_orc = 0
    pulo_orc2 = 0
    habilita = False
    habilita2 = False
    Vel_Mathias = 110

    chao_orc = janela.height*(0.7)
    chao_orc2 = janela.height*(0.7)

    janela.set_title('Deserto do Sol Eterno')
    while True:
        fundo.draw()
        if janela.delta_time() < 1:

            som.play()


            if quest_open:
                quest = Sprite("images/quest.png")
                quest.set_position(1000, plat_2.y - quest.height)
                quest.draw()
                if quest.collided(Mathias):
                    quest_open = False
                    h_buff=random.randint(0,2)
                    if h_buff == 0:
                        if Vida_Mathias == 9:
                            Vida_Mathias += 1
                        if Vida_Mathias == 8:
                            Vida_Mathias += 2
                        if Vida_Mathias <= 7:
                            Vida_Mathias += 3
                    elif h_buff == 1:
                        buff_speed = True
                    elif h_buff == 2:
                        tempo += 30

            if buff_damage:
                damage = 3
                buff_image = GameImage("images/buff_damage.gif")
                buff_image.set_position(0, janela.height*(0.15))
                buff_image.draw()
            if buff_speed:
                Vel_Mathias = 220
                buff_image = GameImage("images/buff_speed.gif")
                buff_image.set_position(50, janela.height*(0.15))
                buff_image.draw()
            if buff_armor:
                buff_image = GameImage("images/buff_armor.gif")
                buff_image.set_position(100, janela.height*(0.15))
                buff_image.draw()

            for i in range (2):
                Mat[i].set_position(Mathias.x, Mathias.y)
                MatA[i].set_position(Mathias.x, Mathias.y)

            platm.draw()
            plath.draw()

            if (Mathias.x + Mathias.width >= platm.x and Mathias.x <= platm.x + platm.width) and Mathias.y + Mathias.height >= platm.y-20 and Mathias.y <= platm.y:
                chao = platm.y - Mathias.height + 3
            elif Mathias.collided(platm):
                pulo = 0
                chao = janela.height*(0.7)
                jumping = True
            if chao == platm.y - Mathias.height + 3 and (Mathias.x <= platm.x - Mathias.width/2 or Mathias.x + Mathias.width/2 >= platm.x + platm.width):
                chao = janela.height*(0.7)
                jumping = True
            if (Mathias.x + Mathias.width >= plath.x and Mathias.x <= plath.x + plath.width) and Mathias.y + Mathias.height >= plath.y-20 and Mathias.y <= plath.y:
                chao = plath.y - Mathias.height + 3
            elif Mathias.collided(plath):
                pulo = 0
                chao = janela.height*(0.7)
            if chao == plath.y - Mathias.height + 3 and (Mathias.x <= plath.x - Mathias.width/2):
                chao = janela.height*(0.7)
                jumping = True

            for i in range (2):
                Mat[i].set_position(Mathias.x, Mathias.y)
                MatA[i].set_position(Mathias.x, Mathias.y)
            golpe += janela.delta_time()
            if golpe > 1 and teclado.key_pressed("space"):
                atack = True
                golpe = 0
                M_anterior = Mathias
            if atack:
                if M_anterior == Mat[0]:
                    Mathias = MatA[0]
                elif M_anterior == Mat[1]:
                    Mathias = MatA[1]
                Mathias.play()
                M = Mathias.get_curr_frame()
                if M == 3:
                    atack = False
                    MatA[0].set_curr_frame(0)
                    MatA[1].set_curr_frame(0)
                    Mathias = M_anterior
            else:

                if teclado.key_pressed("RIGHT"):
                    Mathias = Mat[0]
                    if Mathias.x + Mathias.width <= janela.width:
                        Mathias.x += Vel_Mathias * janela.delta_time()
                    Mathias.play()
                elif teclado.key_pressed("LEFT"):
                    Mathias = Mat[1]
                    if Mathias.x >= 0:
                        Mathias.x -= Vel_Mathias * janela.delta_time()
                    Mathias.play()
                else:
                    Mathias.set_curr_frame(0)

            if teclado.key_pressed("UP") and jumping == False:
                pulo = -400
                jumping = True

            if jumping == True:
                if not atack:
                    Mathias.set_curr_frame(4)
                Mathias.y += pulo * janela.delta_time() + gravidade * janela.delta_time()
                pulo += 300 * janela.delta_time()
                if Mathias.y >= chao:
                    Mathias.y = chao
                    jumping = False
            Mathias.draw()
            Mathias.update()

            if len(orc)!= 0:
                orc[0].set_position(orc_deserto.x, orc_deserto.y)
                orc[1].set_position(orc_deserto.x, orc_deserto.y)
                if vel_Orc < 0:
                    orc_deserto = orc[0]
                    orc_deserto.play()
                if vel_Orc > 0:
                    orc_deserto = orc[1]
                    orc_deserto.play()
                orc_deserto.draw()
                orc_deserto.update()


            if len(orc2)!= 0:
                orc2[0].set_position(orc_deserto2.x, orc_deserto2.y)
                orc2[1].set_position(orc_deserto2.x, orc_deserto2.y)
                if vel_Orc2 < 0:
                    orc_deserto2 = orc2[0]
                    orc_deserto2.play()
                if vel_Orc2 > 0:
                    orc_deserto2 = orc2[1]
                    orc_deserto2.play()
                orc_deserto2.draw()
                orc_deserto2.update()



            barra_de_vida(Vida_Mathias)
            barra_de_vida_vi(vida_orc, orc_deserto)
            barra_de_vida_vi(vida_orc2, orc_deserto2)
            pontuacao(pontos, janela)

            janela.draw_text('TEMPO: ' + str(tempo), janela.width/1.3, janela.height/10, size = 28, color = (200, 2, 2), font_name = 'Tahoma', bold = False, italic = False)

            if tempo == -1:
                colocar_no_ranking(nome, pontos)
                som.stop()
                return [tempo, -1, Vida_Mathias, buff_damage, buff_speed]

            contagem += janela.delta_time()
            fps += 1

            if contagem >= 1:
                fr = fps
                fps = 0
                contagem = 0
                tempo -= 1



            if (orc_deserto.x + orc_deserto.width >= platm.x and orc_deserto.x <= platm.x + platm.width) and orc_deserto.y + orc_deserto.height >= platm.y-20:
                chao_orc = platm.y - orc_deserto.height + 3
            if chao_orc == platm.y - orc_deserto.height + 3 and (orc_deserto.x <= platm.x - orc_deserto.width/3 or orc_deserto.x + orc_deserto.width/2 >= platm.x + platm.width):
                chao_orc = janela.height*(0.7)
                jumping_orc = True
            if (orc_deserto.x + orc_deserto.width >= plath.x and orc_deserto.x <= plath.x + plath.width) and orc_deserto.y + orc_deserto.height >= plath.y-20:
                chao_orc = plath.y - orc_deserto.height + 3
            if chao_orc == plath.y - orc_deserto.height + 3 and orc_deserto.x <= plath.x - orc_deserto.width/3:
                chao_orc = janela.height*(0.7)
                jumping_orc = True


            if Mathias.x > orc_deserto.x - 110 and Mathias.x < orc_deserto.x and int(orc_deserto.y) == int(Mathias.y):
                vel_Orc = 110
                segue = True

            elif Mathias.x < orc_deserto.x + 110 and orc_deserto.x < Mathias.x and int(orc_deserto.y) == int(Mathias.y):
                vel_Orc = -110
                segue = True

            else:
                if orc_deserto.x < platm.x - 150 :
                    vel_Orc = -110
                    segue = False
                if orc_deserto.x > janela.width - orc_deserto.width:
                    vel_Orc = 110
                    segue = False
            orc_deserto.x -= vel_Orc *janela.delta_time()

            if not segue and ((int(orc_deserto.x) >= 250 and int(orc_deserto.x) < 255 and vel_Orc > 0) or (int(orc_deserto.x) >= 790 and int(orc_deserto.x) < 795 and vel_Orc > 0)):
                permissao = random.randint(0, 2)

            if permissao == 1 or permissao == 2 and jumping_orc == False:
                pulo_orc = -400
                jumping_orc = True
                permissao = 0

            if jumping_orc == True:
                orc_deserto.y += pulo_orc * janela.delta_time() + gravidade * janela.delta_time()
                pulo_orc += 300 * janela.delta_time()

                if orc_deserto.y >= chao_orc:
                    orc_deserto.y = chao_orc
                    jumping_orc = False



            if Mathias.collided(orc_deserto) and len(orc) != 0:
                if atack and ((vel_Orc > 0 and Mathias == MatA[0]) or (vel_Orc < 0 and Mathias == MatA[1])):
                    vida_orc -= damage
                    atack1 = 0
                    if vel_Orc > 0:
                        orc_deserto.x += 120
                    elif vel_Orc < 0:
                        orc_deserto.x -= 120
                else:
                    atack1 += janela.delta_time()
                if atack1 >= 0.3:
                    atack1=0
                    Vida_Mathias -= damage_orc
                    if vel_Orc > 0:
                        orc_deserto.x += 120
                    elif vel_Orc < 0:
                        orc_deserto.x -= 120
                if vida_orc <= 0:
                    pontos += 5
                    orc.clear()

            if Mathias.collided(orc_deserto2) and len(orc2) != 0:
                if atack and ((vel_Orc2 > 0 and Mathias == MatA[0]) or (vel_Orc2 < 0 and Mathias == MatA[1])):
                    vida_orc2 -= damage
                    atack2 = 0
                    if vel_Orc2 > 0:
                        orc_deserto2.x += 120
                    elif vel_Orc < 0:
                        orc_deserto2.x -= 120
                else:
                    atack2 += janela.delta_time()
                if atack2 >= 0.3:
                    atack2=0
                    Vida_Mathias -= damage_orc
                    if vel_Orc2 > 0:
                        orc_deserto2.x += 120
                    elif vel_Orc2 < 0:
                        orc_deserto2.x -= 120
                if vida_orc2 <= 0:
                    pontos += 5
                    orc2.clear()
            if Vida_Mathias <= 0:
                som.stop()
                colocar_no_ranking(nome, pontos)
                return [tempo, -1, Vida_Mathias, buff_damage, buff_speed]


            if (orc_deserto2.x + orc_deserto2.width >= platm.x and orc_deserto2.x <= platm.x + platm.width) and orc_deserto2.y + orc_deserto2.height >= platm.y-20:
                chao_orc2 = platm.y - orc_deserto2.height + 3
            if chao_orc2 == platm.y - orc_deserto2.height + 3 and (orc_deserto2.x <= platm.x - orc_deserto2.width/3 or orc_deserto2.x + orc_deserto2.width/2 >= platm.x + platm.width):
                chao_orc2 = janela.height*(0.7)
                jumping_orc2 = True
            if (orc_deserto2.x + orc_deserto2.width >= plath.x and orc_deserto2.x <= plath.x + plath.width) and orc_deserto2.y + orc_deserto2.height >= plath.y-20:
                chao_orc2 = plath.y - orc_deserto2.height + 3
            if chao_orc2 == plath.y - orc_deserto2.height + 3 and orc_deserto2.x <= plath.x - orc_deserto2.width/3:
                chao_orc2 = janela.height*(0.7)
                jumping_orc2 = True


            if Mathias.x > orc_deserto2.x - 110 and Mathias.x < orc_deserto2.x and int(orc_deserto2.y) == int(Mathias.y):
                vel_Orc2 = 110
                segue2 = True

            elif Mathias.x < orc_deserto2.x + 110 and orc_deserto2.x < Mathias.x and int(orc_deserto2.y) == int(Mathias.y):
                vel_Orc2 = -110
                segue2 = True

            else:
                if orc_deserto2.x < platm.x - 150 :
                    vel_Orc2 = -110
                    segue2 = False
                if orc_deserto2.x > janela.width - orc_deserto2.width:
                    vel_Orc2 = 110
                    segue2 = False
            orc_deserto2.x -= vel_Orc2 *janela.delta_time()

            if not segue2 and ((int(orc_deserto2.x) >= 250 and int(orc_deserto2.x) < 255 and vel_Orc2 > 0) or (int(orc_deserto2.x) >= 790 and int(orc_deserto2.x) < 795 and vel_Orc2 > 0)):
                permissao2 = random.randint(0, 2)

            if permissao2 == 1 or permissao2 == 2 and jumping_orc2 == False:
                pulo_orc2 = -400
                jumping_orc2 = True
                permissao2 = 0

            if jumping_orc2 == True:
                orc_deserto2.y += pulo_orc2 * janela.delta_time() + gravidade * janela.delta_time()
                pulo_orc2 += 300 * janela.delta_time()

                if orc_deserto2.y >= chao_orc2:
                    orc_deserto2.y = chao_orc2
                    jumping_orc2 = False


        if Mathias.x + Mathias.width >= janela.width*(0.95) and vida_orc <= 0 and vida_orc2 <= 0:

            som.stop()
            return [tempo, pontos, Vida_Mathias, buff_speed]



        janela.update()
        if teclado.key_pressed("ESC"):
            som.stop()
            colocar_no_ranking(nome, pontos)
            return [tempo, -1, Vida_Mathias, buff_speed]

def castelo(pontos, Vida_Mathias, buff_damage, buff_speed, buff_armor, nome):
    janela = Window(1280, 640)
    janela.set_title('Castelo de Ilinois')
    fundo = GameImage("images/castelobk.png")
    fundo2 = GameImage('images/povoado.gif')
    fundo2.x = 60

    som = Sound('music/castelo.ogg')
    som.play()

    chao = janela.height*(0.75)

    MatD = Animation("images/mathias_d.png", 5, True)
    MatE = Animation("images/mathias_e.png", 5, True)
    MatD.set_sequence_time(0, 5, 100, True)
    MatE.set_sequence_time(0, 5, 100, True)
    Mat = [MatD, MatE]

    MatE.set_position(janela.width/15 - MatE.width/15, chao)
    MatD.set_position(janela.width/15 - MatD.width/15, chao)

    MatAD = Animation("images/mathias_atack.png", 4, False)
    MatAE = Animation("images/mathias_atack2.png", 4, False)
    MatAD.set_sequence_time(0, 4, 50, False)
    MatAE.set_sequence_time(0, 4, 50, False)
    MatA = [MatAD, MatAE]

    plat_1 = Sprite("images/plat_castelo.gif")
    plat_1.set_position(550, chao - 85)


    orc_d = Animation("images/deserto_d.png", 6, True)
    orc_e = Animation("images/deserto_e.png", 6, True)
    orc_d.set_sequence_time(0, 6, 100, True)
    orc_e.set_sequence_time(0, 6, 100, True)
    orc_d.set_position(1040, janela.height*(0.7))
    orc_e.set_position(1040, janela.height*(0.7))
    orc = [orc_d, orc_e]

    fps = 0
    fr = 0
    contagem = 0
    atack1 = 0

    jumping = False
    gravidade = 100

    pulo = 0
    vida_orc = 3
    atack = False

    tela = False
    jumping_orc = False

    Mathias = MatD

    platm = plat_1

    segue = False

    damage_orc = 2
    if buff_armor:
        damage_orc = 1

    damage = 1

    orc_castelo = orc[1]
    vel_Orc = 110
    permissao = 0
    pulo_orc = 0
    chao_orc = janela.height*(0.7)

    M_anterior = Mat[0]
    mago_on = True
    first = True
    golpe = 0
    carregar = 0
    vida_mago = 1
    magias = []
    Vel_Mathias = 110
    habilita = False
    while 1:
        fundo2.draw()
        fundo.draw()


        if janela.delta_time() < 1:
            if mago_on:
                if first:
                    mago = Sprite("images/mago.gif")
                    mago.set_position(1100, janela.height*(0.7))
                    first = False
                carregar += janela.delta_time()
                if carregar >= 1.5:
                    conjurar = random.randint(0, 4)
                    carregar = 0
                    if conjurar == 0 or conjurar == 1:
                        feitico = Sprite("images/magia.gif")
                        feitico.set_position(1050, mago.y + mago.height/2)
                        magias.append(feitico)
                for i in magias:
                    i.draw()
                    i.x -= 120 * janela.delta_time()
                    if i.x + i.width < 0:
                        magias.remove(i)
                    if Mathias.collided(i):
                        if buff_armor:
                            Vida_Mathias -= 2
                        else:
                            Vida_Mathias -= 3
                        magias.remove(i)
                if mago.collided(Mathias) and atack:
                    vida_mago -= 1
                    pontos += 5
                    mago_on = False
                mago.draw()


            if buff_damage:
                damage = 3
                buff_image = GameImage("images/buff_damage.gif")
                buff_image.set_position(0, janela.height*(0.15))
                buff_image.draw()
            if buff_speed:
                Vel_Mathias = 220
                buff_image = GameImage("images/buff_speed.gif")
                buff_image.set_position(50, janela.height*(0.15))
                buff_image.draw()
            if buff_armor:
                buff_image = GameImage("images/buff_armor.gif")
                buff_image.set_position(100, janela.height*(0.15))
                buff_image.draw()

            Mat[0].set_position(Mathias.x, Mathias.y)
            Mat[1].set_position(Mathias.x, Mathias.y)


            platm = plat_1
            platm.draw()

            if (Mathias.x + Mathias.width >= platm.x and Mathias.x <= platm.x + platm.width) and Mathias.y + Mathias.height >= platm.y-20 and Mathias.y <= platm.y:
                chao = platm.y - Mathias.height + 3
            elif Mathias.collided(platm):
                pulo = 0
                chao = janela.height*(0.75)
                jumping = True
            if chao == platm.y - Mathias.height + 3 and (Mathias.x <= platm.x - Mathias.width/2 or Mathias.x + Mathias.width/2 >= platm.x + platm.width):
                chao = janela.height*(0.75)
                jumping = True


            if len(orc)!=0:
                orc[0].set_position(orc_castelo.x, orc_castelo.y)
                orc[1].set_position(orc_castelo.x, orc_castelo.y)
                if vel_Orc < 0:
                    orc_castelo = orc[0]
                    orc_castelo.play()
                if vel_Orc > 0:
                    orc_castelo = orc[1]
                    orc_castelo.play()
                orc_castelo.draw()
                orc_castelo.update()

            barra_de_vida(Vida_Mathias)
            barra_de_vida_vi(vida_orc, orc_castelo)
            barra_de_vida_vi(vida_mago, mago)
            pontuacao(pontos, janela)
            salva = Mathias.x
            for i in range (2):
                Mat[i].set_position(Mathias.x, Mathias.y)
                MatA[i].set_position(Mathias.x, Mathias.y)
            golpe += janela.delta_time()
            if golpe > 1 and teclado.key_pressed("space"):
                atack = True
                golpe = 0
                M_anterior = Mathias
            if atack:
                if M_anterior == Mat[0]:
                    Mathias = MatA[0]
                elif M_anterior == Mat[1]:
                    Mathias = MatA[1]
                Mathias.play()
                M = Mathias.get_curr_frame()
                if M == 3:
                    atack = False
                    MatA[0].set_curr_frame(0)
                    MatA[1].set_curr_frame(0)
                    Mathias = M_anterior
            else:

                if teclado.key_pressed("RIGHT"):
                    Mathias = Mat[0]
                    if Mathias.x + Mathias.width <= janela.width:
                        Mathias.x += Vel_Mathias * janela.delta_time()
                    Mathias.play()
                elif teclado.key_pressed("LEFT"):
                    Mathias = Mat[1]
                    if Mathias.x >= 0:
                        Mathias.x -= Vel_Mathias * janela.delta_time()
                    Mathias.play()
                else:
                    Mathias.set_curr_frame(0)

            if teclado.key_pressed("UP") and jumping == False:
                pulo = -400
                jumping = True

            if jumping == True:
                if not atack:
                    Mathias.set_curr_frame(4)
                Mathias.y += pulo * janela.delta_time() + gravidade * janela.delta_time()
                pulo += 300 * janela.delta_time()
                if Mathias.y >= chao:
                    Mathias.y = chao
                    jumping = False
            Mathias.draw()
            Mathias.update()
            if Mathias.x > salva:
                fundo2.x -= 0.6
            elif Mathias.x < salva:
                fundo2.x += 0.6

            contagem += janela.delta_time()
            fps += 1

            if contagem >= 1:
                fr = fps
                fps = 0
                contagem = 0



            if (orc_castelo.x + orc_castelo.width >= platm.x and orc_castelo.x <= platm.x + platm.width) and orc_castelo.y + orc_castelo.height >= platm.y-20:
                chao_orc = platm.y - orc_castelo.height + 3
            if chao_orc == platm.y - orc_castelo.height + 3 and (orc_castelo.x <= platm.x - orc_castelo.width/3 or orc_castelo.x + orc_castelo.width/2 >= platm.x + platm.width):
                chao_orc = janela.height*(0.7)
                jumping_orc = True

            if Mathias.x > orc_castelo.x - 110 and Mathias.x < orc_castelo.x and int(orc_castelo.y) == int(Mathias.y):
                vel_Orc = 110
                segue = True

            elif Mathias.x < orc_castelo.x + 110 and orc_castelo.x < Mathias.x and int(orc_castelo.y) == int(Mathias.y):
                vel_Orc = -110
                segue = True

            else:
                if orc_castelo.x < platm.x - 250:
                    vel_Orc = -110
                    segue = False
                if orc_castelo.x > platm.x + platm.width + 250:
                    vel_Orc = 110
                    segue = False
            orc_castelo.x -= vel_Orc*janela.delta_time()

            if not segue and ((int(orc_castelo.x) >= 400 and int(orc_castelo.x) < 405 and vel_Orc < 0) or (int(orc_castelo.x) >= 890 and int(orc_castelo.x) < 895 and vel_Orc > 0)):
                permissao = random.randint(0, 2)

            if permissao == 1 or permissao == 2 and jumping_orc == False:
                pulo_orc = -400
                jumping_orc = True
                permissao = 0

            if jumping_orc == True:
                orc_castelo.y += pulo_orc * janela.delta_time() + gravidade * janela.delta_time()
                pulo_orc += 300 * janela.delta_time()

                if orc_castelo.y >= chao_orc:
                    orc_castelo.y = chao_orc
                    jumping_orc = False

            if Mathias.collided(orc_castelo) and len(orc) != 0:
                if atack and ((vel_Orc > 0 and Mathias == MatA[0]) or (vel_Orc < 0 and Mathias == MatA[1])):
                    vida_orc -= damage
                    atack1 = 0
                    if vel_Orc > 0:
                        orc_castelo.x += 120
                    elif vel_Orc < 0:
                        orc_castelo.x -= 120
                else:
                    atack1 += janela.delta_time()
                if atack1 >= 0.2:
                    atack1 = 0
                    Vida_Mathias -= damage_orc
                    if vel_Orc > 0:
                        orc_castelo.x += 120
                    elif vel_Orc < 0:
                        orc_castelo.x -= 120
                if vida_orc <= 0:
                    pontos += 5
                    orc.clear()
        if Vida_Mathias <= 0:
            som.stop()
            colocar_no_ranking(nome,pontos)
            return [-1, Vida_Mathias, buff_damage, buff_speed]


        if Mathias.x + Mathias.width >= janela.width*(0.95) and vida_orc <= 0 and vida_mago <= 0:
            if pontos == 80:
                som.pause()
            return [pontos, Vida_Mathias, buff_damage, buff_speed]

        janela.update()
        if teclado.key_pressed("ESC"):
            som.stop()
            colocar_no_ranking(nome, pontos)
            return [-1, Vida_Mathias, buff_damage, buff_speed]

def fase_final(pontos, Vida_Mathias, buff_damage, buff_speed, buff_armor, nome):
    parte = 1
    buff_fogo = False

    while parte == 1:
        janela = Window(1280, 680)
        janela.set_title('Calabouço do Castelo')
        fundo = GameImage("images/calabouco_b.gif")
        chao = janela.height*(0.8)
        mouse = Mouse()

        som = Sound('music/fase_final.ogg')
        som.play()

        MatD = Animation("images/mathias_d.png", 5, True)
        MatE = Animation("images/mathias_e.png", 5, True)
        MatD.set_sequence_time(0, 5, 100, True)
        MatE.set_sequence_time(0, 5, 100, True)
        Mat = [MatD, MatE]

        MatE.set_position(janela.width/15 - MatE.width/15, chao)
        MatD.set_position(janela.width/15 - MatD.width/15, chao)

        MatAD = Animation("images/mathias_atack.png", 4, False)
        MatAE = Animation("images/mathias_atack2.png", 4, False)
        MatAD.set_sequence_time(0, 4, 50, False)
        MatAE.set_sequence_time(0, 4, 50, False)
        MatA = [MatAD, MatAE]


        plat_1 = Sprite("images/plat_castelo.gif")
        plat_1.set_position(550, chao - 75)

        jumping = False
        gravidade = 100

        pulo = 0
        Mathias = MatD
        Vel_Mathias = 110
        platm = plat_1
        mago_on = True

        mago = Sprite("images/mago_rei1.gif")
        mago.set_position(platm.x + platm.width - mago.width, platm.y - mago.height)
        mago_e = Sprite("images/mago_rei.gif")
        mago_e.set_position(platm.x + platm.width - mago_e.width, platm.y - mago_e.height)
        mago_rei = mago
        troca = True

        golpe = 0
        M_anterior = Mat[0]
        atack = False

        habilita1 = True
        while 1:
            fundo.draw()


            if janela.delta_time() < 1:
                mago_rei.draw()
                platm.draw()


                if buff_damage:
                    damage = 3
                    buff_image = GameImage("images/buff_damage.gif")
                    buff_image.set_position(0, janela.height*(0.15))
                    buff_image.draw()
                if buff_speed:
                    Vel_Mathias = 220
                    buff_image = GameImage("images/buff_speed.gif")
                    buff_image.set_position(50, janela.height*(0.15))
                    buff_image.draw()
                if buff_armor:
                    buff_image = GameImage("images/buff_armor.gif")
                    buff_image.set_position(100, janela.height*(0.15))
                    buff_image.draw()

                if (Mathias.x + Mathias.width >= platm.x and Mathias.x <= platm.x + platm.width) and Mathias.y + Mathias.height >= platm.y - 20 and Mathias.y <= platm.y and habilita1 == True:
                    chao = platm.y - Mathias.height + 3
                    mago_rei = mago_e

                if chao == platm.y - Mathias.height + 3 and (Mathias.x <= platm.x - Mathias.width/2 or Mathias.x + Mathias.width/2 >= platm.x + platm.width):
                    chao = janela.height*(0.8)
                    jumping = True
                    mago_rei = mago

                if chao == platm.y - Mathias.height + 3 and Mathias.x < mago_rei.x and Mathias.x > mago_rei.x - 50 and troca:
                    gio = menu_pergaminho()
                    if gio == 1:
                        buff_fogo = True
                        break
                    if gio == -1:
                        Vida_Mathias = 10
                        break

                barra_de_vida(Vida_Mathias)
                for i in range (2):
                    Mat[i].set_position(Mathias.x, Mathias.y)
                    MatA[i].set_position(Mathias.x, Mathias.y)
                golpe += janela.delta_time()
                if golpe > 1 and teclado.key_pressed("space"):
                    atack = True
                    golpe = 0
                    M_anterior = Mathias
                if atack:
                    if M_anterior == Mat[0]:
                        Mathias = MatA[0]
                    elif M_anterior == Mat[1]:
                        Mathias = MatA[1]
                    Mathias.play()
                    M = Mathias.get_curr_frame()
                    if M == 3:
                        atack = False
                        MatA[0].set_curr_frame(0)
                        MatA[1].set_curr_frame(0)
                        Mathias = M_anterior
                else:

                    if teclado.key_pressed("RIGHT"):
                        Mathias = Mat[0]
                        if Mathias.x + Mathias.width <= janela.width:
                            Mathias.x += Vel_Mathias * janela.delta_time()
                        Mathias.play()
                    elif teclado.key_pressed("LEFT"):
                        Mathias = Mat[1]
                        if Mathias.x >= 0:
                            Mathias.x -= Vel_Mathias * janela.delta_time()
                        Mathias.play()
                    else:
                        Mathias.set_curr_frame(0)


                if teclado.key_pressed("UP") and jumping == False:
                    if Mathias.y > platm.y and 505 <= Mathias.x <= 825:
                        habilita1 = False
                    else:
                        habilita1 = True


                    pulo = -400
                    jumping = True

                if habilita1 == False:
                    pulo += 50


                if jumping == True:
                    if not atack:
                        Mathias.set_curr_frame(4)
                    Mathias.y += pulo * janela.delta_time() + gravidade * janela.delta_time()
                    pulo += 300 * janela.delta_time()
                    if Mathias.y >= chao:
                        Mathias.y = chao
                        jumping = False
                Mathias.draw()
                Mathias.update()
            janela.update()
        parte = 2
    while parte == 2:
        leitura = True
        while leitura:
            per = Window(516, 750)
            per.set_title('Calabouço do Castelo')
            fundo = GameImage("images/pergaminho_do_mago2.gif")
            botao= Sprite("images/botao.png")
            botao.set_position(per.width-botao.width, 0)
            botao_cinza = GameImage('images/botao_cinza.png')
            botao_cinza.set_position(botao.x, botao.y)
            mouse = Mouse()
            while 1:
                fundo.draw()
                botao.draw()
                if teclado.key_pressed("enter"):
                    leitura = False
                    parte = 3
                    break

                if mouse.is_over_object(botao):
                    botao_cinza.draw()
                    if mouse.is_button_pressed(1):
                        leitura = False
                        parte = 3
                        break
                per.update()


    while parte == 3:

        janela = Window(1180, 786)
        janela.set_title('Calabouço do Castelo')
        fundo = GameImage("images/calabouco_c.gif")
        chao = janela.height*(0.75)

        MatD = Animation("images/mathias_d.png", 5, True)
        MatE = Animation("images/mathias_e.png", 5, True)
        MatD.set_sequence_time(0, 5, 100, True)
        MatE.set_sequence_time(0, 5, 100, True)
        Mat = [MatD, MatE]

        MatE.set_position(janela.width/15 - MatE.width/15, chao)
        MatD.set_position(janela.width/15 - MatD.width/15, chao)

        MatAD = Animation("images/mathias_atack.png", 4, False)
        MatAE = Animation("images/mathias_atack2.png", 4, False)
        MatAD.set_sequence_time(0, 4, 50, False)
        MatAE.set_sequence_time(0, 4, 50, False)
        MatA = [MatAD, MatAE]

        plat_1 = Sprite("images/plat_castelo.gif")
        plat_1.set_position(600, chao - 95)

        Illinois_Humano = Animation("images/Illinois_d.png", 3, True)
        Illinois_Humano.set_sequence_time(0, 3, 100, True)
        Illinois_Humanoe = Animation("images/Illinois_e.png", 3, True)
        Illinois_Humanoe.set_sequence_time(0, 3, 100, True)
        Illinois_Humano.set_position(1040, janela.height*(0.75))
        Illinois_Humanoe.set_position(1040, janela.height*(0.75))
        Illi = [Illinois_Humanoe, Illinois_Humano]

        Illinois_Criatura = Animation("images/Illinois_2d.png", 4, True)
        Illinois_Criatura.set_sequence_time(0, 4, 100, True)
        Illinois_Criaturae = Animation("images/Illinois_2.png", 4, True)
        Illinois_Criaturae.set_sequence_time(0, 4, 100, True)
        Illinois_Criatura.set_position(1040, janela.height*(0.75))
        Illinois_Criaturae.set_position(1040, janela.height*(0.75))
        Illi_C = [Illinois_Criaturae, Illinois_Criatura]

        fps = 0
        fr = 0
        contagem = 0


        jumping = False
        gravidade = 100

        pulo = 0
        vida_illi = 9
        atack = False

        jumping_illi = False

        Mathias = MatD


        platm = plat_1

        segue = False


        damage = 1

        Illinois = Illi[0]
        vel_Illinois = 170
        permissao = 0
        pulo_Illi = 0
        chao_Illi = janela.height*(0.75)
        Vel_Mathias = 110

        golpe = 0
        M_anterior = Mat[0]
        atack1 = 0


        feiticos_Mathias = []
        magias_fogo = 3
        conjurar = 0

        habilita1 = True

        while True:
            fundo.draw()




            if janela.delta_time() < 1:


                platm = plat_1


                platm.draw()
                if buff_fogo and magias_fogo > 0:
                    if teclado.key_pressed("C") :
                        conjurar += janela.delta_time()
                        if conjurar >= 1.5:
                            magias_fogo -= 1
                            conjurar = 0
                            magia = Sprite("images/magia_2.gif")
                            magia.set_position(Mathias.x, Mathias.y+Mathias.height/2)
                            feiticos_Mathias.append(magia)
                for i in feiticos_Mathias:
                    i.x += 210 * janela.delta_time()
                    i.draw()
                    if i.x > janela.width:
                        feiticos_Mathias.remove(i)
                    if i.collided(Illinois):
                        vida_illi -= 2
                        feiticos_Mathias.remove(i)

                if (Mathias.x + Mathias.width >= platm.x and Mathias.x <= platm.x + platm.width) and Mathias.y + Mathias.height >= platm.y - 20 and Mathias.y <= platm.y and habilita1 == True:
                    chao = platm.y - Mathias.height + 9
                if chao == platm.y - Mathias.height + 9 and (Mathias.x <= platm.x - Mathias.width/2 or Mathias.x + Mathias.width/2 >= platm.x + platm.width):
                    chao = janela.height*(0.75)
                    jumping = True


                if vida_illi > 3:
                    Illi[0].set_position(Illinois.x, Illinois.y)
                    Illi[1].set_position(Illinois.x, Illinois.y)
                    damage_illi = 2
                    if buff_armor:
                        damage_illi = 1
                    if vel_Illinois < 0:
                        Illinois = Illi[1]
                        Illinois.play()
                    if vel_Illinois > 0:
                        Illinois = Illi[0]
                        Illinois.play()
                    Illinois.draw()
                    Illinois.update()
                elif vida_illi > 0:
                    Illi_C[0].set_position(Illinois.x, Illinois.y)
                    Illi_C[1].set_position(Illinois.x, Illinois.y)
                    damage_illi = 5
                    if buff_armor:
                        damage_illi = 4
                    if vel_Illinois < 0:
                        Illinois = Illi_C[1]
                        Illinois.play()
                    if vel_Illinois > 0:
                        Illinois = Illi_C[0]
                        Illinois.play()
                    Illinois.draw()
                    Illinois.update()
                elif vida_illi <= 0:
                    pontos += 10
                    som.stop()
                    colocar_no_ranking(nome, pontos)
                    return 1

                for i in range (2):
                    Mat[i].set_position(Mathias.x, Mathias.y)
                    MatA[i].set_position(Mathias.x, Mathias.y)
                golpe += janela.delta_time()
                if golpe > 1 and teclado.key_pressed("space"):
                    atack = True
                    golpe = 0
                    M_anterior = Mathias
                if atack :
                    if M_anterior == Mat[0]:
                        Mathias = MatA[0]
                    elif M_anterior == Mat[1]:
                        Mathias = MatA[1]
                    Mathias.play()
                    M = Mathias.get_curr_frame()
                    if M == 3:
                        atack = False
                        MatA[0].set_curr_frame(0)
                        MatA[1].set_curr_frame(0)
                        Mathias = M_anterior
                else:

                    if teclado.key_pressed("RIGHT"):
                        Mathias = Mat[0]
                        if Mathias.x + Mathias.width <= janela.width:
                            Mathias.x += Vel_Mathias * janela.delta_time()
                        Mathias.play()
                    elif teclado.key_pressed("LEFT"):
                        Mathias = Mat[1]
                        if Mathias.x >= 0:
                            Mathias.x -= Vel_Mathias * janela.delta_time()
                        Mathias.play()
                    else:
                        Mathias.set_curr_frame(0)


                if teclado.key_pressed("UP") and jumping == False:

                    if Mathias.y > platm.y and 550 <= Mathias.x <= 865 :
                        habilita1 = False
                    else:
                        habilita1 = True

                    pulo = -400
                    jumping = True

                if habilita1 == False:
                    pulo += 25
            

                if jumping == True:
                    if not atack:
                        Mathias.set_curr_frame(4)
                    Mathias.y += pulo * janela.delta_time() + gravidade * janela.delta_time()
                    pulo += 300 * janela.delta_time()
                    if Mathias.y >= chao:
                        Mathias.y = chao
                        jumping = False
                Mathias.draw()
                Mathias.update()

                barra_de_vida(Vida_Mathias)
                barra_de_vida_vi(vida_illi, Illinois)
                pontuacao(pontos, janela)

                contagem += janela.delta_time()
                fps += 1

                if contagem >= 1:
                    fr = fps
                    fps = 0
                    contagem = 0



                if (Illinois.x + Illinois.width >= platm.x and Illinois.x <= platm.x + platm.width) and Illinois.y + Illinois.height >= platm.y-20:
                     chao_Illi = platm.y - Illinois.height + 9
                if chao_Illi == platm.y - Illinois.height + 9 and (Illinois.x <= platm.x - Illinois.width/3 or Illinois.x + Illinois.width/2 >= platm.x + platm.width):
                     chao_Illi = janela.height*(0.75)
                     jumping_illi = True



                if (Mathias.x > Illinois.x - 150 and Mathias.x < Illinois.x) and int(Mathias.y) == int(Illinois.y):
                     vel_Illinois = 110
                     segue= True


                elif Mathias.x < Illinois.x + 150 and Illinois.x < Mathias.x and int(Mathias.y) == int(Illinois.y):
                     vel_Illinois = -110
                     segue= True

                else:
                   if Illinois.x < platm.x - 200:
                        vel_Illinois = -110
                        segue=False
                   if Illinois.x > janela.width - Illinois.width:
                        vel_Illinois = 110
                        segue=False
                Illinois.x -= vel_Illinois*janela.delta_time()

                if not segue and ((int(Illinois.x) >= 460 and int(Illinois.x) < 470 and vel_Illinois < 0) or (int(Illinois.x) >= 990 and int(Illinois.x) < 1000 and vel_Illinois > 0)):
                     permissao = random.randint(0, 2)


                if permissao == 1 or permissao == 2 and jumping_illi == False:
                     pulo_Illi = -400
                     jumping_illi = True
                     permissao = 0

                if jumping_illi == True:
                     Illinois.y += pulo_Illi * janela.delta_time() + gravidade * janela.delta_time()
                     pulo_Illi += 300 * janela.delta_time()

                     if Illinois.y >= chao_Illi:
                        Illinois.y = chao_Illi
                        jumping_illi = False

                if buff_damage:
                    damage = 3
                    buff_image = GameImage("images/buff_damage.gif")
                    buff_image.set_position(0, janela.height*(0.15))
                    buff_image.draw()
                if buff_speed:
                    Vel_Mathias = 220
                    buff_image = GameImage("images/buff_speed.gif")
                    buff_image.set_position(50, janela.height*(0.15))
                    buff_image.draw()
                if buff_armor:
                    buff_image = GameImage("images/buff_armor.gif")
                    buff_image.set_position(100, janela.height*(0.15))
                    buff_image.draw()

                if Mathias.collided(Illinois) and vida_illi > 0:
                    if atack and ((vel_Illinois > 0 and Mathias == MatA[0]) or (vel_Illinois < 0 and Mathias == MatA[1])):
                        vida_illi -= damage
                        atack1 = 0
                        if vel_Illinois > 0:
                            Illinois.x += 100
                        elif vel_Illinois < 0:
                            Illinois.x -= 100

                    else:
                        atack1 += janela.delta_time()
                    if atack1 >= 0.2:
                        atack1 = 0
                        Vida_Mathias -= damage_illi
                        if vel_Illinois > 0:
                            Illinois.x += 100
                        elif vel_Illinois < 0:
                            Illinois.x -= 100


                    if Vida_Mathias <= 0:
                        som.stop()
                        colocar_no_ranking(nome, pontos)
                        return -1

            janela.update()
            if teclado.key_pressed("ESC"):
                return -1
