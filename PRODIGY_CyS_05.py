from scapy.all import sniff

def packet_callback(packet):
    # Display the packet summary
    print(f"Packet: {packet.summary()}")
    
    # Extract relevant information
    if packet.haslayer('IP'):
        ip_src = packet['IP'].src
        ip_dst = packet['IP'].dst
        protocol = packet['IP'].proto
        payload = bytes(packet.payload)  # Get the raw payload data
        
        # Print extracted information
        print(f"Source IP: {ip_src}")
        print(f"Destination IP: {ip_dst}")
        print(f"Protocol: {protocol}")
        print(f"Payload: {payload}\n")

def main():
    print("Starting packet sniffer...")
    # Start sniffing packets (adjust the count to limit the number of packets captured)
    sniff(prn=packet_callback, count=10)  # Capture 10 packets

if __name__ == "__main__":
    main()
    