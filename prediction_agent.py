class PredictionAgent:
    def make_prediction(self, model, features):
        return model.predict(features)