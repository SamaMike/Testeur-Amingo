# -*- coding: utf-8 -*-
"""
Created on Tue Aug  6 07:39:51 2024

@author: mike
"""

import os
import random
import datetime
import requests
import py_compile
from bs4 import BeautifulSoup

from analyse import analyse

lst_memo = list()
lst_memo0 = list()
val0 = int
equart0 = int
equart1 = int
equart2 = int
diff0 = int
diff1 = int
diff2 = int



def aleatoire(a, b):
    return random.randint(a, b)


def aleatoire_loto(genre):
    while True:
        if genre is 'Blue':
            test = random.randint(1, 49)
            if str(test) == '0':
                return random.randint(1, 49)
            else:
                return test
        elif genre is 'Yellow':
            patient0 = random.randint(1, 10)
            if str(patient0) == '0':
                return random.randint(1, 10)
            else:
                return patient0

def game_loto():
    game_blue = set()
    game_star = set()
    while True:
        if len(game_blue) != 5:
            game_blue.add(aleatoire_loto('Blue'))
        if len(game_star) != 1:
            game_star.add(aleatoire_loto('Star'))
        if len(game_blue) + len(game_star) == 6:
            return list((str(game_blue), str(game_star)))

def verify_data(if__list):
    if__end_char = list()
    if__beg_char = list()
    if__back_list = list()
    if__top_list = list()
    if bool(if__list) is True and type(if__list) is list:
        if type(if__list) == list:
            pass
        if bool(if__end_char) is True:
            end_back = if__end_char.pop()
        if bool(if__back_list) is True:
            end_list = if__back_list.pop()
        if bool(if__beg_char) is True:
            begin = if__beg_char[0]
        if bool(if__top_list) is True and if__top_list == 'get':
            top_list = if__top_list.pop(0)


def listing_data_game():
    if True:
        data = open('data.txt', 'rt')
        file_data = data.readlines()
        hach_file = list()
        for line in file_data:
            if line.endswith('\n') is True:
                hach_file.append(line)
                data.close()


def search_game(rept, tirage_result) -> str:
    release = []
    with open('data.txt', 'a+') as f:
        ligne = rept + '\n'
        temoin = f.readlines()
        list_temoin = ''
        for n in temoin:
            if n == '\n':
                continue
            if n not in ['\n']:
                newText = str(str(n) + ':')
                list_temoin = list_temoin.join(newText)
                lst_memo.append(list_temoin)
        f.write(ligne)

        if len(temoin) != len(f.readlines()):
            release['data'] = 'True'
        else:
            print('Default to save.')
        f.close()
    # URL de la page des résultats Amigo
    url = "https://www.fdj.fr/jeux-de-tirage/amigo/resultats"
    if tirage_result is not None:
        def resultat_amingo_71(tirage_result) -> int:
            # Effectuer la requête HTTP
            response = requests.get(url)
            soup = BeautifulSoup(response.content, 'html.parser')

            # Extraire les numéros gagnants (exemple avec une expression XPath)
            numeros_gagnants = soup.select_one('id.draw-result-blue-balls-{}'.format(str(tirage_result))).text.split()
            return str(numeros_gagnants)

        rA = resultat_amingo_71(tirage_result)
        labdata = open('data_siteAmingo_result.txt', 'a+')
        labdata.write(rA + '\n')
        labdata.close()
        print('resultat_amingo_71 is save.')

def amingo():
    amiLst = set()
    dictList = 0
    while True:
        nm = aleatoire(1, 28)
        Nm: str = str(nm) + ' '
        amiLst.add(Nm)
        dictList += 1
        if len(amiLst) == 7:
            listgame = list()
            for n in amiLst:
                listgame.append(n)
            var_amingo = ''.join(listgame)
            amiLst.clear()
            return var_amingo
        else:
            continue


"""
    1: Faire une liste des premiers, un autre pour le second et ainsi de suite...
    2: Faire la moyenne de chaque listes...
    3: Faire une sequence pour avoir les equart (+ ou - du bien)...
    4: Creer l'algorythme pour la suite.
"""


def avanced_amingo(multiple):
    mult = int(multiple)
    for i in range(mult):
        new_game = amingo()
        if i % 2 == 1:
            lst_memo.append(new_game)
        if i % 2 == 0:
            lst_memo0.append(new_game)
        if  i == '{}'.format(multiple):
            results = Algo1_advanced_Amingo(lst_memo, lst_memo0)

def Algo1_advanced_Amingo(list1, list2):
    # Creation du dossier
    file_equart = open('file_equart.txt', 'rt+')
    list_zip =list((zip(list1, list2)))
    if len(list1) == 2:
        for x in list_zip:
            monk = analyse.x_comp_y(int(x[-1]), int(x[0]))
            var = str('{} ,{}: {}').format(str(x[0]), str(x[-1]),str(monk))
    if len(list1) >= 3:
        for x in list_zip:
            var0 = x[0]
            var1 = x[1]
            for p in [var0, var1]:
                if len(p) == 2:
                    comp = analyse.x_comp_y(int(var0), int(var1))
                    text = '{}, {}:{}'.format(str(var0), str(var1), str(comp))


def adminMenu():
    # URL de la page des résultats Amigo
    url = "https://www.fdj.fr/jeux-de-tirage/amigo/resultats"
    print('Inserez le numero du tirage du jour sans espace.\n: ')
    tirage_numbers = str(input())
    # Effectuer la requête HTTP
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.body')
    # Extraire les numéros gagnants (exemple avec une expression XPath)
    id_amingo = '//*[@id="draw-result-blue-balls-{}"]'.format(tirage_numbers)
    numeros_gagnants = soup.select_one(id_amingo).text.split()
    nb_gg = ''.join(numeros_gagnants)
    return nb_gg


def take_html_amingo():
    url = "https://www.fdj.fr/jeux-de-tirage/amigo/resultats"
    response = requests.get(url)
    return response.text


def take_id_html_amingo(section, div, id):
    pass


def save_numbers(lst):
    with open('data.txt', 'a+') as f:
        date = datetime.datetime.today().strftime('%d.%m.%Y')
        if type(f) != str:
            f.write(str(lst) + '\n')
            print('data save.<{}>'.format(date))
            f.close()
        else:
            f.write(lst)
            print('data save.<{}>'.format(date))
            f.close()


def return_last_numbers():
    with open('data.txt', 'r') as f:
        numbers = f.readlines()
        f.close()
        return numbers[-1]


def algoBetatest01():
    optimus = open('data.txt', 'r+')
    _object_games = optimus.readlines()
    varObject.append(_object_games)
    varAlgo = zip(varObject, amingo())
    yield varAlgo
    optimus.close()


def restart():
    os.system('cls')
    starter()


def starter():
    started = True
    hunter_char = True
    order_web = int(0)
    verify_order = dict(({'order': '{}'.format(str(order_web))}))
    while hunter_char:
        if order_web == 0:
            while started is True or started == 'stat_amingo':
                if started is True:
                    print('Tape\n'
                          '1: Get number Amingo\n'
                          '11 Get Aleatoire loto\n'
                          '2: Advanced amingo \n'
                          '22: advanced loto'
                          '3: Write a sequence number\n'
                          '4: Restart\n'
                          '5: Quit\n')
                    user = input()
                    if user == '1':
                        lst_amingo = amingo()
                        print('tirage {}: {}'.format('1', str(lst_amingo)))
                    elif user == '11':
                        pass
                    elif user == '2':
                        user_args = int(input('Combien de fois ? \n:'))
                        if user_args <= 250:
                            while user_args != 0:
                                am = amingo()
                                save_numbers(am)
                                user_args -= 1
                                if user_args == 0:
                                    text = return_last_numbers()
                                    print('last number: {}\nactual game: {}'.format(str(text), amingo()))
                                    restart()
                    elif user == '22':
                        pass
                    elif user == '3':
                        start01 = True
                        while start01 is True:
                            _user = input('sequences: ')
                            if _user != '0':
                                temoin = _user
                                if _user == "start_sequence":
                                    varset = _user.split('.')
                                    save_numbers(varset)
                                    print('ok ')
                                if _user == 'admin_menu':
                                    adminMenu()
                                if _user == '0':
                                    save_numbers(varset)
                                    restart()
                    elif user == '4':
                        start01 = False
                        if start01 is False:
                            import time
                            while True:
                                vartime = 10
                                for i in range(vartime):
                                    point3 = "..."
                                    point2 = ".."
                                    point1 = "."
                                    print('Restarting {}'.format(point1))
                                    os.system('cls')
                                    if i % 2 == 0:
                                        os.system('cls')
                                        print('Restarting {}'.format(point2))
                                    if i % 2 == 1:
                                        print('Restarting {}'.format(point3))
                                        os.system('cls')
                                    if i == vartime:
                                        restart()
                            started = True
                    elif user == '5':
                        print('Fin du simulateur')
                        py_compile.compile("terminal_main.py")
                        started = False
                    else:
                        print(
                            'Le choix: type {}:{} n\'exist pas.\n'
                            'Tape: 1 For get number Amingo\n'
                            '2 For advanced amingo \n'
                            '3 For write a sequence number\n'
                            '4 For restart a prog\n'
                            '5 For quit'.format(str(user), type(user)))
                        started = True
                if started == 'stat_amingo':
                    html_71 = take_html_amingo()
                    with open('html_data_71.txt', 'w+') as f:
                        f.write(html_71)
                        requete = adminMenu()
                        print(requete)
                        f.close()
        else:
            pass


if __name__ == '__main__':
    varObject = list()
    starter()
