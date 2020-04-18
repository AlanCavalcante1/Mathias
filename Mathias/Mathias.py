from auxiliares.fases_matias import *
from auxiliares.menu_matias import *
from auxiliares.ranking import *
from PPlay.sound import *

som = Sound('music/musica_russa.ogg')


in_game = True
menu_return = 0

som.play()

tempo = 90
pontos = 0
retorno = [tempo, pontos]
buff_damage = False
buff_speed = False
buff_armor = False
Vida_Mathias = 10

continua = True

while in_game:

    som.play()
    nome = receber_nome()
    if menu_return == 0:
        menu_return = menu()



    if nome == "KIRITO":
        pontos = 50
        tempo = 500
        Vida_Mathias = 10
        buff_speed = True
        buff_damage = True
        buff_armor = True

    if menu_return == 2:
        menu_return = abrir_ranking()

    if menu_return == 1 and pontos < 20:
        som.stop()
        for pontos in (0, 10):
            p_fase = floresta(False, pontos, Vida_Mathias, buff_damage, buff_armor, nome)
            pontos = p_fase[0]
            Vida_Mathias = p_fase[1]
            if pontos == -1:
                pontos = 0
                Vida_Mathias = 10
                menu_return = 0
                break
    if menu_return == -1 and pontos < 20:
        som.stop()

        for pontos in (0, 10):
            p_fase = floresta(True, pontos, Vida_Mathias, buff_damage, buff_armor, nome)
            pontos = p_fase[0]
            Vida_Mathias = p_fase[1]
            if pontos == -1:
                pontos = 0
                Vida_Mathias = 10
                menu_return = 0
                break
            buff_damage = p_fase[2]
            buff_armor = p_fase[3]

    if pontos >= 20 and pontos < 50:
        som.stop()
        for pontos in (20, 30, 40):
            if tempo > 0:
                s_fase = deserto(tempo, pontos, Vida_Mathias, buff_damage, buff_speed, buff_armor, nome)
                tempo = s_fase[0]
                pontos = s_fase[1]
                if pontos == -1:
                    tempo = 60
                    pontos = 0
                    buff_damage = False
                    buff_speed = False
                    buff_armor = False
                    Vida_Mathias = 10
                    menu_return = 0
                    break
                Vida_Mathias = s_fase[2]
                buff_speed = s_fase[3]
    if pontos >= 50 and pontos < 80:
        som.stop()
        for pontos in (50, 60, 70):
            t_fase = castelo(pontos, Vida_Mathias, buff_damage, buff_speed, buff_armor, nome)
            pontos = t_fase[0]
            Vida_Mathias = t_fase[1]
            if pontos == -1:
                pontos = 0
                Vida_Mathias = 10
                menu_return = 0
                break

    if pontos >= 80:
        ff1 = fase_final(pontos, Vida_Mathias, buff_damage, buff_speed, buff_armor, nome)
        if ff1 == 1:
            k = animacao_vit()
            if k:
                in_game = False

        if not k:
            pontos = 0
            buff_damage = False
            buff_speed = False
            buff_armor = False

    if menu_return == -2:
        in_game = False


