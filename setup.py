"""Setup script for NoSQLHunter."""

from setuptools import setup, find_packages

with open('README.md', 'r', encoding='utf-8') as f:
    long_description = f.read()

with open('requirements.txt', 'r', encoding='utf-8') as f:
    requirements = [line.strip() for line in f if line.strip() and not line.startswith('#')]

setup(
    name='nosqlhunter',
    version='2.2.1',
    description='Advanced NoSQL Injection Exploitation Framework',
    long_description=long_description,
    long_description_content_type='text/markdown',
    author='aBadRoy',
    url='https://github.com/aBadRoy/NoSQLHunter',
    license='MIT',
    packages=find_packages(),
    include_package_data=True,
    install_requires=requirements,
    entry_points={
        'console_scripts': [
            'nosqlhunter=nosqlhunter.cli:main',
        ],
    },
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Information Technology',
        'Intended Audience :: System Administrators',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Topic :: Security',
        'Topic :: Database',
        'Environment :: Console',
        'Natural Language :: English',
    ],
    python_requires='>=3.7',
    keywords=[
        'nosql-injection', 'mongodb', 'security', 'penetration-testing',
        'vulnerability-scanner', 'nosql', 'injection', 'exploitation',
        'couchdb', 'redis', 'elasticsearch', 'dynamodb', 'cybersecurity',
        'ethical-hacking', 'bug-bounty', 'web-security', 'pentesting'
    ],
    project_urls={
        'Source': 'https://github.com/aBadRoy/NoSQLHunter',
        'Bug Reports': 'https://github.com/aBadRoy/NoSQLHunter/issues',
    },
)
