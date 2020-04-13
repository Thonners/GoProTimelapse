import time
import datetime
import subprocess
from config import target_dir, timestamp_format, gopro_camera_directory, wifictl_path
from goprocam import GoProCamera, constants

def get_battery_level(goProCam):
    """ 
        Gets the battery level as reported by the goPro

        Options are 0-3;
            0: Empty
            1: Low
            2: Med
            3: Full
    """
    # Code to extend the GoProCamera library
    return goProCam.getStatus(constants.Status.Status,
                                       constants.Status.STATUS.BatteryLevel)

def take_timelapse_photo():
    """
        Go through the whole process of taking a photo
            - connect to the relevant wifi (inc disconnect normal wifi)
            - connect to the camera & turn it on
            - take the photo
            - download the image
            - turn the camera off
            - reconnect to teh original wifi
    """
    timestamp = datetime.datetime.now().strftime(timestamp_format)
    print("Taking a photo at: {}".format(timestamp))
    # Connect to the wifi
    connect_gopro_wifi()
    # Connect to the camera
    goproCamera = GoProCamera.GoPro()
    # Take a picture
    image_path = goproCamera.take_photo()
    if image_path == '':
        print("ERROR taking photo.")
    else:
        print('ImagePath = {}'.format(image_path))
        image_path_parts = image_path.split('/')
        image_file_name = image_path_parts[-1]
        target_path = target_dir + '/' + timestamp + ".jpg"
        # Get the image
        goproCamera.downloadMedia(file=image_file_name, folder=gopro_camera_directory, custom_filename=target_path)

        # Check power level
        battery_level = get_battery_level(goproCamera)

        if (battery_level < 1):
            print("WARNING, battery empty!")
        elif (battery_level < 2):
            print("Warning, battery getting low")
        else:
            print("Current battery status: {}".format(battery_level))

    # Turn off the camera
    goproCamera.power_off()

    # Disconnect the wifi, and reconnect to the previous wifi
    disconnect_gopro_wifi()

def connect_gopro_wifi():
    admin_wifi("connect")
    
def disconnect_gopro_wifi():
    admin_wifi("disconnect")
    
def admin_wifi(args):
    print("{}ing gopro wifi".format(args))
    subprocess.call("{} {}".format(wifictl_path,args), shell=True)


if __name__ == "__main__":
    take_timelapse_photo()