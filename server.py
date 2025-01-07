# server.py

import time
import asyncio
import threading

from http.server import SimpleHTTPRequestHandler, HTTPServer

import websockets

############################
# HTTP server for index.html
############################
def start_http_server(port=8000):
    server_address = ('', port)
    httpd = HTTPServer(server_address, SimpleHTTPRequestHandler)
    print(f"Serving HTTP on port {port} (Ctrl+C to stop)...")
    httpd.serve_forever()

###################################
# WebSocket server sending timestamp
###################################
async def time_server(websocket):
    while True:
        # Get the current Linux timestamp
        timestamp = time.time()
        # Send it to the connected client
        await websocket.send(str(timestamp))
        # Wait 1 second before sending the next timestamp
        await asyncio.sleep(1)

async def run_websocket_server(host="localhost", port=8765):
    print(f"Starting WebSocket server on ws://{host}:{port}/ ...")
    async with websockets.serve(time_server, host, port):
        # Keep the WebSocket server running indefinitely
        await asyncio.Future()  # run forever

##########################
# Main entry point
##########################
if __name__ == "__main__":
    # Start the HTTP server in a separate thread
    http_thread = threading.Thread(target=start_http_server, daemon=True)
    http_thread.start()

    # Run the WebSocket server on the main thread
    try:
        asyncio.run(run_websocket_server())
    except KeyboardInterrupt:
        print("Server interrupted and shutting down...")
