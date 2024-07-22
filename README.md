# XML to CSV/SQLite Converter - EL30 / Senior Web Development - Eyad Saleh - Luca Krutzsch

## Description

This application reads an XML file (local or remote) and writes the data to a specified storage solution (CSV).  
The code is designed to be easily extendable to support additional storage solutions in the future, just like already presented with SQLite.

## Table of Contents

- [Patterns Used](#patterns-used)
- [Setup and Run](#setup-and-run)
- [Code Structure](#code-structure)
- [Performance](#performance)
- [SOLID and Clean Code Principles](#solid-and-clean-code-principles)
- [Testing](#testing)

## Patterns Used

- **Factory Pattern**: Used in the `StorageFactory` to create storage instances (CSV, SQLite) based on the provided type.  
         This allows easy addition of new storage types without modifying the existing code.  
- **Abstract Base Class**: The `Storage` class is an abstract base class defining the interface for storage solutions.  
         This ensures that all storage classes implement the required methods.
- **Logging**: Used for error handling and logging messages. This makes the code more maintainable and easier to debug.

## Setup and Run

### Prerequisites

- Python 3.6+
- `pip` (Python package installer)

### Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/your-repo/xml-to-csv-sqlite.git
   cd xml-to-csv-sqlite
2. Install the required packages:

   ```bash
   pip install -r requirements.txt
3. Running the application

   Local XML File to CSV

      ```bash
      python src/main.py path/to/local/coffee_feed.xml csv output.csv
      ```
   where the parameters you might want to replace are: 
      - src/main.py is the file you want/have to execute
      - path/to/local/coffe_feed.xml is replaced by the path to wherever you have stored your CSV file on your disk 
      - csv is the type of data storage you want to convert to
      - output.csv is the name you want to give the new file

   Remote XML File to CSV

      ```bash
      python src/main.py https://example.com/path/to/remote/coffee_feed.xml csv output.csv
      ```
   Local XML File to SQLite

      ```bash 
      python src/main.py path/to/local/coffee_feed.xml sqlite output.db
## Code Structure

   The project is organized into a modular structure with clear separation of concerns:

   xml_to_csv/  
   ├── src/  
   │   ├── __init__.py  
   │   ├── main.py  
   │   ├── xml_reader.py  
   │   ├── storage/  
   │   │   ├── __init__.py  
   │   │   ├── storage.py  
   │   │   ├── csv_storage.py  
   │   │   ├── sqlite_storage.py  
   │   │   ├── storage_factory.py  
   │   ├── utils/  
   │   │   ├── __init__.py  
   │   │   ├── logger.py  
   ├── tests/  
   │   ├── __init__.py  
   │   ├── test_csv_storage.py  
   │   ├── test_sqlite_storage.py  
   │   ├── test_storage_factory.py  
   │   ├── test_xml_reader.py  
   ├── requirements.txt  
   ├── README.md  

### Key Files and Their Roles

- src/main.py: Entry point for the application.
- src/xml_reader.py: Contains logic for reading and parsing XML files.
- src/storage/storage.py: Abstract base class for storage solutions.
- src/storage/csv_storage.py: CSV storage implementation.
- src/storage/sqlite_storage.py: SQLite storage implementation.
- src/storage/storage_factory.py: Factory for creating storage instances.
- src/utils/logger.py: Logging setup for error handling.
- tests/: Contains unit tests for different components of the application.

## Performance

The code is designed to be efficient by using built-in Python libraries for   
XML parsing (xml.etree.ElementTree) and file operations. Error handling   
ensures that any issues are logged, allowing for quick identification and   
resolution without affecting performance.

## SOLID and Clean Code Principles

### Single Responsibility Principle

Each class and function in the project has a single responsibility:

- XMLReader handles reading XML data.
- Storage subclasses handle different storage formats (CSV, SQLite).
- StorageFactory creates instances of storage classes.

### Open/Closed Principle

The StorageFactory and Storage class hierarchy make it easy to add new 
storage types without modifying existing code.

### Liskov Substitution Principle

All storage classes (`CSVStorage`, `SQLiteStorage`) can be used interchangeably 
as they adhere to the `Storage` interface.

### Interface Segregation Principle

The Storage interface ensures that storage classes only implement the 
methods they need.

### Dependency Inversion Principle

High-level modules do not depend on low-level modules; both depend on abstractions.   
The `StorageFactory` creates storage instances based on an abstract `Storage` interface.

## Testing

### Available Tests

Unit tests are available for all key components:

- test_csv_storage.py: Tests for the CSV storage implementation.
- test_sqlite_storage.py: Tests for the SQLite storage implementation.
- test_storage_factory.py: Tests for the storage factory.
- test_xml_reader.py: Tests for the XML reader.

### Running Tests

To run the tests, use the following command:

   ```bash 
   python -m unittest discover -s tests
   ```
### Conclusion

The project follows SOLID principles and clean code practices, ensuring  
maintainability, scalability, and ease of understanding. The modular structure  
and comprehensive error handling make it robust and reliable. The included  
unit tests ensure that all components work as expected, and the factory pattern  
used for storage creation allows for easy extension to new storage types.  
