import sys
import socket
import pyfiglet


ascii_banner = pyfiglet.figlet_format("Python\nPort Scanner")
print(ascii_banner)

ip = sys.argv[1]
open_ports =[] 

ports = range(1, 65535)


def probe_port(ip, port, result = 1): 
  try: 
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
    sock.settimeout(0.5) 
    r = sock.connect_ex((ip, port))   
    if r == 0: 
      result = r 
    sock.close() 
  except Exception as e: 
    pass 
  return result

#Progress counter
count = 0
percent_complete = 0
total_ports = len(ports)

for port in ports: 
    sys.stdout.flush() 
    response = probe_port(ip, port) 
    if response == 0: 
        print(f'Port found: {port}')
        open_ports.append(port) 

    #Track progress
    count += 1
    percent_complete = 100 * count / total_ports
    if (count % 100) == 0:
      print(f'Percentage complete: {percent_complete} after trying port: {port}')
    

if open_ports: 
  print ("Open Ports are: ") 
  print (sorted(open_ports)) 
else: 
  print ("Looks like no ports are open :(")
