# test_timer.py
# Unit tests for timer.py

import time
import unittest

from game.timer import GameTimer


class TestGameTimer(unittest.TestCase):
    # Unit tests for GameTimer 

    def setUp(self):
        self.timer = GameTimer()

    # Initialization

    def test_default_initialization(self):
        self.assertIsNone(self.timer.time_limit)
        self.assertFalse(self.timer.running)
        self.assertFalse(self.timer.paused)
        self.assertFalse(self.timer.countdown)

    def test_countdown_initialization(self):
        timer = GameTimer(60)

        self.assertEqual(timer.time_limit, 60)
        self.assertTrue(timer.countdown)

    # Start / Stop

    def test_start(self):
        self.timer.start()

        self.assertTrue(self.timer.running)
        self.assertFalse(self.timer.paused)
        self.assertIsNotNone(self.timer.start_time)

    def test_stop(self):
        self.timer.start()
        self.timer.stop()

        self.assertFalse(self.timer.running)
        self.assertFalse(self.timer.paused)

    def test_reset(self):
        self.timer.start()
        self.timer.reset()

        self.assertIsNone(self.timer.start_time)
        self.assertFalse(self.timer.running)
        self.assertFalse(self.timer.paused)
        self.assertEqual(self.timer.pause_duration, 0.0)

    # Pause / Resume

    def test_pause(self):
        self.timer.start()
        self.timer.pause()

        self.assertTrue(self.timer.paused)
        self.assertIsNotNone(self.timer.pause_start)

    def test_resume(self):
        self.timer.start()
        self.timer.pause()

        time.sleep(0.05)

        self.timer.resume()

        self.assertFalse(self.timer.paused)
        self.assertIsNone(self.timer.pause_start)
        self.assertGreaterEqual(
            self.timer.pause_duration,
            0
        )

    # Elapsed Time

    def test_elapsed_before_start(self):
        self.assertEqual(
            self.timer.elapsed(),
            0.0
        )

    def test_elapsed_after_start(self):
        self.timer.start()

        time.sleep(0.05)

        self.assertGreater(
            self.timer.elapsed(),
            0
        )

    # Remaining Time

    def test_remaining_stopwatch(self):
        self.assertIsNone(
            self.timer.remaining()
        )

    def test_remaining_countdown(self):
        timer = GameTimer(5)

        timer.start()

        remaining = timer.remaining()

        self.assertLessEqual(
            remaining,
            5
        )

        self.assertGreaterEqual(
            remaining,
            0
        )

    # Expiration

    def test_not_expired_without_limit(self):
        self.assertFalse(
            self.timer.expired()
        )

    def test_expired_after_limit(self):
        timer = GameTimer(1)

        timer.start()

        time.sleep(1.2)

        self.assertTrue(
            timer.expired()
        )

    # Formatting

    def test_format_zero(self):
        self.assertEqual(
            GameTimer.format(0),
            "00:00"
        )

    def test_format_seconds(self):
        self.assertEqual(
            GameTimer.format(65),
            "01:05"
        )

    def test_format_large_time(self):
        self.assertEqual(
            GameTimer.format(3725),
            "62:05"
        )

    def test_formatted_elapsed(self):
        self.timer.start()

        result = self.timer.formatted_elapsed()

        self.assertIsInstance(
            result,
            str
        )

        self.assertEqual(
            len(result),
            5
        )

    def test_formatted_remaining(self):
        timer = GameTimer(30)

        timer.start()

        result = timer.formatted_remaining()

        self.assertIsInstance(
            result,
            str
        )

        self.assertEqual(
            len(result),
            5
        )

    # Properties

    def test_running_property(self):
        self.timer.start()

        self.assertTrue(
            self.timer._running
        )

    def test_paused_property(self):
        self.timer.start()
        self.timer.pause()

        self.assertTrue(
            self.timer._spaused
        )

    def test_countdown_property(self):
        timer = GameTimer(10)

        self.assertTrue(
            timer.countdown
        )

    # String Representation

    def test_stopwatch_string(self):
        text = str(self.timer)

        self.assertIn(
            "Stopwatch",
            text
        )

    def test_countdown_string(self):
        timer = GameTimer(60)

        text = str(timer)

        self.assertIn(
            "Countdown Timer",
            text
        )

    def test_repr(self):
        text = repr(self.timer)

        self.assertIn(
            "Game Timer",
            text
        )

        self.assertIn(
            "time_limit",
            text
        )


if __name__ == "__main__":
    unittest.main() 

