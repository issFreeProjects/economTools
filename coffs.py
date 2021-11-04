from math import log,exp
################## part 1
def fp(i,n):
    return (1+i)**n
def pf(i,n):
    return 1/fp(i,n)
###
def fa(i,n):
    return ((1+i)**n-1)/i
def af(i,n):
    return 1/fa(i,n)
###
def pa(i,n):
    return ((1+i)**n-1)/(i*(1+i)**n)
def ap(i,n):
    return 1/pa(i,n)


################## part 2
def pg(i,n):
    return ((1+i)**n-i*n-1)/(i*i*(1+i)**n)
def gp(i,n):
    return 1/pg(i,n)
###
def fg(i,n):
    return ((1+i)**n-1)/i**2 - n/i
def gf(i,n):
    return 1/fg(i,n)
###
def ag(i,n):
    return ((1+i)**n-i*n-1)/(i*(1+i)**n-1)
def ga(i,n):
    return 1/ag(i,n)


################## part 3
def pa1(i,j,n):
    if(i==j):
        return n/(1+i)
    else:
        return ( 1-( (1+j)**n)/((1+i)**n) )/(i-j)
###
def fa1(i,j,n):
    if(i==j):
        return n*(1+i)**(n-1)
    else:
        return ((1+i)**n-(1+j)**n)/(i-j)


################## part 4
def ie(r,t):
    return (1+r/t)**t-1
###
def pf_inf(r,n):
    return exp(-r*n)
def fp_inf(r,n):
    return 1/pf_inf(r,n)
###
def fa_inf(r,n):
    return (exp(r*n)-1)/(exp(r)-1)
def af_inf(r,n):
    return 1/fa(r,n)
###
def pa_inf(r,n):
    return (exp(r*n)-1)/(exp(r*n)*(exp(r)-1))
def ap_inf(r,n):
    return 1/pa_inf(r,n)
###
def pg_inf(r,n):
    return (exp(r*n)-1-n*(exp(r)-1))/(exp(r*n)*(exp(r)-1)**2)
def gp_inf(r,n):
    return 1/pg_inf(r,n)
###
def ag_inf(r,n):
    return 1/(exp(r)-1) - n/(exp(r*n)-1)
def ga_inf(r,n):
    return 1/ag_inf(r,n)


################## part 5
def r_ie(ie):
    return log(1+ie)
###
def p_fbar(ie,n):
    r = r_ie(ie)
    return (exp(r)-1)/(r*exp(n))
###
def p_abar(ie,n):
    r = r_ie(ie)
    return (exp(r)-1)/(r*exp(r*n))
###
def f_abar(ie,n):
    r = r_ie(ie)
    return (exp(r*n)-1)/r

