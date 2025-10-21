import re
import time
from data import ipv4_data_dict
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
    
def print_unique_ipv4_addrs(ipv4_data_dict: dict):
    for ip in ipv4_data_dict["ipv4_list"]:
        print(ip)
    
     
def main_menu(ipv4_data_dict: dict):
    print("Please select an option")
    print("enter 1 to look for suspicious ip address based multiple connections")
    print("enter 2 to repeat a message on a timer")
    print("enter 3 to print all ip addresses after selecting option 1")
    try:
        option = int(input("Enter Option:"))
    except:
        print("Invalid option")
        pass
    match option:
        case 1:
            find_suspicious_ip_addrs(ipv4_data_dict)
        case 2:
            wait_5_seconds_repeat_message(ipv4_data_dict)
        case 3:
            print_unique_ipv4_addrs(ipv4_data_dict)
        case _:
            print("invalid option")


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