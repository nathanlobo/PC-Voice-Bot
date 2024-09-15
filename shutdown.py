import os, psutil, datetime, time

def shutdown(delay):
    os.system(f"shutdown /s /t {delay}")

def get_boot_time():
    # Get the boot time
    boot_time_timestamp = psutil.boot_time()
    boot_time = datetime.datetime.fromtimestamp(boot_time_timestamp)
    return boot_time

def get_uptime_minSec():
    # Get the current time
    current_time = datetime.datetime.now()
    # Calculate the duration since boot time, splits to remove micro seconds and splits Hours|Mins|Secs
    uptime_duration = str(current_time - get_boot_time()).split(".")[0].split(":")
    uptime_duration = str((int(uptime_duration[0])*60) + (int(uptime_duration[1]))) + (str("." + uptime_duration[2]))
    return uptime_duration

def get_cpu_usage():
    # Get the current CPU usage
    cpu_usage = psutil.cpu_percent(interval=1)
    return cpu_usage

def get_memory_usage():
    # Get the memory usage statistics
    memory_info = psutil.virtual_memory()
    return memory_info

def get_user_session_time():
    # Get the user session start time
    user_sessions = psutil.users()
    if user_sessions:
        session_start = user_sessions[0].started
        session_time = datetime.datetime.fromtimestamp(session_start)
        return session_time

def get_disk_io_stats():
    # Get the disk I/O statistics
    disk_io = psutil.disk_io_counters()
    return disk_io

def get_network_usage():
    # Get the network I/O statistics
    net_io = psutil.net_io_counters()
    return net_io

if __name__ == "__main__":
    usageLimit_inMins = 150.00 # 2hours 30Mins
    while True:
        uptime_duration = get_uptime_minSec() #get_uptime_minSec returns uptime in mins.sec w/ decimal but as string
        print(uptime_duration) # Printed as a string, if it was float it would remove the last 0 from secs
        time.sleep(1)
        target_hour = 13 # 1:00 PM
        target_minute = 30
        now = datetime.datetime.now()
        if now.hour > target_hour or (now.hour == target_hour and now.minute > target_minute):
            print("The time is past 10. Performing the task...")
            if uptime_duration >= usageLimit_inMins:
                # shutdown(10)
                pass
        else:
            print("It's not past the target time yet.")


    # cpu_usage = get_cpu_usage()
    # memory_info = get_memory_usage()
    # user_session_time = get_user_session_time()
    # disk_io = get_disk_io_stats()
    # net_io = get_network_usage()

    # print("PC was started at:", boot_time.strftime("%Y-%m-%d %H:%M:%S"))
    # print("PC has been running for:", str(uptime_duration).split('.')[0])  # Split to remove microseconds
    # print("Current CPU usage:", f"{cpu_usage}%")
    # print(f"Memory Usage: {memory_info.percent}% used of {round(memory_info.total / (1024 ** 3), 2)} GB")
    
    # if user_session_time:
    #     print("Current user session started at:", user_session_time.strftime("%Y-%m-%d %H:%M:%S"))
    
    # print(f"Disk I/O - Read: {disk_io.read_bytes / (1024 ** 3):.2f} GB, Write: {disk_io.write_bytes / (1024 ** 3):.2f} GB")
    # print(f"Network Usage - Sent: {net_io.bytes_sent / (1024 ** 3):.2f} GB, Received: {net_io.bytes_recv / (1024 ** 3):.2f} GB")
