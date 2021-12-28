import copy

from unittest import TestCase

from road_collisions_ireland.models.collision import Collision


class CollisionTest(TestCase):

    TEST_COLLISION_DATA = {
        'lat': 52.44920547929465,
        'lng': -8.419577187763258,
        'year': 2008,
        'weekday': 'tuesday',
        'gender': 'female',
        'age': 70,
        'vehicle_type': 'car',
        'vehicle': '4',
        'hour': '23-3',
        'circumstances': 'single_vehicle_only',
        'num_fatal': 0,
        'num_minor': 4,
        'num_notinjured': 1,
        'num_serious': 0,
        'num_unknown': 7,
        'speed_limit': 80,
        'severity': 'minor',
        'county': 'limerick',
        'carrf': 0,
        'carri': 0,
        'class2': 88,
        'goodsrf': 0,
        'goodsri': 0,
        'mcycrf': 0,
        'mcycri': 0,
        'otherrf': 0,
        'otherri': 0,
        'pcycrf': 0,
        'pcycri': 0,
        'pedrf': 0,
        'pedri': 0,
        'psvrf': 0,
        'psvri': 0,
        'unknrf': 0,
        'unknri': 0
    }

    def test_complete_serialize(self):
        collision = Collision(
            **self.TEST_COLLISION_DATA
        )

        self.assertEqual(
            collision.serialize(),
            {
                'age': 70,
                'carrf': 0,
                'carri': 0,
                'circumstances': 'single_vehicle_only',
                'class2': 88,
                'county': 'limerick',
                'gender': 'female',
                'goodsrf': 0,
                'goodsri': 0,
                'hour': '23-3',
                'lat': 52.44920547929465,
                'lng': -8.419577187763258,
                'mcycrf': 0,
                'mcycri': 0,
                'num_fatal': 0,
                'num_minor': 4,
                'num_notinjured': 1,
                'num_serious': 0,
                'num_unknown': 7,
                'otherrf': 0,
                'otherri': 0,
                'pcycrf': 0,
                'pcycri': 0,
                'pedrf': 0,
                'pedri': 0,
                'psvrf': 0,
                'psvri': 0,
                'severity': 'minor',
                'speed_limit': 80,
                'unknrf': 0,
                'unknri': 0,
                'vehicle': '4',
                'vehicle_type': 'car',
                'weekday': 'tuesday',
                'year': 2008
            }
        )

    def test_incomplete_serialize(self):
        collision_data_copy = copy.deepcopy(self.TEST_COLLISION_DATA)
        del collision_data_copy['year']

        with self.assertRaises(KeyError):
            Collision(
                **collision_data_copy
            )

    def test_parse_raw(self):
        # sort this out when doing raw tests
        pass

    def test_parse(self):
        collision = Collision.parse(
            self.TEST_COLLISION_DATA
        )

        self.assertTrue(
            collision.id,
            Collision(**self.TEST_COLLISION_DATA).id
        )

    def test_id(self):
        collision_1 = Collision(
            **self.TEST_COLLISION_DATA
        )
        collision_2 = Collision(
            **self.TEST_COLLISION_DATA
        )
        self.assertEqual(
            collision_1.id,
            collision_2.id
        )

    def test_serialize(self):
        collision = Collision(
            **self.TEST_COLLISION_DATA
        )
        self.assertEqual(
            collision.serialize(),
            self.TEST_COLLISION_DATA
        )

    def test_props(self):
        collision = Collision(
            **self.TEST_COLLISION_DATA
        )

        for prop, val in self.TEST_COLLISION_DATA.items():
            self.assertEqual(getattr(collision, prop), val)

    def test_speed_limit_kph(self):
        pass

    def test_speed_limit_mph(self):
        pass
