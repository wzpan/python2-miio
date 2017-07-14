MusicBoxApi
===============

Python2 library & console tool for miio. 

**Install**

.. code:: shell

    pip install python2-miio


**Usage**

detect miio components:

.. code:: shell

    miio2 discover


write your code to send messages to your miio components:

.. code:: python

    import miio

    host = '192.168.1.103'  # host
    token = 'xxxxxxx'       # token

    fan = miio.device(host, token)
    fan.send('set_power', ['on'])  # start a smart mi fan

