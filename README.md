# FastAPI Sensor Data Application

This is a FastAPI application for managing sensor data, with PostgreSQL as the database backend. The application supports storing sensor readings and retrieving recent sensor data per device.

## Features

* Create and store sensor data (temperature, humidity, timestamp, device ID)
* Retrieve the latest 5 sensor data records for a specific device
* Database connection management with retry logic
* Dockerized app with PostgreSQL database for easy deployment
* Infrastructure deployment using Pulumi scripts (in `/deployment` folder)

## Technologies Used

* FastAPI
* SQLAlchemy
* PostgreSQL
* Pydantic for data validation
* Docker & Docker Compose
* Pulumi for infrastructure as code

## Getting Started

### Prerequisites

* Docker & Docker Compose installed
* Python 3.9+ (if running locally without Docker)
* Pulumi CLI (for deployment automation)

### Running Locally with Docker

1. Clone the repository:

```bash
git clone git@github.com:MagdEldinr/pax-task.git
cd pax-task
```

2. Build and run the app with Docker Compose:

```bash
docker-compose up --build
```

This will start:

* PostgreSQL database on port `5432`
* FastAPI app on port `8000`

### API Endpoints

* `GET /`
  Root endpoint. Returns a welcome message.

* `GET /api/sensor-data`
  Test endpoint. Returns a sample message.

* `POST /api/sensor-data`
  Create a new sensor data record.

  **Example Request Body:**

  ```json
  {
    "device_id": "sensor-001",
    "timestamp": "2024-05-01T12:00:00Z",
    "temperature": 25.5,
    "humidity": 60
  }
  ```

* `GET /api/sensor-data/{device_id}`
  Returns the latest 5 records for a given device ID.

### Database Schema

* **Table:** `sensor_data`

  * `id`: Integer (Primary Key)
  * `device_id`: String
  * `timestamp`: DateTime
  * `temperature`: Float
  * `humidity`: Float

### Deployment Using Pulumi

Infrastructure-as-Code scripts are located in the `/deployment` directory.

To deploy resources (e.g., RDS, EC2, S3):

```bash
cd deployment
pulumi up
```

Ensure you are logged into Pulumi and AWS CLI before running this.

### Environment Variables

Set the following environment variable if running outside of Docker Compose:

```env
DATABASE_URL=postgresql+asyncpg://root:root@localhost:5432/sensordb
```

## Project Structure

```
.
├── controllers/
│   ├── __init__.py
│   └── sensor_data.py
├── dto.py
├── models/
│   └── sensor_data.py
├── db.py
├── main.py
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
└── deployment/
    └── __main.py__
    └── shared.py
    └── rds.py
    └── ec2.py
    └── s3.py
```
