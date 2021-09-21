import os
from rich.console import Console
console = Console()

def menu_interface():
	asd = os.popen("ip -o link show | awk -F': ' '{print $2}'").read()
	console.print("-----------Menu for interface------------")
	print(asd)

def Assign_ip_add():
	menu_interface()
	interface = input("Enter the interface name : ")
	ip = input("Enter the ip address to assign :")
	ip_assign = os.popen(f"sudo ip address add {ip} dev {interface}").read()
	print(os.popen(f"ip -4 a show {interface}").read())

def Delete_ip_add():
	menu_interface()
	interface = input("Enter the interface name : ")
	ip = input("Enter the ip address to delete :")
	ip_assign = os.popen(f"sudo ip address del {ip} dev {interface}").read()
	print(os.popen(f"ip -4 a show {interface}").read())

def Display_ip_add():
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
    
def Turn_On_Off_interface():
	while True:
		console.print("1.Turn on interface",style="bold cyan")
		console.print("2.Turn off interface",style="bold cyan")
		console.print("3.exit",style="bold cyan")
		ch = int(input("Enter the choice"))
		if ch == 1:
			menu_interface()
			interface = input("Enter the interface name : ")
			on = os.popen(f"sudo ip link set dev {interface} up").read()
			print(os.popen("ip a").read())
		elif ch == 2:
			menu_interface()
			interface = input("Enter the interface name : ")
			off = os.popen(f"sudo ip link set dev {interface} down").read()
			print(os.popen("ip a").read())
		else:
			break
            
def Add_arp_entry():
	menu_interface()
	interface = input("Enter the interface name : ")
	ip = input("Enter the ip address :")
	arp = os.popen(f"sudo ip n add {ip} lladdr 00:45:78:52:ed:55 dev {interface} nud permanent").read()
	print(os.popen("ip n show").read())

def Delete_arp_entry():
	menu_interface()
	interface = input("Enter the interface name : ")
	ip = input("Enter the ip address :")
	arp = os.popen(f"sudo ip n del {ip} dev {interface}").read()
	#arp = os.popen(f"sudo ip n flush {ip} dev {interface} nud permanent").read()
	print(os.popen("ip n show").read())

def Restart_network():
	print(os.popen("sudo systemctl status networking").read())

def Change_hostname():
	name = input("Enter the name you want change as host name : ")
	change_host = os.popen(f"sudo hostname {name}").read()
	print(os.popen("hostnamectl status").read())
    
def Add_dns_server_entry():
	os.popen("sudo cat >> /etc/resolv.conf").read()
	print("Successfully added")

def Exit():
	console.print("Successfully Exited",style="bold green")
	exit()
	

def main_menu():
	console.print("\t1.Assign IP address",style="bold blue")
	console.print("\t2.Delete IP address",style="bold blue")
	console.print("\t3.Display IP address",style="bold blue")
	console.print("\t4.Display all interfaces",style="bold blue")
	console.print("\t5.Configure routing",style="bold blue")
	console.print("\t6.Turn On/Off interface",style="bold blue")
	console.print("\t7.Add ARP entry",style="bold blue")
	console.print("\t8.Delete ARP Entry",style="bold blue")
	console.print("\t9.Restart Network",style="bold blue")
	console.print("\t10.Change Hostname",style="bold blue")
	console.print("\t11.Add DNS server entry",style="bold blue")
	console.print("\t12.Exit",style="bold blue")

operations = {
	"1":Assign_ip_add,
	"2":Delete_ip_add,
	"3":Display_ip_add,
	"4":Display_all_interfaces,
	"5":Configure_routing,
	"6":Turn_On_Off_interface,
	"7":Add_arp_entry,
	"8":Delete_arp_entry,
	"9":Restart_network,
	"10":Change_hostname,
	"11":Add_dns_server_entry,
	"12":Exit
}

while True:
	main_menu()
	ch = input("Enter Choice: ")
	operations[ch]()
