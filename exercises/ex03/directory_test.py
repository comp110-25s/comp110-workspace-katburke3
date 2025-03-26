"""a place for unit tests"""

__author__: str = "730558066"

from exercises.ex03.dictionary import invert
import pytest
from exercises.ex03.dictionary import count
from exercises.ex03.dictionary import favorite_color
from exercises.ex03.dictionary import bin_len


def test_invert_1() -> None:
    """test the invert function with use case 1"""
    assert invert({"a": "b", "c": "d"}) == {"b": "a", "d": "c"}


def test_invert_2() -> None:
    """test the invert function with use case 2"""
    assert invert({"apple": "cat"}) == {"cat": "apple"}


def test_invert_3() -> None:
    """test the invert function with the edge case"""
    assert invert({}) == {}


with pytest.raises(KeyError):
    my_dictionary = {"kris": "jordan", "michael": "jordan"}
    invert(my_dictionary)


def test_count_1() -> None:
    """edge case test for count function"""
    assert count([]) == {}


def test_count_2() -> None:
    """Use case test 1 for count function"""
    assert count(["hi", "hello", "hi"]) == {"hi": 2, "hello": 1}


def test_count_3() -> None:
    """use case test 2 for count funciton"""
    assert count(["dog"]) == {"dog": 1}


def test_fav_col_1() -> None:
    """use case test 1 for fav function"""
    assert favorite_color({"K": "blue", "G": "green", "Z": "blue"}) == "2"


def test_fav_col_2() -> None:
    """edge case test for fav function"""
    assert favorite_color({}) == "0"


def test_fav_col_3() -> None:
    """use case test 2 for fav funciton"""
    assert favorite_color({"Megan": "red"}) == "1"


def test_bin_len_1() -> None:
    """edge case test 1 for bin funciton"""
    assert bin_len([]) == {}


def test_bin_len_2() -> None:
    """use case test 1 for bin function"""
    assert bin_len(["hey", "hi", "sup"]) == {3: {"sup", "hey"}, 2: {"hi"}}


def test_bin_len_3() -> None:
    """use case test 2 for bin function"""
    assert bin_len(["", ""]) == {0: {""}}
