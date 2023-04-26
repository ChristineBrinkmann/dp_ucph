# Import package and module
import numpy as np
import utility as util
import tools


def EGM(sol,t,par):
    sol = EGM_loop(sol,t,par) 
    #sol = EGM_vec(sol,t,par) 
    return sol

def EGM_loop (sol,t,par):
    for i_a,a in enumerate(par.grid_a[t,:]):
        # Hint: Same procedure as in 02_EGM.ipynb
        if t+1<= par.Tr: # No pension in the next period
            fac = par.G*par.L[t]*par.psi_vec # Trick to ease notation and calculations
            w = par.w # xi and psi multiplied
            xi = par.xi_vec # trans shock as vec
            # Future m and c
            m_plus = (1/fac)*par.R*a+xi
            c_plus = tools.interp_linear_1d(sol.m[t+1,:],sol.c[t+1,:], m_plus)
            #Hvorfor bruger vi lige denne funktion?
        else:
            fac = par.G*par.L[t]
            w=1
            xi=1
            # Future m and c
            m_plus = (1/fac)*par.R*a+xi
            c_plus = tools.interp_linear_1d_scalar(sol.m[t+1,:],sol.c[t+1,:], m_plus)
            #Hvorfor bruger vi lige denne funktion?
        # Future expected marginal utility
        marg_u_plus = util.marg_util(fac*c_plus, par) #E[] i Euler
        avg_marg_u_plus = np.sum(w*marg_u_plus) 
        # par.w er 8*9 (72,) lang. Der er altså 72 forskellige vægte til utility   
        # Current c and m (i_a+1 as we save the first index point to handle the credit constraint region)
        sol.c[t,i_a+1]= util.inv_marg_util(par.beta*par.R*avg_marg_u_plus, par) 
        #hele Euler med avg marg util
        sol.m[t,i_a+1]= sol.c[t,i_a+1] + a

    return sol

def EGM_vec (sol,t,par):

    #Fill in:
    
    return sol
