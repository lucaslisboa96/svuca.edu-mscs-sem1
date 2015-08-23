# DATA DECLARATION
.data
.float
const_5f:  		5.0
const_9f:  		9.0
const_32f: 		32.0
const_60f: 		60.0 		#testing purpose
.word 
const_studentid:	150201565 	#my student ID, in integer :) 
const_36:		36		
const_24:		24
const_101:		101
const_59:		59		


.text

# MAIN PROGRAM
main:	
	
	#######################################################
	## - Compress student ID to [25, 35] 
	## - Convert new student ID from Celcius to Fahrenheit
	#######################################################
	lw	$t0, const_studentid	# prepare input, load student_id to $t0
	lw 	$t5, const_24		# prepare input, load 24 to t5
	lw	$t6, const_36		# prepare input, load 36 to t6
	jal 	compress_student_id	# compress student id to range (24, 36) i.e. [25, 35]
	mov.s 	$f12, $f0		# copy compress_student_id output to f12, input  for c2f
	jal 	c2f			# call c2f, once completes, $f0 should be 0x42700000, which is 60 Fahrenheit Degrees
	mov.s	$f2, $f0		# copy & store result of c2f into f2, for verification

	#######################################################
	## - Compress student ID to [60, 100] 
	## - Convert new student ID from Celcius to Fahrenheit
	#######################################################
	lw	$t0, const_studentid	# prepare input, load student_id to $t0
	lw 	$t5, const_59		# prepare input, load 59 to t5
	lw	$t6, const_101		# prepare input, load 101 to t6
	jal 	compress_student_id	# compress student id to range (59, 101) i.e. [60, 100]
	mov.s 	$f12, $f0		# copy compress_student_id output to f12, input  for f2c
	jal 	f2c			# call c2f, once completes, $f0 should be 0x42700000, which is 60 Fahrenheit Degrees
	mov.s	$f4, $f0		# copy & store result of f2c into f4, for verification

	li	$v0, 10			# send exit signal
	syscall				# handover call to OS


# T(¡C) = 5.0/9.0 * (T(¡F) - 32.0)
f2c:	#input: $f12, output: $f0
	lwc1	$f16, const_5f          # f16 = 5.0
     	lwc1  	$f18, const_9f          # f18 = 9.0
     	div.s	$f16, $f16, $f18	# f16 = f16 / f18 = 5.0 / 9.0
     	lwc1	$f18, const_32f         # f18 = 32.0
     	sub.s	$f18, $f12, $f18	# f18 = f12 - f18 = T(¡F) - 32
     	mul.s	$f0,  $f16, $f18	# f0 = f16 * f18 = 5.0/9.0 * (T(¡F) - 32.0)
     	jr	$ra

# T(¡F) = T(¡C) ? 9/5 + 32
c2f:	#input: $f12, output: $f0
	lwc1	$f16, const_5f          # f16 = 5.0
     	lwc1  	$f18, const_9f          # f18 = 9.0
     	div.s	$f16, $f18, $f16	# f16 = f18 / f16 = 9.0 / 5.0 
     	mul.s	$f16, $f12, $f16	# f16 = f12 * f16 = T(¡C) * 9/5
     	lwc1	$f18, const_32f         # f18 = 32.0
     	add.s	$f0, $f16, $f18		# f0 = f16 + f18 = T(¡C) * 9/5 + 32.0
     	jr	$ra			# exit subroutine
     	
compress_student_id: #input: $t0, $t5, $t6, output: $f12
_LOOP:
	srl 	$t0, $t0, 1		# t0 = t0 / 2
	slt 	$t1, $t0, $t6		# t1 = 1 if Student_ID < 36, else 0
	slt	$t2, $t5, $t0		# t2 = 1 if 24 < Student_ID, else 0
	and 	$t1, $t1, $t2		# t1 = AND (t1, t2), i.e. t1 = 1 if 24 < Student_id < 36, else 0	
	bne	$t1, 1, _LOOP		# loop back to SRL until t1 = 1 (i.e. 24 < Student_id < 36)
_END_LOOP: 				# optional label
	mtc1 	$t0, $f0		# move t0 value to floating registers	
  	cvt.s.w $f0, $f0		# convert integer value in f0 to float
  	jr	$ra			# exit subroutine
