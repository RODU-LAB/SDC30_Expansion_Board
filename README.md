# SDC30 Expansion Board  with Raspberry Pi

## SDC Expansion Board

![Untitled](SDC30%20Expansion%20Board%20with%20Raspberry%20Pi%20aebc9b74ae86490ab954c35bc79a887f/Untitled.png)

본 제품은 RODU에서 개발한 SDC30 Expansion Board로 Raspberry Pi에서 호환되며 최대 4개의 센서를 I2C 통신을 통하여 동시에 사용할 수 있는 보드이다.

## Specification

- 선 길이 : 1.5m
- 로컬 저장 가능 (날짜 : 데이터, 데이터….)
- 1분마다 저장 가능

## Prototype Appearance

![Untitled](SDC30%20Expansion%20Board%20with%20Raspberry%20Pi%20aebc9b74ae86490ab954c35bc79a887f/Untitled%201.png)

실제 라즈베리파이에 부착한 모습으로
아래에서부터 1~4번으로 사용되며, 쿨러 전원을 위한 핀이 따로 존재한다.

## Pin Diagram

![Untitled](SDC30%20Expansion%20Board%20with%20Raspberry%20Pi%20aebc9b74ae86490ab954c35bc79a887f/Untitled%202.png)

사용되는 통신 핀의 경우 라즈베리에서 연결되는 SDA/SCL과 전원을 비롯하여 멀티플렉스를 통해 SD1/SC1, SD2/SC2, SD3/SC3, SD4/SC4가 사용된다.

## Software

![Untitled](SDC30%20Expansion%20Board%20with%20Raspberry%20Pi%20aebc9b74ae86490ab954c35bc79a887f/Untitled%203.png)

![Untitled](SDC30%20Expansion%20Board%20with%20Raspberry%20Pi%20aebc9b74ae86490ab954c35bc79a887f/Untitled%204.png)

![Untitled](SDC30%20Expansion%20Board%20with%20Raspberry%20Pi%20aebc9b74ae86490ab954c35bc79a887f/Untitled%205.png)

![Untitled](SDC30%20Expansion%20Board%20with%20Raspberry%20Pi%20aebc9b74ae86490ab954c35bc79a887f/Untitled%206.png)

![Untitled](SDC30%20Expansion%20Board%20with%20Raspberry%20Pi%20aebc9b74ae86490ab954c35bc79a887f/Untitled%207.png)

```python
import board
import time
import adafruit_tca9548a
import adafruit_scd30

# Create I2C bus as normal
i2c = board.I2C()  # uses board.SCL and board.SDA

# Create the TCA9548A object and give it the I2C bus
tca = adafruit_tca9548a.TCA9548A(i2c)

# Create SCD30 sensor objects
scd1 = adafruit_scd30.SCD30(tca[1])
scd2 = adafruit_scd30.SCD30(tca[2])
scd3 = adafruit_scd30.SCD30(tca[3])
scd4 = adafruit_scd30.SCD30(tca[4])

# Open a file in append mode to save data
filename = 'sensor_data.txt'

# Function to write data to file
def write_data_to_file(timestamp, sensor_number, co2, temperature, humidity):
    with open(filename, 'a') as file:
        file.write(f"{timestamp} - Sensor{sensor_number}: CO2: {co2} PPM, Temperature: {temperature:.2f} degrees C, Humidity: {humidity:.2f} % rH\n")

# Main loop

print('Sensor Check Start')
while True:
    # Current timestamp
    timestamp = time.strftime("%Y-%m-%d %H:%M:%S")
    
    # Check data availability and write to file
    if scd1.data_available:
        write_data_to_file(timestamp, 1, scd1.CO2, scd1.temperature, scd1.relative_humidity)
        
    if scd2.data_available:
        write_data_to_file(timestamp, 2, scd2.CO2, scd2.temperature, scd2.relative_humidity)
        
    if scd3.data_available:
        write_data_to_file(timestamp, 3, scd3.CO2, scd3.temperature, scd3.relative_humidity)
        
    if scd4.data_available:
        write_data_to_file(timestamp, 4, scd4.CO2, scd4.temperature, scd4.relative_humidity)
    
    print('data save')
    # Wait for 1 minute before the next iteration
    time.sleep(60)

```

소프트웨어 사용에 대해서는 함께 제공하는 메뉴얼을 참고.