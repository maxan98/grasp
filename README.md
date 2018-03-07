# grasp
SUAI CLI TIMETABLE
=====================

Use **util.py** to fast create symlinks and configure access rights.

**!!!WARNING!!! util.py is currently unavailable for all not posix os**

All info and help u can find just running with -h key.
Output of -h key:
![2018-03-07 14 57 08](https://user-images.githubusercontent.com/24477803/37091064-d99522f0-2217-11e8-97bb-e1efcaa7f266.png)



Supports offline as well as online mod.

2 use offline mod, u ned to cache timetable for your group first:

` grasp -c(--cache) -g(--group) xxxxx(5512 is default)`

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

**!!!WARNING!!! Notice that if your group numbers contains letters - they r in cyrillic. After decoding utf-8 cyrillic letters and latin letters are not the same! For ex. '8431К'. 'K' must be entered in cyrillic**

Offline mod r very useful cuz SUAI adores shutting down their servers and don't turn the half-week

Im still working on some features and on prettyfying the output.

**Now it looks like this :)**

![2018-03-04 21 16 27](https://user-images.githubusercontent.com/24477803/36948864-e09ae29c-1ff1-11e8-8194-b5a18d942ae8.png)

###### PREVIOUS VERSIONs SCREENSHOTS

![2018-03-04 1 04 46](https://user-images.githubusercontent.com/24477803/36939788-42c074f0-1f48-11e8-9a3f-fc0210a50cd0.png)
