"""13-Card Indian Rummy Deadwood & Drop Points Calculator."""

FACE_CARDS = {"A", "K", "Q", "J"}


def card_points(rank: str, is_joker: bool = False) -> int:
    """Return deadwood point value for a single card."""
    if is_joker:
        return 0
    r = rank.strip().upper()
    if r in FACE_CARDS:
        return 10
    val = int(r)
    if 2 <= val <= 10:
        return val
    raise ValueError(f"Unsupported card rank: {rank}")


def hand_penalty(unmatched_ranks: list[str], has_pure_sequence: bool = True) -> int:
    """Calculate capped deadwood penalty (max 80 points)."""
    if not unmatched_ranks:
        return 0
    raw = sum(card_points(r) for r in unmatched_ranks)
    # Without a pure sequence, all non-joker cards count up to the 80-pt cap.
    return min(80, raw) if has_pure_sequence else min(80, max(raw, 80))


if __name__ == "__main__":
    print("Deadwood penalty (K, Q, 8, 3):", hand_penalty(["K", "Q", "8", "3"]))
