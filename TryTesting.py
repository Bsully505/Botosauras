# test_with_pytest.py
import pytest

def roll20_passes():
    assert DiceRoller.roll20() > 0 && DiceRoller.roll20() < 21

def roll12_passes():
    assert DiceRoller.roll12() > 0 && DiceRoller.roll20() < 13

def roll10_passes():
    assert DiceRoller.roll12() > 0 && DiceRoller.roll20() < 11

def roll8_passes():
    assert DiceRoller.roll12() > 0 && DiceRoller.roll20() < 9

def roll6_passes():
    assert DiceRoller.roll12() > 0 && DiceRoller.roll20() < 7

def roll4_passes():
    assert DiceRoller.roll12() > 0 && DiceRoller.roll20() < 5
