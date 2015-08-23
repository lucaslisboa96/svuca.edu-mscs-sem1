li $t0, 150201133 #$t0 = original student ID
add $t1, $t0, $zero #$t1 = $t0, used for intermediate student ID for looping
LOOP: srl $t1, $t1, 1 #each time, SRL 1 bit of intermediate student ID $t1
blt $t1, 1, EXITLOOP # if intermediate student ID $t1 less than 1, exit loop
j LOOP #else, go back to top of the loop to repeat
EXITLOOP: add $t0, $t0, $t1 #on exit loop, add up both original student ID $t0 and intermediate one $t1
li $t3, 0x10010100 #t3 hold the address where we want to store $t0
sw $t0, 0($t3) #save final student ID to 0($t3)