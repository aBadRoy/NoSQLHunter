"""Command-line interface for NoSQLHunter."""

import argparse
import json
import sys
import os

from .exploit import NoSQLInjector, C_GREEN, C_CYAN, C_RESET


def main():
    parser = argparse.ArgumentParser(
        prog='nosqlhunter',
        description='NoSQL Injection Exploitation Framework v2.2 - Automated NoSQL security testing',
        epilog='Example: nosqlhunter --url http://target.com/api --verbose --output report.json',
        formatter_class=argparse.RawDescriptionHelpFormatter
    )

    parser.add_argument('--url', '-u', required=True, help='Target base URL (e.g. http://target.com/api)')
    parser.add_argument('--proxy', '-p', help='Proxy URL (e.g. http://127.0.0.1:8080)')
    parser.add_argument('--dataset', '-d', default='dataset/dataset_nosql.json', help='Path to dataset JSON file')
    parser.add_argument('--depth', '-D', type=int, default=3, help='Crawl depth (default: 3)')
    parser.add_argument('--concurrency', '-c', type=int, default=10, help='Concurrent requests (default: 10)')
    parser.add_argument('--verbose', '-v', action='store_true', help='Enable verbose discovery logs')
    parser.add_argument('--output', '-o', help='Save JSON report to file')

    args = parser.parse_args()

    if args.proxy and not args.proxy.startswith('http'):
        print('[!] Proxy must start with http:// or https://')
        sys.exit(1)

    injector = NoSQLInjector(
        base_url=args.url,
        proxy=args.proxy,
        dataset_path=args.dataset,
        depth=args.depth,
        concurrency=args.concurrency,
        verbose=args.verbose
    )

    report = injector.run()

    if args.output:
        os.makedirs(os.path.dirname(args.output) or '.', exist_ok=True)
        with open(args.output, 'w') as f:
            json.dump(report, f, indent=2)
        print(f"\n{C_GREEN}[+]{C_RESET} Report saved to {C_CYAN}{args.output}{C_RESET}")

    sys.exit(1 if report.get('findings') else 0)


if __name__ == '__main__':
    main()
