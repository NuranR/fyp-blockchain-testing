import json
import sys

def count_proposer_frequency(file_path):
    # Count how many times each proposer appears in the blockchain
    proposer_frequency = {}
    
    try:
        with open(file_path, 'r') as f:
            blockchain_data = json.load(f)

        for block in blockchain_data:
            if 'proposerPublicKey' in block:
                public_key = block['proposerPublicKey']
                
                if public_key in proposer_frequency:
                    proposer_frequency[public_key] += 1
                else:
                    proposer_frequency[public_key] = 1

    except FileNotFoundError:
        print(f"Error: couldn't find {file_path}")
        return {}
    except json.JSONDecodeError:
        print(f"Error: {file_path} is not valid JSON")
        return {}
        
    return proposer_frequency

if __name__ == "__main__":
    file_path = sys.argv[1]
    
    print(f"Analyzing: {file_path}")
    frequency_results = count_proposer_frequency(file_path)
    
    if frequency_results:
        print("\nProposer frequencies:")
        for key, value in frequency_results.items():
            print(f"  {key}: {value}")
        
        total_blocks = sum(frequency_results.values())
        print(f"\nTotal blocks: {total_blocks}")