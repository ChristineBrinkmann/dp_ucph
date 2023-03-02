# import packages used
import numpy as np

def solve_consumption_uncertainty(par):
     # initialize solution class
    class sol: pass
    sol.V = np.zeros([par.num_W,par.T]) 
    sol.C = np.zeros([par.num_W,par.T])
    sol.grid_W = np.zeros([par.num_W,par.T])
    
    # consumption grid as a share of available resources
    grid_C = np.linspace(0.0,1.0,par.num_C) #it is a share!
    
    # Loop over periods
    for t in range(par.T-1, -1, -1):  #from period T-1, until period 0, backwards
        # Maximum cake size grows as t grows due to shocks so  grid depends on t 
        W_max = max(par.eps)*t+par.W #Vi ganger her med t for at tage højde for at kagen den vokser for hver periode
        grid_W = np.linspace(0,W_max,par.num_W) #par.num_w = 200
        sol.grid_W[:,t] = grid_W 
    
        for iw,w in enumerate(grid_W): #iw er indeks, w er value
            c = grid_C*w
            w_c = w - c
            EV_next = 0
        
            if t<par.T-1:
                for s in range(par.K):
                    # weight on the shock 
                    weight = par.pi[s]
                    # epsilon shock
                    eps = par.eps[s]
                    EV_next +=weight*np.interp(w_c+eps,sol.grid_W[:,t+1],sol.V[:,t+1]) 
            V_guess = np.sqrt(c)+par.beta*EV_next
            index = np.argmax(V_guess)
            sol.C[iw,t] = c[index]
            sol.V[iw,t] = np.amax(V_guess)
        
    return sol