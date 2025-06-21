import http.server
import socketserver
import webbrowser
import os

# Set the port
PORT = 8000

# Change to the directory containing the HTML files
os.chdir(os.path.dirname(os.path.abspath(__file__)))

# Create the server
Handler = http.server.SimpleHTTPRequestHandler
httpd = socketserver.TCPServer(("", PORT), Handler)

print(f"🏴‍☠️ PirateRate Server Starting...")
print(f"📁 Serving files from: {os.getcwd()}")
print(f"🌐 Server running at: http://localhost:{PORT}")
print(f"📄 Main page: http://localhost:{PORT}/index.html")
print(f"🧪 Test page: http://localhost:{PORT}/test.html")
print(f"⏹️  Press Ctrl+C to stop the server")

# Open the browser automatically
webbrowser.open(f'http://localhost:{PORT}/index.html')

try:
    httpd.serve_forever()
except KeyboardInterrupt:
    print(f"\n🛑 Server stopped.")
    httpd.shutdown() 