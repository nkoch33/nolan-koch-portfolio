#!/usr/bin/env python3
"""
Simple HTTP server for serving the portfolio website locally.
Run this script and open http://localhost:8000 in your browser.
"""

import http.server
import socketserver
import os
import webbrowser
from pathlib import Path

# Configuration
PORT = 8000
DIRECTORY = Path(__file__).parent

class CustomHTTPRequestHandler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=str(DIRECTORY), **kwargs)
    
    def end_headers(self):
        # Add CORS headers for development
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'GET, POST, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', 'Content-Type')
        super().end_headers()

def main():
    """Start the HTTP server and open the website in browser."""
    
    # Change to the directory containing this script
    os.chdir(DIRECTORY)
    
    # Create server
    with socketserver.TCPServer(("", PORT), CustomHTTPRequestHandler) as httpd:
        print(f"🚀 Portfolio server started!")
        print(f"📁 Serving files from: {DIRECTORY}")
        print(f"🌐 Open your browser and go to: http://localhost:{PORT}")
        print(f"⏹️  Press Ctrl+C to stop the server")
        print("-" * 50)
        
        # Try to open the website automatically
        try:
            webbrowser.open(f'http://localhost:{PORT}')
            print("✅ Browser opened automatically!")
        except:
            print("⚠️  Could not open browser automatically. Please open it manually.")
        
        # Start serving
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print("\n🛑 Server stopped by user.")
            httpd.shutdown()

if __name__ == "__main__":
    main() 