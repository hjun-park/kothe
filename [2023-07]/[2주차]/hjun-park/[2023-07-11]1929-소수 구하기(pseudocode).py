M(시작 수), N(종료 수)
A(소수 리스트)

for 0 -> N: (1)
  A[i] = i

for N의 제곱근까지 반복: (1)
  만약 소수가 아니라면 (if A[i] == 0) 
    then continue

  for (j + j부터) -> (N+1): (j)
    # 해당 수의 배수들은 소수가 아니므로 지움
    A[j] = 0

for M -> N+1: (1)
  if A[i] != 0:
    print(A[i])
