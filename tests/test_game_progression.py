import unittest

from game_progression import Character, Level, WORLDS


class TestGameProgression(unittest.TestCase):
    def test_level_points_scale_with_difficulty(self):
        easy = Level("Easy", 1)
        hard = Level("Hard", 8)
        self.assertLess(easy.points_awarded(), hard.points_awarded())

    def test_rank_progression(self):
        mario = Character(name="Mario")
        self.assertEqual(mario.current_rank(), "Rookie")

        # Simulate enough points to pass multiple ranks
        mario.total_points = 500
        self.assertEqual(mario.current_rank(), "Gold")

    def test_worlds_exist_and_have_levels(self):
        self.assertGreaterEqual(len(WORLDS), 6)
        for world in WORLDS:
            self.assertGreaterEqual(len(world.levels), 3)


if __name__ == "__main__":
    unittest.main()
