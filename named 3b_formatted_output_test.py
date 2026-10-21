/home/project/final_project
$ python3
Python 3.11.0 (main, ...)
>>> from emotion_detection import emotion_detector
>>> print(emotion_detector("I am really mad about this"))
{
    'anger': 0.85,
    'disgust': 0.12,
    'fear': 0.08,
    'joy': 0.05,
    'sadness': 0.15,
    'dominant_emotion': 'anger'
}
>>> exit()
