import speedtest

def bytes_to_mb(bytes):
    return round(bytes/(1024*1024),2)


#initialize Speedtest

st = speedtest.Speedtest()



down_speed =  bytes_to_mb(st.download())


up_speed = bytes_to_mb(st.upload())


ping = st.results.ping



print(f"Download Speed: {down_speed} MB/s")
print(f"Upload Speed: {up_speed} MB/s")
print(f"Ping: {ping} ms")