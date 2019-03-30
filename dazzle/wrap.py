import colorama.ansi

from dazzle.dazzle import t


def code_to_chars(code: int) -> t:
    return t(colorama.ansi.code_to_chars(code))


class Dazzler(colorama.ansi.AnsiCodes):

    def __init__(self):
        super().__init__()
        for name, value in self.__dict__.items():
            if not name.startswith('_'):
                setattr(self, name, t(value))


class DazzledFore(Dazzler, colorama.ansi.AnsiFore):
    pass


class DazzledBack(colorama.ansi.AnsiBack, Dazzler):
    pass


class DazzledStyle(colorama.ansi.AnsiStyle, Dazzler):
    pass


class DazzledCursor(colorama.ansi.AnsiCursor, Dazzler):

    def UP(self, n: int = 1):
        return t(super().UP(n))

    def DOWN(self, n: int = 1):
        return t(super().DOWN(n))

    def FORWARD(self, n: int = 1):
        return t(super().FORWARD(n))

    def BACK(self, n: int = 1):
        return t(super().BACK(n))

    def POS(self, x: int = 1, y: int = 1):
        return t(super().POS(x, y))
