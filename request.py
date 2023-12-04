class Request:
    def __init__(self, mode, input_data, expanded, output_file=None):
        self.mode = mode  # 'pokemon', 'ability', or 'move'
        self.input_data = input_data  # Name, ID, or filename
        self.expanded = expanded  # Boolean flag for expanded information
        self.output_file = output_file  # Optional output file

    # You might add methods to validate or process the request
