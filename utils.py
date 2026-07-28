def clean_command(text: str) -> str:
    """Lowercase and strip a voice command string for easier matching."""
    return text.strip().lower()
