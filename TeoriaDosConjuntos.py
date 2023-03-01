A = [1, 2,3,4,5]
B = [2, 4, 6, 8]

inter = set(A).intersection(B)
union = set(A).union(B)
difference = set(A).difference(B)
subset = set(A).issubset(B)

print(f'A intersercção entre A e B é: {inter}')
print(f'A união entre A e B é: {union}')
print(f'A diferença entre A e B é: {difference}')
print(f'O conjunto A está contido no conjunto B, isto é {subset}')
