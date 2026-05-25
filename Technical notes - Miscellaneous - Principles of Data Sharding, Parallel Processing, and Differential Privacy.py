import numpy as np
from multiprocessing import Pool # Simulated Differential Privacy function
def apply_noise(data_chunk):
    epsilon = 0.5  # Privacy Budget
    noise = np.random.laplace(0, 1/epsilon, len(data_chunk))
    return data_chunk + noise
if __name__ == "__main__":    # 1. Simulate a large dataset
    dataset = np.random.normal(50, 10, 1000000)    # 2. Parallel Processing: Task Division
    chunks = np.array_split(dataset, 4) # Split for 4-core CPU    # 3. Execution: Process chunks in parallel
    with Pool(processes=4) as pool:
        result_chunks = pool.map(apply_noise, chunks)    # 4. Aggregation: Re-combine data
    private_data = np.concatenate(result_chunks)
    print(f"Original Mean: {np.mean(dataset):.2f}")
    print(f"Private Mean (with Noise): {np.mean(private_data):.2f}")