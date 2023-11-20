import datetime
import os, re
import csv
from pathlib import Path
from gradio import utils
from gradio.flagging import FlaggingCallback
import logging
import yaml
import shutil

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s|%(levelname)s|%(pathname)s|%(funcName)s|%(lineno)d|[msg:%(message)s]',
    datefmt='%Y%m%d %H:%M:%S',
    filemode='a+',
)

logger = logging.getLogger(__name__)
current_timestamp = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%s')

def strip_invalid_filename_characters(filename):
    return re.sub(r'[\\/:*?"<>|]', '', filename)


class ResultLogger(FlaggingCallback):
    def __init__(self, folder_path):
        self.folder_path = folder_path

    def setup(self, components, flagging_dir):
        self.components = components
        self.flagging_dir = flagging_dir
        os.makedirs(flagging_dir, exist_ok=True)
        self.log_filepath = Path(flagging_dir) / f"log_{current_timestamp}.csv"


    def flag(self, flag_data, flag_option="", username=None):
        # ... [previous setup code] ...
        csv_data = []
        image_data = []
        logging.info("flag data is %s" % flag_data)
        logging.info("length of flag data is %s" % flag_data)
        flagged_data = flag_data
        logging.info("components are %s" % self.components)
        logging.info("length of components is %s" % len(self.components))
        logging.info("length of flagged_data is %s" % len(flagged_data))

        image_folder_path = Path(self.flagging_dir) / f"GeneratedImages_{current_timestamp}"
        os.makedirs(image_folder_path, exist_ok=True)
        image_paths = []

        gallery_data = flag_data[-1]
        logging.info("Gallery_data %s" % gallery_data)
        image_counter = 0
        for img_info in gallery_data:
            if 'image' in img_info and 'path' in img_info['image']:
                temp_image_path = img_info['image']['path']
                if temp_image_path and os.path.exists(temp_image_path):
                    new_image_name = f"image_{image_counter}{Path(temp_image_path).suffix}"
                    new_image_path = image_folder_path / new_image_name
                    shutil.move(temp_image_path, new_image_path)
                    image_paths.append(str(new_image_path))
                    image_counter += 1

        logging.info("Image_paths: %s" % image_paths)

       
        csv_data = [current_timestamp, flag_option, flag_data[0], image_paths[-2], flag_data[-2]]
        print(csv_data)
        if not os.path.exists(self.log_filepath):
            with open(self.log_filepath, "a", newline="") as csvfile:
                writer = csv.writer(csvfile)
                writer.writerow(["Timestamp", "Flag", "Initial_prompt", "Image folder", "Generated_ad"])
        with open(self.log_filepath, "a", newline="") as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(utils.sanitize_list_for_csv(csv_data))
      
   