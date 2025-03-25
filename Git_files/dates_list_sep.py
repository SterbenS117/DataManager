import random


def split_dates(file_path):
    # Read the file
    with open(file_path, 'r') as file:
        content = file.read().strip()

    # Convert to list of dates
    dates = content.split(',')

    # Shuffle the dates randomly
    random.shuffle(dates)

    # Compute the split index
    split_index = int(0.7 * len(dates))

    # Create 70-30 split
    train_dates = dates[:split_index]
    test_dates = dates[split_index:]

    return train_dates, test_dates


# Example usage
file_path = r"E:\BigRun\2025_Big\sorted_dates_updates_2025_f.txt"  # Update with the actual file path
train, test = split_dates(file_path)

print("Train Set:", train)
print("Test Set:", test)