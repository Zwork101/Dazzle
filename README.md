# Dazzle ✨

*Make your output sparkle, without long repetitive code*


Who doesn't love color, I know I do. However I don't like any color libs, they can take up so much column space, and
can end up being repetitive, leading to functions such as
```py
def announcement(title: str, desc: str):
    print(colorlib.BLUE + "Announcement: " + title + colorlib.WHITE + "\n\n" + desc)
```
I actually have nothing against these functions, but they got me thinking. If I'm always going to end up making
functions, let's cut to the chase.
```py
from dazzle import Fore, INP

announce = Fore.BLUE + "Announcement: " + INP + Fore.WHITE + "\n\n" + INP
announce("Hello World", "Fizz Buzz")
```
Each of these methods would result in the same thing. Another issue with color libs, is that they can be a pain to
implement later down the road. Dazzle has you covered here too.
```py
with Back.BLUE + INP + " " + Fore.RED + " " + INP:
    print("John:", "Howdy Mary")
    print("Mary:", "Howdy John")
```
Dazzle will override the print function, so that it will add the colors provided in the with statement. Keep in mind
that any excess input will be ignored.

## Pitfalls

**Don't**
 * Start it with a normal string, use `t(<string>)` if you need to do that.
 * Use with statement with inconsistent print functions.
 * Wrap it with `()`. It should still work, but their's no need.
 * Use *repr* when requiring an input.
 * Be stupid.

 These were the docs, this is a very small and simple library.
 [here you'll find a list of colors](https://github.com/tartley/colorama/blob/master/colorama/ansi.py#L49) that are
 available. Dazzle covers Fore, Back, Style and Cursor, all as you'd expect. Thanks for using dazzle! ✨
