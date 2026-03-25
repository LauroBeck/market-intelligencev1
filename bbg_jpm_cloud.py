import matplotlib.pyplot as plt
import numpy as np

def run_jpm_cloud_simulation():
    print("\033[1;34m[JPM-IBM HYBRID CLOUD] Simulating 5,000 Node Cluster Deployment...\033[0m")
    
    # Parameters for the 5,000 server deployment
    nodes = 5000
    latency_reduction_per_node = 0.002 # ms
    current_latency = 45.0 # ms for global portfolio assessment
    
    new_latency = current_latency - (nodes * latency_reduction_per_node)
    throughput_increase = ((current_latency / new_latency) - 1) * 100

    # Data for visualization
    categories = ['Pre-Deployment', 'Post-5k Nodes']
    latencies = [current_latency, new_latency]

    plt.figure(figsize=(10, 6), facecolor='black')
    plt.style.use('dark_background')
    
    bars = plt.bar(categories, latencies, color=['#113355', '#00FF00'])
    plt.title("JPM Portfolio Assessment Latency (IBM Cloud Expansion)", color='#BC8CF2')
    plt.ylabel("Latency (ms)")
    plt.grid(axis='y', alpha=0.3)
    
    # Adding throughput label
    plt.text(1, new_latency + 2, f"+{throughput_increase:.1f}% Throughput", 
             color='#00FF00', ha='center', fontweight='bold')

    filename = 'JPM_Cloud_Expansion.png'
    plt.savefig(filename, facecolor='black')
    print(f"\033[1;32m[ANALYSIS]\033[0m Latency dropped to {new_latency:.2f}ms. Chart: {filename}")

if __name__ == "__main__":
    run_jpm_cloud_simulation()
