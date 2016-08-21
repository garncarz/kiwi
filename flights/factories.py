import random
import string

from factory import lazy_attribute
from factory.alchemy import SQLAlchemyModelFactory
from faker import Factory

from . import models
from .database import db_session


faker = Factory.create()

lazy = lambda call: lazy_attribute(lambda obj: call())
lazy_airport = lazy(lambda: ''.join(
    [random.choice(string.ascii_uppercase) for _ in range(3)]
))
lazy_date_time = lazy(lambda:
    faker.date_time_between(start_date='-30d', end_date='+30d')
)
lazy_flight_number = lazy(lambda: ''.join(
    [random.choice(string.ascii_uppercase) for _ in range(2)] +
    [random.choice(string.digits) for _ in range(3)]
))


class Segment(SQLAlchemyModelFactory):
    class Meta:
        model = models.Segment
        sqlalchemy_session = db_session

    source = lazy_airport
    destination = lazy_airport
    departure = lazy_date_time
    arrival = lazy_date_time  # TODO = departure + few hours
    flight_number = lazy_flight_number
