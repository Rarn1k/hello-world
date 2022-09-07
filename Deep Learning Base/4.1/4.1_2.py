items = [('one', 'two'), ('three', 'four'), ('five', 'six'), ('string', 'a')]
"""Отсортировать этот список по последней букве второго элемента каждого tuple, т.е. получить такой список."""
sorted_items = sorted(items, key=lambda x: x[1][-1])
