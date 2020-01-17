This is a project for deploying a  crawler to cloud, it shall be decomposed as

- have an access to the remote linux server
- packup the code and depenpies inside a container
- upload container to remote server and run test
- moniter the data collection preprocess and debugging

Then tasks can be solved as the following way and working flow.

* Connect to the remote linux server with a secure remote desktop protocol
[Origianl tutorial for connection to server](https://phoenixnap.com/kb/ssh-to-connect-to-remote-server-linux-or-windows)
	* Prerequisites
		>1.The remote computer must be turned on at all times and have a network connection.
		>2.The client and server applications need to be installed and enabled.
		>3.You need the IP address or the name of the remote machine you want to connect to.
		>4.You need to have the necessary permissions to access the remote computer.
		>5.Firewall settings need to allow the remote connection.
	* Notes
		1. What is SSH?
			> Secure Shell, sometimes referred to as Secure Socket Shell, 
			is a protocol which allows you to connect securely to a remote 
			computer or a server by using a text-based interface.
		2. What SSH enable?
			> When a secure SSH connection is established, a shell session 
			will be started, and you will be able to manipulate the server
			by typing commands within the client on your local computer.
		3. How Does SSH Work?
			> Two compents will be needed,a client and the corresponding server-side component
			for SSH client, it is an application installed locally.Other than that,remote host
			information shall be required to initiate the connection
			While on the server side, a SSH daemon is constanly listening to a TCP/IP port for \
			possible client request connection. When a connection is initiated from client side,
			SSH daemon will respond with the software and the protocol versions it supports and
			the two will exchange their identification data.If the provided credentials are correct, 
			SSH creates a new session for the appropriate environment.
		4. How to Enable an SSH Connection
			> Install both a client and remote server side SSH compents.
			An open source SSH tool—widely used for Linux distributions— is OpenSSH. Installing 
			OpenSSH is relatively easy. It requires access to the terminal on the server and 
			the computer that you use for connecting
		5. How to Install an OpenSSH Client
			>Before you proceed with installing an SSH client, make sure it is not already installed.
			Many Linux distributions already have an SSH client. For Windows machines, 
			you can install PuTTY or any other client of your choice to gain access to a server.
			To check if the client is available on your Linux-based system, you will need to:
				* Load an SSH terminal. You can either search for “terminal” or press CTRL + ALT + T on your keyboard.
				* Type in ssh and press Enter in the terminal.
				* If the client is installed, you will receive a response that looks like this:
					`[user@hostname [command]` 
				or install it with 
					`sudo apt-get install openssh-client`
		6. How to Install an OpenSSH Server			
			 > provided that you have the necessary privileges to gain access,
			 as well as the hostname or IP address.
			 > In order to accept SSH connections, a machine needs to have the 
			 server-side part of the SSH software toolkit.
			 > If you first want to check if OpenSSH server is available on the 
			 Ubuntu system of the remote computer that needs to accept SSH connections, 
			 you can try to connect to the local host:
				* Open the terminal on the server machine. You can either search for “terminal” 
				* Type in ssh localhost and hit enter.
				* For the systems without the SSH server installed the response will look similar to this:
					```
					username@host:~$ ssh localhost
					ssh: connect to host localhost port 22: Connection refused username@host:~$
					```
			If the above is the case, you will need to install the OpenSSH server. Leave the terminal open and:
				1. Run the following command to install the SSH server:
				2. `sudo apt-get install openssh-server ii.`
				3. Type in your superuser password when asked.
				4. Enter and Y to allow the installation to continue after the disk space prompt.
				5. Check status with `sudo service ssh status'
		7. How to Connect via SSH
			> Now that you have the OpenSSH client and server installed on every machine you need,
			you can establish a secure remote connection with your servers. To do so:
				1. Open the SSH terminal on your machine and run the following command
					`ssh your_username@host_ip_address`
				2. If the username on your local machine matches the one on the server 
				you are trying to connect to, you can just type:
					ssh host_ip_address`
				3. Type in your password and hit Enter. Note that you will not get any feedback on the screen while typing. 
				If you are pasting your password, make sure it is stored safely and not in a text file.
				4. When you are connecting to a server for the very first time, 
				it will ask you if you want to continue connecting. Just type yes and hit Enter. 
				This message appears only this time since the remote server 
				is not identified on your local machine.
				5. An ECDSA key fingerprint is now added and you are connected to the remote server.
				
				Here is the example of a connection request using the OpenSSH client. We will specify the port number as well:
				```
					username@machine:~$ ssh phoenixnap@185.52.53.222 –p7654 phoenixnap@185.52.53.222’s password:
					The authenticity of host '185.52.53.222 (185.52.53.222)' can't be established. 
					ECDSA key fingerprint is SHA256:9lyrpzo5Yo1EQAS2QeHy9xKceHFH8F8W6kp7EX2O3Ps.
					Are you sure you want to continue connecting (yes/no)? yes
					Warning: Permanently added ' 185.52.53.222' (ECDSA) to the list of known hosts. 
					username@host:~$
				```
				You are now able to manage and control a remote machine using your terminal. 
				If you have trouble connecting to a remote server, make sure that:
				* The IP address of the remote machine is correct.
				* The port SSH daemon is listening to is not blocked by a firewall or forwarded incorrectly.
				* Your username and password are correct.
				* The SSH software is installed properly.
				
	*Windows
	
	*Linux



  
