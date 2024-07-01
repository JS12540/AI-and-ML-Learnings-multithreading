import multiprocessing
import pandas as pd
import time

# Example function for data preprocessing
def preprocess_data(row):
    # Simulate some data preprocessing task (e.g., normalization)
    time.sleep(1)  # Simulating some processing time
    return row * 2  # Example: doubling each element in the row

def preprocess_dataset(data):
    # Using multiprocessing to preprocess each row independently
    with multiprocessing.Pool() as pool:
        processed_data = pool.map(preprocess_data, data)
    return processed_data

if __name__ == "__main__":
    # Example dataset
    dataset = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

    # Preprocess the dataset
    start_time = time.time()
    processed_dataset = preprocess_dataset(dataset)
    end_time = time.time()

    # Print results
    print("Original Dataset:")
    print(pd.DataFrame(dataset))
    print("\nProcessed Dataset:")
    print(pd.DataFrame(processed_dataset))
    print(f"\nProcessing time: {end_time - start_time} seconds")
