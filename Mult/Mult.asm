// This file is based on part of www.nand2tetris.org
// and the book "The Elements of Computing Systems"
// by Nisan and Schocken, MIT Press.
// File name: Mult.asm

// Multiplies R1 and R2 and stores the result in R0.
// (R0, R1, R2 refer to RAM[0], RAM[1], and RAM[2], respectively.)

@R0
M=0
// check if R1 is negative
//    if (R1 < 0) {
//        R1 = -R1;
//        SIGN++;}
@SIGN
M = -1

@R1
D = M
@R1END
D;JGE

@R1
M = -M
@SIGN
M = M + 1
(R1END)

@R2
D = M
@R2END
D;JGE

@R2
M = -M
@SIGN
M = M + 1
(R2END)

@R1
D=M
@R3
M=D

@R2
D=M
@R4
M=D

@R5
M=0

@R3
D=M
@R1_POS
D;JGE
@R5
M=M+1     
D=-D
@R3
M=D
(R1_POS)

@R4
D=M
@R2_POS
D;JGE
@R5
M=M+1     
D=-D
@R4
M=D
(R2_POS)

(LOOP)
@R4
D=M
@AFTER_LOOP
D;JEQ

@R0
D=M
@R3
D=D+M
@R0
M=D

@R4
M=M-1

@LOOP

0;JMP

(AFTER_LOOP)
//if sign == 0{r0 = -r0}
@SIGN
D = M
@R0END
D;JNE
@R0
M = -M
(R0END)
(END)
@END
0;JMP