"""
Micropython code for TTGO T-Beam V1.0 and V1.1 to enable GPS in micropython pycom variant

Inspired by:
    - Korving-F @ https://github.com/Korving-F/ublox/
    - Original arduino sketch by LilyGO @ https://github.com/LilyGO/TTGO-T-Beam/tree/master/GPS-T22_v1.0-20190612
    - Kizniche for his advice on @ https://github.com/kizniche/ttgo-tbeam-ttn-tracker/issues/20
    - SparkFun Ublox Arduino Library @ https://github.com/sparkfun/SparkFun_Ublox_Arduino_Library
    - AXP202 lib by lewsxhe @ https://github.com/lewisxhe/AXP202_PythonLibrary

For T22_v1.0 20190612 and the T22_v1.1 20191212 and T22_v1.1 2021
"""

import axp202
from machine import UART

axp=axp202.PMU(address=axp202.AXP192_SLAVE_ADDRESS)
axp.setLDO3Voltage(3300)   # T-Beam GPS  VDD    3v3
axp.enablePower(axp202.AXP192_LDO3)

dev = UART(1, 9600, pins=('G12','G34'))
msg = b'\xb5b\x06\x00\x14\x00\x01\x00\x00\x00\xd0\x08\x00\x00\x80%\x00\x00\x07\x00\x03\x00\x00\x00\x00\x00\xa2\xb5'
dev.write(msg)