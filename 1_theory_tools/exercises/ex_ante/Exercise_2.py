# import packages used
import numpy as np

def solve_VFI(par):
    Cstar = np.zeros([par.W+1])
    
    # Parameters for VFI
    max_iter = par.max_iter   # maximum number of iterations
    delta = 1000 #difference between V_next and V_now
    tol = par.tol #convergence tol. level
    it = 0  #iteration counter 
    V_now = np.zeros([par.W+1]) #arbitrary starting values
    
    while (max_iter>= it and tol<delta):
        it = it+1
        V_next = V_now.copy()
        for w in range(par.W+1):
            c = np.arange(w+1) #+1 fordi den tæller op til værdien lige inden. Hvis der stod arange(5) ville det være 0-4 
            w_c = w - c
            V_guess = np.sqrt(c)+par.beta*V_next[w_c]
            V_now[w] = np.amax(V_guess)
            Cstar[w] = np.argmax(V_guess)
        delta = np.amax(np.abs(V_now - V_next))
    
    class sol: pass
    sol.C = Cstar
    sol.V = V_now
    sol.it = it

    return sol