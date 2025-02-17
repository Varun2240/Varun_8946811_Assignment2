
# Advanced Containers Assignment (15%)

## Author: Varun Gundemoni  
## Repository: [Varun_8946811_Assignment2](https://github.com/Varun2240/Varun_8946811_Assignment2.git)

---

## Overview
This project is a containerized web application that serves an API for staff management using Flask and PostgreSQL. The system is designed with Docker and Docker Compose, ensuring scalability, security, and proper container orchestration.

## Project Structure

```
docker_assignment2/
│-- app.py                   # Flask API implementation
│-- Dockerfile               # Docker image setup for the web application
│-- docker-compose.yml       # Configuration to run multiple containers
│-- requirements.txt         # Python dependencies
│-- init_db.sql              # Database initialization script
│-- logs/                    # Logs directory (bind mount)
│-- README.md                # Documentation
```

---

## Technologies Used

- **Backend:** Python (Flask)
- **Database:** PostgreSQL (containerized)
- **Containerization:** Docker & Docker Compose
- **Networking:** Docker Network for inter-container communication
- **Logging:** Bind Mounts to store logs on the host machine

---

## Setup & Installation

### Prerequisites

Ensure you have the following installed:

- [Docker](https://docs.docker.com/get-docker/)
- [Docker Compose](https://docs.docker.com/compose/install/)

### Steps to Run the Project

1. **Clone the Repository**
   ```sh
   git clone https://github.com/Varun2240/Varun_8946811_Assignment2.git
   cd Varun_8946811_Assignment2
   ```

2. **Start the Containers**
   ```sh
   docker-compose up -d --build
   ```

3. **Verify Running Containers**
   ```sh
   docker ps
   ```

4. **Check Logs**
   ```sh
   docker logs <container_name>
   ```

5. **Access the API**
   - Open your browser or use **curl** / Postman
   - **Base URL:** `http://localhost:5000`
   - **Endpoints:**
     - `GET /staff/<id>` - Retrieve staff data
     - `POST /staff` - Create new staff

---

## API Usage

### 1. Create a Staff Member
```sh
curl -X POST http://localhost:5000/staff      -H "Content-Type: application/json"      -d '{"first_name": "Varun", "last_name": "Gundemoni"}'
```

### 2. Get Staff Details
```sh
curl -X GET http://localhost:5000/staff/1
```

---

## Scaling & Load Balancing (Bonus)

To scale the web application and balance the load, run:
```sh
docker-compose up --scale web=3 -d
```

For load balancing, configure **Nginx** or **HAProxy** as a reverse proxy (Optional).

---

## Security Best Practices Implemented
  
 **Secrets Management** - Environment variables used for credentials  
 **Data Persistence** - Docker Volumes ensure database persistence  
 **Minimal Image Size** - Using Python Slim base image  

---

## Stopping & Cleaning Up

To stop the running containers:
```sh
docker-compose down
```

To remove volumes & networks:
```sh
docker-compose down --volumes --remove-orphans
```

---

## Conclusion

This project successfully implements containerization using Docker & Docker Compose, ensuring scalability, security, and efficiency. If you have any questions, feel free to reach out!

