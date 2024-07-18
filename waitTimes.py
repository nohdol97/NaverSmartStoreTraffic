import setValues

def load_wait_times_from_file():
    try:
        wait_times = {}
        with open('waitTimes.txt', 'r', encoding='utf-8') as f:
            for line in f:
                if ':' in line:
                    key, value = line.strip().split(':')
                    min_value, max_value = map(float, value.split('~'))
                    wait_times[key] = (min_value, max_value)
        setValues.waitTimes = wait_times
        print("Wait times loaded from waitTimes.txt")
    except Exception as e:
        print(f"Error loading wait times from file: {e}")