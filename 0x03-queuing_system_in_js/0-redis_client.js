import redis from 'redis';

// Create a Redis client instance
const client = redis.createClient();

// Example usage: set and get a key
client.set('key', 'value', redis.print);
client.get('key', (err, reply) => {
  console.log('Value:', reply);
});

// Handle errors
client.on('error', (err) => {
  console.error('Redis client error:', err);
});
