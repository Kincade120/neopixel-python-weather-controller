# neopixel-weather-controller-python

A simple python based neopixel controller for use on a RaspberryPi that uses data from https://openweathermap.org/api to display conditions. 

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install foobar.

```bash
pip install requriements.txt
```

## Usage

You will need an api token from https://openweathermap.org/api which you can enter in the config.json file. 

Clone to a suitable location on your RaspberryPi, install as above and then connect your neopixel. Im using a neopixel stick (https://www.adafruit.com/product/1426) but with some simple tweaks you can use a different neopixel.

The pin for the the DIN line on the neopixel is assigned to D18 but can be changed by editing the below line.
```python
pixels = neopixel.NeoPixel(board.D18, 8, brightness=0.5, auto_write=False, pixel_order=neopixel.GRB)
```

Once you have tailored your pixel count and colour combinations you can start the application

```bash
python main.py
```

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
[MIT](https://choosealicense.com/licenses/mit/)