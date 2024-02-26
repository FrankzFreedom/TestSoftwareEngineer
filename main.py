def AlienToInt(Example, numstring):
    alien = {
        'A': 1,
        'B': 5,
        'Z': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'R': 1000
    }
    total = 0
    Explanation = []

    for i in range(len(numstring)):
        Cvalue = alien[numstring[i]]
        Nvalue = alien[numstring[i+1]] if i+1 < len(numstring) else 0

        if Cvalue < Nvalue:
            total -= Cvalue
            Explanation.append([f'{numstring[i]} = {alien[numstring[i]]}'])
        else:
            total += Cvalue
            Explanation.append([f'{numstring[i]} = {alien[numstring[i]]}'])

    explanation_str = ', '.join([' '.join(item) for item in Explanation])
    print(f'Example: {Example}')
    print(f'Output: {total}')
    print(f'Explanation: {explanation_str}')



AlienToInt(1, "AAA")
AlienToInt(2,"LBAAA")
AlienToInt(3,"RCRZCAB")