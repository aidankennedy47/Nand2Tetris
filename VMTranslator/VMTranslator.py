class VMTranslator:
    def vm_push(segment, offset):
        if segment == 'constant':
            return f"@{offset}\n" + "\nD=A\n@SP\nA=M\nM=D\n@SP\nM=M+1\n"
        if segment == 'local':
            return f"@LCL\nD=M\n@{offset}\nA=D+A\nD=M\n@SP\nA=M\nM=D\n@SP\nM=M+1\n"
        if segment == 'argument':
            return f"@ARG\nD=M\n@{offset}\nA=D+A\nD=M\n@SP\nA=M\nM=D\n@SP\nM=M+1\n"
        if segment == 'this':
            return f"@THIS\nD=M\n@{offset}\nA=D+A\nD=M\n@SP\nA=M\nM=D\n@SP\nM=M+1\n"
        if segment == 'that':
            return f"@THAT\nD=M\n@{offset}\nA=D+A\nD=M\n@SP\nA=M\nM=D\n@SP\nM=M+1\n"
        if segment == 'temp':
            return f"@{5 + offset}\nD=M\n@SP\nA=M\nM=D\n@SP\nM=M+1\n"
        if segment == 'pointer':
            return f"@{3 + offset}\nD=M\n@SP\nA=M\nM=D\n@SP\nM=M+1\n"
        if segment == 'static':
            return f"@VMTranslator.{offset}\nD=M\n@SP\nA=M\nM=D\n@SP\nM=M+1\n"
        else:
            return ""

    def vm_pop(segment, offset):
        if segment == 'local':
            return f"@LCL\nD=M\n@{offset}\nD=D+A\n@R13\nM=D\n@SP\nAM=M-1\nD=M\n@R13\nA=M\nM=D\n"
        if segment == 'argument':
            return f"@ARG\nD=M\n@{offset}\nD=D+A\n@R13\nM=D\n@SP\nAM=M-1\nD=M\n@R13\nA=M\nM=D\n"
        if segment == 'this':
            return f"@THIS\nD=M\n@{offset}\nD=D+A\n@R13\nM=D\n@SP\nAM=M-1\nD=M\n@R13\nA=M\nM=D\n"
        if segment == 'that':
            return f"@THAT\nD=M\n@{offset}\nD=D+A\n@R13\nM=D\n@SP\nAM=M-1\nD=M\n@R13\nA=M\nM=D\n"
        if segment == 'temp':
            return f"@SP\nAM=M-1\nD=M\n@{5+offset}\nM=D\n"
        if segment == 'pointer':
            base = 3 + offset
            return f"@SP\nAM=M-1\nD=M\n@{base}\nM=D\n"
        if segment == 'static':
            return f"@SP\nAM=M-1\nD=M\n@VMTranslator.{offset}\nM=D\n"
        else:
            return ""

    def vm_add():
        return "@SP\nAM=M-1\nD=M\n@SP\nAM=M-1\nM=M+D\n@SP\nM=M+1\n"

    def vm_sub():
        return "@SP\nAM=M-1\nD=M\n@SP\nAM=M-1\nM=M-D\n@SP\nM=M+1\n"

    def vm_neg():
        return "@SP\nAM=M-1\nD=M\nM=-D\n@SP\nM=M+1\n"

    def vm_eq():
        return "@SP\nAM=M-1\nD=M\nA=A-1\nD=M-D\n@IS_EQUAL\nD;JEQ\n@SP\nA=M-1\nM=0\n@END\n0;JMP\n(IS_EQUAL)\n@SP\nA=M-1\nM=-1\n(END)\n"

    def vm_gt():
        return "@SP\nAM=M-1\nD=M\nA=A-1\nD=M-D\n@IS_GREATER\nD;JGT\n@SP\nA=M-1\nM=0\n@END\n0;JMP\n(IS_GREATER)\n@SP\nA=M-1\nM=-1\n(END)\n"

    def vm_lt():
        return ""

    def vm_and():
        return "@SP\nAM=M-1\nD=M\nA=A-1\nM=M&D\nM"

    def vm_or():
        return "@SP\nAM=M-1\nD=M\nA=A-1\nM=M|D\n"

    def vm_not():
        return ""

    def vm_label(label):
        return f"({label})\n"

    def vm_goto(label):
        return f"@{label}\n0;JMP\n"

    def vm_if(label):
        return f"@SP\nAM=M-1\nD=M\n@{label}\nD;JNE"

    def vm_function(function_name, n_vars):
        asm = f"({function_name})\n"
        for i in range(n_vars):
            asm += "@0\nD=M\n@SP\nA=M\nM=D\n@SP\nM=M+1\n"
        return asm

    def vm_call(function_name, n_args):
        call_counter = 0
        ret_label = f"RET_ADDRESS{call_counter}"
        call_counter += 1

        asm = ""

        asm+= f"@{ret_label}\nD=A\n@SP\nA=M\nM=D\n@SP\nM=M+1\n"

        for segment in ["LCL", "ARG", "THIS", "THAT"]:
            asm += f"@{segment}\nD=M\n@SP\nA=M\nM=D\n@SP\nM=M+1\n"
        
        asm += "@SP\nD=M\n"
        asm += f"@5\nD=D-A\n@{n_args}\nM=D\n"

        asm += "@SP\nD=M\n@LCL\nM=D\n"
        asm += f"@{function_name}\n0;JMP\n"

        asm += f"({ret_label})\n"
        return asm

    def vm_return():
        return ""

# A quick-and-dirty parser when run as a standalone script.
if __name__ == "__main__":
    import sys
    if(len(sys.argv) > 1):
        with open(sys.argv[1], "r") as a_file:
            for line in a_file:
                tokens = line.strip().lower().split()
                if(len(tokens)==1):
                    if(tokens[0]=='add'):
                        print(VMTranslator.vm_add())
                    elif(tokens[0]=='sub'):
                        print(VMTranslator.vm_sub())
                    elif(tokens[0]=='neg'):
                        print(VMTranslator.vm_neg())
                    elif(tokens[0]=='eq'):
                        print(VMTranslator.vm_eq())
                    elif(tokens[0]=='gt'):
                        print(VMTranslator.vm_gt())
                    elif(tokens[0]=='lt'):
                        print(VMTranslator.vm_lt())
                    elif(tokens[0]=='and'):
                        print(VMTranslator.vm_and())
                    elif(tokens[0]=='or'):
                        print(VMTranslator.vm_or())
                    elif(tokens[0]=='not'):
                        print(VMTranslator.vm_not())
                    elif(tokens[0]=='return'):
                        print(VMTranslator.vm_return())
                elif(len(tokens)==2):
                    if(tokens[0]=='label'):
                        print(VMTranslator.vm_label(tokens[1]))
                    elif(tokens[0]=='goto'):
                        print(VMTranslator.vm_goto(tokens[1]))
                    elif(tokens[0]=='if-goto'):
                        print(VMTranslator.vm_if(tokens[1]))
                elif(len(tokens)==3):
                    if(tokens[0]=='push'):
                        print(VMTranslator.vm_push(tokens[1],int(tokens[2])))
                    elif(tokens[0]=='pop'):
                        print(VMTranslator.vm_pop(tokens[1],int(tokens[2])))
                    elif(tokens[0]=='function'):
                        print(VMTranslator.vm_function(tokens[1],int(tokens[2])))
                    elif(tokens[0]=='call'):
                        print(VMTranslator.vm_call(tokens[1],int(tokens[2])))

        