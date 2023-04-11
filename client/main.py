from setup import Setup
from image_convert import SendImages
from image_sort import SortImages
import datetime
import time


if __name__ == "__main__":

    # set the target time here (testing purposes 1 minute from current time)
    now = datetime.datetime.now()
    target_time = now + datetime.timedelta(minutes=1)

    # Set the target time to a fixed time
    #target_time = datetime.time(hour=23, minute=00)

    while True:
        now = datetime.datetime.now()
        if now >= target_time:
            print("Target time reached!")
            # The images are sent to the server and an index for the class is returned as response
            Setup.index_list = (SendImages.send_string_to_api(
                SendImages.image_convert(Setup.files, Setup.input_dir)))

            # Based on the response the images are then sorted
            SortImages.sort(Setup.files, Setup.input_dir,
                            Setup.output_dir, Setup.index_list, Setup.folders)
            break
        else:
            print("Current time is:", now)
            print("Target time is:", target_time)
            time.sleep(60)  # wait for 60 seconds before checking again
