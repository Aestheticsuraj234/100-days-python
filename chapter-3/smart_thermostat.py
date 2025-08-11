device_status = "active"

temperature = 38


if device_status == "active":
    if temperature > 35:
        print("High temperature🟢")
    else:
        print("Normal temperature🟡")    
else:
    print("Device is offline🔴")