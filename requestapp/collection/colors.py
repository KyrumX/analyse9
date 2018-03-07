from requestapp.collection.static import LIGHT_COLORS


def get_matching_color_bg(textcolor):
    if textcolor in LIGHT_COLORS:
        return '#000000'
    return '#FFFFFF'

def get_matching_color_text(bgcolor):
    if bgcolor == '#FFFFFF':
        return '#000000'
    return '#FFFFFF'