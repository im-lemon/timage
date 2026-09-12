from render_image import render

import sys
import os

if not len(sys.argv) == 2:
    raise ValueError(
        "timage: Pass in an image file."
    )

else:


    def cls():
        if os.name == 'nt':
            os.system('cls')
        else:
            os.system('clear')

    if sys.argv[1] == "--help" or sys.argv[1] == "-h":
        cls()
        ht = """
Timage - A chafa-like image-displayer written in python.
        
Timage is a chafa-like tool written in python, it uses code from my older project RenderTool (https://github.com/im-lemon/rendertool) alongside
a new system for detecting colours (AI-Assisted), the timage.ps1 shell script aliasses timage to itself upon first run, so you can do:
        
timage <img-file.jpg>

instead of:

./timage <img-file.jpg> in that shell session.

Additional info:

GIT: https://github.com/im-lemon/timage.git
ISSUES: https://github.com/im-lemon/timage/issues/
        
        """

        print(ht)
        exit(0)

    cls()

    render(
        sys.argv[1]
    )