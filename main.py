from mpmath import mp
import sys
import time

def compute_pi_chunk(start_digit, chunk_size):
    mp.dps = start_digit + chunk_size + 10  # buffer for edge precision
    pi_str = str(mp.pi)[2:]  # strip the "3."
    return pi_str[start_digit:start_digit + chunk_size]

def save_pi_chunks(filename, total_digits, chunk_size=500):
    start_time = time.time()
    with open(filename, 'w') as f:
        for current_digit in range(0, total_digits, chunk_size):
            chunk = compute_pi_chunk(current_digit, chunk_size)
            f.write(chunk)

            elapsed = time.time() - start_time
            processed = min(current_digit + chunk_size, total_digits)
            estimated_total = (elapsed / processed) * total_digits
            remaining = estimated_total - elapsed
            percent = (processed / total_digits) * 100

            sys.stdout.write(
                f"\rProgress: {processed:,}/{total_digits:,} "
                f"({percent:.6f}%) | Estimated time left: {remaining/60:.2f} min"
            )
            sys.stdout.flush()
    sys.stdout.write("\nDone!\n")

if __name__ == "__main__":
    print("PiCalc by SaiPa\n")

    try:
        total_digits = int(input("Enter the total number of digits of Pi to calculate: "))
        chunk_size = int(input("Enter the chunk size: "))

        if total_digits <= 0 or chunk_size <= 0:
            print("Both values must be positive integers.")
        else:
            save_pi_chunks("pi_digits.txt", total_digits=total_digits, chunk_size=chunk_size)

    except ValueError:
        print("Please enter valid integer values.")
