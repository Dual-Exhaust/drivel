# drivel
A command line tool for Google Drive use in Linux.

Written in python 3.7.x
Requires consent of the user to use the app; external link needs to be followed to connect to Google Drive; May have to set up Google API credentials and download the credentials.json in order to use but I'm not sure yet.

I use WSL so following the link was no problem but I am not sure for how to follow the link if you are in a full Linux setup. Might have to just make sure the user has setup a browser beforehand.

# Commands

### drlist

Lists the files or folders in your drive. Currently will only list in the outer most directory. Defaults to the ten most recent items but you can also specify the number of items to display.

> Usage: drlist <optional number>
  
  
### drget

Downloads a file. You pass it the name of the file and if it exists it will download it in the current directory.

> Usage: drget <file name>
