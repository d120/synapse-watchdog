# HTTP Watchdog for synapse server
This little python script checks the availability of the synapse Matrix server every 30 seconds. If the server is not responsive, it will simply restart it with systemctl.

## Dependencies

* Python3
* Systemd
* sudo
* A systemd service-file for synapse called `synapse`

## Installation

* Create user synapse or change user in matrix-watchdog.service
* give this user sudo nopasswd privileges for `systemctl restart synapse`
* copy matrix-watchdog.service to `/etc/systemd/system`
* copy matrix-watchdog.py to `/opt`
* run `systemctl enable matrix-watchdogi.service` to autostart watchdog
* run `systemctl start matrix-watchdog.service`
