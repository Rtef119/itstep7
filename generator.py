def gen_step(chiclo, max_step):
    i=0
    for n in range(max_step):
        yield chiclo**i
        i+=1

rez = gen_step(100000, 500)
print(rez)
for t in rez:
    print(t)

