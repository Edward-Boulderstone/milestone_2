import pytest

from milestone_2.Card import Card


def test_card_equality() -> None:
    """
    Tests that two cards with the same face value are equal
    """
    assert Card("Heart", 2) == Card("Heart", 2)
    assert Card("Spade", 1) == Card("Spade", 1)
    assert Card("Diamond", 13) == Card("Diamond", 13)
    assert Card("Club", 5) == Card("Club", 5)


def test_card_out_of_bounds_fails() -> None:
    """
    Tests that only cards with appropriate suit names and face values can be instantiated
    """
    with pytest.raises(AssertionError):
        Card("S", 2)

    with pytest.raises(AssertionError):
        Card("Hearts", 2)

    with pytest.raises(AssertionError):
        Card("Heart", -1)

    with pytest.raises(AssertionError):
        Card("Heart", 15)


def test_card_numerical_values() -> None:
    """
    Tests that cards blackjack values are correct
    """
    assert Card("Diamond", 1).get_value() == 11
    assert Card("Heart", 2).get_value() == 2
    assert Card("Heart", 3).get_value() == 3
    assert Card("Heart", 4).get_value() == 4
    assert Card("Heart", 5).get_value() == 5
    assert Card("Heart", 6).get_value() == 6
    assert Card("Heart", 7).get_value() == 7
    assert Card("Heart", 8).get_value() == 8
    assert Card("Heart", 9).get_value() == 9
    assert Card("Heart", 10).get_value() == 10
    assert Card("Heart", 11).get_value() == 10
    assert Card("Heart", 12).get_value() == 10
