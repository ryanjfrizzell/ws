import io


class SearchStuff:
    def __init__(self, word_list, list_matrix):
        self.mrix = list_matrix
        try:
            self.wl = io.open(word_list, 'r')
            self.searchwords = self.wl.readlines()
        except Exception as e:
            raise("failed to open file %s" % e)

    def search_for_str(self, search_string, line):
        """
        to make this simple we'll assume we're searching the line
        ffzzcatzz
        :param search_string: the string to look for ex: cat in ffzzcatzz
        :param line: the line we're looking in ex: ffzzcatzz
        :return: boolean if search_string exists in line
        did some quick comparisons running time on regex vs
        string in line. Tests were done extremely simply
        (bash) time testscript.py
        testscript.py contained very simple examples
        """
        ln = line.lower().strip()
        st = search_string.lower().strip()
        if st in ln:
            return True

    def flatten_lst(self, lst):
        return ''.join(lst)

    def search_tdlr(self):
        """
        search top down left right, the most easy of the search options
        ran out of time to do this more correctly but we get results
        also need to turn these into more functional versions of themselves
        via map
        """
        self.found = []
        self.s = []
        for z in self.mrix:
            self.s.append(self.flatten_lst(z))

        for m in self.s:
            self.find_str_in_list(m, self.searchwords)

    def find_str_in_list(self, srch, sl):
        for z in sl:
            if self.search_for_str(z, srch):
                print("found %s in %s" % (z.strip(), srch))
            else:
                continue
