# test_with_pytest.py
import pytest
import DiceRoller

def roll20_passes():
    returned = DiceRoller.roll20()
    assert returned > 0 and returned < 21

def roll12_passes():
    returned = DiceRoller.roll12()
    assert returned > 0 and returned < 13

def roll10_passes():
    returned = DiceRoller.roll10()
    assert returned > 0 and returned < 11

def roll8_passes():
    returned = DiceRoller.roll8()
    assert returned > 0 and returned < 9

def roll6_passes():
    returned = DiceRoller.roll6()
    assert returned > 0 and returned < 7

def roll4_passes():
    returned = DiceRoller.roll4()
    assert returned > 0 and returned < 5


