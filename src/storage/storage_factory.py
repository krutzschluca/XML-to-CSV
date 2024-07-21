from storage.csv_storage import CSVStorage
from storage.sqlite_storage import SQLiteStorage

class StorageFactory:
    _registry = {}

    @staticmethod
    def register_storage(storage_type, storage_class):
        StorageFactory._registry[storage_type] = storage_class

    @staticmethod
    def get_storage(storage_type, storage_path):
        storage_class = StorageFactory._registry.get(storage_type)
        if not storage_class:
            raise ValueError(f"Unsupported storage type: {storage_type}")
        return storage_class(storage_path)

# Register storage types
StorageFactory.register_storage('csv', CSVStorage)
StorageFactory.register_storage('sqlite', SQLiteStorage)
