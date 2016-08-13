from datetime import timedelta

from .models import Segment, Itinerary
from .database import db_session


CHANGE_MIN = timedelta(hours=1)
CHANGE_MAX = timedelta(hours=4)


def _find_itineraries(history):
    previous = history[-1]

    for actual in Segment.query \
            .filter(Segment.source == previous.destination) \
            .filter(Segment.departure >= previous.arrival + CHANGE_MIN) \
            .filter(Segment.departure <= previous.arrival + CHANGE_MAX) \
            .all():

        segments = history + [actual]

        itinerary = Itinerary(segments=segments)
        db_session.add(itinerary)
        db_session.commit()

        _find_itineraries(segments)


def find_itineraries():
    for first in Segment.query.all():
        _find_itineraries([first])
