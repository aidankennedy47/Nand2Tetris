@10

D=A
@SP
A=M
M=D
@SP
M=M+1

@LCL
D=M
@0
D=D+A
@R13
A=M
M=D
@SP
M=M-1
A=M
D=M
@R13
A=M
M=D

@20

D=A
@SP
A=M
M=D
@SP
M=M+1

@ARG
D=M
@1
D=D+A
@R13
A=M
M=D
@SP
M=M-1
A=M
D=M
@R13
A=M
M=D

@30

D=A
@SP
A=M
M=D
@SP
M=M+1

@THIS
D=M
@2
D=D+A
@R13
A=M
M=D
@SP
M=M-1
A=M
D=M
@R13
A=M
M=D

@40

D=A
@SP
A=M
M=D
@SP
M=M+1

@THAT
D=M
@3
D=D+A
@R13
A=M
M=D
@SP
M=M-1
A=M
D=M
@R13
A=M
M=D

@50

D=A
@SP
A=M
M=D
@SP
M=M+1

@SP
M=M-1
A=M
D=M
@9
M=D

@60

D=A
@SP
A=M
M=D
@SP
M=M+1

@SP
M=M-1
A=M
D=M
@3
M=D

@70

D=A
@SP
A=M
M=D
@SP
M=M+1

@SP
M=M-1
A=M
D=M
@VMTranslator.5
M=D

