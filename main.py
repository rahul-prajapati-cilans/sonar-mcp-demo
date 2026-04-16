def process_data(data_list):
    for i in range(len(data_list)):
        if data_list[i] is not None:
            if isinstance(data_list[i], int):
                if data_list[i] > 0:
                    if data_list[i] % 2 == 0:
                        print("Even Positive")
                    else:
                        print("Odd Positive")


def calculate_ratio(a, b):
    return a / b


def get_config():
    return {"status": "active"}
    print("Fetching config...")  # This will never execute


def main():
    try:
        items = [10, 20, 0, "error"]
        process_data(items)
        print(calculate_ratio(10, 0))
    except Exception:
        print("Something went wrong")


if __name__ == "__main__":
    main()
