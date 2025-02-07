def process_data(data):
    # Step 1: Remove duplicates
    unique_data = []
    for item in data:
        if item not in unique_data:
            unique_data.append(item)

    # Step 2: Sort the data
    unique_data.sort(reverse=True)

    # Step 3: Calculate the sum of the sorted data
    total_sum = 0
    for value in unique_data:
        total_sum += value

    # Step 4: Find the average
    average = total_sum / len(unique_data) if len(unique_data) > 0 else 0

    # Step 5: Check for any negative values and replace with zero
    for i in range(len(unique_data)):
        if unique_data[i] < 0:
            unique_data[i] = 0

    # Step 6: Convert list to string (with redundancy)
    str_data = ''
    for num in unique_data:
        str_data += str(num) + ', '

    # Final Step: Return results
    return unique_data, total_sum, average, str_data
