#python3
# 221RDC045 Aigars Kraulis 18.grupa

def parallel_processing(n, m, data):
    threadList = []
    timeList = []
    output = []
    for i in range(n):
        threadList.append(i)
        timeList.append(0)

    counter = 0
    time = 0
    for i in range(m):
        output.append(threadList[counter])
        output.append(timeList[counter])
        while True:
            timeList[counter] = timeList[counter] + 1
            data[i] = data[i] - 1
            if data[i] == 0:
                break
        
        counter += 1
        if counter == len(threadList):
            counter = 0
            time += 1

    return output

def main():
    # TODO: create input from keyboard
    # input consists of two lines
    # first line - n and m
    # n - thread count 
    # m - job count
    firstInput = input()
    splitInput = firstInput.split()
    n = int(splitInput[0])
    m = int(splitInput[1])
    
    # second line - data 
    # data - contains m integers t(i) - the times in seconds it takes any thread to process i-th job
    data = list(map(int, input().split()))

    # TODO: create the function
    result = parallel_processing(n, m, data)

    
    # TODO: print out the results, each pair in it's own line
    for i in range(0, len(result), 2):
        print(result[i], result[i+1])

if __name__ == "__main__":
    main()


def parallel_processing(n, m, data):
    output = []
    # TODO: write the function for simulating parallel tasks, 
    # create the output pairs
    threadList = []
    timeList = []
    for i in range(n):
        threadList.append(i)
        timeList.append(0)

    counter = 0
    time = 0
    for i in range(m):
        output.append(threadList[counter])
        output.append(timeList[counter])
        while True:
            timeList[counter] = timeList[counter] + 1
            data[i] = data[i] - 1
            if data[i] == 0:
                break
        
        counter += 1
        if counter == len(threadList):
            counter = 0
            time += 1

    return output

def main():
    # TODO: create input from keyboard
    # input consists of two lines
    # first line - n and m
    # n - thread count 
    # m - job count
    n = 0
    m = 0

    # second line - data 
    # data - contains m integers t(i) - the times in seconds it takes any thread to process i-th job
    data = []

    # TODO: create the function
    result = parallel_processing(n, m, data)
    
    # TODO: print out the results, each pair in it's own line



if __name__ == "__main__":
    main()
