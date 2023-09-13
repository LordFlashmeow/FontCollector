from fontTools.ttLib import TTFont, newTable, getTableModule
from fontTools.ttLib.tables.O_S_2f_2 import *
import os

from font_collector.font.font_parser import FontParser, PlatformID
from langcodes import Language
from typing import Hashable
from fontTools.ttLib.tables._c_m_a_p import CmapSubtable

import os
from langcodes import Language
import pytest
from font_collector import Name, InvalidVariableFontException
from font_collector.font.font_parser import FontParser, NameID
from fontTools.ttLib.tables._n_a_m_e import NameRecord
from fontTools.ttLib.ttFont import TTFont

dir_path = os.path.dirname(os.path.realpath(__file__))


def test_is_valid_variable_font():
    font_path = os.path.join(os.path.dirname(dir_path), "variable font tests", "Test #1", "Test #1.ttf")
    font = TTFont(font_path)
    assert FontParser.is_valid_variable_font(font) == False

    font_path = os.path.join(os.path.dirname(dir_path), "variable font tests", "Test #2", "Test #2.ttf")
    font = TTFont(font_path)
    assert FontParser.is_valid_variable_font(font) == True

    font_path = os.path.join(os.path.dirname(dir_path), "variable font tests", "Test #3", "Test #3.ttf")
    font = TTFont(font_path)
    assert FontParser.is_valid_variable_font(font) == False

    font_path = os.path.join(os.path.dirname(dir_path), "variable font tests", "Test #4", "Test #4.ttf")
    font = TTFont(font_path)
    assert FontParser.is_valid_variable_font(font) == True

    font_path = os.path.join(os.path.dirname(dir_path), "variable font tests", "Test #5", "Test #5.ttf")
    font = TTFont(font_path)
    assert FontParser.is_valid_variable_font(font) == True

    font_path = os.path.join(os.path.dirname(dir_path), "variable font tests", "Test #6", "Test #6.ttf")
    font = TTFont(font_path)
    assert FontParser.is_valid_variable_font(font) == True

    font_path = os.path.join(os.path.dirname(dir_path), "variable font tests", "Test #7", "Test #7.ttf")
    font = TTFont(font_path)
    assert FontParser.is_valid_variable_font(font) == True

    font_path = os.path.join(os.path.dirname(dir_path), "variable font tests", "Test #8", "Test #8.ttf")
    font = TTFont(font_path)
    assert FontParser.is_valid_variable_font(font) == True

    font_path = os.path.join(os.path.dirname(dir_path), "variable font tests", "Test #9", "Test #9.ttf")
    font = TTFont(font_path)
    assert FontParser.is_valid_variable_font(font) == True

    font_path = os.path.join(os.path.dirname(dir_path), "variable font tests", "Test #10", "Test #10.ttf")
    font = TTFont(font_path)
    # In reality, it is false since it contain an invalid axis_value_id, but this check is done later.
    assert FontParser.is_valid_variable_font(font) == True

    font_path = os.path.join(os.path.dirname(dir_path), "variable font tests", "Test #11", "Test #11.ttf")
    font = TTFont(font_path)
    assert FontParser.is_valid_variable_font(font) == True

    font_path = os.path.join(os.path.dirname(dir_path), "variable font tests", "Test #12", "Test #12.ttf")
    font = TTFont(font_path)
    with pytest.raises(InvalidVariableFontException) as exc_info:
        FontParser.is_valid_variable_font(font)
    assert str(exc_info.value) == "The font has a stat table, but it doesn't have any DesignAxisRecord"


def test_get_var_font_family_prefix():
    name_record_family = NameRecord()
    name_record_family.nameID = NameID.FAMILY_NAME
    name_record_family.string = b"example"
    name_record_family.platformID = 3
    name_record_family.platEncID = 0
    name_record_family.langID = 0x409

    name_record_typo = NameRecord()
    name_record_typo.nameID = NameID.TYPOGRAPHIC_FAMILY_NAME
    name_record_typo.string = b"example"
    name_record_typo.platformID = 3
    name_record_typo.platEncID = 0
    name_record_typo.langID = 0x409

    name_record_designer = NameRecord()
    name_record_designer.nameID = NameID.DESIGNER
    name_record_designer.string = b"example"
    name_record_designer.platformID = 3
    name_record_designer.platEncID = 0
    name_record_designer.langID = 0x409


    assert FontParser.get_var_font_family_prefix([name_record_family, name_record_typo], platform_id=3) == set([Name(name_record_typo.string.decode("utf_16_be", "ignore"), Language.get("en"))])
    assert FontParser.get_var_font_family_prefix([name_record_family, name_record_designer], platform_id=3) == set([Name(name_record_family.string.decode("utf_16_be", "ignore"), Language.get("en"))])
    assert FontParser.get_var_font_family_prefix([name_record_family, name_record_designer], platform_id=0) == set()
    assert FontParser.get_var_font_family_prefix([name_record_designer], platform_id=3) == set()

"""
def test_get_distance_between_axis_value_and_coordinates():
    assert False

def test_get_axis_value_from_coordinates():
    font = TTFont(os.path.join(dir_path, "variable font tests", "Test #1", "AdventPro - Original.ttf"))

    print(FontParser.get_axis_value_from_coordinates(font, font["fvar"].instances[0].coordinates))

    result = FontParser.get_axis_value_from_coordinates(font, font["fvar"].instances[0].coordinates)

    for axis_value in result:
        print(axis_value.Value)
        print(axis_value.AxisIndex)
        

    print(font["fvar"].instances[0].coordinates)

    assert False

def test_get_axis_value_table_property():
    #font_path = os.path.join(os.path.dirname(dir_path), "variable font tests", "Test #11", "Test #11.ttf")
    font_path = os.path.join(os.path.dirname(dir_path), "variable font tests", "Test #11", "AdventPro - Original.ttf")
    font = TTFont(font_path)

    
    print(FontParser.get_axis_value_table_property(font, font["STAT"].table.AxisValueArray.AxisValue))
    # Test font without ElidedFallbackNameID
    assert False
"""

def test_get_filtered_names():
    names_record = []

    name_record = NameRecord()
    name_record.nameID = 1
    name_record.string = b"test"
    name_record.platformID = 3
    name_record.platEncID = 2
    name_record.langID = 0
    names_record.append(name_record)

    expected_name = Name(name_record.string.decode("utf_16_be"), Language.get("und"))

    assert FontParser.get_filtered_names(names_record, platformID=0) == set()
    assert FontParser.get_filtered_names(names_record, platformID=3) == set([expected_name])
    assert FontParser.get_filtered_names(names_record, platEncID=0) == set()
    assert FontParser.get_filtered_names(names_record, platEncID=2) == set([expected_name])
    assert FontParser.get_filtered_names(names_record, nameID=0) == set()
    assert FontParser.get_filtered_names(names_record, nameID=1) == set([expected_name])
    assert FontParser.get_filtered_names(names_record, langID=1) == set()
    assert FontParser.get_filtered_names(names_record, langID=0) == set([expected_name])


    name_record = NameRecord()
    name_record.nameID = 2
    name_record.string = b"test"
    name_record.platformID = 1
    name_record.platEncID = 2
    name_record.langID = 2
    names_record.append(name_record)


def test_get_font_italic_bold_property_with_freetype():
    font_path = os.path.join(os.path.dirname(dir_path), "fonts", "font_cmap_encoding_2.ttf")
    assert (False, False, 400) == FontParser.get_font_italic_bold_property_with_freetype(font_path, 0)

    # Invalid font_path
    with pytest.raises(FileNotFoundError) as exc_info:
        FontParser.get_font_italic_bold_property_with_freetype("example", 0)
    assert str(exc_info.typename) == "FileNotFoundError"


def test_get_font_italic_bold_property_microsoft_platform():
    # Test font with invalid os/2 table
    invalid_0s2_table_font_path = os.path.join(os.path.dirname(dir_path), "fonts", "font_with_invalid_os2_table.ttf")
    invalid_0s2_table_font = TTFont(invalid_0s2_table_font_path)
    assert (False, False, 400) == FontParser.get_font_italic_bold_property_microsoft_platform(invalid_0s2_table_font, invalid_0s2_table_font_path, 0)

    font = TTFont()
    font["OS/2"] = os2 = newTable("OS/2")

    os2.fsSelection = 0b000001
    os2.usWeightClass = 500
    assert (True, False, 500) == FontParser.get_font_italic_bold_property_microsoft_platform(font, "example", 0)

    os2.fsSelection = 0b100001
    os2.usWeightClass = 400
    assert (True, True, 400) == FontParser.get_font_italic_bold_property_microsoft_platform(font, "example", 0)


def test_get_font_italic_bold_property_mac_platform():
    font = TTFont()
    # Test font without head table. It need to fallback to freetype.
    invalid_0s2_table_font_path = os.path.join(os.path.dirname(dir_path), "fonts", "font_with_invalid_os2_table.ttf")
    assert (False, False, 400) == FontParser.get_font_italic_bold_property_mac_platform(font, invalid_0s2_table_font_path, 0)

    font["head"] = head = newTable("head")

    head.macStyle = 0b01
    assert (False, True, 800) == FontParser.get_font_italic_bold_property_mac_platform(font, "example", 0)

    head.macStyle = 0b10
    assert (True, False, 400) == FontParser.get_font_italic_bold_property_mac_platform(font, "example", 0)


def test_get_supported_cmaps():
    font_path = os.path.join(os.path.dirname(dir_path), "fonts", "font_mac.ttf")
    font = TTFont(font_path)

    cmaps = FontParser.get_supported_cmaps(font["cmap"].tables)

    assert len(cmaps) == 1
    assert cmaps[0].platformID == PlatformID.MACINTOSH and cmaps[0].platEncID == 0
    

def test_get_cmap_encoding():
    # It could be any format
    cmap_format = 0
    cmap = CmapSubtable.newSubtable(cmap_format)

    # Non-supported platform
    cmap.platformID = PlatformID.UNICODE
    assert FontParser.get_cmap_encoding(cmap) == None

    cmap.platformID = PlatformID.MICROSOFT
    cmap.platEncID = 0
    assert FontParser.get_cmap_encoding(cmap) == "utf_16_be"

    cmap.platformID = PlatformID.MICROSOFT
    cmap.platEncID = 1
    assert FontParser.get_cmap_encoding(cmap) == "utf_16_be"

    cmap.platformID = PlatformID.MICROSOFT
    cmap.platEncID = 2
    assert FontParser.get_cmap_encoding(cmap) == "cp932"

    cmap.platformID = PlatformID.MICROSOFT
    cmap.platEncID = 3
    assert FontParser.get_cmap_encoding(cmap) == "cp936"

    cmap.platformID = PlatformID.MICROSOFT
    cmap.platEncID = 4
    assert FontParser.get_cmap_encoding(cmap) == "cp950"

    cmap.platformID = PlatformID.MICROSOFT
    cmap.platEncID = 5
    assert FontParser.get_cmap_encoding(cmap) == "cp949"

    cmap.platformID = PlatformID.MICROSOFT
    cmap.platEncID = 6
    assert FontParser.get_cmap_encoding(cmap) == "cp1361"

    cmap.platformID = PlatformID.MICROSOFT
    cmap.platEncID = 10
    assert FontParser.get_cmap_encoding(cmap) == "utf_16_be"

    cmap.platformID = PlatformID.MACINTOSH
    cmap.platEncID = 0
    assert FontParser.get_cmap_encoding(cmap) == "mac_roman"

    # Non-supported platEncID
    cmap.platformID = PlatformID.MACINTOSH
    cmap.platEncID = 1
    assert FontParser.get_cmap_encoding(cmap) == None