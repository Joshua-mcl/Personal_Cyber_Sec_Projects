import datetime


from log_functions import find_suspicious_ip_addrs
from log_functions import wait_5_seconds_repeat_message


def main():

    ipv4_data_dict = {
    "ipv4_list" : [],
    "sus_ip_list" : [],
    "ipv_4_dict" : {}
    }

    find_suspicious_ip_addrs(ipv4_data_dict)
    wait_5_seconds_repeat_message("I will now display admin log attempts")


if __name__ == "__main__":
    main()