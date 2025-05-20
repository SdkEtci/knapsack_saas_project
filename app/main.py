import pandas as pd
import numpy as np
from flask import Flask, jsonify, send_from_directory
from flask_cors import CORS
import os

app = Flask(__name__, static_folder='app/index.html')
CORS(app)

def parse_array_string(s):
    # Remove brackets and split by whitespace
    s = s.strip('[]')
    # Split by whitespace and convert to float
    return np.array([float(x) for x in s.split()])

def load_and_process_data():
    # Load the dataset
    data = pd.read_csv('./data/knapsack_5_items.csv')

    # Extract relevant columns and convert string representations of arrays to actual arrays
    weights = data['Weights'].apply(parse_array_string).to_numpy()
    prices = data['Prices'].apply(parse_array_string).to_numpy()
    capacities = data['Capacity'].to_numpy()
    best_picks = data['Best picks'].apply(lambda x: parse_array_string(x) if pd.notna(x) else None).to_numpy()
    best_prices = data['Best price'].to_numpy()

    # Create list of projects with their attributes
    projects = []
    for i in range(len(weights)):
        # For each row, create 5 projects (one for each item)
        for j in range(5):
            # Check if best_picks exists and is valid for this row
            if best_picks[i] is not None:
                projects.append({
                    'id': f"{i}_{j}",
                    'cost': float(prices[i][j]),
                    'benefit': float(weights[i][j]),
                    'capacity': float(capacities[i]),
                    'best_pick': float(best_picks[i][j])
                })
    return projects

def greedy_by_benefit(projects, max_budget, max_time):
    selected = []
    remaining_budget = max_budget
    remaining_time = max_time
    total_benefit = 0
    
    # Sort projects by benefit descending
    sorted_projects = sorted(projects, key=lambda x: x['benefit'], reverse=True)
    
    for project in sorted_projects:
        if project['cost'] <= remaining_budget:
            selected.append(project)
            remaining_budget -= project['cost']
            total_benefit += project['benefit']
    
    return {
        'selected_projects': selected,
        'total_projects': len(selected),
        'total_cost': max_budget - remaining_budget,
        'total_benefit': total_benefit,
        'budget_remaining': remaining_budget
    }

def greedy_by_efficiency(projects, max_budget, max_time):
    selected = []
    remaining_budget = max_budget
    remaining_time = max_time
    total_benefit = 0
    
    # Sort projects by benefit/cost ratio descending
    sorted_projects = sorted(projects, key=lambda x: x['benefit']/x['cost'], reverse=True)
    
    for project in sorted_projects:
        if project['cost'] <= remaining_budget:
            selected.append(project)
            remaining_budget -= project['cost']
            total_benefit += project['benefit']
    
    return {
        'selected_projects': selected,
        'total_projects': len(selected),
        'total_cost': max_budget - remaining_budget,
        'total_benefit': total_benefit,
        'budget_remaining': remaining_budget
    }

@app.route('/api/knapsack-results', methods=['GET'])
def get_knapsack_results():
    # Define budget and time constraints
    total_budget = 7800
    total_time = 960
    
    # Load and process data
    projects = load_and_process_data()
    
    # Run both strategies
    benefit_results = greedy_by_benefit(projects, total_budget, total_time)
    efficiency_results = greedy_by_efficiency(projects, total_budget, total_time)
    
    # Prepare response data
    response_data = {
        'benefit_strategy': benefit_results,
        'efficiency_strategy': efficiency_results,
        'total_budget': total_budget,
        'total_time': total_time
    }
    
    return jsonify(response_data)
    
@app.route('/')
def home():
    return "Knapsack SaaS is running!"
    
if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
