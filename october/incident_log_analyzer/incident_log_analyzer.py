import datetime

from log_functions import find_suspicious_ip_addrs


def main():

    ipv4_data_dict = {
    "ipv4_list" : [],
    "sus_ip_list" : [],
    "ipv_4_dict" : {}
    }

    find_suspicious_ip_addrs(ipv4_data_dict)


if __name__ == "__main__":
    main()











