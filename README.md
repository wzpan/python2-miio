# MusicBoxApi

[![Software License](https://img.shields.io/badge/license-MIT-brightgreen.svg)](LICENSE.txt)
[![platform](https://img.shields.io/badge/python-2.7-green.svg)]()

Python2 library & console tool for miio. 

## Install

``` sh
pip install python2-miio
```

## Usage

* detect miio components:

``` sh
miio discover
```

* write your code to send messages to your miio components.

``` py
import miio

host = '192.168.1.103'  # host
token = 'xxxxxxx'       # token

fan = miio.device(host, token)
fan.send('set_power', ['on'])  # start a smart mi fan
```
