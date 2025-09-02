import librosa
import numpy as np
import joblib

class EmotionRecognizer:
    def _init_(self, model_path="models/emotion_model.pkl"):
        self.model = joblib.load(model_path)

    def extract_features(self, audio_path):
        # Extract MFCC features
        y, sr = librosa.load(audio_path, sr=None)
        mfcc = librosa.feature.mfcc(y=y, sr=sr, n_mfcc=40)
        return np.mean(mfcc.T, axis=0).reshape(1, -1)

    def predict_emotion(self, audio_path):
        features = self.extract_features(audio_path)
        emotion = self.model.predict(features)[0]
        return emotion
