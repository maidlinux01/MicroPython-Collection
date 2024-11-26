"""
A lightweight MicroPython implementation for interfacing with an AtlasScientific Ezo devices via I2C. 
Author: Tim Hanewich - https://github.com/maidlinux01
Version: 1.0
Get updates to this code file here: https://github.com/maidlinux01/MicroPython-Collection/blob/master/Ezo_i2c/Ezo_i2c.py

License: MIT License
Copyright 2024 Luis Enrique Morales Mendez
Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the “Software”), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:
The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.
THE SOFTWARE IS PROVIDED “AS IS”, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
"""

import machine

class Ezo_i2c:
    """Class for reading and send commands to an Enzo device via I2C."""
    
    def __init__(self, i2c:machine.I2C, address:int = 0x63):
        """
        Creates a new MPU6050 class for reading gyro rates and acceleration data.
        :param i2c: A setup I2C module of the machine module.
        :param address: The I2C address of the MPU-6050 you are using (0x68 is the default).
        """
        self.address = address
        self.i2c = i2c
        
    def send_cmd(self, cmd:str) -> None:
        """Send command to Ezo device"""
        self.i2c.writeto(self.address, bytearray(cmd,"ascii"))

    def recive_cmd(self) -> int:
        """Send command to Ezo device"""
        return self.i2c.readfrom(self.address, 1)
    