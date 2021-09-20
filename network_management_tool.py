import os

def menu_interface():
    print("-----------Menu for interface------------")
    print("1.wlp7s0")
    print("2.enp14s0")

def Assign_IP_address():
    menu_interface()
    choice = int(input("Enter your choice : "))
    if choice == 1:
        ip = input("Enter the ip address to assign :")
        cmd =f"sudo ip address add {ip} dev wlp7s0"
        ip_assign = os.popen(cmd).read()
        print(os.popen("ip -4 a show wlp7s0").read())
    elif choice == 2:
        ip = input("Enter the ip address to assign :")
        cmd = f"sudo ip address add {ip} dev enp14s0"
        ip_assign = os.popen(cmd).read()
        print(os.popen("ip -4 a show enp14s0").read())

def Delete_IP_address():
    menu_interface()
    choice = int(input("Enter your choice : "))
    if choice == 1:
        ip = input("Enter the ip address to delete :")
        cmd =f"sudo ip address add {ip} dev wlp7s0"
        ip_assign = os.popen(cmd).read()
        print(os.popen("ip -4 a show wlp7s0").read())
    elif choice == 2:
        ip = input("Enter the ip address to delete :")
        cmd = f"sudo ip address add {ip} dev enp14s0"
        ip_assign = os.popen(cmd).read()
        print(os.popen("ip -4 a show enp14s0").read())

def Display_IP_address():
    menu_interface()
    ch = int(input("Enter the choice"))
    if ch == 1:
        print(os.popen("ip -4 a show wlp7s0").read())
    elif ch == 2:
        print(os.popen("ip -4 a show enp14s0").read())

def Display_all_interfaces():
    print(os.popen("ip l").read())

def Configure_routing():
    menu_interface()
    choice = int(input("Enter your choice : "))
    if choice == 1:
        ip = input("Enter the ip address to delete :")
        cmd =f"sudo ip r add 10.2.3.0/24 via {ip} dev wlp7s0"
        ip_assign = os.popen(cmd).read()
        print(os.popen("ip r").read())
    elif choice == 2:
        ip = input("Enter the ip address to delete :")
        cmd = f"sudo ip r add 20.2.3.0/26 via {ip} dev enp14s0"
        ip_assign = os.popen(cmd).read()
        print(os.popen("ip r").read())

def Turn_OnOff_interface():
    while True:
        print("1.Turn on interface")
        print("2.Turn off interface")
        print("3.exit")
        ch = int(input("Enter the choice"))
        if ch == 1:
            cmd = "sudo ip link set dev wlp7s0 un"
            on = os.popen(cmd).read()
            print(os.popen("ip a").read())
        elif ch == 2:
            cmd = "sudo ip link set dev wlp7s0 down"
            off = os.popen(cmd).read()
            print(os.popen("ip a").read())
        else:
            break

def Add_ARP_entry():
    cmd = "sudo ip n add 192.168.1.10 lladdr 00:45:78:52:ed:55 dev wlp7s0 nud permanent"
    arp = os.popen(cmd).read()
    print(os.popen("ip n show").read())

def Delete_ARP_Entry():
    cmd = "sudo ip n flush 192.168.1.10 dev wlp7s0 nud permanent"
    arp = os.popen(cmd).read()
    print(os.popen("ip n show").read())

def Restart_Network():
    cmd = "sudo systemctl status networking"
    print(os.popen(cmd).read())

def Change_hostname():
    cmd = "sudo hostname sachin"
    change_host = os.popen(cmd).read()
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
