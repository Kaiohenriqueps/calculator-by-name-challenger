import sys


def check_total(my_dict, ops_calc, result_str):
    for key, value in my_dict.items():
        if str(ops_calc) == str(value):
            return f"{result_str} {key}"
    return f"{result_str} unknown"


def def_op(my_dict, input_ops):
    evals = input_ops[1:]
    if my_dict:
        my_dict[evals[0]] = evals[1]
    else:
        my_dict = {}
        my_dict[evals[0]] = evals[1]
    return my_dict


def calc_op(my_dict, input_ops):
    evals = input_ops[1:]
    result_str = " ".join(input_ops[1:])
    result = []
    if my_dict:
        for elem in evals:
            print(f"elem: {elem}")
            if elem != "=":
                if elem not in my_dict and elem != "-" and elem != "+":
                    return f"{result_str} unknown"
                else:
                    if elem in my_dict:
                        result.append(my_dict[elem])
                    if elem == "+" or elem == "-":
                        result.append(elem)
        ops_calc = eval("".join(result))
        return check_total(my_dict, ops_calc, result_str)
    else:
        return f"{result_str} unknown"


if __name__ == "__main__":
    my_dict = {}
    for input in sys.stdin:
        input_ops = input.split()
        command = input_ops[0]
        if command == "def":
            my_dict = def_op(my_dict, input_ops)
        elif command == "calc":
            print(calc_op(my_dict, input_ops))
        elif command == "clear":
            my_dict = None
        print(f"my_dict: {my_dict}")
