from sklearn.ensemble import RandomForestRegressor

class ModelTrainingAgent:
    def train_model(self, features, target):
        model = RandomForestRegressor()
        model.fit(features, target)
        return model
