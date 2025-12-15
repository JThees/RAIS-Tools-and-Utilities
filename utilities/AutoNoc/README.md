<div align="center">

# Resonant AI Systems TOOLS & UTILITIES

## AutoNoc

### Built by Resonant AI Core
**Research & Development Division of Resonant AI Systems**

![License](https://img.shields.io/badge/license-Apache%202.0-blue)
![Status](https://img.shields.io/badge/status-active%20development-brightgreen)
![Scope](https://img.shields.io/badge/scope-infrastructure%20tool-purple)
![Division](https://img.shields.io/badge/division-Resonant%20AI%20Core-black)

**Autonomous network operations center on hardware you control.**

Raspberry Pi 5-based physical monitoring station for infrastructure surveillance. Environmental sensing, vibration detection, GPS positioning, and visual status displays integrated into a single hardware platform.
Not cloud monitoring. Not SaaS dashboards. **Local-first observability on your hardware.**

</div>

---

## WHAT THIS IS

AutoNoc is a hardware monitoring station that combines multiple sensor types with visual displays to provide continuous infrastructure surveillance and autonomous alerting.

**Core components:**
- Environmental monitoring (temperature, humidity, barometric pressure)
- Distributed temperature sensing across server rack spaces
- Vibration detection for equipment health monitoring
- GPS positioning and time synchronization
- Visual status indication via LED matrix and RGB strips
- Autonomous alerting for threshold violations

Built on Raspberry Pi 5 (16GB) with NVMe boot, designed for 24/7 operation in server rack environments. All sensors connected via GPIO, displays driven independently with external power.

---

## WHY IT EXISTS

Server room monitoring requires multiple independent systems: environmental sensors, equipment health checks, alerting infrastructure. Combining these into a single integrated platform reduces complexity and enables correlation across sensor data.

**Problem solved:**
Manual infrastructure monitoring misses gradual degradation. Temperature creep, vibration changes, and environmental drift happen slowly. Automated monitoring with threshold triggers catches problems before failures occur.

**Use cases:**
- Server rack environmental monitoring
- Lab equipment health surveillance
- Physical security sensor integration
- Research infrastructure observability

Built for operators running their own hardware who need continuous monitoring without cloud dependencies.

---

## FEATURES

### Sensor Capabilities
- **BME280 environmental sensor** - Temperature, humidity, barometric pressure (I2C)
- **4x DS18B20 temperature probes** - Distributed rack temperature monitoring (1-wire)
- **5x SW-420 vibration sensors** - Equipment vibration/shock detection (digital GPIO)
- **2x GY-NEO6MV2 GPS modules** - Location tracking and time sync (UART)

### Display Systems
- **2x MAX7219 LED matrix** - 8x32 pixel scrolling status displays
- **2x WS2812B RGB LED strips** - Color-coded status indication
- **3.5" HDMI touchscreen** - Local dashboard and configuration interface

### Alert Architecture (Planned)
- Threshold-based trigger logic
- SMS/email notifications via external services
- Local alarm (buzzer/LED patterns)
- Event logging with timestamp and sensor correlation

### Infrastructure
- **Raspberry Pi 5 (16GB)** with NVMe boot (Samsung 980 Pro 500GB)
- **Active cooling** for thermal stability
- **Rack-mountable** on 1U server shelf
- **External power monitoring** via P3 P4400 Kill-A-Watt

---

## REQUIREMENTS

**Hardware:**
- Raspberry Pi 5 (8GB or 16GB recommended)
- NVMe HAT + NVMe SSD (boot performance)
- Sensors listed in hardware section (BME280, DS18B20, SW-420, GPS modules)
- Displays (MAX7219, WS2812B, HDMI touchscreen)
- 27W USB-C power supply
- Breadboard or power distribution board for sensor wiring

**Software:**
- Raspberry Pi OS (64-bit, Bookworm or later)
- Python 3.9+
- GPIO libraries (RPi.GPIO or gpiod)
- Sensor-specific libraries (smbus2, bme280, pyserial, rpi_ws281x, luma.led_matrix)

**Optional:**
- InfluxDB (for time-series data logging)
- Grafana (for dashboard visualization)
- SMS/email service credentials (for remote alerting)

---

## INSTALLATION

**Current Status:** Hardware assembly in progress. Installation instructions will be added when software development begins.

### Hardware Assembly (In Progress)

1. **Core platform setup**
   - Install NVMe HAT on Raspberry Pi 5
   - Flash Raspberry Pi OS to NVMe SSD
   - Configure boot from NVMe (requires bootloader update)
   - Install active cooler

2. **GPIO preparation**
   - Pins 1-10 and 39-40 unavailable (NVMe HAT conflict)
   - Working range: GPIO pins 11-38 (28 pins available)
   - Wire GPIO pins 11-38 to breakout board for sensor access

3. **Sensor wiring** (Planned)
   - BME280 → Pins 27-28 (I2C, GPIO0/1)
   - GPS modules → Pins 35, 38 (UART, GPIO19/20)
   - Vibration sensors → Pin 13 (GPIO27, digital input)
   - Temperature probes → Pin 11 (GPIO17, 1-wire)
   - All sensors powered from Pin 17 (3.3V, ~70mA total draw)

4. **Display wiring** (Planned)
   - LED matrix and RGB strips require external 5V power supply
   - Common ground with Pi GPIO
   - Data lines connected to available GPIO pins

5. **Software installation** (Not Started)
   - Clone repository
   - Install Python dependencies
   - Configure sensor communication (I2C, UART, 1-wire)
   - Test individual sensors
   - Configure display drivers

Full installation guide will be added once hardware assembly completes.

---

## USAGE

**Usage documentation will be added when software development begins.**

Planned functionality:
- Systemd service for continuous monitoring
- Configuration file for sensor thresholds
- Local web interface for status dashboard
- Manual alert triggers for testing
- Data export for external analysis

---

## STATUS & ROADMAP

**Current Status:** Active Development (Hardware Assembly Phase)

### Completed
- Core platform assembled (Pi 5, NVMe HAT, active cooling)
- Boot from NVMe working (Samsung 980 Pro 500GB)
- GPIO pins 11-38 wired to breakout board
- All sensors and displays received and identified
- Power distribution strategy planned

### In Progress
- Wiring sensors to GPIO pins
- Configuring I2C/UART/GPIO communication protocols
- Breadboard power distribution setup

### Not Started
- Software development (sensor polling daemon)
- Sensor calibration and testing
- Display programming (LED matrix, RGB strips)
- Alert logic implementation
- Production deployment and rack mounting

### Known Issues
- **I2C bus configuration** - Default I2C (pins 3/5) available, alternate I2C (GPIO0/1) requires device tree overlay configuration
- **False I2C detection** - Initial testing showed devices detected on all I2C addresses (bus configuration error)
- **Power distribution** - Pin 17 (3.3V) must power all sensors, breadboard module needed for clean wiring

### Roadmap
- **Phase 1 (Current)** - Complete sensor wiring, test I2C/UART communication, basic sensor reading scripts
- **Phase 2** - Wire displays, implement status display code, GPS time sync
- **Phase 3** - Monitoring daemon, alert logic, threshold configuration, logging infrastructure
- **Phase 4** - Custom case panels (RAIC logo, symbols, screen mount), rack mounting, production deployment

**Target:** Operational monitoring station by Q1 2025

---

## HARDWARE DETAILS

### Core Platform
- **Raspberry Pi 5** (16GB RAM)
- **GeekPi N04 NVMe HAT** + Samsung 980 Pro 500GB NVMe SSD
- **GeekPi Active Cooler** (thermal management)
- **27W USB-C GaN Power Supply**

### Sensors
- **Waveshare BME280** - Environmental sensor (I2C)
- **5x SW-420** - Vibration/shock sensors (digital)
- **4x DS18B20** - Waterproof temperature probes (1-wire)
- **2x GY-NEO6MV2** - GPS modules (UART)

### Displays
- **2x MAX7219 LED Matrix** (8x32 pixels)
- **2x WS2812B RGB LED Strips**
- **HAMTYSAN 3.5" HDMI Touchscreen**

### Infrastructure
- **SABRENT 4-Port USB 3.0 Hub**
- **ElectroCookie Mini PC Case** (for custom panel modifications)
- **Breadboard kit** (power distribution)
- **P3 P4400 Kill-A-Watt** (external power monitoring)
- **19" 1U Server Shelf** (rack mounting)

**Total Hardware Cost:** ~$420

---

## GPIO PIN ALLOCATION

**Pins 1-10 and 39-40 unavailable** (NVMe HAT physical clearance)

**Working range: Pins 11-38** (28 GPIO pins)

### Planned Connections

| Component | Power | Ground | Data Pins | Protocol |
|-----------|-------|--------|-----------|----------|
| BME280 | Pin 17 (3.3V) | Pin 20 | Pins 27-28 (GPIO0/1) | I2C |
| GPS | Pin 17 (3.3V) | Pin 25 | Pins 35, 38 (GPIO19/20) | UART |
| Vibration | Pin 17 (3.3V) | Pin 14 | Pin 13 (GPIO27) | Digital |
| Temp Probes | Pin 17 (3.3V) | Pin 14 | Pin 11 (GPIO17) | 1-Wire |

**Note:** LED displays require external 5V power supply, not GPIO power.

---

## LICENSE

**Apache License 2.0**

See [LICENSE](LICENSE) file for full text.

Use freely. Modify freely. Deploy freely.
Attribution appreciated but not required.

---

## CONTACT

**General Inquiries**
ops@resonantaisystems.com

**Research Collaboration**
https://resonantaicore.com

**Enterprise Partnerships**
https://resonantaisystems.com

---

*Part of the Resonant AI Systems public research toolkit. Built for autonomous infrastructure monitoring, local-first operation, and operator-controlled systems.*
