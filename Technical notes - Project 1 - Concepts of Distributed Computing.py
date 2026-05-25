import multiprocessing
import time # Simulated Task: A heavy calculation (Pillar: Parallelism)
def compute_node_task(data_chunk):
    node_name = multiprocessing.current_process().name
    print(f"[{node_name}] Processing chunk: {data_chunk}...")
    time.sleep(1) # Simulating computational latency
    result = data_chunk * data_chunk
    return result
if __name__ == "__main__":    # Centralized data to be distributed
    complex_task_data = [10, 20, 30, 40, 50, 60]
    print("Master Node: Partitioning tasks across available nodes...")    # Initializing a pool of worker nodes
    with multiprocessing.Pool(processes=3) as cluster:   # Map: Distributing tasks (Pillar: Scaling)
        results = cluster.map(compute_node_task, complex_task_data)    # Aggregation (Pillar: High Performance)
    print(f"\nFinal Aggregated Result: {results}")