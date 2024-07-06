from sklearn.metrics import mean_absolute_error

class MonitoringAgent:
    def monitor_performance(self, model, validation_data, threshold):
        predictions = model.predict(validation_data['features'])
        error = mean_absolute_error(validation_data['target'], predictions)
        if error > threshold:
            # Trigger retraining
            return True
        return False