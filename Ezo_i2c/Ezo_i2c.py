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
    
    def __init__(self, i2c:machine.I2C, address:int):
        """
        Creates a new Ezo_i2c class for reading gyro rates and acceleration data.
        :param i2c: A setup I2C module of the machine module.
        :param address: The I2C address of the Ezo Sensor you are using (varies from device in device).
        """
        self.address = address
        self.i2c = i2c
        
    def send_cmd(self, cmd:str) -> None:
        """Send command to Ezo device"""
        self.i2c.writeto(self.address, bytes(cmd,"ascii"))

    def recive_cmd(self,nbytes) -> str:
        """
        Recive any data from an Ezo device the data output is an string
        :param nbytes: Lenght of bytes to read from the Ezo Device
        """
        raw_data = self.i2c.readfrom(self.address,nbytes)
        count = 0
        bytes_data = []
        for i in raw_data:
            if i == 1:
                print("OK")
            if count > 0:
                bytes_data.append(i)
            if i == 0:
                break
            count += 1
        return  "".join(map(chr, bytes_data)) # Convert bytes encoded in ASCII
    