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
