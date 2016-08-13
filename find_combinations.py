#!/usr/bin/env python3

import sys

from flights import models, parser, engine


def main():
    models.create_db()
    parser.parse_csv(iter(sys.stdin.readline, ''))
    engine.find_itineraries()
    for itinerary in models.Itinerary.query.all():
        print(itinerary)


if __name__ == '__main__':
    main()
