import json, sys

def par_gen(data, sep='-', filename='par'):
    """extract all parameters from JSON structure"""


    parameters = []

    for k, v in data.items():
        if isinstance(v, dict) and v:
            for l, w in v.items():
                if isinstance(w, dict) and w:
                    for m, x in w.items():
                        if isinstance(x, dict) and x:
                            for n, y in x.items():
                                if isinstance(y, dict) and y:
                                    for o, z in y.items():
                                        if isinstance(z, dict) and z:
                                            for p, aa in z.items():
                                                if isinstance(aa, dict) and aa:
                                                    for q, ab in aa.items():
                                                        if isinstance(ab, dict) and ab:
                                                            for r, ac in ab.items():
                                                                # print(k,l,m,n,o,p,q,r, sep=sep, end='')
                                                                # print('==>', ac)
                                                                parameters.append(k+sep+l+sep+m+sep+n+sep+o+sep+p+sep+q+sep+r)
                                                        else:
                                                            # print(k,l,m,n,o,p,q, sep=sep, end='')
                                                            # print('==>', ab)
                                                            parameters.append(k+sep+l+sep+m+sep+n+sep+o+sep+p+sep+q)
                                                elif isinstance(aa, list):
                                                    for a,b in aa[0].items():
                                                        # print(k,l,m,n,o,p,a, sep=sep, end='')
                                                        # print('==>', b)
                                                        parameters.append(k+sep+l+sep+m+sep+n+sep+o+sep+p+sep+a)
                                                else:
                                                    # print(k,l,m,n,o,p, sep=sep, end='')
                                                    # print('==>', aa)
                                                    parameters.append(k+sep+l+sep+m+sep+n+sep+o+sep+p)
                                        elif isinstance(z, list):
                                            try:
                                                for every in z:
                                                    for a,b in every.items():
                                                        if isinstance(b, dict) and b:
                                                            for c,d in b.items():
                                                                # print(k,l,m,n,o,'*',z.index(every),'*',a,c, sep=sep, end='')
                                                                # print('==>', d)
                                                                parameters.append(k+sep+l+sep+m+sep+n+sep+o+'*'+str(z.index(every))+'*'+a+sep+c)
                                                        else:
                                                            # print(k,l,m,n,o,'*',z.index(every),'*',a, sep=sep, end='')
                                                            # print('==>', b)
                                                            parameters.append(k+sep+l+sep+m+sep+n+sep+o+'*'+str(z.index(every))+'*'+a)
                                            except AttributeError:
                                                for item in z:
                                                    # print(k,l,m,n,o, sep=sep, end='')
                                                    # print('==>', item)
                                                    parameters.append(k+sep+l+sep+m+sep+n+sep+o+sep+item)

                                        else:
                                            # print(k,l,m,n,o, sep=sep, end='')
                                            # print('==>', z)
                                            parameters.append(k+sep+l+sep+m+sep+n+sep+o)
                                elif isinstance(y, list) and y:
                                    try:
                                        for a,b in y[0].items():
                                            # print(k,l,m,n,a, sep=sep, end='')
                                            # print('==>', b)
                                            parameters.append(k+sep+l+sep+m+sep+n+sep+a)
                                    except AttributeError:
                                        for item in y:
                                            # print(k,l,m,n, sep=sep, end='')
                                            # print('==>', item)
                                            parameters.append(k+sep+l+sep+m+sep+n+sep+item)

                                else:
                                    # print(k,l,m,n, sep=sep, end='')
                                    # print('==>', y)
                                    parameters.append(k+sep+l+sep+m+sep+n)
                        elif isinstance(x, list):
                            if isinstance(x[0],dict):
                                for a,b in x[0].items():
                                    # print(k,l,m,a, sep=sep, end='')
                                    # print('==>', b)
                                    parameters.append(k+sep+l+sep+m+sep+a)
                            else:
                                # print(k,l,m,x[0], sep=sep)
                                parameters.append(k+sep+m+sep+x[0])
                        else:
                            # print(k,l,m, sep=sep, end='')
                            # print('==>', x)
                            parameters.append(k+sep+l+sep+m)
                elif isinstance(w, list) and w:
                    try:
                        for every in w:
                            for a,b in every.items():
                                if isinstance(b, dict) and b:
                                    for c,d in b.items():
                                        # print(k,l,'*',w.index(every),'*',a,c, sep=sep, end='')
                                        # print('==>', d)
                                        parameters.append(k+sep+l+'*'+str(w.index(every))+'*'+a+sep+c)
                                else:
                                    # print(k,l,'*',w.index(every),'*',a, sep=sep, end='')
                                    # print('==>', b)
                                    parameters.append(k+sep+l+'*'+str(w.index(every))+'*'+a)
                    except AttributeError:
                        for item in w:
                            # print(k,l, sep=sep, end='')
                            # print('==>', item)
                            parameters.append(k+sep+l+item)
                else:
                    # print(k,l, sep=sep, end='')
                    # print('==>', w)
                    parameters.append(k+sep+l)
        else:
            # print(k, sep=sep, end='')
            # print('==>', v)
            parameters.append(k)

    with open(filename+'.json', 'w+') as par_file:
        json.dump(dict(zip(range(1, len(parameters) + 1), sorted(parameters))), par_file)

