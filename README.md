# grasp
SUAI CLI TIMETABLE
=====================

Use **util.py** to fast create symlinks and configure access rights.

**!!!WARNING!!! util.py is currently unavailable for all not posix os**

All info and help u can find just running with -h key.
Output of -h key:
![2018-03-02 16 14 50](https://user-images.githubusercontent.com/24477803/36900662-414bd6a0-1e35-11e8-98d9-cc57884a808c.png)



Supports offline as well as online mod.

2 use offline mod, u ned to cache timetable for your group first:

` grasp -c(--cache) -g(--group) xxxxx(5512 is default)`

After that u can use offline mod just running with **-f** key

` grasp -f -g 8431К -d mon`

**!!!WARNING!!! Notice that if your group numbers contains letters - they r in cyrillic. After decoding utf-8 cyrillic letters and latin letters are not the same! For ex. '8431К'. 'K' must be entered in cyrillic**

Offline mod r very useful cuz SUAI adores shutting down their servers and don't turn the half-week

Im still working on some features and on prettyfying the output.

Now it looks like this :)

![2018-03-04 1 04 46](https://user-images.githubusercontent.com/24477803/36939788-42c074f0-1f48-11e8-9a3f-fc0210a50cd0.png)