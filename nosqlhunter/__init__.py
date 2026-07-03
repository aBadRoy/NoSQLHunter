"""
NoSQLHunter - Advanced NoSQL Injection Exploitation Framework
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Automated NoSQL injection detection, exploitation, and data extraction tool
supporting MongoDB, CouchDB, Redis, Elasticsearch, DynamoDB, and more.

Usage:
    nosqlhunter --url http://target.com
    python -m nosqlhunter --url http://target.com -v -o report.json
"""

__title__ = "NoSQLHunter"
__version__ = "2.2.1"
__author__ = "aBadRoy"
__license__ = "MIT"
__description__ = "Advanced NoSQL Injection Exploitation Framework"

from .exploit import NoSQLInjector
