import socket
import threading
import tkinter as tk

from vidstream import *

# Use your own IP address
local_ip_address = "192.168.0.7"

# Define ports for different streams
camera_port = 1111
audio_port = 3333

# Create instances for streaming server and audio receiver
server = StreamingServer(local_ip_address, 9999)
receiver = AudioReceiver(local_ip_address, 8888)

# Function to start listening for incoming streams
def start_listening():
    t1 = threading.Thread(target=server.start_server)
    t2 = threading.Thread(target=receiver.start_server)
    t1.start()
    t2.start()

# Function to start camera stream
def start_camera_stream():
    camera_client = CameraClient(text_target_ip.get(1.0,'end-1c'), camera_port)
    t3 = threading.Thread(target=camera_client.start_stream)
    t3.start()

# Function to start screen sharing
def start_screen_sharing():
    screen_client = ScreenShareClient(text_target_ip.get(1.0,'end-1c'), camera_port)
    t4 = threading.Thread(target=screen_client.start_stream)
    t4.start()

# Function to start audio stream
def start_audio_stream():
    audio_sender = AudioSender(text_target_ip.get(1.0,'end-1c'), audio_port)
    t5 = threading.Thread(target=audio_sender.start_stream)
    t5.start()

# GUI setup
window = tk.Tk()
window.title("Reinaldo call v0.0.1 Alpha")
window.geometry("640x480")

label_target_ip = tk.Label(window, text="Target IP:")
label_target_ip.pack()

text_target_ip = tk.Text(window, height=1)
text_target_ip.pack()

btn_listen = tk.Button(window, text="Start Listening", width=50, command=start_listening)
btn_listen.pack(anchor=tk.CENTER, expand=True)

btn_camera = tk.Button(window, text="Start Camera Stream", width=50, command=start_camera_stream)
btn_camera.pack(anchor=tk.CENTER, expand=True)

btn_screen = tk.Button(window, text="Start Screen Share", width=50, command=start_screen_sharing)
btn_screen.pack(anchor=tk.CENTER, expand=True)

btn_audio = tk.Button(window, text="Start Audio Stream", width=50, command=start_audio_stream)
btn_audio.pack(anchor=tk.CENTER, expand=True)

window.mainloop()
