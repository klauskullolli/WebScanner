import socket


if __name__ == '__main__':
    
    server_addr_port = ("127.0.0.1", 3000)
    # bufferSize = 4096
    try:
        clinet = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
        url = "https://movies123.design/home/"
        clinet.sendto(url.encode("utf-8"), server_addr_port)
        clinet.close()
        
        print("hello")
        
    except :
        print("Client failed to send data")
