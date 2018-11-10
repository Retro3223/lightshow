import pytest
from unittest.mock import MagicMock, patch


@pytest.fixture(scope='function')
def get_platform_gpio():
    with patch('Adafruit_GPIO.get_platform_gpio', new=MagicMock()) as GPIO:
        yield GPIO

@pytest.fixture(scope='function')
def spidev():
    with patch('Adafruit_GPIO.SPI.SpiDev', new=MagicMock()) as spidev:
        yield spidev
