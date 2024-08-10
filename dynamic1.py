import random
import math
from function_code import dynamic1

def simulated_annealing(bounds, max_iterations, initial_temp, cooling_rate, random_number):
    # Generate an initial random candidate
    candidate = [random.uniform(bounds[0][0], bounds[0][1]), random.uniform(bounds[1][0], bounds[1][1])]
    candidate_eval = dynamic1(candidate, random_number)
    
    # Current temperature
    temp = initial_temp
    
    for i in range(max_iterations):
        # Take a step in a random direction
        new_candidate = [
            candidate[0] + random.uniform(-1, 1),
            candidate[1] + random.uniform(-1, 1)
        ]
        
        # Ensure the new candidate is within bounds
        new_candidate[0] = max(bounds[0][0], min(bounds[0][1], new_candidate[0]))
        new_candidate[1] = max(bounds[1][0], min(bounds[1][1], new_candidate[1]))

        # Evaluate the new candidate
        new_candidate_eval = dynamic1(new_candidate, random_number)
        
        # Calculate the change in evaluation
        delta_eval = new_candidate_eval - candidate_eval
        
        # Determine if we should accept the new candidate
        if delta_eval < 0 or math.exp(-delta_eval / temp) > random.random():
            candidate, candidate_eval = new_candidate, new_candidate_eval
        
        # Cool the temperature
        temp *= cooling_rate
        
        # (Optional) Print progress
        # if i % 100 == 0:
        #    print(f"Iteration {i}, candidate: {candidate}, value: {candidate_eval}")
    
    return candidate, candidate_eval

if __name__ == "__main__":
    # Set a random number atleast 6 digits long
    random_number = 12128551

    # Define the bounds of the search space
    bounds = [(-100, 100), (-100, 100)]
    # Define the maximum number of iterations
    max_iterations = 1000
    # Define the initial temperature
    initial_temp = 100.0
    # Define the cooling rate
    cooling_rate = 0.99
    
    # Perform simulated annealing
    best_candidate, best_value = simulated_annealing(bounds, max_iterations, initial_temp, cooling_rate, random_number)
    print(f"Best candidate: {best_candidate}, Best value: {best_value}")
