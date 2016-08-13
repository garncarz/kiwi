#!/usr/bin/env python3

import sys

from flights import models, parser


def load():
    parser.parse_csv(iter(sys.stdin.readline, ''))


def main():
    models.create_db()
    load()


if __name__ == '__main__':
    main()
