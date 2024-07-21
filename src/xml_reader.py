import xml.etree.ElementTree as ET
import logging
import requests
from io import StringIO

def read_xml(file_path):
    try:
        if file_path.startswith('http://') or file_path.startswith('https://'):
            response = requests.get(file_path, timeout=10)
            response.raise_for_status()  # Check that the request was successful
            content = StringIO(response.text)
            tree = ET.parse(content)
        else:
            tree = ET.parse(file_path)
        
        root = tree.getroot()
        items = []
        for item in root.findall('item'):
            item_data = {
                'entity_id': item.find('entity_id').text,
                'CategoryName': item.find('CategoryName').text,
                'sku': item.find('sku').text,
                'name': item.find('name').text,
                'description': item.find('description').text if item.find('description') is not None else '',
                'shortdesc': item.find('shortdesc').text if item.find('shortdesc') is not None else '',
                'price': item.find('price').text,
                'link': item.find('link').text,
                'image': item.find('image').text,
                'Brand': item.find('Brand').text,
                'Rating': item.find('Rating').text,
                'CaffeineType': item.find('CaffeineType').text if item.find('CaffeineType') is not None else '',
                'Count': item.find('Count').text if item.find('Count') is not None else '',
                'Flavored': item.find('Flavored').text if item.find('Flavored') is not None else '',
                'Seasonal': item.find('Seasonal').text if item.find('Seasonal') is not None else '',
                'Instock': item.find('Instock').text,
                'Facebook': item.find('Facebook').text,
                'IsKCup': item.find('IsKCup').text
            }
            items.append(item_data)
        return items
    except requests.exceptions.RequestException as e:
        logging.error(f"Network error when fetching remote XML file: {e}")
    except ET.ParseError as e:
        logging.error(f"Error parsing XML file: {e}")
    except FileNotFoundError as e:
        logging.error(f"Local XML file not found: {e}")
    except Exception as e:
        logging.error(f"An unexpected error occurred: {e}")
    return []
