from ansi_color_codes import Color

#function for color string
def color_string(string: str, color: str) -> str:
    return f"{color}{string}{Color.END}"
#imported to main python file 
