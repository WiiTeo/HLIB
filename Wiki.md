What is an HLIB file ?
An HLIB File is a Library for HCMD.

How to create an HLIB file ?
Thats very simple !

First, go to filesystem/ folder, and go to lib/ folder

Create a file named "mylib_lib.hlib" (this is an example name)

Open the file with a text editor

Write the example :

elif userType == "mylib":
    print("You use MyLib in your HCMD Lib folder")
And save.

Now open HCMD

Type the command : "hlib_install"

Now type the name of your hlib file (for example i choice mylib_lib.hlib)

And restart HCMD

Now your Lib is installed !

Type (for example) "mylib"

And "You use MyLib in your HCMD Lib Folder" appear !
