from .lexerconstants import CHAR_MAP


class Debug(object):

    def __init__(self, string):
        self.translate_tuple = (
            (CHAR_MAP['space'], '.'),
            (CHAR_MAP['tab'], '_'),
            (CHAR_MAP['lf'], '|'),
        )
        self.string = self._translate(string)

    def __str__(self):
        return self.string

    def _translate(self, string):
        for i in self.translate_tuple:
            string = string.replace(i[0], i[1])
        return string
