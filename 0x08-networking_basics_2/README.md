0x08. Networking basics #1

0. Write a Bash script that configures an Ubuntu server with the below requirements.

Requirements:

localhost resolves to 127.0.0.2
facebook.com resolves to 8.8.8.8.

1. Write a Bash script that displays all active IPv4 IPs on the machine it’s executed on.

2. Write a Bash script that listens on port 98 on localhost.

Terminal 0

Starting my script.

Terminal 1

Connecting to localhost on port 98 using telnet and typing some text.
Terminal 0

Receiving the text on the other side.

For the sake of the exercise, this connection is made entirely within localhost.
This isn’t really exciting as is, but we can use this script across networks as well.Try running it between your local PC and your remote server for fun!

As you can see, this can come in very handy in a multitude of situations. Maybe you’re
debugging socket connection issues, or you’re trying to connect to a software and you are unsure if
the issue is the software or the network, or you’re working on firewall rules… Another tool to add to your debugging toolbox!
