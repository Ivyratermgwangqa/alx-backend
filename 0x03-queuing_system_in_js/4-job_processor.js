import kue from 'kue';

const queue = kue.createQueue();

const jobData = {
  phoneNumber: '1234567890',
  message: 'Hello, this is a test message'
};

const job = queue.create('push_notification_code', jobData)
  .save((err) => {
    if (err) {
      console.log('Error creating job:', err);
    } else {
      console.log('Notification job created:', job.id);
    }
  });

job.on('complete', () => {
  console.log('Notification job completed');
}).on('failed', (err) => {
  console.log('Notification job failed:', err);
});

queue.process('push_notification_code', (job, done) => {
  console.log(`Processing job ${job.id}:`, job.data);
  done();
});
