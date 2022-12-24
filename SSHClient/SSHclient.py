import socket
import ssl
import argparse

class Client:
    def __init__(self):
        self.ssl_ctx = None
        arg_parser = argparse.ArgumentParser(
            description="--domian server_domain  --port server_port")
        arg_parser.add_argument('--domain')
        arg_parser.add_argument('--port')
        args=arg_parser.parse_args()

        self.domain = args.domain
        self.port = args.port
        if self.port is None or self.domain is None :
            print("Usage: --domain server_domain  --port server_port")
            exit(-1)
        else:
            if self.domain is not None:
                self.ip = socket.gethostbyname(self.domain)
        self.address = (self.ip, int(self.port))


    def create_ssl_context(self,  private_key_file, host_cert_file,CA_cert_file,):
        ctx = ssl.SSLContext(ssl.PROTOCOL_TLS)
        ctx.check_hostname = False
        ctx.load_cert_chain(host_cert_file, private_key_file)
        ctx.load_verify_locations(CA_cert_file)
        ctx.verify_mode = ssl.CERT_REQUIRED
        self.ssl_ctx = ctx

    def start(self):
        sock = socket.socket()
        ssl_socket=self.ssl_ctx.wrap_socket(sock, False)
        ssl_socket.connect(self.address)
        try:
            while True:
                print("ssh>", end="")
                command = input()
                command=command.strip()
                if command == "ls" or command=="pwd" :
                    request=command
                    ssl_socket.send(request.encode("utf-8"))
                    response = ssl_socket.recv(8192).decode("utf-8")
                    print(response)
                elif command == "exit":
                    ssl_socket.send("exit".encode("utf-8"))
                    break
                elif command=="":
                    continue
                else:
                    print("Invalid Command")
        except Exception as e:
            e.with_traceback()
        finally:
            ssl_socket.close()
            sock.close()
if __name__ == "__main__":
    client = Client()
    client.create_ssl_context("client.key","client.crt","ca.crt")
    client.start()
