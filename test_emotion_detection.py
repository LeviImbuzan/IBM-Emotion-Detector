"""Unit tests for the emotion_detector function."""

import unittest
from EmotionDetection.emotion_detection import emotion_detector


class TestEmotionDetection(unittest.TestCase):
    """Test cases for emotion_detector covering all five dominant emotions."""

    def test_dominant_emotion_joy(self):
        """Test that joyful text returns joy as dominant emotion."""
        result = emotion_detector("I am glad this happened")
        self.assertEqual(result['dominant_emotion'], 'joy')

    def test_dominant_emotion_anger(self):
        """Test that angry text returns anger as dominant emotion."""
        result = emotion_detector("I am really mad about this")
        self.assertEqual(result['dominant_emotion'], 'anger')

    def test_dominant_emotion_disgust(self):
        """Test that disgusted text returns disgust as dominant emotion."""
        result = emotion_detector("I feel disgusted just hearing about this")
        self.assertEqual(result['dominant_emotion'], 'disgust')

    def test_dominant_emotion_sadness(self):
        """Test that sad text returns sadness as dominant emotion."""
        result = emotion_detector("I am so sad about this")
        self.assertEqual(result['dominant_emotion'], 'sadness')

    def test_dominant_emotion_fear(self):
        """Test that fearful text returns fear as dominant emotion."""
        result = emotion_detector("I am really afraid that this will happen")
        self.assertEqual(result['dominant_emotion'], 'fear')


if __name__ == '__main__':
    unittest.main()
