JPG_TEXT = """
Your files are [JPG].
please select your convert type.
[A] Convert to .png
[B] Convert to .webp
"""
PNG_TEXT = """
Your files are [PNG].
please select your convert type.
[A] Convert to .jpg
[B] Convert to .webp
"""
WEBP_TEXT = """
Your files are [WEBP].
please select your convert type.
[A] Convert to .png
[B] Convert to .jpg
"""
JPG = "jpg"
PNG = "png"
WEBP = "webp"
RGB = "RGB"


PLEASE_WAIT = "Please wait 5 second ......"
ERROR_404_FILES = "[ERROR] FILES NOT FOUND...."
SOURCE = "[SOURCE] Please enter the path of files: "
DESTINATION = "[DESTINATION] Please enter a path save new files: "
CHOICE = "[x] select: "
ERROR_CORRECT_CHOICE = "Please choice correct item [A] or [B]."


def ERROR_CONVERT(file):
    print(F"[ERROR] Convert fail on file : {file}")
    
def SUCCESS_CONVERT(file):
    print(F"[OK] {file}")
