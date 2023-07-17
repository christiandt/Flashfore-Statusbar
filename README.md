# FlashforgeStatusbar
Mac Status Bar app and CLI tool to show current progress from Flashforge 3D printers.

![alt tag](img/bar.png)

## Install
Download the latest version from [https://github.com/christiandt/FlashforgeStatusbar/releases](https://github.com/christiandt/FlashforgeStatusbar/releases). 

Unzip and move `FlashforgeStatusbar.app` to the Applications folder of your computer.

UDP broadcast will be used to find the IP address if the IP address is set to `auto`. If you do not have a static IP on your printer, reset the ip config variable to `auto` to do a new broadcast.

## Gotchas
Code is hacked together on vacation, expect stuff to break.

## UI Windows
![alt tag](img/preferences.png)
![alt tag](img/about.png)

## CLI version / Development Environment:
To download necessary requirements, run the make command:

    make

To run the meter, simply run the make run command:

    make run

You can provide an integer as argument to specify the update interval. Data will be fetched from the API of the router, so only local connections will be made, and thus not incur traffic on your mobile connection.

	make run update=10

This will set an update interval of 10 seconds. If the IP address is set to `auto`, UDP broadcast will be used to find the IP address of the printer. The default port is set to 8899 (ootb default), but you can override it using the environment variable `FLASHFORGE_PORT`. 

## Example Output:

[██████████████████████████████████████████----------------------------------------------------------] 42%
