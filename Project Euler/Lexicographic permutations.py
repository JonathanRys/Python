
digits = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
counter = 1
for a in digits:
    for b in digits:
        if b == a: continue
        for c in digits:
            if c in [a, b]: continue
            for d in digits:
                if d in [a, b, c]: continue
                for e in digits:
                    if e in [a, b, c, d]: continue
                    for f in digits:
                        if f in [a, b, c, d, e]: continue
                        for g in digits:
                            if g in [a, b, c, d, e, f]: continue
                            for h in digits:
                                if h in [a, b, c, d, e, f, g]: continue
                                for i in digits:
                                    if i in [a, b, c, d, e, f, g, h]: continue
                                    for j in digits:
                                        if j in [a, b, c, d, e, f, g, h, i]: continue
                                        if counter == 1000000:
                                            print(counter)
                                            print(str(a) + str(b) + str(c) + str(d) + str(e) + str(f) + str(g) + str(h) + str(i) + str(j))
                                        counter += 1
