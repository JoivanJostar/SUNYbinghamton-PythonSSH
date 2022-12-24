import Util
import ssl
import socket
import  argparse

class Server:
    def __init__(self):
        self.ssl_ctx = None
        self.utility = Util.utility()
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
        purpose = ssl.Purpose.CLIENT_AUTH
        ctx = ssl.create_default_context(purpose)
        ctx.load_cert_chain(host_cert_file, private_key_file)
        ctx.load_verify_locations(CA_cert_file)
        ctx.verify_mode = ssl.CERT_REQUIRED
        self.ssl_ctx = ctx

    def service_loop(self):
        listen_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0)
        ssl_socket = self.ssl_ctx.wrap_socket(listen_socket, True)
        ssl_socket.bind(self.address)
        print("bind the address " + self.ip + ": " + self.port)
        print("wait for connection")
        ssl_socket.listen(5)
        while True:
            connection, client_address = ssl_socket.accept()
            print(f"A connection has been established.The client address is  {client_address}")
            try:
                self.handle_connection(connection, client_address)
            except Exception as e:
                e.with_traceback()
            finally:
                connection.close()

    def handle_connection(self, connection, client_address):
        while True:
            str_command = connection.recv(100).decode("utf-8")
            if str_command == "ls":
                response = self.utility.str_readPWD(5)
            elif str_command == "pwd":
                response = self.utility.getPWD()
            elif str_command == "exit":
                break
            else:
                print("Unexcepted command " + str_command)
            connection.send(response.encode("utf-8"))

if __name__ == "__main__":
    server = Server()
    server.create_ssl_context("server.key","server.crt","ca.crt")
    server.service_loop()
