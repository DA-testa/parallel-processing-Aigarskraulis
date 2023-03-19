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
    n, m = map(int, input().split())
    data = list(map(int, input().split()))
    result = process_in_parallel(n, m, data)
    for i in range(0, len(result), 2):
        print(result[i], result[i+1])

if __name__ == "__main__":
    main()
