import random

def main():
    num_names = int(input("Enter the number of names: "))
    names = []
    for i in range(num_names):
        name = input(f"Enter name {i+1}: ")
        names.append(name)
    
    # Shuffle the names
    random.shuffle(names)
    
    # Create Secret Santa assignments (each gives to the next in the shuffled list)
    assignments = {}
    for i in range(len(names)):
        giver = names[i]
        receiver = names[(i + 1) % len(names)]
        assignments[giver] = receiver
    
    # Print assignments
    for giver, receiver in assignments.items():
        print(f"{giver} gives to {receiver}")

if __name__ == "__main__":
    main()