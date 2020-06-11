# windows_pass_pi
Simple script which steals and converts into hash Windows's SYSTEM and SAM files on Python 3             
# INSTALL:               
git clone https://zertmark/windows_pass_pi.git && cd windows_pass_pi && chmod +x windows_pass_pi && apt-get update && apt-get install samdump2               
# RUN:             
python3 windows_password_stealer.py -h               
usage: windows_password_stealer.py [-h] disk         

Windows password stealer              

positional arguments:                   
  disk        Disk with C:\ partition on it               
 
optional arguments:                                     
  -h, --help  show this help message and exit                                    
