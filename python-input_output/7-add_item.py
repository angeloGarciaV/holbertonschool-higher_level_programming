#!/usr/bin/python3
"""Add all arguments to a Python list and save them to a file."""
if __name__ == "__main__":
    import sys
    save_to_json_file = __import__('7-save_to_json_file').save_to_json_file
    load_from_json_file = \
        __import__('8-load_from_json_file').load_from_json_file
    try:
        items = load_from_json_file("add_item.json")
    except FileNotFoundError:
        with open("add_item.json", "w") as f:
            f.write("[]")
    items.extend(sys.argv[1:])
    save_to_json_file(items, "add_item.json")
