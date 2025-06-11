import sys

def usage():
    """
    Print usage instructions to stderr.
    """
    print(f"Usage: python {sys.argv[0]} FNAME", file=sys.stderr)

def fletcher32_checksum(filename):
    """
    Compute the Fletcher-32 checksum for a given file.

    Parameters:
    - filename (str): Path to the file.

    Returns:
    - int: The computed Fletcher-32 checksum as a 32-bit integer.
    """
    sum1 = 0
    sum2 = 0

    try:
        # Open the file in binary read mode
        with open(filename, 'rb') as f:
            while True:
                # Read one byte at a time
                byte = f.read(1)
                if not byte:
                    break  # End of file

                # Convert byte to integer value
                elem = byte[0]

                # Update Fletcher-32 sums with modulo 65535
                sum1 = (sum1 + elem) % 65535
                sum2 = (sum2 + sum1) % 65535

    except FileNotFoundError:
        # Print error and exit if file is not found
        print(f"fopen() for {filename} returned NULL, quitting", file=sys.stderr)
        sys.exit(2)

    # Combine the two 16-bit sums into a single 32-bit value
    f32 = (sum2 << 16) | sum1
    return f32

def main():
    """
    Main function to handle command-line argument and display checksum.
    """
    # Ensure exactly one argument is provided (the filename)
    if len(sys.argv) != 2:
        usage()
        sys.exit(1)

    filename = sys.argv[1]

    # Compute Fletcher-32 checksum
    checksum = fletcher32_checksum(filename)

    # Print the filename and its checksum in 8-digit hexadecimal
    print(f"{filename}: {checksum:08x}")

if __name__ == "__main__":
    main()
