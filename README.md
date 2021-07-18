# sendemail ![img](https://img.shields.io/badge/status-In%20development-brightgreen)

This project aims to create a specific email for each specific problem, error or other stuff, starting from a general template and adapted using Python Jinja2

### Description

This app takes arguments:
- `-f` or `--power-failure` to send an email when the power went out
- `-r` or `--power-restore` to send an email on power return
- `-k` or `--power-kill` to send an email when the UPS running out and the server will be stoped
- `-T` or `--test` to set debugging mode

In debugging mode the server sends email using the configuration under `[TEST]` section.

In the `config.ini` there are all the settings needed to make the app work properly.

In the `[SMTP]` section there are all the settings to connect the app to the smtp server. In the `[POWER]` section there are all the necessary setting in case of  power failure
