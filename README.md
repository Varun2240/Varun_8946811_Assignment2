
# Advance Containers Assignment - Web Application with PostgreSQL

This project contains a simple web application with a PostgreSQL database, implemented using Docker and Docker Compose. The application exposes an API to create and fetch user data. 



## Project Structure

- `app.py`: The Flask web application.
- `docker-compose.yml`: The Docker Compose configuration to orchestrate the web and database containers.
- `Dockerfile`: The Dockerfile to build the Flask application container.
- `init_db.sql`: SQL file to initialize the database with a `staff` table.
- `requirements.txt`: List of dependencies for the Python application (Flask, psycopg2).
- `logs/`: Directory to store application logs via bind mount.

## Setup and Configuration

1. **Clone the repository:**
   ```bash
   git clone https://github.com/your-repository/advance-containers.git
   cd advance-containers
   ```

2. **Build the containers:**
   Use Docker Compose to build the containers for both the web application and the PostgreSQL database:
   ```bash
   docker-compose build
   ```

3. **Start the containers:**
   Start the application and database containers using Docker Compose:
   ```bash
   docker-compose up
   ```

   This will start the web application on port 5000 and the PostgreSQL database.

## API Endpoints

1. **POST /staff**: Create a new staff member.
   - **Request body**:
     ```json
     {
       "first_name": " Varun",
       "last_name": "Gundemoni"
     }
     ```
   - **Response**:
     ```json
     {
       "id": 1
     }
     ```

2. **GET /staff/{id}**: Fetch a staff member by ID.
   - **Example request**: `/staff/1`
   - **Response**:
     ```json
     {
       "id": 1,
       "first_name": "John",
       "last_name": "Doe"
     }
     ```


## Logging

The application logs are saved in the `logs/` directory on the host machine, using a bind mount. This allows you to access the logs from your local system.

## Stopping the Containers

To stop the running containers, use the following command:
```bash
docker-compose down
```

This will stop the containers and remove them. If you want to remove the volumes as well, add the `-v` flag:
```bash
docker-compose down -v
```

## Sample Data

You can add sample data by sending a POST request to the `/staff` endpoint:
```bash
curl -X POST -H "Content-Type: application/json" -d '{"first_name": "John", "last_name": "Doe"}' http://localhost:5000/staff
```

To fetch a staff member by ID:
```bash
curl http://localhost:5000/staff/1
```

## Troubleshooting

- If the web application cannot connect to the database, check the database logs to ensure it's running and the credentials are correct.
- Ensure that all containers are up and running by checking the logs with:
  ```bash
  docker-compose logs
  ```

## Conclusion

This project demonstrates the use of Docker and Docker Compose to containerize a Flask web application with a PostgreSQL database. The application is scalable, secure, and designed to persist data across container restarts using volumes and bind mounts.

---

**Note**: If you need additional features, like load balancing and scaling, make sure to add a reverse proxy (Nginx/HAProxy) and adjust the `docker-compose.yml` file to replicate the `web` service.
