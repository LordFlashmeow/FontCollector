import os
from font_collector import FontType
from fontTools.ttLib.ttFont import TTFont

dir_path = os.path.dirname(os.path.realpath(__file__))


def test_from_font():
    font_path = os.path.join(os.path.dirname(dir_path), "fonts", "PENBOX.otf")
    opentype_font = TTFont(font_path)
    assert FontType.from_font(opentype_font) == FontType.OPENTYPE

    font_path = os.path.join(os.path.dirname(dir_path), "fonts", "font_mac.TTF")
    opentype_font = TTFont(font_path)
    assert FontType.from_font(opentype_font) == FontType.TRUETYPE
