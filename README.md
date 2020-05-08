# raspberry-pi-docker

This project builds a Docker container that includes a base UNIX image, Raspberry Pi Camera software driver and a Python program that takes images in an infinite loop.

Launch the container with this "docker run", which exposes the camera device to the container.  The container takes still images every N seconds, writes them to a container mount, which is exposed externally to a mount point you choose.

docker run --privileged --device=/dev/vchiq -v /home/pi/ml_image:/ml_image -ti image_capture

The purpose of this program is to feed into an Amazon SageMaker machine learning pipeline.  Initially, these images can be used to create a first set of Amazon SageMaker Ground Truth training job, to create labelled data.

Ultimately, this container should be registered in Amazon ECR so it can be deployed to the device through Amazon IoT and Greengrass software.  Operated through IoT, the system is able to continuously capture images, produce inference at edge through another inference container (project coming).  A narrow stream of important moments are fed to the AWS cloud for action.
