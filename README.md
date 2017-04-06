# News Flash for Omega's OLED Expansion
Displays news headlines on the OLED Expansion for the Onion Omega2.

To install:

* `opkg update`
* `opkg install python-light python-urllib3 pyOledExp`
* Copy the two files into the same directory
* Add an API key from https://newsapi.org/ to `config.json`
* Run:

``` bash
python oledNewsFlash.py
```

Cloning the repo to your Omega also works instead of copying.
