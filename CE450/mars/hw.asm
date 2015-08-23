li $t0, 150201133
li $t1, 0x10010060
sw $t0, ($t1)
add $s0, $t0,  $zero
sw $s0, 200($t1)
j L1
L1: add $s1, $s0, $t1
sw $s1, 400($t1)