import numpy as np

def cart_to_sph(cart_co_ords):
# transformation between co-ordinate systems

    x, y, z = cart_co_ords[:,0], cart_co_ords[:,1], cart_co_ords[:,2]
    r = np.linalg.norm(cart_co_ords, axis=1)
    azi = np.arctan2(y,x)
    elev = np.arccos(z/r)

    return np.array([r, azi, elev]).T


def sph_to_cart(sph_co_ords):

    # allow for lack of r value (i.e. for unit sphere)
    if sph_co_ords.shape[1] < 3:
        azi, elev = sph_co_ords[:,0], sph_co_ords[:,1]
        r = 1

    else:
        r, azi, elev = sph_co_ords[:,0], sph_co_ords[:,1], sph_co_ords[:,2]

    x = r * np.cos(azi) * np.sin(elev)
    y = r * np.sin(azi) * np.sin(elev)
    z = r * np.cos(elev)

    return np.array([x, y, z]).T


def normalise(x, axis=None):
    return x / np.linalg.norm(x, axis=axis).reshape(-1,1)



def f_to_k( f, c=343 ):
    # converts frequency in Hz to wavenumber

    k = (f / (1/(2*np.pi)) / c)

    return k


def k_to_f( k, c=343 ):
    # converts wavenumber to frequency in Hz

    f = (k*c) * (1/(2*np.pi))

    return f