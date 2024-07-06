# main.py
from data_collection_agent import DataCollectionAgent
from feature_engineering_agent import FeatureEngineeringAgent
from model_training_agent import ModelTrainingAgent
from prediction_agent import PredictionAgent
from monitoring_agent import MonitoringAgent

# Step 1: Collect Data
data_agent = DataCollectionAgent()
data = data_agent.collect_data('AAPL', '2010-01-01', '2023-01-01')

# Step 2: Feature Engineering
feature_agent = FeatureEngineeringAgent()
features_data = feature_agent.create_features(data)
features = features_data[['MA20', 'MA50', 'Lag1', 'Lag2']]
target = features_data['Close']

# Step 3: Train Model
model_agent = ModelTrainingAgent()
model = model_agent.train_model(features, target)

# Save the model
import joblib
joblib.dump(model, 'model.pkl')

# Step 4: Make Prediction
prediction_agent = PredictionAgent()
predictions = prediction_agent.make_prediction(model, features)

# Step 5: Monitor Performance
monitoring_agent = MonitoringAgent()
if monitoring_agent.monitor_performance(model, {'features': features, 'target': target}, threshold=5.0):
    print("Retraining Required")
else:
    print("Model Performance is Good")

# Step 6: Deploy API (run deployment_agent.py)