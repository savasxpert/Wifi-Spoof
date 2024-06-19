import subprocess
from scapy.all import ARP, Ether, srp

def get_device_name(mac_address):
    try:
        # Linux tabanlı sistemlerde hostname komutunu kullanarak cihaz adını alır
        result = subprocess.check_output(['arp', '-a']).decode()
        for line in result.splitlines():
            if mac_address in line:
                return line.split(' ')[0]
        return "Bilinmiyor"
    except Exception as e:
        return "Bilinmiyor"
#wifi arayüzünüzü burada belirtin:örnek wlan0
def get_mac_and_distance():
    try:
        result = subprocess.check_output(['iw', 'dev', 'wlan0', 'station', 'dump']).decode()
        mac_addresses = []
        for line in result.splitlines():
            if "Station" in line:
                mac_addresses.append(line.split()[1])
        return mac_addresses
    except Exception as e:
        return []

def scan_network():
    target_ip = "192.168.1.1/24"  # Ağ adresinizi burada belirtin
    arp = ARP(pdst=target_ip)
    ether = Ether(dst="ff:ff:ff:ff:ff:ff")
    packet = ether/arp

    result = srp(packet, timeout=3, verbose=0)[0]

    clients = []
    for sent, received in result:
        clients.append({'ip': received.psrc, 'mac': received.hwsrc})

    return clients

if __name__ == "__main__":
    print("Ağ taraması yapılıyor...")
    devices = scan_network()
    mac_addresses = get_mac_and_distance()

    for device in devices:
        mac_address = device['mac']
        device_name = get_device_name(mac_address)
        distance = "Bilinmiyor"  # Mesafe hesaplama eklenebilir
        print(f"IP Adresi: {device['ip']}, MAC Adresi: {mac_address}, Cihaz Adı: {device_name}, Mesafe: {distance}")
