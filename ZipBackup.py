#!/usr/bin/env python

########################################
## Dropbox Archive and Backup Utility ##
##### Writen by: Paul Rachwalski #######
###### Nov. 20, 2013 Python 2.x ########
########################################


import dropbox, os, pickle, zipfile, time

#Identifies app is registered
app_key = "z6acfynbqy7a6c9"
app_secret = "7bpj9c6ie780xeo"


#Function to write all files in directory to a .zip
def zipdir(path, zip):
    for root, dirs, files in os.walk(path):
        for file in files:
            zip.write(os.path.join(root, file))


#Function to authorize program for first time users
def authorize():
    app_key = "z6acfynbqy7a6c9"
    app_secret = "7bpj9c6ie780xeo"

    #Allows account to use flow from this program
    flow = dropbox.client.DropboxOAuth2FlowNoRedirect(app_key, app_secret)
    authorize_url = flow.start()

    os.system('clear')
    print "Go here to authorize your account: " + authorize_url
    code = raw_input("Enter authorization code: ").strip()
    access_token, user_id = flow.finish(code)
    pickle.dump(access_token, open("token.p", "wb"))
    print "Restart program now"


if __name__ == '__main__':
    os.system('clear')
    print "Enter '-auth' to authorize your account to this program \n"

    folder = raw_input("Directory to backup: ")
    
    #If user enters -auth, authorize the program to their account
    if folder == "-auth":
        authorize() 

    #Begin backup process
    else:
        #Name format is user name + current date + .zip
        name = raw_input("Name for backup: ") 
        date = time.strftime("%m-%d-%y")
        name = name + "_" + date + ".zip"
        
        #Converts directory into .zip file
        zip = zipfile.ZipFile(name, 'w')
        zipdir(folder, zip)
        zip.close()
        
        #Connects to dropbox account
        access_token = pickle.load(open("token.p", "rb"))
        client = dropbox.client.DropboxClient(access_token)
    
        print "Linked account: ", client.account_info(), "\n"
        
        #Reads and uploads file to dropbox account
        f = open(name)
        response = client.put_file('/'+name, f)
        print "uploaded:", response, "\n"
        
        #Deletes created .zip file from system
        os.system("rm " + name)        
