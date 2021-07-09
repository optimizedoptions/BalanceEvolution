from numpy import random,mean,std,amax,amin
import matplotlib.pyplot as plt

class Simulation:       
    def __init__(self):
        '''
        Simulation() -> class constructor.
        '''
        self.npaths=1
        self.ntrades=1
        self.winratio=-1.0
        self.capital=-1.0
        self.profit=-1.0
        self.loss=1.0
        self.ruinprob=0.0
        self.ruinindex=-1.0
        self.balance=[]
            
    def setparams(self,winratio,capital,profit,loss,npaths,ntrades):
        '''
        setparams(self,winratio,capital,profit,loss,npaths,ntrades) -> sets the 
        parameters for an MC simulation.
        '''
        if isinstance(npaths,int):
            if npaths>0:
                self.npaths=npaths
            else:
                raise ValueError("Number of trade paths must be greater than zero!")
            
                return
        else:
            raise TypeError("Number of trades must be an integer!")
            
            return
            
        if isinstance(ntrades,int):
            if ntrades>0:
                self.ntrades=ntrades
            else:
                raise ValueError("Maximum number of trades must be greater than zero!")
                
                return
        else:
            raise TypeError("Maximum number of trades must be an integer!")
            
            return
            
        if isinstance(winratio,float) or isinstance(winratio,int):
            if winratio>0.0:
                self.winratio=winratio
            else:
                raise ValueError("Winning ratio must be greater than zero!")
            
                return
        else:
            raise TypeError("Winning ratio must be a float number!")
            
            return
            
        if isinstance(capital,float) or isinstance(capital,int):
            if capital>0.0:
                self.capital=capital
            else:
                raise ValueError("Capital must be greater than zero!")
                
                return
        else:
            raise TypeError("Capital must be a float number!")
            
            return
            
        if isinstance(profit,float) or isinstance(profit,int):
            if profit>0.0:
                self.profit=profit
            else:
                raise ValueError("Profit must be greater than zero!")
                
                return
        else:
            raise TypeError("Profit must be a float number!")
            
            return
            
        if isinstance(loss,float) or isinstance(loss,int):
            if loss<0.0:
                self.loss=loss
            else:
                raise ValueError("Loss must be less than zero!")
                
                return
        else:
            raise TypeError("Loss must be a float number!")
            
            return
            
    def run(self):
        '''
        run() -> runs an MC simulation for a number of trading paths with
        a maximum number of trades per path.
        '''
        self.balance=[]
        self.consecutivelosses=[]
        self.consecutivewins=[]
        self.ruinprob=0.0
        self.ruinindex=-1.0
            
        ruinindex=ruined=0
            
        for i in range(self.npaths):
            nlosses=0
            maxconsecutivelosses=0
            nwins=0
            maxconsecutivewins=0
            isruined=False
            
            for j in range(self.ntrades):
                if j==0:
                    self.balance.append([self.capital])
                else:
                    if isruined:
                        self.balance[i].append(self.balance[i][j-1])
                    else:
                        r=random.uniform(0.0,1.0)
                
                        if r<=self.winratio:
                            self.balance[i].append(self.balance[i][j-1]+
                                                   self.profit)
                        
                            nwins+=1
                            nlosses=0
                        
                            if nwins>maxconsecutivewins:
                                maxconsecutivewins=nwins
                        else:
                            self.balance[i].append(self.balance[i][j-1]+
                                                   self.loss)
                        
                            nlosses+=1
                            nwins=0
                        
                            if nlosses>maxconsecutivelosses:
                                maxconsecutivelosses=nlosses
                            
                            if self.balance[i][j]<=0.0:
                                ruined+=1
                                ruinindex+=j
                                isruined=True
                                                        
            self.consecutivelosses.append(maxconsecutivelosses)
            self.consecutivewins.append(maxconsecutivewins)
                            
        self.ruinprob=ruined/self.npaths
        
        if ruined>0:
            self.ruinindex=ruinindex/ruined

    def getavgbalance(self):
        '''
        getavgbalance() -> returns the average final balance taken over all the 
        trading paths. Additionally, it also calculates the standard deviation, 
        the maximum and minimum.
        '''
        finalbalance=[]
        
        for i in range(self.npaths):
            finalbalance.append(self.balance[i][-1])
            
        return (mean(finalbalance),std(finalbalance),amax(finalbalance),
                amin(finalbalance))

    def getavgconsecutivelosses(self):
        '''
        getavgconsecutivelosses() -> returns the average, standard deviation,
        maximum and minimum consecutive losses over all the trading paths.
        '''
        return (mean(self.consecutivelosses),std(self.consecutivelosses),
                amax(self.consecutivelosses),amin(self.consecutivelosses))

    def getavgconsecutivewins(self):
        '''
        getavgconsecutivelosses() -> returns the average, standard deviation,
        maximum and minimum consecutive wins over all the trading paths.
        '''
        return (mean(self.consecutivewins),std(self.consecutivewins),
                amax(self.consecutivewins),amin(self.consecutivewins))   
    
    def getbalance(self,index=-1):
        '''
        getbalance(index) -> returns a list containing the trading path
        specified by 'index' or all trading paths if a negative index is
        passed as argument.
        '''
        if index>=0 and index<self.npaths:
            return self.balance[index]
        else:
            return self.balance
        
    def getprofitabletradingpaths(self,profit=-1.0):
        '''
        getprofitabletradingpaths(profit) -> returns the ratio of trading 
        paths that will end up with a balance higher than 'profit' or higher
        than the initial capital, if 'profit' is less than the initial capital.
        '''
        profitable=0
        
        if profit<self.capital:
            profit=self.capital
        
        for i in range(self.npaths):
            if self.balance[i][-1]>=profit:
                profitable+=1
                
        return profitable/self.npaths
        
    def getfirsthit(self,profit):
        '''
        getfirsthit(profit) -> returns the ratio of trading paths that reach 
        the profit balance 'profit' and after how many trades, on average.
        '''
        reached=reachindex=0
        avgreachindex=-1.0
        
        for i in range(self.npaths):            
            for j in range(len(self.balance[i])):
                if self.balance[i][j]>=profit:
                    reached+=1
                    reachindex+=j
                    
                    break
        
        if reached>0:        
            avgreachindex=float(reachindex)/reached
                
        return (float(reached)/self.npaths,avgreachindex)
        
    def plottradingpaths(self):
        '''
        plottradingpaths() -> plots the MC-generated trading paths.
        '''      
        index=[j for j in range(self.ntrades)]
        
        plt.title("Trading paths")
        plt.xlabel("Trade index")
        plt.ylabel("Account balance")
        plt.xlim(left=0,right=self.ntrades)
        
        for i in range(self.npaths):
            plt.plot(index,self.balance[i])
            
        plt.show()
        
    def plothist(self):
        '''
        plothist() -> plots a histogram of terminal account balance.
        '''
        finalbalance=[]

        for i in range(self.npaths):
            finalbalance.append(self.balance[i][-1])
        
        plt.title("Histogram of terminal account balance")
        plt.axvline(self.capital,ls='--',color='green')
        plt.xlabel("Account balance")
        plt.ylabel("Counts")
        plt.grid(True)
        plt.hist(finalbalance,bins=50)
        plt.show()