#!/usr/bin/python3

import os
import subprocess
import time

optionsfile = "/etc/distroupdate-automatic-upgrades.conf"
logfile = "/var/log/distroupdate.log"
log = open(logfile, "a")
log.write("\n-- Automatic Upgrade starting %s:\n" % time.strftime('%a %d %b %Y %H:%M:%S %Z'))
log.flush()

pkla_source = "/usr/share/distroupdate/automation/99-distroupdate-temporary.pkla"
pkla_target = "/etc/polkit-1/localauthority/90-mandatory.d/99-distroupdate-temporary.pkla"
try:
    # Put shutdown and reboot blocker into place
    os.symlink(pkla_source, pkla_target)
except:
    pass

try:
    # Parse options file
    arguments = []
    if os.path.isfile(optionsfile):
        with open(optionsfile) as options:
            for line in options:
                line = line.strip()
                if line and not line.startswith("#"):
                    arguments.append(line)

    # Run distroupdate-cli through systemd-inhibit
    cmd = ["/bin/systemd-inhibit", '--why="Performing automatic updates"',
           '--who="Update Manager"',  "--what=shutdown", "--mode=block",
           "/usr/bin/distroupdate-cli", "upgrade", "--refresh-cache", "--yes"]
    cmd.extend(arguments)
    subprocess.run(cmd, stdout=log, stderr=log)

except:
    import traceback
    log.write("Exception occurred:\n")
    log.write(traceback.format_exc())

try:
    # Remove shutdown and reboot blocker
    os.unlink(pkla_target)
except:
    pass

log.write("-- Automatic Upgrade completed\n")
log.close()
