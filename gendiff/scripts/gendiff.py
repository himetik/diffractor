"""Generate diff of two files."""

from gendiff.cli import parse_cli_args
from gendiff.gendiff import generate_diff


def main():
    """Generate diff of two files."""
    # Parse command-line arguments using the parse_cli_args function
    args = parse_cli_args()

    # Generate the diff between the two files specified by the arguments
    # and format it according to the specified format
    diff = generate_diff(args.first_file, args.second_file, args.format)

    # Print the generated diff
    print(diff)


# Ensure the main function is called only when this script is executed directly
if __name__ == '__main__':
    main()
