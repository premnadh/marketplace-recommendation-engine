from src.collaborative_filtering import CollaborativeFilteringEngine

engine = CollaborativeFilteringEngine("data/interactions.csv")

score = engine.predict(user_id=1, product_id=42198)

print("Predicted rating:", score)