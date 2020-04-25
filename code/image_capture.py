import datetime as dt
from picamera import PiCamera
from time import sleep
import time
import os

#  initialize camera and seed variables
file_base = 'ml_image/'
file_path = file_base+'capture/'
sleep_time = 20       #seconds
prune_interval = 15   #minutes
prune_age = (24*60*60)    #seconds
image_capture_pixel = 300

camera = PiCamera()
camera.resolution=(image_capture_pixel,image_capture_pixel)
camera.annotate_text_size=10


def prune_image_folder():

  now = time.time()
  cutoff = now - prune_age
 
  for filename in os.listdir(file_path):
    f = str(file_path) + filename
    t = os.stat(f)
    c = t.st_ctime
    
    # delete files if aged or zero bytes 
    if c < cutoff:
      #print ('*** aged ',f)
      os.remove(f)
    else:
      if os.stat(f).st_size == 0:
        #print ('*** zero ',f)
        os.remove(f)

def create_dir(createpath):
  
  if not os.path.exists(createpath):
    os.makedirs(createpath)
  os.chmod (createpath, 0o777)

def main():
  
  # create directory if required at deploy
  create_dir(file_path)
  create_dir(file_base+'result')
  create_dir(file_base+'groundtruth')
  create_dir(file_base+'undefined')
  create_dir(file_base+'capture')

  # initial directory pruning at start
  prune_image_folder()

  # enter perpetual image capture loop 
  while True:
  
   timestamp = str(dt.datetime.now().strftime('%Y%m%d%H%M%S'))
   filename = file_path+timestamp+'.jpg'
   camera.annotate_text = timestamp
   camera.capture(filename)
   os.chmod (filename, 0o775)
   
   if int(time.strftime('%M')) % prune_interval == 0:
     print (time.strftime('%M'),'run prune')
     prune_image_folder()
 
   sleep(sleep_time)


if __name__== "__main__":
  main()
