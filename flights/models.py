import logging

from sqlalchemy import (
    Column, Integer, DateTime, String,
    Table, ForeignKey,
)
from sqlalchemy.orm import relationship

from .database import Base, db_engine


logger = logging.getLogger(__name__)


class Segment(Base):
    __tablename__ = 'segment'

    source = Column(String(3), nullable=False, index=True)
    destination = Column(String(3), nullable=False)
    departure = Column(DateTime, nullable=False, index=True)
    arrival = Column(DateTime, nullable=False)
    flight_number = Column(String(5), primary_key=True)

    def __repr__(self):
        return '<Segment %s>' % self.flight_number

    def __str__(self):
        return '%(flight_number)s: %(source)s @ %(departure)s ' \
               '-> %(destination)s @ %(arrival)s' % self.__dict__


class Itinerary(Base):
    __tablename__ = 'itinerary'

    id = Column(Integer, primary_key=True)
    segments = relationship('Segment', secondary=lambda: itinerary_segment)

    def __repr__(self):
        return '<Itinerary %d>' % self.id

    def __str__(self):
        return ','.join([segment.flight_number for segment in self.segments])


itinerary_segment = Table('itinerary_segment', Base.metadata,
    Column('itinerary_id', Integer, ForeignKey('itinerary.id')),
    Column('flight_number', String(5), ForeignKey('segment.flight_number')),
)


def create_db():
    """Creates the DB schema."""

    logger.info('Creating DB schema...')
    Base.metadata.create_all(db_engine)
