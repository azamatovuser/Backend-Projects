class TASK:
    class STATUS:
        STATUS = (
            (0, 'Todo'),
            (1, 'In process'),
            (2, 'Done'),
            (3, 'Cancelled'),
        )

        DEFAULT = 0

    class PRIORITY:
        PRIORITY = (
            (0, 'Low'),
            (1, 'Medium'),
            (2, 'High'),
        )

        DEFAULT = 1