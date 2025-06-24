# 🔁 DevOps Assignment: Nginx Reverse Proxy + Docker

This project demonstrates a basic **Docker Compose setup** with two backend services and an **Nginx reverse proxy** routing between them.

## 📁 Project Structure
├── docker-compose.yml
├── nginx/
│ ├── nginx.conf
│ └── Dockerfile
├── service_1/
│ ├── app.py
│ └── Dockerfile
├── service_2/
│ ├── app.py
│ └── Dockerfile
-------------------------

## 🚀 How to Run the Project

> 🐳 Make sure Docker & Docker Compose are installed

1️⃣ Clone the repo

```bash
git clone https://github.com/your-username/your-repo-name.git
cd your-repo-name

2️⃣ Run with Docker Compose
bash
Copy
Edit
docker compose up --build
This command builds all services and starts the system.

Access the Services
Once running, go to:

✅ http://localhost:8080/service1 → Returns {"service": "service1"}

✅ http://localhost:8080/service2 → Returns {"service": "service2"}

⚙️ Routing via Nginx
Nginx is used as a reverse proxy:
/service1 routes to Flask service 1 (port 5001)
/service2 routes to Flask service 2 (port 5002)
Logs are enabled in custom format with timestamp and path.

✅ Bonus Features
Clean reverse proxy routing
JSON response per service
Healthchecks (optional — add in docker-compose)

📽️ Demo
https://www.loom.com/share/732e554643574157a79bb5e9c489f4c5?sid=17c63a5b-6935-4f71-94bc-112b3cfd9262


