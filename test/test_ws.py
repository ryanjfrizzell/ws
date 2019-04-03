from ws.lmatrix import *
from ws.searchstuff import *
import pytest


def test_lmatrix_creates_string():
    a=LMatrix(15)
    assert a.gen_string().__len__()==15

def test_matching_grids():
    a=LMatrix(30)
    b=LMatrix(30)
    assert a.grid == a.grid
    assert a.grid != b.grid

def test_grid_dimensions():
    a = LMatrix(10)
    assert len(a.grid.splitlines()) == 10
    assert len(a.grid.splitlines()[0]) == 10

def test_matrix():
    a = LMatrix(10)
    assert a.mtrix[9][9]
    # should cause index error
    with pytest.raises(IndexError):
        assert a.mtrix[10][10]

def test_flatten_lst():
    a = LMatrix(11)
    s = SearchStuff('./words.txt', a.mtrix)
    assert s.flatten_lst(['a','b', 'z', 'q']) == 'abzq'
def test_search_for_str():
    a = LMatrix(11)
    s = SearchStuff('./words.txt', a.mtrix)
    assert s.search_for_str( 'catbird', 'asdfacaxcastcatbirdfccvzzziidddjj')

def test_search_stuff():
    a = LMatrix(11)
    s = SearchStuff('./words.txt', a.mtrix)
    s.search_tdlr()

