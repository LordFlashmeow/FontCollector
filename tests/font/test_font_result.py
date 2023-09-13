import collections
import os
import pytest
import string
from font_collector import Font, FontResult, FontType, Name
from langcodes import Language
from typing import Hashable

dir_path = os.path.dirname(os.path.realpath(__file__))


def test__init__():
    font = Font(
        "example",
        0,
        {Name("family_names", Language.get("en"))},
        {Name("exact_names", Language.get("en"))},
        400,
        False,
        False,
        FontType.TRUETYPE
    )
    mismatch_bold = True
    mismatch_italic = False

    font_result = FontResult(font, mismatch_bold, mismatch_italic)

    assert font_result.font == font
    assert font_result.mismatch_bold == mismatch_bold
    assert font_result.mismatch_italic == mismatch_italic


def test__repr__():
    font = Font(
        "example",
        0,
        {Name("family_names", Language.get("en"))},
        {Name("exact_names", Language.get("en"))},
        400,
        False,
        False,
        FontType.TRUETYPE
    )
    mismatch_bold = True
    mismatch_italic = False

    font_result = FontResult(font, mismatch_bold, mismatch_italic)
    assert repr(font_result) == 'FontResult(Font="Font(Filename="example", Font index="0", Family_names="{Name(value="family_names", lang_code="en")}", Exact_names="{Name(value="exact_names", lang_code="en")}", Weight="400", Italic="False", Glyph emboldened="False", Font type="TRUETYPE")", Mismatch bold="True", Mismatch italic="False")'
