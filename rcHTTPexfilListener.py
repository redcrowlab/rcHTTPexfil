import sys
import base64
from http.server import HTTPServer, BaseHTTPRequestHandler

##########################################################
# rcHTTPexfilListener.py - Listens on a specified port 
# receives data on that port over HTTP
# decodes the data (which should be base64) and then
# writes it out to a text file which is named with the 
# date, time, and IP of the originating host.

##########################################################
# Receive the incoming data, decode it, and write it out
class RequestHandler(BaseHTTPRequestHandler):
    def do_POST(self):
        content_length = int(self.headers['Content-Length'])
        encoded_content = self.rfile.read(content_length).decode()
        decoded_content = base64.b64decode(encoded_content).decode()
        
        filename = generate_filename(self.client_address[0])
        write_data_to_file(decoded_content, filename)

        self.send_response(200)  # OK
        self.send_header('Content-type', 'text/plain')
        self.end_headers()
        self.wfile.write(b'Data received successfully.')


##########################################################
# Generate a filename that includes the date/time and
# source IP the file came from.
def generate_filename(ip_address):
    import datetime

    current_time = datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
    filename = f"{current_time}_{ip_address}_surveyData.txt"
    return filename


##########################################################
# Write the decoded data out to a file using the generated
# filename.
def write_data_to_file(data, filename):
    with open(filename, 'w') as file:
        file.write(data)


##########################################################
# Run the server on the specified interface/IP and port.
def run_server(interface, port):
    server_address = (interface, port)
    httpd = HTTPServer(server_address, RequestHandler)
    print(f'Listening on {interface}:{port}')
    httpd.serve_forever()


##########################################################
# MAIN
if __name__ == '__main__':
    if len(sys.argv) < 3:
        print('Usage: python listener.py <interface> <port>')
        sys.exit(1)

    interface = sys.argv[1]
    port = int(sys.argv[2])
    run_server(interface, port)
