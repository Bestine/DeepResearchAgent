def show_prompt(prompt: str, title: str = "Prompt") -> None:
    """
    Display a prompt with a title in a readable format.

    Args:
        prompt (str): The prompt string to display.
        title (str): The title to display above the prompt.
    """
    print(f"\n{'=' * 60}")
    print(f"{title}")
    print(f"{'-' * 60}")
    print(prompt.strip())
    print(f"{'=' * 60}\n")