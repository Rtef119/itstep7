def gen_step(chiclo):
    i=0
    while True:
        result = chiclo**i
        yield result
        if result>100**10:
            return
        i+=1

rez = gen_step(122345)
print(rez)
for t in rez:
    print(t)

