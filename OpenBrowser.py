import os
import sys
import webbrowser
import configparser
import time

def get_executable_dir():
    return os.path.dirname(os.path.abspath(sys.argv[0]))

# Config file path
config_file = os.path.join(get_executable_dir(), 'config.ini')
config = configparser.ConfigParser()
config.read(config_file)
url = config['Settings'].get('URL', 'http://example.com')  # Default URL
sleep_time = config['Settings'].getint('Waittime', 5)  # Default wait time
time.sleep(sleep_time)
webbrowser.open(url)
