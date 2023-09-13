from typing import Hashable
from font_collector import UsageData


def test__init__():
    fontname = "Test"
    weight = 700
    italic = False
    ass_style = AssStyle(fontname, weight, italic)

    assert ass_style.fontname == fontname
    assert ass_style.weight == weight
    assert ass_style.italic == italic


def test_ordered_lines_property():
    fontname = "Example"
    weight = 700
    italic = False
    ass_style = AssStyle(fontname, weight, italic)

    fontname = "@Test"
    ass_style.fontname = fontname
    assert ass_style.fontname == "Test"


def test__eq__():
    ass_style_1 = AssStyle(
        "Test", 
        700, 
        False
    )

    ass_style_2 = AssStyle(
        "test", # Different
        700,
        False
    )
    assert ass_style_1 == ass_style_2


    ass_style_3 = AssStyle(
        "Test", 
        800, # Different
        False
    )
    assert ass_style_1 != ass_style_3

    ass_style_4 = AssStyle(
        "Test", 
        700, 
        True # Different
    )

    assert ass_style_1 != ass_style_4


def test__repr__():
    characters_used = {"a", "b"}
    lines = {1, 2}
    ass_style = UsageData(characters_used, lines)

    assert repr(ass_style) == 'UsageData(Font name="Example", Weight="700", Italic="False")'
