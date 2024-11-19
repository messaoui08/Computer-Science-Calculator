def calculate_ip_details(ip, subnet_mask):
    ip_parts = list(map(int, ip.split('.')))
    mask_parts = list(map(int, subnet_mask.split('.')))
    
    network_address = [ip_parts[i] & mask_parts[i] for i in range(4)]
    broadcast_address = [network_address[i] | (~mask_parts[i] & 255) for i in range(4)]
    
    total_hosts = (2 ** (32 - sum(bin(x).count('1') for x in mask_parts))) - 2
    available_hosts = total_hosts

    return {
        'Network Address': '.'.join(map(str, network_address)),
        'Broadcast Address': '.'.join(map(str, broadcast_address)),
        'Total Hosts': total_hosts,
        'Available Hosts': available_hosts
    }