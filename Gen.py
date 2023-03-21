import time

generation = 10
axiom = 'A'
chr_1, rule_1 = 'A','AB'
chr_2, rule_2 = 'B','A'

# def apply_rules(axiom):
#     res = ''
#     for char in axiom:
#         if char == chr_1:
#             res += rule_1
#         else:
#             res += rule_2
#     return res

def apply_rules(axiom):
    return ''.join([rule_1 if char == chr_1 else rule_2 for char in axiom])

for gen in range(1, generation+1):
    print(f'generation {gen}: {axiom}')
    time.sleep(1)
    axiom = apply_rules(axiom)