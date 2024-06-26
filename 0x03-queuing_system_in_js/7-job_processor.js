import kue from 'kue';

const queue = kue.createQueue();

function sendNotification(phoneNumber, message, job, done) {
  job.progress(0, 100);
  if (!phoneNumber || !message) {
    return done(new Error('Invalid phone number or message'));
  }

  job.progress(50, 100);
  console.log(`Sending notification to ${phoneNumber}, with message: ${message}`);
  done();
}

queue.process('push_notification_code_2', 2, (job, done) => {
  sendNotification(job.data.phoneNumber, job.data.message, job, done);
});
