#!/usr/bin/env python3
# encoding=utf8
import sys


import os
import re
import time
from bs4 import BeautifulSoup, Tag, NavigableString
import requests
import argparse
from pprint import pprint
from colorama import Fore
from colorama import Style
from colorama import init
import time
import pickle
import subprocess
#from tui import *

session = False
debug = False
d = {'mon':[],'tue':[],'wed':[],'thu':[],'fri':[],'sat':[],'sun':[]}
onlinesbor = '-1'
oflinesbor = '-2'

def customizesimmilar(day):
  if debug:
      t = time.time()

  tmp_elem = ''
  for elem in range(len(d[day])):
    tmp_elem = d[day][elem]
    for i in range(elem,len(d[day])):
      if i == elem:
        continue
      if d[day][i] == tmp_elem:
        d[day][i] = d[day][i] + '!'
  if debug:
      print('customizesimmilar',float(time.time()-t))

def customizetimetabletomatchcurrentweek(mode, day):
  if debug:
    t1 = time.time()
  supported_days = ('mon','tue','wed','thu','fri','sat','sun','whole')
  firstp = -1
  secp = -1
  todel = []
  todel1 = []
  atleastonepair = False
  apdel = []
  modechar = ''
  if mode == 1:
    modechar = '▼'
  elif mode == 0:
    modechar = '▲'
  if day == 'whole':
    customizetimetabletomatchcurrentweek(mode,'mon')
    customizetimetabletomatchcurrentweek(mode,'tue')
    customizetimetabletomatchcurrentweek(mode,'wed')
    customizetimetabletomatchcurrentweek(mode,'thu')
    customizetimetabletomatchcurrentweek(mode,'fri')
    customizetimetabletomatchcurrentweek(mode,'sat')
    customizetimetabletomatchcurrentweek(mode,'sun')
    return
  global group
  #33 если день передали говяный - шлеп в пиздц
  if day not in supported_days:
    raise ValueError("invalid day:"+day)
    ### При выводе фильтровал ; а они были отдельным элементом и индексы сбвали - был костыль. Ниже блок их УДАЛЯЕТ а не просто маскирует
  customizesimmilar(day)
  for elem in d[day]:
    if ';' in elem or group in elem:
      apdel.append(d[day].index(elem))
  for i in range(len(apdel)):
    d[day].pop(apdel[i])
    for j in range(i,len(apdel)):
      apdel[j] = apdel[j]-1
  if mode == 2:
    return
  #ОСТАВИТЬ КРАСНУЮ(ВЕРХНЮЮ)
  for elem in d[day]:
    if modechar in elem:
      todel.append(d[day].index(elem))
  smth = []
  for elem in d[day]:
    if '5512' in elem:
      smth.append(d[day].index(elem))
  #print(smth,'smth')
  ### удаляем время пар когда нужно
  finaldell = []
  for i in range(len(todel)):
    if todel[i]+1 >= len(d[day]):
      break
    if 'пара ' in d[day][todel[i]-1] and 'пара ' in d[day][todel[i]+1]:
      finaldell.append(d[day].index(d[day][todel[i]-1]))

  finaldell.extend(todel)
  finaldell.extend(smth)
  finaldell.sort()
  #print(finaldell)
  for i in range(len(finaldell)):
    d[day].pop(finaldell[i])
    for j in range(i,len(finaldell)):
      finaldell[j] = finaldell[j]-1

  if 'пара ' in d[day][len(d[day])-1]:
    d[day].pop()
  if debug:
      print('customizesimmilartomatchcurrentweek',float(time.time()-t1))




def query_yes_no(question, default="no"):
    """Ask a yes/no question via raw_input() and return their answer.

    "question" is a string that is presented to the user.
    "default" is the presumed answer if the user just hits <Enter>.
        It must be "yes" (the default), "no" or None (meaning
        an answer is required of the user).

    The "answer" return value is True for "yes" or False for "no".
    """
    if debug:
      t2 = time.time()
    valid = {"yes": True, "y": True, "ye": True,
             "no": False, "n": False}
    if default is None:
        prompt = " [y/n] "
    elif default == "yes":
        prompt = " [Y/n] "
    elif default == "no":
        prompt = " [y/N] "
    else:
        raise ValueError("invalid default answer: '%s'" % default)

    while True:
        sys.stdout.write(question + prompt)
        choice = input().lower()
        if default is not None and choice == '':
            return valid[default]
        elif choice in valid:
            return valid[choice]
        else:
            sys.stdout.write("Please respond with 'yes' or 'no' "
                             "(or 'y' or 'n').\n")

    if debug:
        print('queryyesno',time.time()-t2)
def week(r):

  ithinkits_res = -1
  sp = BeautifulSoup(r,'html.parser')
  select = sp.select('em')
  #print(select)
  if select[0].text[0] == '▲':
    ithinkits_res = 1
  elif select[0].text[0] == '▼':
    ithinkits_res = 0
  else:
    ithinkits_res = -1
  if ns.offline:
    with open (os.path.expanduser('~/cached/'+group+'.pkl'),'rb') as pc:
        data = pickle.load(pc)
        t = time.time()
        kek = time.localtime(t)
        if (int(time.strftime('%W',kek)) - int(time.strftime('%W',data)))%2 == 0:
          return ithinkits_res

        else:
          if ithinkits_res == 1:
            return 0
          elif ithinkits_res == 0:
            return 1
          else:
            return -1

  else:
    return ithinkits_res

def prpr(d):
    for i in d:
      if i.count(';') != 0:
        if isinstance(i, NavigableString):
          continue
        i.remove(';')
      print(i,sep='\n')

def parsesession():
        if debug:
          t4 = time.time()
        r = requests.get("http://raspsess.guap.ru/").content.decode('utf-8')
        soup = BeautifulSoup(r, "html.parser")
        select = soup.find('option',text=group)
        group_prefix = select.attrs['value']

        r = requests.get("http://raspsess.guap.ru/?g="+group_prefix).content.decode('utf-8')
        if debug:
          print('site',time.time()-t4)
        Soup = BeautifulSoup(r, 'html.parser')
        days = list(Soup.select('h3'))

        day = []
        #print(day)
        for dy in days:
            day.append(dy.text)

        daysii = list(Soup.select('h4'))

        dayii = []
        #print(dayii)
        for dy in daysii:
            dayii.append(dy.text)

        pairs = Soup.select('.study')
        #pprint(pairs)
        #print('df')
        j = 0
        cheat = []
        for i in pairs:
            str = i
            #print(day[j])
           # print(str)

            j+=1
            #print(i.find('span').text)
            t = i.find('span').previous
            tt = t.previous
            ttt = tt.previous;

            cheat.append(Fore.BLUE+Style.BRIGHT+ttt.previous+Style.RESET_ALL)

            cheat.append(Fore.BLUE+Style.BRIGHT+t.previous+Style.RESET_ALL)
            cheat.append(Fore.GREEN+Style.BRIGHT+i.find('span').text)
            #cheat.append('\n')
        print('_________________')
        prpr(cheat)


def site():
    if session:
        parsesession()
        exit()
    if debug:
      t4 = time.time()
    r = requests.get("http://rasp.guap.ru/").content.decode('utf-8')
    soup = BeautifulSoup(r, "html.parser")
    select = soup.find('option',text=group)
    group_prefix = ""
    try:
      group_prefix = select.attrs['value']
    except:
      print("Looks like site (rasp.guap.ru) is temporary unavailable. Check later or use offline mod.")
      exit()
    r = requests.get("http://rasp.guap.ru/?g="+group_prefix).content.decode('utf-8')
    if debug:
      print('site',time.time()-t4)
    return r

def parseonline(r):

    # r = requests.get("http://rasp.guap.ru/").content.decode('utf-8')
    # soup = BeautifulSoup(r, "html.parser")
    # select = soup.find('option',text=group)
    # group_prefix = select.attrs['value']

    # r = requests.get("http://rasp.guap.ru/?g="+group_prefix).content.decode('utf-8')
    if debug:
      t5 = time.time()
    if week(r) == 0:
      if ns.nnac:
        #print(Fore.BLUE+Style.BRIGHT+'Сейчас нижняя неделя'+Style.RESET_ALL)
        pass
      else:
        #print(Fore.BLUE+Style.BRIGHT+'Сейчас ▼ неделя'+Style.RESET_ALL)
        pass
    elif week(r) == 1:
      if ns.nnac:
        #print((Fore.RED+Style.BRIGHT+'Сейчас верхняя неделя'+Style.RESET_ALL))
        pass
      else:
        #print(Fore.RED+Style.BRIGHT+'Сейчас ▲ неделя'+Style.RESET_ALL)
        pass
    else:
      print('У меня траблы с определением недели')
    Soup = BeautifulSoup(r, 'html.parser')
    days = list(Soup.select('h3'))

    day = []
    #print(day)
    for dy in days:
        day.append(dy.text)

    daysii = list(Soup.select('h4'))

    dayii = []
    #print(dayii)
    for dy in daysii:
        dayii.append(dy.text)

    lenofday = len(day)
    for i in day:
      if i == 'Вне сетки расписания':
        lenofday -= 1
    if lenofday == 1:
      #print("Учимся всего", lenofday, "день")
      pass
    elif lenofday >=2 and lenofday < 5:
      #print("Учимся всего", lenofday, "дня")
      pass
    elif lenofday >= 5:
      #print("Учимся всего", lenofday, "дней")
      pass



    pairs = Soup.select('.study')
    #pprint(pairs)
    #print('df')
    j = 0
    cheat = []
    for i in pairs:
        str = i
        #print(day[j])
       # print(str)

        j+=1
        #print(i.find('span').text)
        t = i.find('span').previous
        tt = t.previous
        ttt = tt.previous;
        cheat.append(ttt.previous)
        cheat.append(t.previous)
        cheat.append(i.find('span').text)
        #print('_________________')

    #print(len(pairs),len(day),len(dayii))

    global d
    pattern = re.compile('Понедельник')
    columns = Soup.find(text=pattern)
    if isinstance(columns, NavigableString):
        pass
    elif columns is None:
        pass
    else:
        columns = columns.next
    #columns = columns.next
   # print( columns.next.text)
   # print(columns)
    #mon pairs detecting
    # counter = 0
    # pat = re.compile(group)
    # while True:
    #     columns = columns.next
    #     if isinstance(columns, NavigableString):
    #         continue
    #     # if columns.name != 'span':
    #     #     print('!!!!!!!!!!!!!!!!!!!!!!!!!!!!!')
    #     #     continue
    #     text = columns.text
    #
    #     print(text,'ssds')
    #     if (text.find('Вторник') == -1):
    #
    #         d['mon'].append(columns.text)
    #
    #
    #     else:
    #         break
    #TODO РАССОРТИРОВАТЬ НОРМАЛЬНО
    cases = "Nothing"
    for i in cheat:
       if i == 'Понедельник':
           cases = 'mon'
       if i == 'Вторник':
           cases = 'tue'
       if i == 'Среда':
           cases = 'wed'
       if i == 'Четверг':
           cases = 'thu'
       if i == 'Пятница':
           cases = 'fri'
       if i == 'Суббота':
           cases = 'sat'
       if i == 'Вне сетки расписания':
           cases = 'sun'
       if i == 'Nothin':
           continue
       d[cases].append(i)


# Баг с подсчетом кол-ва дней. Если есть ВНЕ СЕТКИ РАСПИСАНИЯ ПУНКТ - СЧИТАЛ НЕ ВЕРНО СУКА (FIXED)
# Раскрашиваем аутпут
    for i in d['mon']:
      if len(i) == len(group):
        d['mon'].remove(i)
    for i in d['tue']:
      if i.find('Группа:') != -1:
        d['tue'].remove(i)
      if len(i) == len(group):
        d['tue'].remove(i)
    for i in d['wed']:
      if len(i) == len(group):
        if i != 'Среда':
          d['wed'].remove(i)
    for i in d['thu']:
      if len(i) == len(group):
        d['thu'].remove(i)
    for i in d['fri']:
      if i.find('Группа:') != -1:
        d['fri'].remove(i)
      if len(i) == len(group):
        d['fri'].remove(i)
    for i in d['sat']:
      if i.find('Группа:') != -1:
        d['sat'].remove(i)
      if len(i) == len(group):
        d['sat'].remove(i)


    if debug:
      print('1 parseonline',float(time.time()-t5))




    if debug:
      t6 = time.time()

    d['mon'].insert(0,Fore.BLUE+Style.BRIGHT+'Понедельник'+Style.RESET_ALL)
    if len(d['mon']) > 1:
      d['mon'].pop(1)
      for i in range(len(d['mon'])):
       if d['mon'][i].find('пара ') != -1:
         tmp = d['mon'][i]
         d['mon'][i] = ''+Fore.GREEN+Style.BRIGHT+tmp+Style.RESET_ALL
       if d['mon'][i].find('▼') != -1:
        tmp2 = d['mon'][i]
        d['mon'][i] = ''+Fore.BLUE+Style.BRIGHT+tmp2[0]+Style.RESET_ALL+tmp2[1:]
       if d['mon'][i].find('▲') != -1:
        tmp2 = d['mon'][i]
        d['mon'][i] = ''+Fore.RED+Style.BRIGHT+tmp2[0]+Style.RESET_ALL+tmp2[1:]
    else:
      d['mon'].append('Выходной')
    d['tue'].insert(0,Fore.BLUE+Style.BRIGHT+'Вторник'+Style.RESET_ALL)
    if len(d['tue']) > 1:
      d['tue'].pop(1)
      for i in range(len(d['tue'])):
        if d['tue'][i].find('пара ') != -1:
          tmp = d['tue'][i]
          d['tue'][i] = ''+Fore.GREEN+Style.BRIGHT+tmp+Style.RESET_ALL
        if d['tue'][i].find('▼') != -1:
         tmp2 = d['tue'][i]
         d['tue'][i] = ''+Fore.BLUE+Style.BRIGHT+tmp2[0]+Style.RESET_ALL+tmp2[1:]
        if d['tue'][i].find('▲') != -1:
         tmp2 = d['tue'][i]
         d['tue'][i] = ''+Fore.RED+Style.BRIGHT+tmp2[0]+Style.RESET_ALL+tmp2[1:]
    else:
      d['tue'].append('Выходной')
    d['wed'].insert(0,Fore.BLUE+Style.BRIGHT+'Среда'+Style.RESET_ALL)
    if len(d['wed']) > 1:
      d['wed'].pop(1)
      for i in range(len(d['wed'])):
        if d['wed'][i].find('пара ') != -1:
          tmp = d['wed'][i]
          d['wed'][i] = ''+Fore.GREEN+Style.BRIGHT+tmp+Style.RESET_ALL
        if d['wed'][i].find('▼') != -1:
         tmp2 = d['wed'][i]
         d['wed'][i] = ''+Fore.BLUE+Style.BRIGHT+tmp2[0]+Style.RESET_ALL+tmp2[1:]
        if d['wed'][i].find('▲') != -1:
         tmp2 = d['wed'][i]
         d['wed'][i] = ''+Fore.RED+Style.BRIGHT+tmp2[0]+Style.RESET_ALL+tmp2[1:]
    else:
      d['wed'].append('Выходной')
    d['thu'].insert(0,Fore.BLUE+Style.BRIGHT+'Четверг'+Style.RESET_ALL)
    if len(d['thu']) > 1:
      d['thu'].pop(1)
      for i in range(len(d['thu'])):
        if d['thu'][i].find('пара ') != -1:
          tmp = d['thu'][i]
          d['thu'][i] = ''+Fore.GREEN+Style.BRIGHT+tmp+Style.RESET_ALL
        if d['thu'][i].find('▼') != -1:
         tmp2 = d['thu'][i]
         d['thu'][i] = ''+Fore.BLUE+Style.BRIGHT+tmp2[0]+Style.RESET_ALL+tmp2[1:]
        if d['thu'][i].find('▲') != -1:
         tmp2 = d['thu'][i]
         d['thu'][i] = ''+Fore.RED+Style.BRIGHT+tmp2[0]+Style.RESET_ALL+tmp2[1:]
    else:
      d['thu'].append('Выходной')
    d['fri'].insert(0,Fore.BLUE+Style.BRIGHT+'Пятница'+Style.RESET_ALL)
    if len(d['fri']) > 1:
      d['fri'].pop(1)
      for i in range(len(d['fri'])):
        if d['fri'][i].find('пара ') != -1:
          tmp = d['fri'][i]
          d['fri'][i] = ''+Fore.GREEN+Style.BRIGHT+tmp+Style.RESET_ALL
        if d['fri'][i].find('▼') != -1:
         tmp2 = d['fri'][i]
         d['fri'][i] = ''+Fore.BLUE+Style.BRIGHT+tmp2[0]+Style.RESET_ALL+tmp2[1:]
        if d['fri'][i].find('▲') != -1:
         tmp2 = d['fri'][i]
         d['fri'][i] = ''+Fore.RED+Style.BRIGHT+tmp2[0]+Style.RESET_ALL+tmp2[1:]
    else:
      d['fri'].append('Выходной')
    d['sat'].insert(0,Fore.BLUE+Style.BRIGHT+'Суббота'+Style.RESET_ALL)
    if len(d['sat']) > 1:
      d['sat'].pop(1)
      for i in range(len(d['sat'])):
        if d['sat'][i].find('пара ') != -1:
          tmp = d['sat'][i]
          d['sat'][i] = ''+Fore.GREEN+Style.BRIGHT+tmp+Style.RESET_ALL
        if d['sat'][i].find('▼') != -1:
         tmp2 = d['sat'][i]
         d['sat'][i] = ''+Fore.BLUE+Style.BRIGHT+tmp2[0]+Style.RESET_ALL+tmp2[1:]
        if d['sat'][i].find('▲') != -1:
         tmp2 = d['sat'][i]
         d['sat'][i] = ''+Fore.RED+Style.BRIGHT+tmp2[0]+Style.RESET_ALL+tmp2[1:]
    else:
      d['sat'].append('Выходной')
    d['sun'].insert(0,Fore.BLUE+Style.BRIGHT+'Вне сетки расписания'+Style.RESET_ALL)
    if len(d['sun']) > 1:
      d['sun'].pop(1)
      for i in range(len(d['sun'])):
        if d['sun'][i].find('пара ') != -1:
          tmp = d['sun'][i]
          d['sun'][i] = ''+Fore.GREEN+Style.BRIGHT+tmp+Style.RESET_ALL
      d['sun'].pop(1)
    else:
      d['sun'].append('Радуйся если тут пусто')
    global onlinesbor
    onlinesbor = Soup.select('span')[0].text
    try:
      file = open(os.path.expanduser('~/cached/'+group),'r')
      rr = file.read()
      file.close()
      global oflinesbor
      spp = BeautifulSoup(rr,'html.parser')

      oflinesbor = spp.select('span')[0].text
    except IOError:
      print(Fore.RED+Style.BRIGHT+'No cached timetable exists! Try 2 reinstall using pip install -U or u just never cached this group\'s timetable before. If so, do it NOW!'+Style.RESET_ALL)
      oflinesbor = onlinesbor+'FAKE WRONG'



    if debug:
      print('2 parseonline massive',float(time.time()-t6))



### тут фильтранем неделю
    global change_week

    #print(change_week)
    if nweek != 'c':
        weekz = int(nweek)

    else:
        weekz = week(r)
    #print(weekz)
    if(ns.today):
      weekz = week(r)
      if kek == 7:
        if weekz == 1:
          weekz = 0
        elif weekz == 0:
          weekz = 1
    if change_week:
      if weekz == 1:
        weekz = 0
      elif weekz == 0:
        weekz = 1
    #print(weekz)
    customizetimetabletomatchcurrentweek(weekz,dz)
    if ns.nnac:
      for i in range(len(d['mon'])):
        d['mon'][i]=d['mon'][i].replace('▼','Нижняя')
        d['mon'][i]=d['mon'][i].replace('▲','Верхняя')
        #print (d['mon'][i])

    if dz == 'whole':
           customizesimmilar('mon')
           customizesimmilar('tue')
           customizesimmilar('wed')
           customizesimmilar('thu')
           customizesimmilar('fri')
           customizesimmilar('sat')
           customizesimmilar('sun')

           prpr(d['mon'])
           print('_________________')

           prpr(d['tue'])
           print('_________________')

           prpr(d['wed'])
           print('_________________')

           prpr(d['thu'])
           print('_________________')

           prpr(d['fri'])
           print('_________________')

           prpr(d['sat'])
           print('_________________')

           prpr(d['sun'])
    elif dz == 'mon':
           customizesimmilar('mon')
           prpr(d['mon'])
    elif dz == 'tue':
           customizesimmilar('tue')
           prpr(d['tue'])
    elif dz == 'wed':
           customizesimmilar('wed')
           prpr(d['wed'])
    elif dz == 'thu':
           customizesimmilar('thu')
           prpr(d['thu'])
    elif dz == 'fri':
           customizesimmilar('fri')
           prpr(d['fri'])
    elif dz == 'sat':
           customizesimmilar('sat')
           prpr(d['sat'])
    elif dz == 'sun':
           customizesimmilar('sun')
           prpr(d['sun'])

def parseofline():

  try:
    file = open(os.path.expanduser('~/cached/'+group),'r')
  except IOError:
    print('File doesnt exists! Try 2 running with --cache key or just ask for timetable once in --online mod')
    exit()
  r = file.read()
  file.close()
  parseonline(r);

def createParser():
  parser = argparse.ArgumentParser(description = 'SUAI Online/Offline timetable')
  return parser
def cachett():
  r = requests.get("http://rasp.guap.ru/").content.decode('utf-8')
  soup = BeautifulSoup(r, "html.parser")
  select = soup.find('option',text=group)
  group_prefix = select.attrs['value']
  r = requests.get("http://rasp.guap.ru/?g="+group_prefix).content.decode('utf-8')
  if not os.path.exists(os.path.expanduser('~/cached')):
    os.makedirs(os.path.expanduser('~/cached'))
  file = open(os.path.expanduser('~/cached/'+group),'w')
  file.write(r)
  file.close()
  tlol = time.time()
  lol = time.localtime(t)
  with open (os.path.expanduser('~/cached/'+group+'.pkl'),'wb') as f:
      pickle.dump(lol,f)

  print('Cached successful! \n File name - ',os.path.abspath(file.name))

def main():
    init()
    parser = createParser()
    grouparg = parser.add_mutually_exclusive_group()
    grouparg.add_argument('-o','--online',help=Fore.RED+Style.BRIGHT+'[REQUIRED] Online'+Style.RESET_ALL+' mod',action='store_true')
    grouparg.add_argument('-f','--offline',help=Fore.RED+Style.BRIGHT+'[REQUIRED] Offline'+Style.RESET_ALL+' mod',action='store_true')
    parser.add_argument('-c','--cache',help=Fore.RED+Style.BRIGHT+'[REQUIRED] Cache '+Style.RESET_ALL+'timetable',action='store_true')
    parser.add_argument('-t','--today',help=Fore.RED+Style.BRIGHT+'Today\'s'+Style.RESET_ALL+' timetable',action='store_true')
    parser.add_argument('-G','--gui',help='Run with GUI(ALPHA! Very unstable!)',action='store_true')
    parser.add_argument('-V','--version',help = 'prints version and exit',action='store_true')
    grouparg.add_argument('-ov','--onlineversion',help = 'prints version stored in online repository and exit',action='store_true')
    grouparg.add_argument('-v','--verbose',help = 'Verbose output. Debug info.',action='store_true')
    parser.add_argument('-g', '--group', default='5512', help= 'Your group number. DEFAULT = 5512')
    parser.add_argument('-d', '--dz', default='whole', help = 'Day of week. EX.'+Fore.RED+Style.BRIGHT+'TOMORROW(tom)'+Style.RESET_ALL+', MONDAY(mon), TUESDAY(tue), WEDNESDAY(wed) ans so on..')
    parser.add_argument('-w', '--week', default='2', help = 'Red, blue or whole week. EX. 0 = blue lower, 1 = red upper, 2 = whole c = current')
    parser.add_argument('-N','--nnac',help = 'removes non-ascii-characters',action='store_true')
    parser.add_argument('-s','--session',help = 'Session timetable. Works only like grasp -os(g)xxxx',action='store_true')
    grouparg.add_argument('-l','--local',help = 'Prints Local cache storage path and exit',action='store_true')
    global ns
    ns = parser.parse_args()
    global session
    global local
    local = ns.local
    session = ns.session
    global group
    global nweek
    global zavtra
    global dz
    global t
    global kek
    global debug
    global change_week
    vers = 5.8
    if ns.verbose:
      debug = True
    if(ns.version):
      print('Version:',vers)
      exit()
    # if os.path.exists(os.path.expanduser('~/cached/e.ini')):
    #     name = open(os.path.expanduser('~/cached/n.ini'),'r')
    #     #print('Welcome,',name.read())
    #     name.close()
    # else:
    #     name = input("Hi! Looks like u'r using SUAI Timetable the first time.\n Please tell me what's your name to make our communication better :)\n ---> ")
    #     email = input("Great! And your email to get in touch with with all updates)\n --->")
    #     namef = open(os.path.expanduser('~/cached/n.ini'),'w')
    #     namef.write(name)
    #     emailf = open(os.path.expanduser('~/cached/e.ini'),'w')
    #     emailf.write(email)
    #     namef.close()
    #     emailf.close()
    if(ns.onlineversion):
      req = requests.get('https://raw.githubusercontent.com/maxan98/grasp/master/setup.py').content.decode('utf-8')
      ver = float(req[784:787])
      print('Online version:',ver)
      exit()
    tuidate = ""
    group = ns.group
    dz = ns.dz
    nweek = ns.week
    zavtra = False
    t = time.time()
    kek = time.localtime(t).tm_wday
    diff = 1
    change_week = False
    tuu = False
    if ns.gui:
      tuu = True
      dz = 'tom'
      ns.dz = 'tom'
      try:
          tui = Tui()
          tui.run()
      except Exception as e:
          tuidate = e.args[0]
          ns.group = e.args[1]
          group = ns.group
          #print(tuidate)
          #print(ns.group)
          diff = time.strptime(tuidate,'%Y-%M-%d').tm_mday-time.localtime(t).tm_mday
          kek = time.strptime(tuidate,'%Y-%M-%d').tm_wday
          #print(diff)
          dz = 'tom'
          zavtra = True
          #print(int(time.strftime('%W',time.strptime(tuidate,'%Y-%M-%d'))),int(time.strftime('%W',time.localtime(t))),'time')
          if (int(time.strftime('%W',time.strptime(tuidate,'%Y-%M-%d')))%2 ==0):
            change_week = True


    if dz == 'tom':
      zavtra = True
      #kek+=diff
      if tuu:
        kek = kek-1
      else:
        kek+=1
      if kek<0:
        kek = 0
      ns.today = True
    if(ns.today):
      #print('kek',kek)
      #print(kek%7)

      if kek == 0:
        dz = 'mon'
      if kek == 1:
        dz = 'tue'
      if kek == 2:
        dz = 'wed'
      if kek == 3:
        dz = 'thu'
      if kek == 4:
        dz = 'fri'
      if kek == 5:
        dz = 'sat'
      if kek == 6:
        dz = 'sun'
      if kek == 7:
        dz = 'mon'




    if ns.cache:
      cachett()
    elif ns.online:
      parseonline(site())
      #print(onlinesbor)
      if onlinesbor != oflinesbor:
        if query_yes_no('Would you like to cache timetable for this group?'):
          print('Caching..')
          cachett()
      else:
        #print('Timetable is up to date')
        pass
        req = requests.get('https://raw.githubusercontent.com/maxan98/grasp/master/setup.py').content.decode('utf-8')
        ver = float(req[784:787])
        if vers < ver:
          # TRY CATCH На сабпроцы
          if query_yes_no('A new version of app is available. Update now?', default = 'no'):
            if subprocess.call(["pip3", "install", "-U","git+https://github.com/maxan98/grasp.git"]) != 0:
              if subprocess.call(["pip", "install", "-U","git+https://github.com/maxan98/grasp.git"]) != 0:
                print('Updated!')
            else:
              print('Updated!')
        else:
          #print('App is up to date.')
          pass


    elif ns.offline:


      parseofline()
    else:
      print(Fore.RED+"Wrong usage. Use '-h' for help."+Style.RESET_ALL)
if __name__ == '__main__':
  main()
