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

## Setup

```
sofa setup
```

> Verify that `sofa` is installed by running the following.

```
sofa sofa
```

> If successful, `sofa` should return 'sofa'.

## Configuration

`.sofa/config.json`

```json
{
  "wallpath": "Pictures", // Path for wallpapers
  "templates": [{ "name": "example", "path": "~/.config/example/example.conf" }] // Templater
}
```

### wallpath

> Define where `sofa` fetches wallpapers from. (Note: must be accessible via `$HOME`)

### templates

> Color templates for anything.

```json
{ "name": "example", "path": "~/.config/example/example.conf" }
```

#### name

> Name of the template in `.sofa/templates`. (Note: must be without file extension)

#### path

> Path where the generated template gets saved to. (Note: must include file name and extension)

## Usage

```
sofa --help
```

## Dependencies

### linux

> Install with [`yay`](https://github.com/Jguer/yay)

```
yay -S python-material-color-utilities fzf hyprpaper jq
```
