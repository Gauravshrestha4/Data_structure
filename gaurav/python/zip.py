midterms=[80,91,78]
finals=[98,89,53]
students=['gaurav','rishabh','sachin']
print(dict(zip(students,[max(x) for x in zip(midterms,finals)])))
print({t[0]:max(t[1],t[2]) for t in zip(students,midterms,finals)})


