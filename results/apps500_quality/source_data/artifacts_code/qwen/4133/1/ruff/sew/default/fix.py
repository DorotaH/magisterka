import re


def feed_golorp(golorp_name):
    # Extract the shape of the golorp's jaws from the name
    jaws_pattern = r'\(([^()]*)\)'
    jaws_match = re.search(jaws_pattern, golorp_name)
    if  not  jaws_match:
        return  "false"
    jaws = jaws_match.group(1).split(',')
    
    # Determine the number of variables needed
    num_variables = len(jaws)
    
    # Initialize the sequence of variable values
    sequence = [0] * num_variables
    
    # Check if the golorp can be fed
    for i in range(num_variables):
        # Find the minimum value that can be assigned to the current variable
        for value in range(10):
            if  all(value>=int(jaws[j][i]) for  j in  range(num_variables)):
                sequence[i]=value
                break
        else:
            return  "false"
    
    # Convert the sequence to a string and return
    return ''.join(map(str, sequence))

# Read the input from standard input
golorp_name = input().strip()

# Print the answer to standard output
print(feed_golorp(golorp_name))