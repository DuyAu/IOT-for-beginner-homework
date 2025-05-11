import pynmea2

# Path to your NMEA file
file_path = "output(1).nmea"

# Open and parse the file
with open(file_path, 'r') as file:
    for line in file:
        try:
            msg = pynmea2.parse(line.strip())
            
            if isinstance(msg, pynmea2.types.talker.GGA):
                print("\n--- GGA Sentence (Fix Data) ---")
                print(f"Time (UTC): {msg.timestamp}")
                print(f"Latitude: {msg.latitude} {msg.lat_dir}")
                print(f"Longitude: {msg.longitude} {msg.lon_dir}")
                print(f"Fix quality: {msg.gps_qual}")
                print(f"Number of satellites: {msg.num_sats}")
                print(f"Altitude: {msg.altitude} {msg.altitude_units}")
            
            elif isinstance(msg, pynmea2.types.talker.RMC):
                print("\n--- RMC Sentence (Recommended Minimum Data) ---")
                print(f"Date: {msg.datestamp}")
                print(f"Time (UTC): {msg.timestamp}")
                print(f"Speed (knots): {msg.spd_over_grnd}")
                print(f"Course: {msg.true_course}")
                print(f"Latitude: {msg.latitude} {msg.lat_dir}")
                print(f"Longitude: {msg.longitude} {msg.lon_dir}")
                print(f"Status: {msg.status}")
        
        except pynmea2.ParseError:
            continue
