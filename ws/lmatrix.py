import random
import string


class LMatrix:

    def __init__(self, len):
        """
        :param len: lenth of the matrix/string list we're making

        summary: we take in a length and produce a string of lenXlen
        we also return this string as a 2D Array,
        which is more useful for doing advanced searching
        EX: diagonal matching will require some advanced search
        that will require us to have the ability to move in
        multiple directions through the array
        """
        self.len = int(len)
        self.g = self.make_grid()
        self.matrix = self.make_matrix()

    @property
    def mtrix(self):
        """ so we can get the 2D matrix easily """
        return self.matrix

    @property
    def grid(self):
        """ so we can get the string out easily """
        return self.g

    def gen_string(self):
        """ create a lowercase string of len """
        return ''.join([random.choice(string.ascii_lowercase)
                        for _ in range(self.len)])

    def make_grid(self):
        """ create our grid with a range of len"""
        grid = ''
        for x in range(self.len):
            grid += self.gen_string() + "\n"
        return grid

    def make_matrix(self):
        """ converts our grid into a 2D array """
        m = []
        for l in self.g.splitlines():
            m.append(list(l))
        return m
