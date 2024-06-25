# 0x03. Queuing System in JS

This project demonstrates a queuing system using Redis and Kue in a Node.js environment. It includes various functionalities such as Redis operations, job processing, and seat reservation with an API.

## Table of Contents
- [Requirements](#requirements)
- [Installation](#installation)
- [Usage](#usage)
- [Files](#files)
- [Author](#author)

## Requirements
- Node.js
- npm
- Redis

## Installation
1. **Clone the repository:**
   ```sh
   git clone https://github.com/Ivyratermgwangqa/queuing_system_in_js.git
   cd queuing_system_in_js
   ```

2. **Install dependencies:**
   ```sh
   npm install
   ```

3. **Run Redis server:** Make sure you have Redis installed and running on your machine. You can download and install Redis from [Redis.io](https://redis.io/download).

## Usage
### Start the Servers
- To start the stock management server:
  ```sh
  npm run dev 9-stock.js
  ```

- To start the seat reservation server:
  ```sh
  npm run dev 100-seat.js
  ```

### API Endpoints

#### Stock Management API
- **List all products:**
  ```
  GET /list_products
  ```
- **Get a specific product by ID:**
  ```
  GET /list_products/:itemId
  ```
- **Reserve a product by ID:**
  ```
  GET /reserve_product/:itemId
  ```

#### Seat Reservation API
- **Get available seats:**
  ```
  GET /available_seats
  ```
- **Reserve a seat:**
  ```
  GET /reserve_seat
  ```
- **Process the reservation queue:**
  ```
  GET /process
  ```

## Files
- **`package.json`**: Contains project metadata and dependencies.
- **`.babelrc`**: Configuration file for Babel.
- **`0-redis_client.js`**: Basic Redis client connection.
- **`1-redis_op.js`**: Redis client with basic operations.
- **`2-redis_del.js`**: Redis client with delete operation.
- **`4-redis_advanced_op.js`**: Redis client with advanced operations using hash sets.
- **`5-subscriber.js`**: Redis subscriber.
- **`5-publisher.js`**: Redis publisher.
- **`6-job_creator.js`**: Creates jobs in Kue.
- **`7-job_processor.js`**: Processes jobs in Kue.
- **`8-job.js`**: Module to create push notification jobs.
- **`8-job.test.js`**: Test cases for `8-job.js`.
- **`9-stock.js`**: API server for stock management.
- **`100-seat.js`**: API server for seat reservation.

## Author
- **Your Name**
  - [GitHub](https://github.com/Ivyratermgwangqa)

---
