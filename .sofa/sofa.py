import sys
import json
from pathlib import Path
from material_color_utilities_python import *

with open(str(Path.home()) + "/.sofa/config.json") as c:
    config = json.load(c)

if sys.argv[1] == "templater":

    def fetch_colors(type: str):  # light | dark
        img = Image.open(str(Path.home()) + f"/{config['wallpath']}/wallpaper")
        basewidth = 64
        wpercent = basewidth / float(img.size[0])
        hsize = int((float(img.size[1]) * float(wpercent)))
        img = img.resize((basewidth, hsize), Image.Resampling.LANCZOS)
        newtheme = themeFromImage(img)

        colorscheme = newtheme.get("schemes").get(type)

        return colorscheme

    def templater(colors):
        for i in config["templates"]:
            with open(str(Path.home()) + f"/.sofa/templates/{i['name']}", "rt") as a:
                with open(str(Path.home()) + i["path"], "wt") as b:
                    for l in a:
                        b.write(
                            l.replace(
                                "{primary}", str(hexFromArgb(colors.get_primary()))
                            )
                            .replace(
                                "{onPrimary}", str(hexFromArgb(colors.get_onPrimary()))
                            )
                            .replace(
                                "{primaryContainer}",
                                str(
                                    hexFromArgb(colors.get_primaryContainer()),
                                ),
                            )
                            .replace(
                                "{onPrimaryContainer}",
                                str(hexFromArgb(colors.get_onPrimaryContainer())),
                            )
                            .replace(
                                "{secondary}", str(hexFromArgb(colors.get_secondary()))
                            )
                            .replace(
                                "{onSecondary}",
                                str(hexFromArgb(colors.get_onSecondary())),
                            )
                            .replace(
                                "{secondaryContainer}",
                                str(hexFromArgb(colors.get_secondaryContainer())),
                            )
                            .replace(
                                "{onSecondaryContainer}",
                                str(hexFromArgb(colors.get_onSecondaryContainer())),
                            )
                            .replace(
                                "{tertiary}",
                                str(hexFromArgb(colors.get_tertiary())),
                            )
                            .replace(
                                "{onTertiary}",
                                str(hexFromArgb(colors.get_onTertiary())),
                            )
                            .replace(
                                "{tertiaryContainer}",
                                str(hexFromArgb(colors.get_tertiaryContainer())),
                            )
                            .replace(
                                "{onTertiaryContainer}",
                                str(hexFromArgb(colors.get_onTertiaryContainer())),
                            )
                            .replace(
                                "{error}",
                                str(hexFromArgb(colors.get_error())),
                            )
                            .replace(
                                "{onError}",
                                str(hexFromArgb(colors.get_onError())),
                            )
                            .replace(
                                "{errorContainer}",
                                str(hexFromArgb(colors.get_errorContainer())),
                            )
                            .replace(
                                "{onErrorContainer}",
                                str(hexFromArgb(colors.get_onErrorContainer())),
                            )
                            .replace(
                                "{background}",
                                str(hexFromArgb(colors.get_background())),
                            )
                            .replace(
                                "{onBackground}",
                                str(hexFromArgb(colors.get_onBackground())),
                            )
                            .replace(
                                "{surface}",
                                str(hexFromArgb(colors.get_surface())),
                            )
                            .replace(
                                "{onSurface}",
                                str(hexFromArgb(colors.get_onSurface())),
                            )
                            .replace(
                                "{surfaceVariant}",
                                str(hexFromArgb(colors.get_surfaceVariant())),
                            )
                            .replace(
                                "{onSurfaceVariant}",
                                str(hexFromArgb(colors.get_onSurfaceVariant())),
                            )
                            .replace(
                                "{outline}",
                                str(hexFromArgb(colors.get_outline())),
                            )
                            .replace(
                                "{shadow}",
                                str(hexFromArgb(colors.get_shadow())),
                            )
                            .replace(
                                "{inverseSurface}",
                                str(hexFromArgb(colors.get_inverseSurface())),
                            )
                            .replace(
                                "{inverseOnSurface}",
                                str(hexFromArgb(colors.get_inverseOnSurface())),
                            )
                            .replace(
                                "{inversePrimary}",
                                str(hexFromArgb(colors.get_inversePrimary())),
                            )
                        )

    templater(fetch_colors("light"))
