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
  "wallpath": "Pictures",
  "templates": [
    { 
      "name": "example", 
      "path": "/.config/example/example.conf", 
      "type": "hex" 
      }
      ]
}
```

### mode

> Light or dark, the choice is yours

### wallpath

> Define where `sofa` fetches wallpapers from. (Note: must be accessible via `$HOME`)

### templates

> Color templates for anything.

```json
{ "name": "example", "path": "/.config/example/example.conf", "type": "hex" }
```

##### name

> Name of the template in `.sofa/templates`. (Note: must be without file extension)

##### path

> Path where the generated template gets saved to. (Note: must include file name and extension and be accessible via `$HOME`)

#### type

> Format in which color data is represented. (Note: can only be hex/argb)

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
yay -S python-material-color-utilities fzf hyprpaper jq python-pywal gradience pywalfox
```
