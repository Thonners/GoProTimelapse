# GoProTimelapse
Set of scripts to enable taking periodic photos on a GoPro  
Python script handles interaction with the camera, bash controls the networking, and assumes netctl is managing the connections.
They were written on a PC running Arch Linux, but should work on Raspberry Pi too.

## Prerequisites
[goprocam](https://github.com/KonradIT/gopro-py-api)

## Installation
1. Ensure goprocam is installed as per the prerequisites
1. Create a netctl profile called 'gopro' that can connect to the camera's wifi
1. Edit the wifictl script to give the appropriate name for your 'default' wifi connection (replace 'lodge-2' in these scripts)
1. Copy the .service and .timer files from the systemd directory to /etc/systemd/system/.  
1. Edit the path to your python environment & the timelapse.py script in /etc/systemd/system/gopro-timelapse.service
1. Test the scripts work:  
`$> sudo systemctl start gopro-timelapse.service`  
1. Start and enable the timer:  
`$> sudo systemctl enable --now gopro-timelapse.timer`  

## Configuration  
##### WiFi Profiles
These scripts assume netctl will be managing the network, and that the wifi profiles for the gopro and your normal connection are set in the wifictl script. Change them as necessary.  
To generate a netctl profile for the gopro, (install if reqruied and) run `wifi-menu`. Select the appropriate wifi network and ensure it's named `gopro`.  
To get your current network profile (if you're using netctl), run `netctl list`. The profile with the * is the currently active profile.
##### Photo Interval
The length of time between photos is set in the gopro-timelapse.timer file, in the `OnUnitActiveSec=1h` line. Change `1h` to the desired period between photos. It may be necessary to call `sudo systemctl daemon-reload` before restarting the timer `sudo systemctl restart gopro-timelapse.timer`.

## Manual Usage
To take a picture manually, at custom intervals, simply call  
`$> python timelapse.py`
