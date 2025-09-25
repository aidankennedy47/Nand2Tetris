// Sorts the array of length R2 whose first element is at RAM[R1] in ascending order in place. Sets R0 to True (-1) when complete.
// (R0, R1, R2 refer to RAM[0], RAM[1], and RAM[2], respectively.)
 
@R2
D = M
@R0
M = D - 1

(OUTER)
@R0
D = M
@END
D;JEQ

@R1
D = M
@BASE
M = D
@BASE
D = M
@R1 
M = D

@R0
D = M
@R2
M = D

(INNER)
@R2
D = M
@INNER_END
D;JEQ

@R1
A = M
D = M

@R1
M = M + 1
A = M
D = D - M
@R1
M = M - 1

@SKIP
D;JLE

@R1
A = M
D = M
@TMP
M = D

@R1
M = M + 1
A = M
D = M
@R1
A = M
M = D

@TMP
D = M
@R1
M = M + 1
A = M
M = D

(SKIP)
@R1
M = M + 1

@R2
M = M - 1

@INNER
0;JMP

(INNER_END)
@R0
M = M - 1
@OUTER
0;JMP

(END)
@R0
M = -1

(TMP)
(BASE)