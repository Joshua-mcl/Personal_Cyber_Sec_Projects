import datetime
from log_functions import main_menu
from data import ipv4_data_dict

def main():

   

    while True:
        main_menu(ipv4_data_dict)

if __name__ == "__main__":
    main()