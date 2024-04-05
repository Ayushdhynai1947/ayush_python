class ExampleClass:
    def __init__(self, list_of_tuples):
        self.list = list_of_tuples

    def iterate_until_priority(self, priority):
        index = 0
        while index < len(self.list) and self.list[index] <= priority:
            print(f"Index: {index}, Tuple: {self.list[index]}")
            index += 1

# Example usage:
example_list = [(1, 5), (2, 8), (3, 3), (4, 9), (5, 2)]
example_instance = ExampleClass(example_list)
example_instance.iterate_until_priority(6)
