import os


def ft_tqdm(lst: range) -> None:
    """
    function that mimics tqdm function
    It takes an iterable and prints a progress bar while it loops through it
    It yields the current element of the loop
    """
    # Get total elements and check for invalid
    total = len(lst)
    if total == 0:
        return

    # Get terminal width
    try:
        width = os.get_terminal_size().columns
    except OSError:
        width = 80  # fallback

    # Reserve space for percentage + brackets + counters
    reserved = 20  # Taking into account percent, bar components, counter
    bar_width = max(10, width - reserved)  # If width is less, then use 10

    # Enumerate returns a tuple (index,element) and unpacks it.
    # So I save it with i and elem
    for i, elem in enumerate(lst, start=1):
        progress = i / total
        percent = int(progress * 100)
        filled = int(progress * bar_width)
        # Format the bar string and the complete line that will be printed
        # Note that:
        # "=" * filled : to fill with '=' the current progress/amount
        # " " * (bar_width - filled - 1) : to fill with whitespace what remains
        bar = "=" * filled + ">" + " " * (bar_width - filled - 1)
        line = f"{percent:3d}%|[{bar}]| {i}/{total}"
        # Note: "\r" overwrites the old line, and flush print immediately
        print("\r" + line, end="", flush=True)
        yield elem
