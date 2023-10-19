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

    def type_converter(value, type: str):  # hex | argb
        if type == "hex":
            return str(hexFromArgb(value))
        if type == "argb":
            return str(value)

    def templater(colors):
        for i in config["templates"]:
            with open(str(Path.home()) + f"/.sofa/templates/{i['name']}", "rt") as a:
                with open(str(Path.home()) + i["path"], "wt") as b:
                    for l in a:
                        b.write(
                            l.replace(
                                "{primary}",
                                type_converter(colors.get_primary(), i["type"]),
                            )
                            .replace(
                                "{onPrimary}",
                                type_converter(colors.get_onPrimary(), i["type"]),
                            )
                            .replace(
                                "{primaryContainer}",
                                type_converter(
                                    colors.get_primaryContainer(), i["type"]
                                ),
                            )
                            .replace(
                                "{onPrimaryContainer}",
                                type_converter(
                                    colors.get_onPrimaryContainer(), i["type"]
                                ),
                            )
                            .replace(
                                "{secondary}",
                                type_converter(colors.get_secondary(), i["type"]),
                            )
                            .replace(
                                "{onSecondary}",
                                type_converter(colors.get_onSecondary(), i["type"]),
                            )
                            .replace(
                                "{secondaryContainer}",
                                type_converter(
                                    colors.get_secondaryContainer(), i["type"]
                                ),
                            )
                            .replace(
                                "{onSecondaryContainer}",
                                type_converter(
                                    colors.get_onSecondaryContainer(), i["type"]
                                ),
                            )
                            .replace(
                                "{tertiary}",
                                type_converter(colors.get_tertiary(), i["type"]),
                            )
                            .replace(
                                "{onTertiary}",
                                type_converter(colors.get_onTertiary(), i["type"]),
                            )
                            .replace(
                                "{tertiaryContainer}",
                                type_converter(
                                    colors.get_tertiaryContainer(), i["type"]
                                ),
                            )
                            .replace(
                                "{onTertiaryContainer}",
                                type_converter(
                                    colors.get_onTertiaryContainer(), i["type"]
                                ),
                            )
                            .replace(
                                "{error}",
                                type_converter(colors.get_error(), i["type"]),
                            )
                            .replace(
                                "{onError}",
                                type_converter(colors.get_onError(), i["type"]),
                            )
                            .replace(
                                "{errorContainer}",
                                type_converter(colors.get_errorContainer(), i["type"]),
                            )
                            .replace(
                                "{onErrorContainer}",
                                type_converter(
                                    colors.get_onErrorContainer(), i["type"]
                                ),
                            )
                            .replace(
                                "{background}",
                                type_converter(colors.get_background(), i["type"]),
                            )
                            .replace(
                                "{onBackground}",
                                type_converter(colors.get_onBackground(), i["type"]),
                            )
                            .replace(
                                "{surface}",
                                type_converter(colors.get_surface(), i["type"]),
                            )
                            .replace(
                                "{onSurface}",
                                type_converter(colors.get_onSurface(), i["type"]),
                            )
                            .replace(
                                "{surfaceVariant}",
                                type_converter(colors.get_surfaceVariant(), i["type"]),
                            )
                            .replace(
                                "{onSurfaceVariant}",
                                type_converter(
                                    colors.get_onSurfaceVariant(), i["type"]
                                ),
                            )
                            .replace(
                                "{outline}",
                                type_converter(colors.get_outline(), i["type"]),
                            )
                            .replace(
                                "{shadow}",
                                type_converter(colors.get_shadow(), i["type"]),
                            )
                            .replace(
                                "{inverseSurface}",
                                type_converter(colors.get_inverseSurface(), i["type"]),
                            )
                            .replace(
                                "{inverseOnSurface}",
                                type_converter(
                                    colors.get_inverseOnSurface(), i["type"]
                                ),
                            )
                            .replace(
                                "{inversePrimary}",
                                type_converter(colors.get_inversePrimary(), i["type"]),
                            )
                        )

    templater(fetch_colors(config["mode"]))
