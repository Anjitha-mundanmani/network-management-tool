import os

def menu_interface():
    asd = os.popen("ip -o link show | awk -F': ' '{print $2}'").read()
    print("-----------Menu for interface------------")
    asd = " ".join(asd.split(":\n"))
    print(asd.replace(' ', '\n'))

def Assign_IP_address():
    menu_interface()
    interface = input("Enter the interface name : ")
    ip = input("Enter the ip address to assign :")
    ip_assign = os.popen(f"sudo ip address add {ip} dev {interface}").read()
    print(os.popen(f"ip -4 a show {interface}").read())

def Delete_IP_address():
    menu_interface()
    interface = input("Enter the interface name : ")
    ip = input("Enter the ip address to delete :")
    ip_assign = os.popen(f"sudo ip address del {ip} dev {interface}").read()
    print(os.popen(f"ip -4 a show {interface}").read())

def Display_IP_address():
    menu_interface()
    interface = input("Enter the interface name : ")
    print(os.popen(f"ip -4 a show {interface}").read())

def Display_all_interfaces():
    print(os.popen("ip l").read())

def Configure_routing():
    menu_interface()
    interface = input("Enter the interface name : ")
    ip = input("Enter the ip address :")
    ip_assign = os.popen(f"sudo ip r add 10.2.3.0/24 via {ip} dev {interface}").read()
    print(os.popen("ip r").read())
    
def Turn_OnOff_interface():
    while True:
        print("1.Turn on interface")
        print("2.Turn off interface")
        print("3.exit")
        ch = int(input("Enter the choice"))
        if ch == 1:
            menu_interface()
            interface = input("Enter the interface name : ")
            on = os.popen(f"sudo ip link set dev {interface} un").read()
            print(os.popen("ip a").read())
        elif ch == 2:
            menu_interface()
            interface = input("Enter the interface name : ")
            off = os.popen(f"sudo ip link set dev {interface} down").read()
            print(os.popen("ip a").read())
        else:
            break
            
def Add_ARP_entry():
    menu_interface()
    interface = input("Enter the interface name : ")
    ip = input("Enter the ip address :")
    cmd = f"sudo ip n add {ip} lladdr 00:45:78:52:ed:55 dev {interface} nud permanent"
    arp = os.popen(cmd).read()
    print(os.popen("ip n show").read())

def Delete_ARP_Entry():
    menu_interface()
    interface = input("Enter the interface name : ")
    ip = input("Enter the ip address :")
    arp = os.popen(f"sudo ip n flush {ip} dev {interface} nud permanent").read()
    print(os.popen("ip n show").read())

def Restart_Network():
    print(os.popen("sudo systemctl status networking").read())

def Change_hostname():
    name = input("Enter the name you want change as host name : ")
    change_host = os.popen(f"sudo hostname {name}").read()
    print(os.popen("hostnamectl status").read())
    
def Add_DNS_server_entry():
    dns = os.popen("sudo cat >> /etc/resolv.conf").read()
    print("Successfully added")

def main_menu():
    print("1.Assign IP address")
    print("2.Delete IP address")
    print("3.Display IP address")
    print("4.Display all interfaces")
    print("5.Configure routing")
    print("6.Turn On/Off interface")
    print("7.Add ARP entry")
    print("8.Delete ARP Entry")
    print("9.Restart Network")
    print("10.Change Hostname")
    print("11.Add DNS server entry")

operations = {
    "1":Assign_IP_address,
    "2":Delete_IP_address,
    "3":Display_IP_address,
    "4":Display_all_interfaces,
    "5":Configure_routing,
    "6":Turn_OnOff_interface,
    "7":Add_ARP_entry,
    "8":Delete_ARP_Entry,
    "9":Restart_Network,
    "10":Change_hostname,
    "11":Add_DNS_server_entry
}

while True:
	main_menu()
	ch = input("Enter Choice: ")
	operations[ch]()
