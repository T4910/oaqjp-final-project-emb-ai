from EmotionDetection.emotion_detection import emotion_detector
import unittest

class TestEmotionDetection(unittest.TestCase):
    def test_emotion_detection(self):
        # Joy test
        joy_result = emotion_detector("I am glad this happened.")
        self.assertEqual(joy_result['dominant_emotion'], "joy")
        
        # Anger test
        anger_result = emotion_detector("I am really mad about this.")
        self.assertEqual(anger_result['dominant_emotion'], "anger")
        
        # Disgust test
        disgust_result = emotion_detector("I feel disgusted just hearing about this.")
        self.assertEqual(disgust_result['dominant_emotion'], "disgust")
        
        # Sadness test
        sad_result = emotion_detector("I am so sad about this.")
        self.assertEqual(sad_result['dominant_emotion'], "sadness")
        
        # Fear test
        fear_result = emotion_detector("I am really afraid that this will happen.")
        self.assertEqual(fear_result['dominant_emotion'], "fear")

unittest.main()