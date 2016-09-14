import pytest
from sqlalchemy import func

from flights.database import db_session
from flights import engine, models, factories


def assert_itinerary(segments):
    # thanks to agronholm from #sqlalchemy
    assert (db_session.query(models.itinerary_segment.c.itinerary_id)
        .filter(models.itinerary_segment.c.flight_number.in_(
            segment.flight_number for segment in segments
        ))
        .group_by(models.itinerary_segment.c.itinerary_id)
        .having(func.count() == len(segments))
        .first())


def test_one_itinerary():
    s1 = factories.Segment()
    s2 = factories.next_segment(s1, 2)
    db_session.commit()

    engine.find_itineraries()

    assert models.Itinerary.query.count() == 1
    assert_itinerary([s1, s2])


def test_multiple_itineraries():
    s1 = factories.Segment()
    s2 = factories.next_segment(s1, 2)
    s3 = factories.next_segment(s2, 1)
    s4 = factories.next_segment(s1, 3)
    db_session.commit()

    engine.find_itineraries()

    assert models.Itinerary.query.count() == 4

    assert_itinerary([s1, s2, s3])
    assert_itinerary([s1, s2])
    assert_itinerary([s2, s3])
    assert_itinerary([s1, s4])

    with pytest.raises(AssertionError) as exc:
        assert_itinerary([s2, s4])
