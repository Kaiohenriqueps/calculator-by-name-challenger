import sys


def check_total(my_dict, ops_calc, result_str):
    for key, value in my_dict.items():
        if str(ops_calc) == str(value):
            return f"{result_str} {key}"
    return f"{result_str} unknown"


if __name__ == "__main__":
    my_dict = {}
    for input in sys.stdin:
        input_ops = input.split()
        command = input_ops[0]
        if command == "def":
            if my_dict:
                evals = input_ops[1:]
                my_dict[evals[0]] = evals[1]
            else:
                my_dict = {}
                evals = input_ops[1:]
                my_dict[evals[0]] = evals[1]
        elif command == "calc":
            evals = input_ops[1:]
            result_str = " ".join(input_ops[1:])
            result = []
            not_in_dict = False
            if my_dict:
                for elem in evals:
                    if elem == "=":
                        continue
                    if elem == "+" or elem == "-":
                        result.append(elem)
                    elif elem in my_dict:
                        result.append(my_dict[elem])
                    elif elem not in my_dict:
                        print(f"{result_str} unknown")
                        not_in_dict = True
                        break
                if not not_in_dict:
                    ops_calc = eval("".join(result))
                    print(check_total(my_dict, ops_calc, result_str))
            else:
                print(f"{result_str} unknown")
        elif command == "clear":
            my_dict = None
