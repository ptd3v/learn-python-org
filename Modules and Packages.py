#This is a summary of content and completed test exercise from learnpython.org

#Modules and Packages
#Game.py Example
import draw

def play_game():
    ...
def main():
    result = play_game()
    draw.draw_game(result)

#If this script is executed, then main() will be executed
if __name__ == '__main__':
    main()

#Draw.py
def draw_game():
    ...

def clear_screen(screen):
    ...

#Game.py, import the draw module
from draw import draw_game

def main():
    result = play_game()
    draw_game(result)

#Game.py, import the draw module
from draw import *

def main():
    result = play_game()
    draw_game(result)

#Game.py, import the draw module
if visual_mode:
    #In visual mode, we draw using graphics
    import draw_visual as draw
else:
    #In textual mode, we print out text
    import draw_textual as draw

def main():
    result = play_game()
    #This can either be visual or textual depending on visual_mode
    draw.draw_game(result)

#Draw.py

def draw_game():
    #When clearing the screen we can use the main screen object initialized in this module
    clear_screen(main_screen)
    ...

def clear_screen(screen):
    ...

class Screen():
    ...

#Initialize main_screen as a singleton
main_screen = Screen()

PYTHONPATH=/foo python game.py
sys.path.append("/foo")

#Import the library
import urllib

#Use it
urllib.urlopen(...)

#Full list of Python build in modules: https://docs.python.org/3/library/

>>> import urllib
>>> dir(urllib)
['ContentTooShortError', 'FancyURLopener', 'MAXFTPCACHE', 'URLopener', '__all__', '__builtins__',
'__doc__', '__file__', '__name__', '__package__', '__version__', '_ftperrors', '_get_proxies',
'_get_proxy_settings', '_have_ssl', '_hexdig', '_hextochr', '_hostprog', '_is_unicode', '_localhost',
'_noheaders', '_nportprog', '_passwdprog', '_portprog', '_queryprog', '_safe_map', '_safe_quoters',
'_tagprog', '_thishost', '_typeprog', '_urlopener', '_userprog', '_valueprog', 'addbase', 'addclosehook',
'addinfo', 'addinfourl', 'always_safe', 'basejoin', 'c', 'ftpcache', 'ftperrors', 'ftpwrapper', 'getproxies',
'getproxies_environment', 'getproxies_macosx_sysconf', 'i', 'localhost', 'main', 'noheaders', 'os',
'pathname2url', 'proxy_bypass', 'proxy_bypass_environment', 'proxy_bypass_macosx_sysconf', 'quote',
'quote_plus', 'reporthook', 'socket', 'splitattr', 'splithost', 'splitnport', 'splitpasswd', 'splitport',
'splitquery', 'splittag', 'splittype', 'splituser', 'splitvalue', 'ssl', 'string', 'sys', 'test', 'test1',
'thishost', 'time', 'toBytes', 'unquote', 'unquote_plus', 'unwrap', 'url2pathname', 'urlcleanup', 'urlencode',
'urlopen', 'urlretrieve']

help(urllib.urlopen)

#Various methods of Importing Modules
import foo.bar
from foo import bar

#Module and Packages Exercise Solution
find_members = []
for member in dir(re):
    if "find" in member:
        find_members.append(member)

print(sorted(find_members))