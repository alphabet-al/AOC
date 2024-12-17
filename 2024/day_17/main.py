
def get_combo_operand_value(operand, registers):
    if 0 <= operand <= 3:
        return operand
    elif operand == 4:
        return registers[0]
    elif operand == 5:
        return registers[1]
    elif operand == 6:
        return registers[2]
    elif operand > 6:
        raise ValueError(f"Combo operand invalid: {operand}")
        

def run_instruction(opcode, operand, reg, ins_ptr, output):
    combo = get_combo_operand_value(operand, reg)
    if opcode == 0:
        numerator = reg[0]
        reg[0] = int(numerator / 2 ** combo)
    elif opcode == 1:
        reg[1] = reg[1] ^ operand
    elif opcode == 2:
        reg[1] = combo % 8
    elif opcode == 3:
        if reg[0] != 0:
            return operand, output
    elif opcode == 4:
        reg[1] = reg[1] ^ reg[2]
    elif opcode == 5:
        output.append(combo % 8)
    elif opcode == 6:
        numerator = reg[0]
        reg[1] = int(numerator / 2 ** combo)
    elif opcode == 7:
        numerator = reg[0]
        reg[2] = int(numerator / 2 ** combo)
    
    ins_ptr += 2  
    print(output)
    return ins_ptr, output

def run_prog(reg, prog):
    instruction_ptr = 0
    output = []

    while instruction_ptr < len(prog):
    
        opcode = prog[instruction_ptr]
        operand = prog[instruction_ptr + 1]
        instruction_ptr, output = run_instruction(opcode, operand, reg, instruction_ptr, output)

    output = [str(ch) for ch in output]
    output = ",".join(output)

    return output



def main(reg, prog):
    ans = run_prog(reg, prog)
    print(ans)
        

if __name__ == "__main__":
    path = r"C:\AOC\2024\day_17\test_data.txt"
    # path = r"C:\AOC\2024\day_17\data.txt"

    with open(path, "r") as f:
        top, bottom = f.read().split("\n\n")
    
    registers = [int(row.split(": ")[1]) for row in top.splitlines()]
    program = [int(ch) for ch in bottom.split(": ")[1].split(",")]

    main(registers, program)
        