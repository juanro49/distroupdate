#!/bin/sh
ln -s /usr/share/distroupdate/automation/99-distroupdate-temporary.pkla /etc/polkit-1/localauthority/90-mandatory.d/99-distroupdate-temporary.pkla
echo "\n-- Automatic Removal $(date):\n" >> /var/log/distroupdate.log
systemd-inhibit --why="Performing autoremoval" --who="Update Manager" --what=shutdown --mode=block /usr/bin/apt-get autoremove --purge -y >> /var/log/distroupdate.log 2>&1
rm -f /etc/polkit-1/localauthority/90-mandatory.d/99-distroupdate-temporary.pkla
