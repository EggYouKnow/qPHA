import numpy as np
from scipy.optimize import curve_fit, root

# Data loading and analysis


def load_data(filename):
    ipt_dt = np.loadtxt(filename, delimiter=',', skiprows=1)
    data_fit = {'OD': [], 'FI': [], 'Pha(%)': []}
    data_pred = {'OD': [], 'FI': [], 'Pha(%)': []}
    for i in range(ipt_dt.shape[0]):
        if np.isnan(ipt_dt[i, 2]):
            data_pred['OD'].append(ipt_dt[i, 0])
            data_pred['FI'].append(ipt_dt[i, 1])
        else:
            data_fit['OD'].append(ipt_dt[i, 0])
            data_fit['FI'].append(ipt_dt[i, 1])
            data_fit['Pha(%)'].append(ipt_dt[i, 2])
    return data_fit, data_pred

# linear functions
def fit_func_linear(xdata, a, b1, b2, k):
    '''
    PHA = a*(OD-b1)/(k*(G-b2)-(O-b1))
    '''
    ydata = a*(xdata[:, 0]-b1)/(k*(xdata[:, 1] - b2)-(xdata[:, 0] - b1))
    return ydata

# exponential functions


def func(xdata, a, b1, b2, k, c):
    '''
    OD = b1 + a*(FI-b2)*PHA/(exp(k*PHA)+c)
    '''
    ydata = b1 + a*(xdata[:, 0]-b2)*xdata[:, 1]/(np.exp(k*xdata[:, 1])+c)
    return ydata


def fit_func_by_solve(z, x, y, a, b1, b2, k, c):
    return b1 + a*(y-b2)*z/(np.exp(k*z)+c)-x


def fit_func_exp(xdata, a, b1, b2, k, c):
    z = []
    params = [a, b1, b2, k, c]
    if xdata.shape[1] == 1:
        tmp = root(fit_func_by_solve, [0], args=(
            xdata[0], xdata[1], *params)).x
        return tmp[0]
    else:
        for i in range(xdata.shape[0]):
            tmp = root(fit_func_by_solve, [0], args=(
                xdata[i, 0], xdata[i, 1], *params)).x
            z.append(tmp[0])
        z = np.array(z)
        return z

# fitting method
def fit_surface(dt, functype, ini_para=[], para_bnd=[]):

    x = np.array(dt['OD'])
    y = np.array(dt['FI'])
    z = np.array(dt['Pha(%)'])

    fit_x = np.stack((x, y), axis=1)
    fit_y = np.copy(z)

    # Fit data
    if functype == 'Linear':
        fit_func = fit_func_linear
        if len(ini_para) == 4:
            para_ini = ini_para
        else:
            para_ini = [1.59e+09, -2.34e+00, -7.60e+02, 4.49e+05]
        if len(para_bnd) == 2:
            bnd = para_bnd
        else:
            bnd = tuple([[-np.inf]*4, [np.inf]*4])
    elif functype == 'Exponential':
        fit_func = fit_func_exp
        if len(ini_para) == 5:
            para_ini = ini_para
        else:
            para_ini = [2.15998496e-07, -7.87920007e-01,
                        -1.19824526e+02, 3.92188755e-06, -9.99874799e-01]
        if len(para_bnd) == 2:
            bnd = para_bnd
        else:
            bnd = tuple([[-np.inf]*5, [np.inf]*5])

    params, pcov = curve_fit(fit_func, fit_x, fit_y,
                             p0=para_ini, maxfev=100000, bounds=bnd)
    # Comp. R^2
    r_2 = r2comp(fit_x, fit_y, params, fit_func)

    return params, r_2

# Prediciton method
def pred_PHA(dt, functype, params=[]):
    x = np.array(dt['OD'])
    y = np.array(dt['FI'])

    fit_x = np.stack((x, y), axis=1)

    if functype == 'Linear':
        fit_func = fit_func_linear
        if params == []:
            params = [1.59e+09, -2.34e+00, -7.60e+02, 4.49e+05]
    elif functype == 'Exponential':
        fit_func = fit_func_exp
        if params == []:
            params = [2.15998496e-07, -7.87920007e-01,
                      -1.19824526e+02, 3.92188755e-06, -9.99874799e-01]

    z = fit_func(fit_x, *params)
    return z


def r2comp(fit_x, fit_y, params, fitfunc):
    # Comp. R^2
    fitted_y = np.array(fitfunc(fit_x, *params))
    r_2 = r_square(fit_y, fitted_y)
    return r_2


def r_square(y, yp):
    ymean = np.mean(y)
    return 1-np.sum((yp-y)**2)/np.sum((y-ymean)**2)
