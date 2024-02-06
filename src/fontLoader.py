from PyQt5.QtGui import QFontDatabase, QFont

def load_custom_font(font_file):
    font_id = QFontDatabase.addApplicationFont(font_file)
    font_family = QFontDatabase.applicationFontFamilies(font_id)[0]
    custom_font = QFont(font_family)
    return custom_font