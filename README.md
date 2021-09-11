# Micro Dot pHAT manager

Micro Dot pHAT manager is a framework for the Pimoroni Micro Dot pHAT.

It controls the Micro Dot pHAT using various *apps* which you can switch between with a CLI utility.

## Installation

First, clone the repository and change directory into it:

```shell
git clone git@github.com:tsbarnes/microdotphat.git ~/microdotphat
cd ~/microdotphat
```

Then, install the requirements:

```shell
pip3 install -r requirements.txt
```

Now you're ready to run it:

```shell
python3 app.py
```

If you want it to start automatically on boot:

```shell
sudo cp ~/microdotphat/microdotphat.service /etc/systemd/system/
sudo systemctl daemon-reload
sudo systemctl enable microdotphat
```

## Apps

The included *apps* are as follows:

* `graph` - displays a line graph of the system load
* `scrolling_text` - scrolls through a line of text
* `thermal` - reports the CPU temperature
* `webtext` - a receiver app for [webtext](https://github.com/tsbarnes/webtext)

## CLI

To use the CLI client, run `cli.py`. It takes a command line argument for previous, next, etc.

The current list of CLI commands is as follows:

* `python3 cli.py next` - change to next app
* `python3 cli.py previous` - change to previous app
