Download GroupMe Messages
=============

This is a tool to download GroupMe messages to a CSV file and display simple stats about those messages.

Example usage:
- Number of messages by each user
- Number of favorited messages
- Number of times a user spews profanity
- Average length of a user's message
- Number of times a user says "lol"

As well, there is now Image support! Run get_pic.py afterward to download the images to your local directory. Note: Zip Compression is not supported yet, so hold off of that for a little bit.


Getting Access Token
--------------
In order to download GroupMe messages, you need an unique access token provided to you by GroupMe. To get this, log into GroupMe's <a href="https://dev.groupme.com" target="_blank">Developers</a> website and create a sample Application. You should then be given a 32-bit access token.

Dependencies
--------------
You need to install Python's <a href="http://docs.python-requests.org/en/latest/" target="_blank">request</a> library: ```pip install request```

retrieve_msgs.py now works on Python 3.4, but run_stats.py does not as of yet.

Instructions
--------------
1. Get your GroupMe Access Token using the instructions above.
2. Run ```retrieve_msgs.py```, pass in your access token, and follow the command line interface to download your GroupMe messages to a CSV file.
3. Run ```run_stats.py``` and pass in your CSV file to display some simple stats about your messages.
4. Run ```get_pic.py``` to obtain all images in your group.