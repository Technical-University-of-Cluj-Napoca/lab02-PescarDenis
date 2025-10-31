import sys
from BST import BST
from search_engine import search_loop

def main():
    ENGLISH_URL = "https://raw.githubusercontent.com/dwyl/english-words/refs/heads/master/words.txt"
    ROMANIAN_URL = "https://raw.githubusercontent.com/davidxbors/romanian_wordlists/refs/heads/master/wordlists/ro_50k.txt"
    source = None
    kwargs = {}

    #Parse the CLI arguments
    if len(sys.argv) == 3 and sys.argv[1] == "--file":
        source = sys.argv[2]
        kwargs["file"] = True
    elif len(sys.argv) == 3 and sys.argv[1] == "--url":
        source = sys.argv[2]
        kwargs["url"] = True
    elif len(sys.argv) == 3 and sys.argv[1] == "--lang":
        lang = sys.argv[2].lower()
        if lang == "en":
            source = ENGLISH_URL
        elif lang == "ro":
            source = ROMANIAN_URL
        else:
            print("Unsupported language. Use 'en' or 'ro'.")
            sys.exit(1)
        kwargs["url"] = True
    else:
        print("Usage: ")
        print("py main.py --file <path>")
        print("py main.py --url <url>")
        print("py main.py --lang [en|ro]")
        sys.exit(1)

    print(f"Building BST from {source}")
    bst = BST(source, **kwargs)
    print("BST built successfully!")

    print("\nStart typing to search (press ESC to exit):")
    search_loop(bst)


if __name__ == "__main__":
    main()
