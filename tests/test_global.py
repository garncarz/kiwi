from flights import engine, models, parser


def test_main():
    with open('input.csv', 'r') as csv_file:
        parser.parse_csv(csv_file)
    engine.find_itineraries()

    assert models.Itinerary.query.count() == 36
