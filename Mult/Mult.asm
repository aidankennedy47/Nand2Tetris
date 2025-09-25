// This file is based on part of www.nand2tetris.org
// and the book "The Elements of Computing Systems"
// by Nisan and Schocken, MIT Press.
// File name: Mult.asm

// Multiplies R1 and R2 and stores the result in R0.
// (R0, R1, R2 refer to RAM[0], RAM[1], and RAM[2], respectively.)


@R0
M = 0

@R1
D = M
@R1_POS
D;JGE
D = -D
@R1
M = D
(R1_POS)

@R2
D = M
@R2_POS
D;JGE
D = -D
@R2
M = D
(R2_POS)

(LOOP)
@R2
D = M
@END
D;JEQ

@R0
D = M
@R1
D = D + M
@R0
M = D

@R2
M = M - 1

@LOOP
0;JMP

(END)

@R1
D = M
@R1_NEG
D;JGE
D = -D
@R1
M = D

@R2
D = M
@R2_NEG
D;JGE
D = -D
@R2
M = D