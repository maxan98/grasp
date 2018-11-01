## UPD.> iOS shortcut command integration.
## PISHI VK SKAZHU KAK 
![lt6kh7c7g3i](https://user-images.githubusercontent.com/24477803/47880421-4c071b80-de34-11e8-936d-07b365fb5a14.jpg)
![uzip7eydjfm](https://user-images.githubusercontent.com/24477803/47880417-47dafe00-de34-11e8-9143-78146aac5117.jpg)
***


НИКОГДА СЛЫШИШЬ НИКОГДА НЕ СМОТРИ КОД ЭТОГО ЧУДА, У ЭТОЙ КАКАШКИ КУЧА ФИЧ И ОНА ИСПОЛЬЗУЕТСЯ КАК В ВК БОТЕ ТАК И В ДИАЛОГАХ АЛИСЫ, шорткатах iOS И МНОГО ГДЕ ЕЩЕ.. И Я КАЖДЫЙ РАЗ СТРАДАЮ ВПИХИВАЯ ЭТО ТУДА. ОЧ ПОЛЕЗНАЯ ШЛЯПА, НО ЖУУУУУУУУУУУТКИЙ КОД, НЕ СМОТРЕТЬ!
# 
SUAI CLI TIMETABLE

A small CLI app written in Python3 for my own use and 4 educational purposes.
Grasp provides information about the schedule of classes in my university (SUAI). The information is parsed from the official site (rasp.guap.ru) and is provided in a convenient form, with all possible selections, filters and other, the parity of the week is also taken into account. For example - schedule for tomorrow, schedule for Tuesday next week and so on - is a correct request for grasp. A feature is the possibility of correct operation in offline. In offline mode, the current day of the week, the parity of the week and so on are correctly calculated.
Caching takes place either on a separate key or at the end of the request for a timetable on-line in order to remind the user to periodically re-cache the schedule


## Getting Started

Currently worling only under python 3.x. The only thing u need 2 run this util is Python! Just download it from python.org

### Installing

After installing python u re ready to install the app :)

**pip / Github (THE EASIEST WAY)**
```
pip install git+https://github.com/maxan98/grasp.git
or
pip3 install git+https://github.com/maxan98/grasp.git
```

or

```
git clone https://github.com/maxan98/grasp.git
python grasp/setup.py install
```


## Usage/help/screenshots/additional info

Auto upgrades when new version is available.
If u want 2 force-upgrade the app use
```
pip3 install -U git+https://github.com/maxan98/grasp.git
```

All info and help u can find just running with -h key.
Output of -h key:
![2018-03-07 14 57 08](https://user-images.githubusercontent.com/24477803/37091064-d99522f0-2217-11e8-97bb-e1efcaa7f266.png)



Supports offline as well as online mod.

2 use offline mod, u ned to cache timetable for your group first:

`grasp -c(--cache) -g(--group) xxxxx(5512 is default)`

or just check your Timetable once in online mod. After that u will be asked 2 cache your tt automatically:

`Would you like to cache timetable for this group? [y/N]`

Jyst type **YES**!

After that u can use offline mod just running with **-f** key

` grasp -f -g 8431К -d mon`

U can use variaty of different usefull keys.

Also, u r able 2 combine them like this:

` grasp -ftg 8431К` 

With command above u call 4 --offline --today and --group :) As simple as possible)

There r only 3 REQUIRED keys. Choose one of them or app wont run.
-o --online

-f --offline

-c --cache

All other keys can be omitted.

If omitted:

Default for group is 5512.
For day is WHOLE
For week is both

**!!!WARNING!!! Notice that if your group numbers contains letters - they r in cyrillic. After decoding utf-8 cyrillic letters and latin letters are not the same! For ex. '8431К'. 'K' must be entered in cyrillic**

Offline mod r very useful cuz SUAI adores shutting down their servers and don't turn the half-week

Im still working on some features and on prettyfying the output.

**Now it looks like this :)**

![2018-03-04 21 16 27](https://user-images.githubusercontent.com/24477803/36948864-e09ae29c-1ff1-11e8-8194-b5a18d942ae8.png)

**Or like this if u prefer TUI**

Tui mod is very useful for requesting exotic timetable such as next month second friday :)

Tui works like GUI, just navigate using mouse or arrows on your keyboard and hit ENTER to confirm.
![2018-04-08 1 15 48](https://user-images.githubusercontent.com/24477803/38460828-a47ba85c-3aca-11e8-8921-bae3822fbd10.png)

###### PREVIOUS VERSIONs SCREENSHOTS

![2018-03-04 1 04 46](https://user-images.githubusercontent.com/24477803/36939788-42c074f0-1f48-11e8-9a3f-fc0210a50cd0.png)
