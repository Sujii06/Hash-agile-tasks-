def get_largest(array, n):
    largest = 0
    for i in range(1, n):
        if array[i] > array[largest]:
            largest = i
    return largest


def get_second_largest(array, n):
    largest = get_largest(array, n)
    result = -1
    for i in range(n):
        if array[i] != array[largest]:
            if result == -1 or array[i] > array[result]:
                result = i
    return result


def main():
    elements = input("Enter the elements separated by space or comma: ")

    array = [int(x) for x in elements.replace(",", " ").split()]

    n = len(array)

    if n < 2:
        print("At least two elements are required to find the second largest.")
        return
    largest_ind = get_largest(array, n)
    second_largest_ind = get_second_largest(array, n)
    print(f"The largest element is: {array[largest_ind]}")

    if second_largest_ind != -1:
        print(f"The second largest element is: {array[second_largest_ind]}")
    else:
        print("There is no second largest element.")


main()
