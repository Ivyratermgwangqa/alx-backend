import { createClient } from 'redis';

const client = createClient();

client.on('error', (err) => console.error('Redis client not connected to the server:', err));
client.on('connect', () => {
  console.log('Redis client connected to the server');
  client.set('school', 'Holberton', redis.print);
  client.del('school', (err, reply) => {
    if (err) throw err;
    console.log(reply);
  });
});
