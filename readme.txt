########################################
## Dropbox Archive and Backup Utility ##
##### Writen by: Paul Rachwalski #######
###### Nov. 20, 2013 Python 2.x ########
########################################

1.) What is it? 

This program is designed to take a given directory, compress it into a .zip file, and upload the compressed file to a Dropbox account for backup purposes.

2. ) How do I set it up?

	To run the program, the user must first have the Dropbox Python API installed. If it is not installed, on a unix system, enter the terminal, and type:
> pip install dropbox
	
	Once it is installed, the user can then authorize their account. To do this, run the program, and when the prompt appears asking for a directory, enter
> -auth
and follow the instructions on the screen. It will give the user a URL to go to, and when the user signs in on dropbox.com and opens the given URL, it will give the user an access token. The user then copies the token into the program's prompt, and the program will save the token as a file called token.p in order to ensure the user does not have to reauthorize their account each use. 
NOTE: If the user moves the python file for this program without moving the token.p file with it, the user will have to reauthorize the account.
	After authorization, the program will exit automatically and then the user will have to start it again. This time, the user will enter which directory to use, and give it a name, and the computer will take it from there. 

Enjoy and feel free to modify!
