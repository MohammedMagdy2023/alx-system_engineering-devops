# FireWall

UFW cheat sheet
===

Usage
---
```
ufw [--dry-run] enable|disable|reload
ufw [--dry-run] default allow|deny|reject [incoming|outgoing]
ufw [--dry-run] logging on|off|LEVEL
    toggle logging. Logged packets use the LOG_KERN syslog facility. Systems configured for rsyslog
    support may also log to /var/log/ufw.log. Specifying a LEVEL turns logging on for the specified LEVEL.
    The default log level is 'low'.
ufw [--dry-run] reset
ufw [--dry-run] status [verbose|numbered]
ufw [--dry-run] show REPORT
ufw [--dry-run] [delete] [insert NUM] allow|deny|reject|limit [in|out] [log|log-all] PORT[/protocol]
ufw [--dry-run] [delete] [insert NUM] allow|deny|reject|limit [in|out on INTERFACE] [log|log-all]
    [proto protocol] [from ADDRESS [port PORT]] [to ADDRESS [port PORT]]
ufw [--dry-run] delete NUM
ufw [--dry-run] app list|info|default|update
```

Examples
---
- `ufw status verbose`
- `ufw app list`
- `ufw allow in on eth0 log from any to any app SSH-22022`
- `ufw [delete] allow in proto udp from 193.204.114.105 to 12.34.56.78 port 123`


Enable Packet Forwarding Open the UFW network variables file /etc/ufw/sysctl.conf with a text editor1. Uncomment net/ipv4/ip_forward=1. 
This can be done by running the following command:

`|   sudo nano /etc/ufw/sysctl.conf`

Then, uncomment net/ipv4/ip_forward=1.
Configure Port Forwarding on UFW You can configure UFW to forward traffic from an external port to an internal port.
To do this, edit the /etc/ufw/before.rules file1:

`|   sudo nano /etc/ufw/before.rules`

In the before.rules file, add a NAT table after the filter table:
```
*nat
:PREROUTING ACCEPT [0:0]
-A PREROUTING -p tcp --dport 80 -j REDIRECT --to-port 500
COMMIT
```

This NAT table will redirect incoming traffic from the external port (80) to the internal port (500)1. You can adjust the table to forward traffic from any other external port to any other internal port.
Allow Traffic Through the Internal Port Allow traffic through the internal port:

`|   sudo ufw allow 500/tcp`

Restart UFW Finally, restart UFW:

`|   sudo systemctl restart ufw`

Please replace 80 and 500 with your desired external and internal ports respectively. Always ensure to replace these values with your actual port numbers