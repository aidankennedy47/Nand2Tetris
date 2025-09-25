// Finds the smallest element in the array of length R2 whose first element is at RAM[R1] and stores the result in R0.
// (R0, R1, R2 refer to RAM[0], RAM[1], and RAM[2], respectively.)

@R1
A = M
D = M

@R0
M = D

@R2
M = M - 1

@R1
M = M + 1

(LOOP)
@R2
D = M
@END
D;JEQ

@R1
A = M
D = M

@R0
D = D - M
@UPDATE
D;JLT

@SKIP
0;JMP

(UPDATE)
@R1
A = M
D = M
@R0
M = D

(SKIP)
@R1
M = M + 1

@R2
M = M - 1

@LOOP
0;JMP

(END)