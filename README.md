# sms-sender
sms maximum length is 160; a longer message is broken down into chunks of at least 160 characters 


A company has hired you as a consultant to develop software that can be used for sending SMS to their end-users. Currently, the maximum number of characters possible for one message is 160. Some of the messages the company sends contain more than 160 characters and need to be broken up into smaller chunks.

The company has expressed concerns that when sending messages in different chunks there is no guarantee that the messages will be delivered to the end-user’s phone in order. To circumvent this problem, the company would like to add pagination to the end of the message to give proper context to the end-user if needed. 

As an example, the following message has 212 characters:
As a reminder, you have an appointment with Dr. Smith tomorrow at 3:30 pm. If you are unable to make this appointment, please call our customer service line at least 1 hour before your scheduled appointment time.

The message should be sent in two chunks as such:
* As a reminder, you have an appointment with Dr. Smith tomorrow at 3:30 pm. If you are unable to make this appointment, please call our customer service  (1/2)

and

* line at least 1 hour before your scheduled appointment time. (2/2)

Your task is to develop a function that takes in a string message and returns an array of string messages with pagination if needed. For this exercise, the maximum number of characters in the input message is 1440. Also, do not break words into syllables and hyphens.

