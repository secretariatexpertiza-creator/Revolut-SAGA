with open(out, "w", encoding="utf-8") as g:
    nr = 1

    for d,t,eur,ron,exp in cache:

        exp = exp.replace(";", " ")[:50]  # IMPORTANT

        if t == "inc":
            g.write(f"{d};OP;{nr};{exp};5124.3;704;{eur:.2f};EUR\n")
            nr += 1

        elif t == "pl":
            cont = map_account(exp)
            g.write(f"{d};OP;{nr};{exp};{cont};5124.3;{eur:.2f};EUR\n")
            nr += 1

        elif t == "fx":
            kurs = get_bnr(d)
            diff = round(eur * kurs - ron, 2)

            g.write(f"{d};NC;{nr};Schimb;581.2;5124.3;{eur:.2f};EUR\n")
            nr += 1

            g.write(f"{d};NC;{nr};Schimb;5121.3;581.2;{ron:.2f};RON\n")
            nr += 1

            if diff > 0:
                g.write(f"{d};NC;{nr};Dif curs;665;581.2;{diff:.2f};RON\n")
            elif diff < 0:
                g.write(f"{d};NC;{nr};Dif curs;581.2;765;{abs(diff):.2f};RON\n")

            nr += 1