# eucl(r, u, v, 0, u', v') = (r, u, v)
# eucl(r, u, v, r', u', v') = eucl(r', u', v', r - (r÷r')*r', u - (r÷r')*u', v - (r÷r')*v')  pour r' ≠ 0
# euclid(a, b) = eucl(a, 1, 0, b, 0, 1)

def eucl(r, u, v, rp, up, vp):
    if rp == 0:
        return (r, u, v)
    return eucl(rp, up, vp, r-(r//rp)*rp, u-(r//rp)*up, v-(r//rp)*vp)

def euclid(a,b):
    return eucl(a, 1, 0, b, 0, 1)[1:]




    