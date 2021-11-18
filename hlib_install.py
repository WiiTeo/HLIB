import os
import sys

# This is a part of HCMD, this is the HLIB_INSTALL part.
# (C) 2021 WiiTeo

libtoinstall = input("Name of HLIB to Install : ")
os.chdir("lib")
if os.path.isfile(libtoinstall):
  print(libtoinstall + " found !")
  hlib = open(libtoinstall, 'r')
  os.chdir("../../")
  hcmd_py = open("hcmd.py", "a")
  for hlib_line in hlib:
    hcmd_py.write("\n\n            " + hlib_line)
  hcmd_py.close()
  hlib.close()
  print("HCMD require to restart to active the new library.")
  exit_with_code("1")
else:
  print("Error ! The Lib file is not in the lib dir (H:/lib/)")
  os.chdir("../")
  
# END
