# 911_reminder

## Disclaimer
It's a joke americans, don't blow up my family tree please. Neither fly into it.

## What it is
This is a small discord bot that sends a daily message at 09:11 consisting of a cinematic gif of the twin towers. 
Note: my server uses another timezone, thats why the code says 08:11.

## How it works
* bot.py: This is where the magic happens. Once started, the script will run in an endless while-loop, checking the time each cycle and eventually sending the message.
* 911.gif: Not gonna explain that one you fool.
* 911_reminder.service: Is a systemd service that ultimately runs the bot.py script. This service is trimmed to work under ubuntu. Following commands allow you to start and stop it, as well as see its state:
  * systemctl start 911_reminder
  * systemctl status 911_reminder
  * systemctl stop 911_reminder

## Security
Get outta here, I know what i'm doing
