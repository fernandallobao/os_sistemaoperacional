# importando bibliotecas
import os
import platform
import psutil
import socket

# informações do sistema
print(f"\nSistema Operacional: {platform.system()} {platform.release()}.") # nome do so
print(f"Nome do usuário: {os.environ.get('USERNAME')}.") # usuário ativo do pc
print(f"IPv4: {socket.gethostbyname(socket.gethostname())}") # endereço de IPv4 do pc

# coletando informações sobre TCP e UDP
print("Portas abertas:\n")
connectall = psutil.net_connections(kind='inet')
only_udp = [conn for conn in psutil.net_connections(kind='inet') if conn.type == socket.SOCK_DGRAM]

# Separando informações sobre portas
only_tcp_listening_ports = [conn.laddr.port for conn in connectall if conn.status == psutil.CONN_LISTEN] # TCP
only_udp_listening_ports = [conn.laddr.port for conn in only_udp] # UDP

# removendo portas repetidas da lista
only_tcp_listening_ports = list(set(only_tcp_listening_ports))
only_udp_listening_ports = list(set(only_udp_listening_ports))

# organizando as portas da menor para a maior
only_tcp_listening_ports.sort()
only_udp_listening_ports.sort()

# Mostrando apenas portas TCP
print("TCP:\n")
for port in only_tcp_listening_ports:
    print(f"TCP port = {port} Open")

#Mostrando apenas portas UDP
print("\nUDP:\n")
for port in only_udp_listening_ports:
    print(f"UDP port = {port} Open")

print("\n")