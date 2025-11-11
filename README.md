# ulauncher-screen-brightness

A Ulauncher extension to set the screen brightness of configured screens with ddcutil.

## To install the extension

- Open Ulauncher preferences
- Click "Add extension"
- Paste `https://github.com/tmerten/ulauncher-screen-brightness` as Extension URL
- Click Add

## Requirements

You need to have `ddcutil` installed.

- Ubuntu/Debian: `sudo apt-get install ddcutil`

## Configure the extension

- Open Ulauncher preferences
- Click "Ulauncher Screen Brightness"
  - Set the brightness keyword (for example you can change the keyword to `b` for faster access)
  - Enter the displays you want the extension to control as comma separated values

## Use the extension

- Open Ulauncher
  - enter `brightness` (or whatever keyword you configured above)
    - select a brightness from the list
  - OR enter `brightness <number>` and select the first item from the list to set to number
    - `number` needs to be between `1` and `100`

## Limitations

The extension assumes that you want to set the brightness of all the configured screens to the same value.
There is currently no intention to make this more flexible.
