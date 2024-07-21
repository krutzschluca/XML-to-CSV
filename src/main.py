import argparse
import logging
from utils.logger import setup_logging
from xml_reader import read_xml
from storage.storage_factory import StorageFactory

def main():
    setup_logging()

    parser = argparse.ArgumentParser(description="Process an XML file and output to a storage solution.")
    parser.add_argument('xml_file', type=str, help="Path to the input XML file (local or remote)")
    parser.add_argument('storage_type', type=str, help="Type of storage (csv, sqlite)")
    parser.add_argument('storage_path', type=str, help="Path to the storage file or database")

    args = parser.parse_args()

    try:
        data = read_xml(args.xml_file)
        if data:
            storage = StorageFactory.get_storage(args.storage_type, args.storage_path)
            storage.write(data)
    except ValueError as e:
        logging.error(f"Value error: {e}")
    except Exception as e:
        logging.error(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
