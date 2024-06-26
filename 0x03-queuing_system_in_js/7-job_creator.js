import kue from 'kue';

const queue = kue.createQueue();

const jobs = [
  // Array of job data
];

jobs.forEach((jobData) => {
  const job = queue.create('push_notification_code_2', jobData).save((err) => {
    if (!err) console.log(`Notification job created: ${job.id}`);
  });

  job.on('complete', () => {
    console.log(`Notification job ${job.id} completed`);
  }).on('failed', (err) => {
    console.log(`Notification job ${job.id} failed: ${err}`);
  }).on('progress', (progress) => {
    console.log(`Notification job ${job.id} ${progress}% complete`);
  });
});
