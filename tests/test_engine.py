from datetime import timedelta as td

from flights.database import db_session
from flights import engine, models, factories


def test_one_itinerary():
    s1 = factories.Segment()
    s2 = factories.Segment(source=s1.destination,
                           departure=s1.arrival + td(hours=2))
    db_session.commit()
    engine.find_itineraries()

    assert models.Itinerary.query.count() == 1
