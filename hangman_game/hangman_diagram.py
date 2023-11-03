# this is the image of life stages of life when guess


def draw_hangman(attempts):
    hangman_stages = [
        """
            +---+
            |   |
                |
                |
                |
                |
        =========

        You are completely hanged bro
        """,
        """
            +---+
            |   |
            O   |
                |
                |
                |
        =========
        """,
        """
            +---+
            |   |
            O   |
            |   |
                |
                |
        =========
        """,
        """
            +---+
            |   |
            O   |
           /|   |
                |
                |
        =========
        """,
        """
            +---+
            |   |
            O   |
           /|\  |
                |
                |
        =========
        """,
        """
            +---+
            |   |
            O   |
           /|\  |
           /    |
                |
        =========
        """,
        """
            +---+
            |   |
            O   |
           /|\  |
           / \  |
                |
        =========
        """
    ]

    return hangman_stages[attempts]

