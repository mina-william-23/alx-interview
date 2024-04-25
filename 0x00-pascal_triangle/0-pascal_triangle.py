#!/usr/bin/python3
'''Pascal's Triangle is a mathematical construct that follows a simple recursive formula.'''


# Create a function that will return a 2D list representation of Pascal's Triangle up to the nth level.
def generate_pascals_triangle(num_rows):
    """Generate Pascal's Triangle up to the nth level."""
    triangle = []

    for row_num in range(num_rows):
        row = [None] * (row_num + 1)
        row[0], row[-1] = 1, 1

        for j in range(1, len(row) - 1):
            row[j] = triangle[row_num - 1][j - 1] + triangle[row_num - 1][j]

        triangle.append(row)

    return triangle
