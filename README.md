# raspberry-pi-docker

This project builds a Docker container that includes a base unix image and Raspberry Pi Camera software drive.

Launch the container with this run, which exposes the camera device to the container.  The container takes small still images every N seconds, writes them to a container mount, which is exposed externally to a mount point you choose.

docker run --privileged --device=/dev/vchiq -v /home/pi/ml_image:/ml_image -ti image_capture
