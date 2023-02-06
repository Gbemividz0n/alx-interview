import sys

def process_line(line, metrics):
    parts = line.split()
    if len(parts) != 9:
        return

    try:
        status_code = int(parts[8])
        file_size = int(parts[-1])
    except ValueError:
        return

    if status_code not in metrics['status_codes']:
        return

    metrics['total_size'] += file_size
    metrics['status_codes'][status_code] += 1

def print_metrics(metrics):
    print("File size: {}".format(metrics['total_size']))
    for status_code in sorted(metrics['status_codes'].keys()):
        print("{}: {}".format(status_code, metrics['status_codes'][status_code]))

def main():
    metrics = {
        'total_size': 0,
        'status_codes': {
            200: 0,
            301: 0,
            400: 0,
            401: 0,
            403: 0,
            404: 0,
            405: 0,
            500: 0
        }
    }
    line_count = 0

    try:
        for line in sys.stdin:
            process_line(line, metrics)
            line_count += 1
            if line_count % 10 == 0:
                print_metrics(metrics)
    except KeyboardInterrupt:
        print_metrics(metrics)

if __name__ == '__main__':
    main()
