// Finds the smallest element in the array of length R2 whose first element is at RAM[R1] and stores the result in R0.
// (R0, R1, R2 refer to RAM[0], RAM[1], and RAM[2], respectively.)

//    R2 is size
//    R1 is array (address obv)
//

//    int @R0 = R1[0];
@R1
A = M
D = M

@R0
M = D
//    for (int i = 1; i < size; ++i) {
@I
M = 1
(LOOPSTART)
@I
M = M + 1
@I
D = M
@R2
D = D - M
@LOOPEND
D;JLE

@SIGN1
M = -1
@SIGN2
M = -1

// if r0 < 0 {sign1++}
@R0
D = M
@R0END
D;JGE
@SIGN1
M = M + 1
(R0END)

// if r1I < 0 {sign2++}
@I
D = M
@R1
A = D + M
D = M
@R1IEND
D;JGE
@SIGN2
M = M + 1
(R1IEND)
@SIGN1
D = M
@R1INEG
D;JEQ
@R1IPOS
0;JMP
(R1INEG)
@SIGN2
D = M
@SKIPIF
D;JNE
@DOIF
0;JMP
(R1IPOS)
@SIGN2
D = M
@STARTIF
D;JNE
@IFSKIP
0;JMP
//        if (R1[i] < @R0) { @R0 = R1[i]; }
(STARTIF)
@I
D = M
@R1
A = D + M
D = M
@R0
D = D - M
@R1END
D;JGE
(DOIF)
@I
D = M
@R1
A = D + M
D = M
@R0
M = D
(R1END)
(IFSKIP)
@LOOPSTART
0;JMP
(LOOPEND)
//    }

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