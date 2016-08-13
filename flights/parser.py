import csv

import dateutil.parser

from . import models
from .database import db_session


def parse_csv(csvfile):
    reader = csv.DictReader(csvfile)
    for row in reader:
        for column in ['departure', 'arrival']:
            row[column] = dateutil.parser.parse(row[column])
        segment = models.Segment(**row)
        db_session.add(segment)
        db_session.commit()
