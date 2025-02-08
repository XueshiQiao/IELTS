import re


def process_line(line):
    # Skip empty lines or lines with "..."
    if not line.strip() or "..." in line:
        return None

    # Basic pattern: word + pronunciation + meaning
    pattern = r"^(\w+[\w\s\-\\/*]*?)\s+(/[^/]+/|\[[^\]]+\]|\{[^\}]+\})\s+(.+)$"

    match = re.match(pattern, line)
    if match:
        word, pronunciation, meaning = match.groups()
        # Clean up the data
        word = word.strip("* ")
        pronunciation = pronunciation.strip()
        meaning = meaning.strip()
        return [word, pronunciation, meaning]
    else:
        print(f"Skipping line: {line}")
        return None


def convert_file(input_file, output_file):
    with open(input_file, "r", encoding="utf-8") as f:
        lines = f.readlines()

    # Process and filter valid entries
    processed_lines = []
    for line in lines:
        result = process_line(line)
        if result:
            processed_lines.append(result)

    # Write to new file
    separator = "\t"
    with open(output_file, "w", encoding="utf-8") as f:
        # Write header
        f.write(f"Word{separator}Pronunciation{separator}Meaning\n")
        # Write data
        for word, pron, meaning in processed_lines:
            # Convert all pronunciation styles to /.../ format
            if pron.startswith("[") and pron.endswith("]"):
                pron = "/" + pron[1:-1] + "/"
            elif pron.startswith("{") and pron.endswith("}"):
                pron = "/" + pron[1:-1] + "/"
            f.write(f"{word}{separator}{pron}{separator}{meaning}\n")


# Use the function
convert_file(
    "IELTS Word List Unified.txt",
    "IELTS_Word_List_Formatted_with_Tab.txt",
)
