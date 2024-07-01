import multiprocessing
from sklearn.datasets import load_iris
from sklearn.ensemble import RandomForestClassifier

def train_model(seed):
    print(f"Training model with seed {seed}...")
    # Load dataset
    data = load_iris()
    X, y = data.data, data.target
    # Create and train the model
    model = RandomForestClassifier(n_estimators=100, random_state=seed)
    model.fit(X, y)
    print(f"Model trained with seed {seed}")

seeds = [42, 43, 44, 45]

processes = []
for seed in seeds:
    process = multiprocessing.Process(target=train_model, args=(seed,))
    processes.append(process)
    process.start()

for process in processes:
    process.join()

print("Model training completed.")
