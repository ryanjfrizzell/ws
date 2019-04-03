import argparse


class GetArgs():

    def __init__(self):
        self.opts = argparse.ArgumentParser()
        self.opts.add_argument('-g', '--gridsize', default="15",
                               help="the grid size to generate")
        self.opts.add_argument('-w', '--wordlist', default="words.txt",
                               help="the location of your wordlist to search")
        self.args = self.opts.parse_args()

    @property
    def grid(self):
        return self.args.gridsize

    @property
    def words(self):
        return self.args.wordlist
