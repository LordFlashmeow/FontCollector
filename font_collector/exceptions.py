class NameNotFoundException(Exception):
    "Raised when the Naming Table doesn't contain an NameID"
    pass


class InvalidNameRecord(Exception):
    "Raised when a NameRecord isn't supported by GDI"
    pass


class InvalidFontException(Exception):
    "Raised when a font isn't valid"
    pass


class InvalidVariableFontException(Exception):
    "Raised when a variable font isn't valid"
    pass


class InvalidLanguageCode(ValueError):
    "Raised when a string does not conform to IETF BCP-47."
    pass


class OSNotSupported(Exception):
    "Raised when an OS isn't supported"
    pass