from user_agents import parse

brandVivo = ["Vivo", "vivo", "VIVO"]
brandXiaomi = ["Xiaomi", "xiaomi", "XIAOMI", "XiaoMi"]
brandAsus = ["Asus", "asus", "ASUS"]
brandNokia = ["Nokia", "nokia", "NOKIA"]
brandApple = ["Apple", "apple", "APPLE"]
brandMotorola = ["Motorola", "motorola", "MOTOROLA"]
brandSamsung = ["Samsung", "samsung", "SAMSUNG"]

OSLinux = ["Linux", "linux", "LINUX"]
OSWindows = ["Windows", "windows", "WINDOWS"]
OSMacosx = ["Macosx", "macosx", "MACOSX", "MacOSX", "MacOS", "Macos", "MacOs", "macos", "MACOS", "Mac OS", "Mac Os", "MAC OS", "mac os", "Mac OSX", "Mac Osx", "MAC OSX", "mac osx", "Mac OS X", "Mac OS x", "mac os x" ]
OSAndroid = ["Android", "android", "ANDROID"]
OSIOS = ["IOS", "Ios", "ios", "iOS"]

def supernetter(ip, flush_bits=10):
    parts = ip.split('.')
    bins = []
    for part in parts:
        bins.append(str(bin(int(part)))[2:])

    for i in range(len(bins)):
        diff = 8 - len(bins[i])
        if diff > 0:
            bins[i] = ("0"*diff) + bins[i]
    flush_bits_left = flush_bits
    
    zeroed = 4
    for i in range(3, -1, -1):
        if(flush_bits_left > 8):
            bins[i] = ("0" * 8)
            flush_bits_left = flush_bits_left - 8
            zeroed -= 1
        else:
            break
    
    if flush_bits_left == 0:
        return generate_ip_from_bins(bins)
    
    if zeroed <= 0:
        return generate_ip_from_bins(bins)

    bin_index_left = zeroed - 1

    final_bin = []
    for i in range(len(bins[bin_index_left]) - 1, -1, -1):
        if flush_bits_left > 0:
            final_bin.insert(0, '0')
            flush_bits_left -= 1
        else:
            final_bin.insert(0, bins[bin_index_left][i])
    
    bins[bin_index_left] = ''.join(final_bin)
    return generate_ip_from_bins(bins)

def generate_ip_from_bins(bins):
    parts = []
    for each_bin in bins:
        parts.append(str(int(each_bin, 2)))
    
    return '.'.join(parts)

def transform_tpoint(tpoint) :
    wanted = {}
    wanted["dataid"] = tpoint.get("dataid")
    wanted["urlid"] = tpoint.get("urlid")
    wanted["availableRam"] = tpoint.get("availableRam")
    wanted["city"] = tpoint.get("city")
    wanted["ipaddress"] = tpoint.get("ipaddress")
    wanted["latitude"] = tpoint.get("latitude")
    wanted["longitude"] = tpoint.get("longitude")
    if tpoint.get("battery"):
        try:
            wanted['battery'] = str(int(tpoint['battery']))
        except Exception as e:
            print(e)
            wanted['battery'] = None
    try:
        user_agent = parse(tpoint.get("userAgent"))
        wanted['brand'] = get_ua_brand(user_agent)
        wanted['os'] = get_ua_os(user_agent)
        wanted['device'] = get_ua_model(user_agent)
    except Exception as e:
        print(e)
    return wanted

def get_ua_os(ua_object):
    if not ua_object:
        return "OtherOS"
    if ua_object.os.family in OSLinux :
        return "Linux"
    elif ua_object.os.family in OSWindows :
        return "Windows"
    elif ua_object.os.family in OSMacosx :
        return "MacOSX"
    elif ua_object.os.family in OSAndroid :
        return "Android"
    elif ua_object.os.family in OSIOS :
        return "iOS"
    else :
        return "OtherOS" 

def get_ua_brand(ua_object):
    if not ua_object:
        return "OtherBrand"
    if ua_object.device.brand in brandVivo :
        return "Vivo"
    elif ua_object.device.brand in brandXiaomi :
        return "Xiaomi"
    elif ua_object.device.brand in brandAsus :
        return "Asus"
    elif ua_object.device.brand in brandNokia :
        return "Nokia"
    elif ua_object.device.brand in brandApple :
        return "Apple"
    elif ua_object.device.brand in brandMotorola :
        return "Motorola"
    elif ua_object.device.brand in brandSamsung :
        return "Samsung"
    else :
        return "OtherBrand"

def get_ram_gbs(ram_string):
    if not ram_string:
        return "OtherRAM"
    if ram_string == "8":
        return "EightGB"
    elif ram_string == "6":
        return "SixGB"
    elif ram_string == "4":
        return "FourGB"
    elif ram_string == "2":
        return "TwoGB"
    else:
        return "OtherRAM"

def get_ua_model(ua_object):
    if not ua_object:
        return "Unknown Model"
    return ua_object.device.model