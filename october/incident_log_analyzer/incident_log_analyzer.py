import re
import datetime

ipv4_pattern = r'\b((25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\b'
ipv4_list = []
ipv4_dict = {}
sus_ip_addrs = []
with open('sample_auth.log', 'r') as l:
    print('Welcome to my make shift log analyzer')
    print(f"To begin I wil now display the contents of :{l.name}")
    
    for line in l.readlines():
        for match in re.finditer(ipv4_pattern, line, re.S):
            match_text = match.group()
            if match_text in ipv4_list:
                if ipv4_dict.get(match_text) == None:
                    ipv4_dict[match_text] = 1
                else:
                    if ipv4_dict.get(match_text) >= 5 and match_text not in sus_ip_addrs:
                        sus_ip_addrs.append(match_text)
                    ipv4_dict[match_text] = ipv4_dict.get(match_text) + 1
            else:
                ipv4_list.append(match_text)

    print("Displaying list of suspicious ip addresses:")
    print()
    for ip in sus_ip_addrs:
        print(f"{ip} appeared {ipv4_dict.get(ip)} times")
    
    
                
                





l.close()