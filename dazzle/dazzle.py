import builtins

INP = object()  # object to recognize inputs


class t(str):

    def __add__(self, other: object):
        if isinstance(other, str) or other is INP:
            return ColorChain([self, other])
        elif isinstance(other, ColorChain):
            return ColorChain([self, *other])
        else:
            raise NotImplementedError


class ColorChain(tuple):
    _print = print

    def __enter__(self):
        builtins.print = self

    def __exit__(self, *stuff):
        builtins.print = self._print

    def __add__(self, other: object):
        if isinstance(other, str) or other is INP:
            return ColorChain([*self, other])
        elif isinstance(other, ColorChain):
            return ColorChain([*self, *other])
        else:
            raise NotImplementedError

    def __repr__(self):
        if not self.count(INP):
            return self(write=False)
        return repr(super())

    def __call__(self, *text, write: bool = True):
        requires = self.count(INP)
        if requires > len(text):
            raise ValueError("Not enough input for chain. Provided {}, requires {}".format(len(text), requires))

        sentence = ""
        text = list(text)
        for item in self:
            if item is INP:
                sentence += text.pop(0)
            else:
                sentence += item
        if write:
            self._print(sentence)
        else:
            return sentence
