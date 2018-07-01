
   # ---- Step 1: Open the enumerated device and get a handle to it -------------
   
   mvnc.global_set_option(mvnc.GlobalOption.RW_LOG_LEVEL, 2)
   # Look for enumerated NCS device(s); quit program if none found.
   devices = mvnc.enumerate_devices()
   if len(devices) == 0:
       print("No devices found")
       quit()
   
   # Get a handle to the first enumerated device and open it
   device = mvnc.Device(devices[0])
   device.open()
