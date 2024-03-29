import json
import os
import sys
from pathlib import Path

from material_color_utilities_python import hexFromArgb, themeFromImage
from PIL import Image

config = json.loads(
    Path.home().joinpath(".sofa", "config.json").read_text(encoding="utf-8")
)
placeholders = (
    "primary",
    "onPrimary",
    "primaryContainer",
    "onPrimaryContainer",
    "secondary",
    "onSecondary",
    "secondaryContainer",
    "onSecondaryContainer",
    "tertiary",
    "onTertiary",
    "tertiaryContainer",
    "onTertiaryContainer",
    "error",
    "onError",
    "errorContainer",
    "onErrorContainer",
    "background",
    "onBackground",
    "surface",
    "onSurface",
    "surfaceVariant",
    "onSurfaceVariant",
    "outline",
    "shadow",
    "inverseSurface",
    "inverseOnSurface",
    "inversePrimary",
)
func_map = {
    "{" + placeholder + "}": f"get_{placeholder}" for placeholder in placeholders
}


def fetch_colors(type: str):  # light | dark
    img = Image.open(Path.home().joinpath(config["wallpath"], "wallpaper"))
    basewidth = 64
    wpercent = basewidth / float(img.size[0])
    hsize = int(float(img.size[1]) * float(wpercent))
    img = img.resize((basewidth, hsize), Image.Resampling.LANCZOS)
    newtheme = themeFromImage(img)
    return newtheme.get("schemes", {}).get(type)


def type_converter(value, type: str) -> str:  # hex | argb | rgb
    if type == "hex":
        return hexFromArgb(value)
    if type == "rgb":
        h = hexFromArgb(value).lstrip("#")
        return str(tuple(int(h[i : i + 2], 16) for i in (0, 2, 4)))
    if (
        type == "rgba"
    ):  # This can be used but is not recommended, requires you to add the finishing ) and extra value to define opacity if needed
        h = hexFromArgb(value).lstrip("#")
        return str(tuple(int(h[i : i + 2], 16) for i in (0, 2, 4))).removesuffix(")")

    return str(value)


def activation(actions) -> None:
    for a in actions:
        os.system(a)


def templater(colors) -> None:
    for template in config["templates"]:
        with (
            Path.home()
            .joinpath(".sofa", "templates", template["name"])
            .open(mode="r", encoding="utf-8") as a,
            Path.home()
            .joinpath(template["path"])
            .open(mode="w", encoding="utf-8") as b,
        ):
            for line in a:
                filled_line = line
                for placeholder, func in func_map.items():
                    filled_line = filled_line.replace(
                        placeholder,
                        type_converter(getattr(colors, func)(), template["type"]),
                    )
                b.write(filled_line)
        if "actions" in template:
            activation(template["actions"])


if __name__ == "__main__":
    if sys.argv[1] == "templater":
        mode = config["mode"]
        if len(sys.argv) > 2:
            mode = sys.argv[2]
    templater(fetch_colors(mode))
