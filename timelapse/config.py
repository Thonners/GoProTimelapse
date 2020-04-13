from pathlib import Path
# Settings for the timelapse

# Directory on the GoPro into which it saves the images/videos (full path managed by GoProCamera package, e.g.: <gopro IP>/videos/DCIM/gopro_camera_directory)
gopro_camera_directory = '100GOPRO'

# Directory into which to save the photos (no trailing /)
target_dir = '{}/coding/gopro/data/output_files'.format(Path.home())

# String format for the time/date format
timestamp_format = '%Y-%m-%d_%H%M'

# Path to the script that will admin the wifi
wifictl_path = '{}/coding/gopro/bash/wifictl'.format(Path.home())