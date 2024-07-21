# XML to CSV/SQLite Converter

## Description

This application reads an XML file (local or remote) and writes the data to a specified storage solution (CSV or SQLite). The code is designed to be easily extendable to support additional storage solutions in the future.

## Table of Contents

- [Patterns Used](#patterns-used)
- [Setup and Run](#setup-and-run)
- [Code Structure](#code-structure)
- [Performance](#performance)
- [SOLID and Clean Code Principles](#solid-and-clean-code-principles)
- [Testing](#testing)

## Patterns Used

- **Factory Pattern**: Used in the `StorageFactory` to create storage instances (CSV, SQLite) based on the provided type. This allows easy addition of new storage types without modifying the existing code.
- **Abstract Base Class**: The `Storage` class is an abstract base class defining the interface for storage solutions. This ensures that all storage classes implement the required methods.
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
