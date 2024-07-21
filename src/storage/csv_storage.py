import csv
import logging
from storage.storage import Storage

class CSVStorage(Storage):
    def __init__(self, file_path):
        self.file_path = file_path

    def write(self, data):
        try:
            with open(self.file_path, mode='w', newline='', encoding='utf-8') as file:
                writer = csv.DictWriter(file, fieldnames=data[0].keys())
                writer.writeheader()
                for row in data:
                    writer.writerow(row)
        except PermissionError as e:
            logging.error(f"Permission error writing CSV file: {e}")
        except IOError as e:
            logging.error(f"IO error writing CSV file: {e}")
        except Exception as e:
            logging.error(f"An unexpected error occurred while writing CSV file: {e}")
