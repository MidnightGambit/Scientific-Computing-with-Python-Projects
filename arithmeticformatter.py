def arithmetic_arranger(problems, show_answers=False):
    # Check if there are too many problems
    if len(problems) > 5:
        return "Error: Too many problems."
    
    # Initialize the strings for the lines of the result
    top_row = ""
    second_row = ""
    dashes_row = ""
    answers_row = ""
    
    for problem in problems:
        # Split each problem into operands and operator
        parts = problem.split()
        
        # Validate if the operator is correct
        if parts[1] not in ['+', '-']:
            return "Error: Operator must be '+' or '-'."
        
        # Validate if the operands are digits
        if not parts[0].isdigit() or not parts[2].isdigit():
            return "Error: Numbers must only contain digits."
        
        # Validate if the operands are within the length limit
        if len(parts[0]) > 4 or len(parts[2]) > 4:
            return "Error: Numbers cannot be more than four digits."
        
        # Format the top row, second row and dashes
        width = max(len(parts[0]), len(parts[2])) + 2  # Operator and space
        
        top_row += f"{parts[0]:>{width}}    "
        second_row += f"{parts[1]} {parts[2]:>{width - 2}}    "
        dashes_row += '-' * width + "    "
        
        # If show_answers is True, calculate and format the answers
        if show_answers:
            if parts[1] == '+':
                result = str(int(parts[0]) + int(parts[2]))
            else:
                result = str(int(parts[0]) - int(parts[2]))
            answers_row += f"{result:>{width}}    "
    
    # Remove the extra space at the end of each row
    top_row = top_row.rstrip()
    second_row = second_row.rstrip()
    dashes_row = dashes_row.rstrip()
    if show_answers:
        answers_row = answers_row.rstrip()
    
    # Return the final formatted string
    if show_answers:
        return f"{top_row}\n{second_row}\n{dashes_row}\n{answers_row}"
    else:
        return f"{top_row}\n{second_row}\n{dashes_row}"
