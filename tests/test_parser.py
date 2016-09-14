from datetime import datetime

from io import StringIO

from flights import models, parser


def test_parser():
    csv_file = StringIO(
        'source,destination,departure,arrival,flight_number\n'
        'USM,HKT,2016-10-11T10:10:00,2016-10-11T11:10:00,PV511\n'
        'USM,HKT,2016-10-11T18:15:00,2016-10-11T19:15:00,PV476'
    )
    parser.parse_csv(csv_file)

    assert models.Segment.query.count() == 2
    assert models.Segment.query.filter_by(flight_number='PV511') \
        .one().arrival == datetime(year=2016, month=10, day=11,
                                   hour=11, minute=10)
