# WebSocket Certification with Nginx

This project demonstrates how to use Nginx to secure WebSocket connections with SSL/TLS certificates. It includes a Python server that serves both HTTP and WebSocket connections, and an Nginx configuration to proxy and secure these connections.

## Components

- **Python Server**: Serves HTTP and WebSocket connections.
- **Nginx**: Acts as a reverse proxy and secures the WebSocket connections with SSL/TLS.
- **Docker Compose**: Manages the services and their dependencies.

## Prerequisites

- Docker
- Docker Compose
- OpenSSL (for generating SSL/TLS certificates)

## Setup

### 1. Generate SSL/TLS Certificates

Generate a self-signed certificate using OpenSSL:

```bash
openssl req -x509 -newkey rsa:4096 -keyout key.pem -out cert.pem -days 365
```

### Run

#### With Docker

##### 2. Build and Run the Services
Use Docker Compose to build and run the services:

```bash
docker-compose up --build
```

This will:

- Build the Python server image and install the required packages.
- Start the Python server and Nginx services.

##### 3. Access the Services
- The Python server will be running on ports 8000 (HTTP) and 8765 (WebSocket).
- Nginx will be accessible on port 8443 and will proxy requests to the Python server.

#### Without Docker

##### 2. Start the Python Server

```bash
python server.py
```

##### 3. Start Nginx

```bash
nginx -c nginx.conf
```



### Notes
- This setup uses self-signed certificates for demonstration purposes. For production use, obtain certificates from a trusted Certificate Authority (CA).
- Ensure that the ports 8000, 8443, and 8765 are not in use by other services on your host machine.