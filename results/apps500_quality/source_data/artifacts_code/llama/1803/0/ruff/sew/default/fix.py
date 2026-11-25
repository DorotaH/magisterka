

def  process_input():
    # Read the number of wires
    n=int(input())

    # Read the initial number of birds on each wire
    birds=list(map(int, input().split()))

    # Read the number of shots
    m=int(input())

    # Process each shot
    for _ in range(m):
        # Read the wire and the position of the bird to be shot
        wire, position=map(int, input().split())

        # Adjust the birds on the wire
        birds[wire-1]-=1
        birds=adjust_birds(birds, wire-1, position-1)
        birds=adjust_birds(birds, wire, position)

    # Print the number of birds on each wire
    for bird in birds:
        print(bird)


def  adjust_birds(birds, index, position):
    if index>0 and birds[index]>0:
        # Move birds to the left to the previous wire
        birds[index - 1] += birds[index] - position
        birds[index] = position
    if index + 1<len(birds) and birds[index + 1]>0:
        # Move birds to the right to the next wire
        birds[1 + index] += birds[index] - (birds[1 + index] - 1)
        birds[index] = birds[1 + index] - 1
    return  birds

process_input()