import time
import numpy as np
from multiprocessing import Pool

def apply_noise(data_chunk):
    """
    Applies Laplace noise to a data chunk for Differential Privacy.
    """
    epsilon = 0.5  # Privacy Budget per chunk
    # NumPy's laplace takes (loc, scale, size)
    noise = np.random.laplace(0, 1 / epsilon, size=len(data_chunk))
    return data_chunk + noise

if __name__ == "__main__":
    # 1. Simulate a large dataset (1,000,000 elements)
    print("Generating dataset...")
    dataset = np.random.normal(50, 10, 1000000)
    
    # 2. Parallel Processing: Task Division
    num_cores = 4
    chunks = np.array_split(dataset, num_cores)
    
    # 3. Execution: Process chunks in parallel and time it
    print(f"Processing chunks in parallel across {num_cores} cores...")
    start_time = time.time()
    
    with Pool(processes=num_cores) as pool:
        result_chunks = pool.map(apply_noise, chunks)
        
    # 4. Aggregation: Re-combine data
    private_data = np.concatenate(result_chunks)
    end_time = time.time()
    
    # 5. Results
    print("\n--- Results ---")
    print(f"Original Mean:             {np.mean(dataset):.4f}")
    print(f"Private Mean (with Noise): {np.mean(private_data):.4f}")
    print(f"Execution Time:            {end_time - start_time:.4f} seconds")
