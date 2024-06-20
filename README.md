# Wifi-Spoof
collecting information about the devices around you in a simple and straightforward way and in a very short time

# WiFi Network Scanner

This tool shows the MAC addresses, device names and distances from the access point of the devices on the WiFi network you are connected to.

## Requirements

- `scapy` library: `pip install scapy`
- A Linux-based system
- `iw` command: `sudo apt-get install iw`

## Usage

To run the Python script, enter the following commands in the terminal:


python3 wifi_spoof.py



This script basically obtains the MAC addresses and device names of the devices on the network. Additional work can be done to calculate the distance from the access point. Also, more detailed information can be collected using platform specific commands and libraries.

