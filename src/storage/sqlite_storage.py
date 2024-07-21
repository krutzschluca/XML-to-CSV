import sqlite3
import logging
from storage.storage import Storage

class SQLiteStorage(Storage):
    def __init__(self, db_path):
        self.db_path = db_path

    def write(self, data):
        try:
            conn = sqlite3.connect(self.db_path)
            cursor = conn.cursor()
            
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS items (
                    entity_id TEXT,
                    CategoryName TEXT,
                    sku TEXT,
                    name TEXT,
                    description TEXT,
                    shortdesc TEXT,
                    price TEXT,
                    link TEXT,
                    image TEXT,
                    Brand TEXT,
                    Rating TEXT,
                    CaffeineType TEXT,
                    Count TEXT,
                    Flavored TEXT,
                    Seasonal TEXT,
                    Instock TEXT,
                    Facebook TEXT,
                    IsKCup TEXT
                )
            ''')

            for row in data:
                cursor.execute('''
                    INSERT INTO items (
                        entity_id, CategoryName, sku, name, description, shortdesc, price, link, image, Brand, Rating, CaffeineType, Count, Flavored, Seasonal, Instock, Facebook, IsKCup
                    ) VALUES (
                        :entity_id, :CategoryName, :sku, :name, :description, :shortdesc, :price, :link, :image, :Brand, :Rating, :CaffeineType, :Count, :Flavored, :Seasonal, :Instock, :Facebook, :IsKCup
                    )
                ''', row)

            conn.commit()
            conn.close()
        except sqlite3.DatabaseError as e:
            logging.error(f"Database error: {e}")
        except sqlite3.IntegrityError as e:
            logging.error(f"Integrity error in SQLite database: {e}")
        except Exception as e:
            logging.error(f"An unexpected error occurred while writing to SQLite database: {e}")
