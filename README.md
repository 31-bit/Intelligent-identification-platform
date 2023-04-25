# Intelligent-identification-platform

The project is to providing a framework which allow user to interact with the vision solution. The outline is shown below:

![Project framework](https://github.com/31-bit/Intelligent-identification-platform/blob/master/Project_structure.png)

**collector:** provide fetch image function, to get the camera image and store it the device temporally **(you may change the temp path here)**
**Sheduler:** The main function of whole project. Taking action by using cronjob in system level. To start up, user have to configure in system terminal, please follow the insturction below.
**CNN:** function module. A well trained model is expected to recogonize whether a image is a car or not, and write it into two dictionary car or non-car. Currently providing two user API for training and predicting.
**S3:** (not contained in this respository) Store image in Web, saving local memory and computing resources. Write in a image, return a URL of the image. And also provide api for frontend to look the Pic by URL.
**database:** store the image information except the image itself, and also model detials.

##


Scheduler module is the main file
setting cronjob in command line by following procedure.

```
*/1 * * * * /bin/date >> /User/time.txt
*/1 * * * * /opt/homebrew/anaconda3/envs/opencv/bin/python3.10 /Users/leonard/PycharmProjects/opencv/Scheduler.py
```
