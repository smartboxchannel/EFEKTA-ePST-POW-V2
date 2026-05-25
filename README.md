# EFEKTA-ePST-POW-V2


![EFEKTA ePST POW V2](https://raw.githubusercontent.com/smartboxchannel/EFEKTA-ePST-POW-V2/refs/heads/main/images/logo_promo2.png) 

# EFEKTA ePST POW V2 Pressure Sensor with E-Ink Display

Pressure sensor with e-ink display, featuring a wider operating temperature range compared to V1. Powered via USB Type-C with backup power from 2 AAA batteries. Available as Zigbee end device or router (on request). Designed for Zigbee networks. Compatible with Home Assistant via Zigbee2MQTT and ZHA, Sprut Hub, HOMEd. Suitable for monitoring liquid pressure in water supply and heating systems.

## Properties

| Property | Description |
|----------|-------------|
| **Pressure** | Measured pressure value in kPa, transmitted by the sensor |
| **Bar** | Measured pressure value in Bar *¹ |
| **Psi** | Measured pressure value in PSI *² |
| **Temperature** | Measured temperature value from internal sensor |
| **Battery low** | Flag indicating batteries are nearly depleted |
| **Battery** | Remaining charge in %. Updates once every 6 hours or on button press |
| **Mains voltage** | Sensor supply voltage in volts |
| **Reading interval** | Sensor reading interval in seconds. Default: 20s (standard radio module) / 40s (signal amplifier version). Min: 10s, Max: 360s |
| **Tx radio power** | Transmitter power setting in dBm |
| **Comparison previous data** | Enable comparison with previous data. Works only in timer-based reporting mode. If enabled, data is sent only when new reading differs by more than 0.25°C from previous. If disabled, data is sent after every sensor reading |
| **Pressure offset** | Adjust pressure sensor reading, step 0.1 kPa |
| **Temperature offset** | Adjust temperature sensor reading, step 0.1°C |
| **Invert** | Invert e-ink display colors |
| **Fast mode** | E-ink display refresh mode: fast (1.5 sec), ultra fast (300 ms) |
| **Sensor identifier** | Identifier of the installed sensor |
| **Linkquality** | Signal quality (LQI) *³ |

*¹ Not transmitted by the device, calculated on the host side. In Zigbee2MQTT, calculation is implemented in the converter.*

*² Not transmitted by the device, calculated on the host side. In Zigbee2MQTT, calculation is implemented in the converter.*

*³ Signal quality — a property not transmitted by the sensor, but calculated by the network coordinator based on received data evaluation.*

## Joining and Leaving the Network

### Joining
Press and hold the button. After 1 second, the display will show a network search message. Continue holding the button — joining typically begins after 5-8 seconds. If no open network is found, the sensor will exit search mode after 15 seconds.

During joining, position the sensor close to the coordinator (1-2 meters) or a router with good signal strength.

If you don't see all configuration attribute values in the properties tab (empty fields, switches in undefined state) or no battery/temperature entries in the reports page, the configuration (which follows immediately after the interview) likely did not complete fully.

When the sensor is joined to the network, a short button press triggers an unscheduled reading of all sensors and data transmission.

### Leaving
Hold the button for 10 seconds. After 10 seconds, the display will show a network leave message. The sensor will send a leave notification and erase all settings from memory.

## External Converter Setup
- **Zigbee2MQTT:** [Adding an External Converter](https://telegra.ph/Dobavlenie-vneshnego-konvertera-v-zigbee-2-mqtt-12-11)
- **Sprut Hub:** [Adding an External Template](https://clck.ru/362h5z)

## Sensor Detection
The sensor features connected sensor detection. If the system LED lights up, the pressure sensor is not detected. After several failed attempts to read the pressure sensor, the device will transmit error data: 10 bar and -40°C.

## High-Frequency Interference

High-frequency interference in the 220V mains can cause sensor malfunction, indicated by:

- **Indication:** System LED on the device lights up and stays solid (not blinking)
- **Data:** Sensor stops transmitting correct values. Error readings of 10 bar and -40°C are sent (corresponding to sensor read error)

### Troubleshooting:
1. **Ferrite ring:** Install a ferrite filter (ring) on the USB cable to suppress high-frequency interference
2. **Power stabilization:** Connect the sensor to 220V mains through a dedicated power stabilizer or quality surge protector with noise filtering
3. **Mains isolation:** Disconnect USB power and switch to battery operation — this completely eliminates 220V mains interference

> ⚠️ **Warning:** Do not connect or disconnect the external pressure sensor while the device is powered. Disconnect the power cable and/or remove batteries before connecting or disconnecting the sensor.

## Technical Specifications

| Parameter | Value |
|-----------|-------|
| **Model** | ePST POW V2 |
| **Protocol** | ZigBee 3.0 |
| **Radio sensor dimensions** | 8 × 3 × 3 cm |
| **Sensor** | XDB401 (pressure and temperature) |
| **External sensor cable length** | 100 cm |
| **Pressure sensor housing** | AISI 304 stainless steel |
| **Pressure measurement accuracy** | 1% FS |
| **Operating temperature range** | -40°C ~ +105°C |
| **Burst pressure** | 300% FS |
| **Thread** | 1/4 |
| **E-ink display operating temperature** | 0°C ~ +60°C |
| **Primary power** | USB Type-C |
| **Backup power** | 2 AAA batteries (not included) |
