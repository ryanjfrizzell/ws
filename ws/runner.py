from ws.cli import GetArgs
from ws.version import __version__ as ver
from ws.lmatrix import LMatrix
from ws.searchstuff import SearchStuff
import os


class RunIt:
    def __init__(self):
        """
        makes it easy to run from the command line everything
        is wrapped here
        """
        self.args = GetArgs()
        self.matrix = LMatrix(self.args.grid)
        self.wloc = os.path.abspath(self.args.words)

    def run(self):
        """
        :return: output findings
        """
        print("hello! you're running version %s of ws" % (ver))
        print("your word file is located at: %s" % self.wloc)
        print("your word grid is: \n%s" % self.matrix.grid)
        a = SearchStuff(self.wloc, self.matrix.mtrix)
        a.search_tdlr()
