from datetime import timedelta

from .models import Segment, Itinerary
from .database import db_session


CHANGE_MIN = timedelta(hours=1)
CHANGE_MAX = timedelta(hours=4)


def find_itineraries():
    for first in Segment.query.all():
        for second in Segment.query \
                .filter(Segment.source == first.destination) \
                .filter(Segment.departure >= first.arrival + CHANGE_MIN) \
                .filter(Segment.departure <= first.arrival + CHANGE_MAX) \
                .all():
            itinerary = Itinerary(segments=[first, second])
            db_session.add(itinerary)
            db_session.commit()
