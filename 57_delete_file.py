
# delete file

import os
 
#  give correct file location here
if os.path.exists("data.txt"):
    os.remove("data.txt")
    # remove folder => os.rmdir("folder name")
else:
    print("File Not Found")