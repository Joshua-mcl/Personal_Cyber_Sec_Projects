import re
import time

def find_suspicious_ip_addrs(ipv4_data_dict: dict) -> dict:
    """Finds ip addresses that have connected 5 times and returns a dict containing a list of them while outputing information to screen"""
    ipv4_pattern = r'\b((25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\b'

    with open('sample_auth.log', 'r') as l:
        print('Welcome to my make shift log analyzer')
        print(f"To begin I wil now display the contents of :{l.name}")
        
        for line in l.readlines():
            for match in re.finditer(ipv4_pattern, line, re.S):
                match_text = match.group()
                if match_text in ipv4_data_dict["ipv4_list"]:
                    if ipv4_data_dict["ipv_4_dict"].get(match_text) == None:
                        ipv4_data_dict["ipv_4_dict"][match_text] = 1
                    else:
                        if ipv4_data_dict["ipv_4_dict"].get(match_text) == 5 and match_text not in ipv4_data_dict["sus_ip_list"]:
                            ipv4_data_dict["sus_ip_list"].append(match_text)
                        ipv4_data_dict["ipv_4_dict"][match_text] = ipv4_data_dict["ipv_4_dict"].get(match_text) + 1
                else:
                    ipv4_data_dict["ipv4_list"].append(match_text)

        print("Displaying list of suspicious ip addresses:")
        print()
        for ip in ipv4_data_dict["sus_ip_list"]:
            print(f"{ip} appeared {ipv4_data_dict["ipv_4_dict"].get(ip)} times")

        l.close()
        return ipv4_data_dict   

def wait_5_seconds_repeat_message(message: str):
    if message == None:
        message ="................................"
    countdown_ticks = 5
    print(message)
    print(f"in {countdown_ticks}(s)")
    countdown_ticks -= 1
    time.sleep(1)
    print(message)
    print(f"in {countdown_ticks}(s)")
    countdown_ticks -= 1
    time.sleep(1)
    print(message)
    print(f"in {countdown_ticks}(s)")
    countdown_ticks -= 1
    time.sleep(1)
    print(message)
    print(f"in {countdown_ticks}(s)")
    countdown_ticks -= 1
    time.sleep(1)
    print(message)
    print(f"in {countdown_ticks}(s)")
    countdown_ticks -= 1
    time.sleep(1)
    return