import os

from langcodes import Language
from font_collector import FactoryABCFont, Helpers, Font, Name, FontType

dir_path = os.path.dirname(os.path.realpath(__file__))


def test_variable_font_to_collection():
    font_path = os.path.join(os.path.dirname(dir_path), "fonts", "Asap-VariableFont_wdth,wght.ttf")
    font_index = 0
    save_path = os.path.join(dir_path, "Asap - Test.ttf")
    try:
        Helpers.variable_font_to_collection(font_path, font_index, save_path)
        generated_fonts = FactoryABCFont.from_font_path(save_path)
    except Exception:
        pass
    finally:
        # Always delete the generated font
        if os.path.isfile(save_path):
            os.remove(save_path)

    print(generated_fonts)

    expected_fonts = [
        Font(
            save_path,
            0,
            set([Name("Asap Thin", Language.get("en"))]),
            set([Name("Asap Thin", Language.get("en"))]),
            100,
            False,
            False,
            FontType.TRUETYPE
        ),
        Font(
            save_path,
            1,
            set([Name("Asap ExtraLight", Language.get("en"))]),
            set([Name("Asap ExtraLight", Language.get("en"))]),
            200,
            False,
            False,
            FontType.TRUETYPE
        ),
        Font(
            save_path,
            2,
            set([Name("Asap Light", Language.get("en"))]),
            set([Name("Asap Light", Language.get("en"))]),
            300,
            False,
            False,
            FontType.TRUETYPE
        ),
        Font(
            save_path,
            3,
            set([Name("Asap", Language.get("en"))]),
            set([Name("Asap Regular", Language.get("en"))]),
            400,
            False,
            False,
            FontType.TRUETYPE
        ),
        Font(
            save_path,
            4,
            set([Name("Asap Medium", Language.get("en"))]),
            set([Name("Asap Medium", Language.get("en"))]),
            500,
            False,
            True,
            FontType.TRUETYPE
        ),
        Font(
            save_path,
            5,
            set([Name("Asap SemiBold", Language.get("en"))]),
            set([Name("Asap SemiBold", Language.get("en"))]),
            600,
            False,
            True,
            FontType.TRUETYPE
        ),
        Font(
            save_path,
            6,
            set([Name("Asap", Language.get("en"))]),
            set([Name("Asap Bold", Language.get("en"))]),
            700,
            False,
            True,
            FontType.TRUETYPE
        ),
        Font(
            save_path,
            7,
            set([Name("Asap ExtraBold", Language.get("en"))]),
            set([Name("Asap ExtraBold", Language.get("en"))]),
            800,
            False,
            True,
            FontType.TRUETYPE
        ),
        Font(
            save_path,
            8,
            set([Name("Asap Black", Language.get("en"))]),
            set([Name("Asap Black", Language.get("en"))]),
            900,
            False,
            True,
            FontType.TRUETYPE
        )
    ]

    # The generated collection can be in any order. To test it, we need to try all the possible font_index
    for font in expected_fonts:
        font_found = False

        for i in range(len(expected_fonts)):
            font.font_index = i
            if font in generated_fonts:
                font_found = True
                break
        
        assert font_found