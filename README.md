<div align="center">

<img src="sofa.png" width="80">

# sofa

Soft Organic Furniture Arrangement

</div>

## Install

```
git clone https://github.com/SlumberDemon/sofa.git

sudo cp sofa/sofa /usr/local/bin

sudo chmod +x /usr/local/bin/sofa
```

> Verify that `sofa` is installed by running the following.

```
sofa sofa
```

> If successful, `sofa` should return 'sofa'.

## Setup

```
sofa setup
```

> Default setup contains examples

## Configuration

`.sofa/config.json`

```json
{
  "mode": "light",
  "wallpath": "Pictures",
  "templates": [
    {
      "name": "example",
      "path": ".config/example/example.conf",
      "type": "hex",
      "actions": ["app -q", "app"]
    }
  ]
}
```

### mode

> Light or dark, the choice is yours

### wallpath

> Define where `sofa` fetches wallpapers from. (Note: must be accessible via `$HOME`) Learn how to setup wallpapers [here](#wallpapers)

### templates

> Color templates for anything.

```json
{
  "name": "example",
  "path": ".config/example/example.conf",
  "type": "hex",
  "actions": ["app -q", "app"]
}
```

##### name

> Name of the template in `.sofa/templates`. (Note: must be without file extension)

##### path

> Path where the generated template gets saved to. (Note: must include file name and extension and be accessible via `$HOME`)

##### actions

> Execute commands after styles are generated (Note: commands are run in order of array)

#### type

> Format in which color data is represented. (Note: can only be hex/argb)

| Type                 | Format                 |
| -------------------- | ---------------------- |
| hex                  | #ffffff                | 
| argb                 | 4286130513             | 
| argb                 | (0, 0, 0)              | 

#### Usables

| Value                | Variable               |
| -------------------- | ---------------------- |
| primary              | {primary}              |
| onPrimary            | {onPrimary}            |
| primaryContainer     | {primaryContainer}     |
| onPrimaryContainer   | {onPrimaryContainer}   |
| secondary            | {secondary}            |
| onSecondary          | {onSecondary}          |
| secondaryContainer   | {secondaryContainer}   |
| onSecondaryContainer | {onSecondaryContainer} |
| tertiary             | {tertiary}             |
| onTertiary           | {onTertiary}           |
| tertiaryContainer    | {tertiaryContainer}    |
| onTertiaryContainer  | {onTertiaryContainer}  |
| error                | {error}                |
| onError              | {onError}              |
| errorContainer       | {errorContainer}       |
| onErrorContainer     | {onErrorContainer}     |
| background           | {background}           |
| onBackground         | {onBackground}         |
| surface              | {surface}              |
| onSurface            | {onSurface}            |
| surfaceVariant       | {surfaceVariant}       |
| onSurfaceVariant     | {onSurfaceVariant}     |
| outline              | {outline}              |
| shadow               | {shadow}               |
| inverseSurface       | {inverseSurface}       |
| inverseOnSurface     | {inverseOnSurface}     |
| inversePrimary       | {inversePrimary}       |

## Usage

```
sofa --help
```

## Dependencies

### linux

> Install with [`yay`](https://github.com/Jguer/yay)

```
yay -S python-material-color-utilities fzf swww jq python-pywal gradience pywalfox hyprpaper
```

> Extra pywal theming for [`Vscode`](https://marketplace.visualstudio.com/items?itemName=dlasagno.wal-theme), [`Firefox`](https://addons.mozilla.org/en-US/firefox/addon/pywalfox/), [`Rofi`](https://github.com/dylanaraps/pywal/wiki/Customization#rofi)

## Thank you

- [End_4's config](https://github.com/end-4/dots-hyprland), for inspirations ~~and code snippets~~
- [Lemon](https://github.com/lemonyte/), for improving the python code

