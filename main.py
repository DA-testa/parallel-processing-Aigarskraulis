#phyton3
#221RDC045 Aigars Kraulis 18.grupa

def process_in_parallel(n, m, data):
    threads = list(range(n))
    times = [0] * n
    output = []
    counter = 0
    time = 0
    for i in range(m):
        output.append(threads[counter])
        output.append(times[counter])
        while True:
            times[counter] += 1
            data[i] -= 1
            if data[i] == 0:
                break
        counter = (counter + 1) % n
        if counter == 0:
            time += 1
    return output

def main():
      # TODO: create input from keyboard
    # input consists of two lines
    # first line - n and m
    # n - thread count 
    # m - job count
    n, m = map(int, input().split())
    # second line - data 
    # data - contains m integers t(i) - the times in seconds it takes any thread to process i-th job
    data = list(map(int, input().split()))
      # TODO: create the function
    result = process_in_parallel(n, m, data)
      # TODO: print out the results, each pair in it's own line
    for i in range(0, len(result), 2):
        print(result[i], result[i+1])

if __name__ == "__main__":
    main()
