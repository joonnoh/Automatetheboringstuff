#!/usr/bin/env python

# Python script used to SSH into Raspberry Pi server and check status of Pi-hole ad blocker

from paramiko import SSHClient

# Connect to Pi via SSH
yourIP = '192.168.4.40'  # Change this to your Pi's static IP address
name = 'pi'  # Change this to your Pi's username
client = SSHClient()
client.load_system_host_keys()
client.connect(yourIP, username=name)

# Run pihole status command and print output
print('Pi-hole Status:')
stdin, stdout, stderr = client.exec_command('pihole status')
for line in stdout:
    print(line.rstrip())

# In progress: Get Chronometer to exit, SIGINT and timeout doesn't seem to work
# Run pihole -c command and print output
#stdin, stdout, stderr = client.exec_command('pihole -c')
#for line in stdout:
#   print(line.rstrip())

# Exit
stdin.close()
stdout.close()
stderr.close()
client.close()