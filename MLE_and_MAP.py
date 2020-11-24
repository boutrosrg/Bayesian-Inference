# -*- coding: utf-8 -*-
"""
Created on Tue Nov 24 17:15:35 2020

@author: boutros El-Gamil
"""
import numpy as np
import random
import matplotlib.pyplot as plt
import scipy.stats as stats

def mle_diabetes_normal_curve01(data):
    '''
    this function gets data samples, calculates it's mean and standard 
    deviation, and draw the corresponded normal PDF function
    
    INPUTS:
        data: list of data samples describe the BG levels of diabetes patient
    '''
    
    # get moments of data normal distribution
    mu =np.mean(data)
    sigma = np.std(data)
    
    # get domain space of the distribution
    domain = np.linspace(min(data)-2, max(data)+3)
    
    # plot data
    plt.plot(domain, stats.norm.pdf(domain, mu, sigma), color = 'b')        
    plt.axvline(x=round(np.mean(data),2),ymax=0.94)    
    plt.text(158, 0.083, '$mean= $' + str(round(np.mean(data),2)),
             fontweight="bold", color = 'b')
    plt.text(158, 0.076, '$sd= $' + str(round(np.std(data),2)),
             fontweight="bold", color = 'b')
        
    plt.xticks(color='black')    
    plt.yticks(color='black')
    
    plt.xlabel('BG (mg/dl)',fontsize='large', color='black',
               fontweight='bold', fontstyle='italic')
    
    plt.ylabel('probability', color='black', fontweight='bold', 
               fontstyle='italic')
        
    plt.show()

def mle_diabetes_normal_curve02(data):
    '''
    this function gets data samples, calculates it's mean and standard 
    deviation, and draw the corresponded normal PDF function along with 
    vertical lines corresponded to each data sample
    
    INPUTS:
        data: list of data samples describe the BG levels of diabetes patient
    '''
    
    # get moments of data normal distribution
    mu =round(np.mean(data),5)
    sigma = round(np.std(data),5)    
    
    # get domain space of the distribution
    domain = np.linspace(min(data) - 2 , max(data) + 3 )    
    
    # plot data
    plt.plot(domain, stats.norm.pdf(domain, mu, sigma),  color = 'b') 
            
    mu_prob = 0

    for i in data:  
        mu_prob += stats.norm(mu, sigma).pdf(i)

        
        if (i > 160 and i < 175):
            y = 11.058823 * stats.norm(mu, sigma).pdf(i)            
            
        elif (i == 175):     
            y = 10.3 * stats.norm(mu, sigma).pdf(i)
            
        else:
            y = 9 * stats.norm(mu, sigma).pdf(i)            
        
        plt.axvline(x=i, ymax=  y)
        plt.plot(i, stats.norm(mu, sigma).pdf(i), 'ro')
        
        
    plt.xticks(color='black')    
    plt.yticks(color='black')
    
    plt.xlabel('BG (mg/dl)',fontsize='large', color='black',
               fontweight='bold', fontstyle='italic')
    
    plt.ylabel('probability', color='black', fontweight='bold', 
               fontstyle='italic')            
    
    plt.show()
    
def mle_diabetes_normal_curve03(data):
    '''
    this function generates random values over BG range and calculates the 
    corresponded pdf of the normal distribution   
    
    INPUTS:
        data: list of data samples describe the BG levels of diabetes patient
    '''    
    
    # get sd of data normal distribution
    sigma = round(np.std(data),5)
    
    # set empty lists of mu random values and corresponded PDF        
    mu_random = []
    pdf_random = []
    
    # create 1000 random values in data range
    for i in range(0,1000):
        x = random.randrange(min(data)-3, max(data)+3) + random.random()         
                
        # sum up likelihood probabilities of data samples over each random mu
        mu2_prob = 0
        for j in data:
            mu2_prob += stats.norm(x, sigma).pdf(j)
        
        # append values to lists
        mu_random.append(x)
        pdf_random.append(mu2_prob)
          
    # plot data
    plt.plot(mu_random,pdf_random, 'b.')
    plt.axvline(x=round(mu_random[pdf_random.index(max(pdf_random))],2),
                ymax=0.94)
    
    plt.xticks(np.arange(157.5, 178, 2.5), color='black')    
    plt.yticks(color='black')
    
    plt.xlabel('BG (mg/dl)',fontsize='large', color='black',
               fontweight='bold', fontstyle='italic')
    
    plt.ylabel('likelihood (sum)', color='black', fontweight='bold', 
               fontstyle='italic')  
        
    plt.text(158, 0.4, '$max\;L= $' + str(round(max(pdf_random),2)),
             fontweight="bold", color = 'b')
    
    plt.text(158, 0.37, '$corr.\;BG= $' + 
             str(round(mu_random[pdf_random.index(max(pdf_random))],2)),
             fontweight="bold", color = 'b')
    
    plt.show()
    
def map_diabetes_normal_curve01(data):
    '''
    this function draws likelihood and prior distributions of data samples
    
    INPUTS:
        data: list of data samples describe the BG levels of diabetes patient
    '''   
    
    # get likelihood distribution moments
    mu_l =round(np.mean(data),2)
    sigma_l = round(np.std(data),2)
    
    # get prior distribution moments
    mu_prior = 171
    sigma_prior = 3
    
    # set likelihood & prior domains
    domain_l = np.linspace(min(data)-6, max(data)+7)
    domain_prior = np.linspace(min(data)-5, max(data)+6)    
    
    # plot distributions
    plt.plot(domain_l, stats.norm.pdf(domain_l, mu_l, sigma_l), 
             color = 'b')            
    
    plt.plot(domain_prior, stats.norm.pdf(domain_prior, mu_prior, sigma_prior), 
             color = 'g')
    
    plt.text(157, 0.08, 'likelihood', fontweight="bold",
             fontstyle= "italic", color = 'b')
    plt.text(157, 0.07, '$mean= $' + str(mu_l), fontweight="bold",
             fontstyle= "italic", color = 'b')
    plt.text(157, 0.06, '$sd= $' + str(sigma_l), fontweight="bold",
             fontstyle= "italic", color = 'b')
    
    plt.text(174, 0.12, 'prior', fontweight="bold",
             fontstyle= "italic", color = 'g')
    plt.text(174, 0.11, '$mean= $' + str(mu_prior), fontweight="bold",
             fontstyle= "italic", color = 'g')
    plt.text(174, 0.1, '$sd= $' + str(sigma_prior), fontweight="bold",
             fontstyle= "italic", color = 'g')
    
    plt.xticks(color='black')    
    plt.yticks(color='black')
    
    plt.xlabel('BG (mg/dl)',fontsize='large', color='black',
               fontweight='bold', fontstyle='italic')
    
    plt.ylabel('probability', color='black', fontweight='bold', 
               fontstyle='italic')
    
    plt.show()
    
def map_diabetes_normal_curve02(data):
    '''
    this function draws both prior and likelihood curves, calculate and plot 
    the corresponded posterior distribution
    
    INPUTS:
        data: list of data samples describe the BG levels of diabetes patient    
    '''   
    
    # get likelihood distribution moments
    mu_l =round(np.mean(data),2)
    sigma_l = round(np.std(data),2)
    
    # set prior distribution moments    
    mu_prior = 171
    sigma_prior = 3
    
    # get likelihood & prior domains
    domain_l = np.linspace(min(data)-5, max(data)+7, num= 250)        
    domain_prior = np.linspace(min(data)-5, max(data)+7)
    
    # plot likelihood & prior domains
    plt.plot(domain_l, stats.norm.pdf(domain_l, mu_l, sigma_l), 
             color = 'b')
    plt.plot(domain_prior, stats.norm.pdf(domain_prior, mu_prior, sigma_prior), 
             color = 'g')
    
    # add text
    prior_ypos = 0.12 
    plt.text(174, prior_ypos, 'prior', fontweight="bold",
             fontstyle= "italic", color = 'g')
    plt.text(174, prior_ypos-0.009, '$mean= $' + str(mu_prior), 
             fontweight="bold", fontstyle= "italic", color = 'g')
       
    lh_ypos = 0.075       
    plt.text(158, lh_ypos, 'likelihood', fontweight="bold",
             fontstyle= "italic", color = 'b')
    plt.text(158, lh_ypos-0.009, '$mean= $' + str(int(mu_l)), 
             fontweight="bold", fontstyle= "italic", color = 'b')
                   
    for i in data:                                                  
        plt.plot(i, stats.norm(mu_l, sigma_l).pdf(i), 'ro')
        
    plt.xticks(color='black')    
    plt.yticks(color='black')
    
    plt.xlabel('BG (mg/dl)',fontsize='large', color='black',
               fontweight='bold', fontstyle='italic')
    
    plt.ylabel('probability', color='black', fontweight='bold', 
               fontstyle='italic')
    
    
    ## calculate posterior
    # set empty lists of mu random values and corresponded PDF 
    mu_random = []
    pdf_random = []
    
    for i in range(0,500):
        # generate random BG values
        x = random.randrange(min(data)-5, max(data)+7) + random.random()         
        
        # calculate prior marginal probabilty
        m_prob = sum(stats.norm(x, sigma_prior).pdf(j) for j in data)
        
                
        # initialize posterior prob
        post_prob = 1
        
        # loop over data samples
        for j in data:
            
            # calculate Likelihood probability
            lh_prob = stats.norm(x, sigma_prior).pdf(j)                      
            
            # calculate posterior probability
            post_prob *= lh_prob * m_prob
        
        # append data to empty lists
        mu_random.append(x)
        pdf_random.append(post_prob)   
        
        plt.plot(x, post_prob**0.08, '.', color= 'black', markersize= 2)
    
    post_ypos = 0.124
    plt.text(162, post_ypos, 'posterior$^\mathbf{0.08}}$', fontweight="bold",
             fontstyle= "italic", color = 'black')
    plt.text(162, post_ypos-0.009, 
             '$mean= $' + str(round(mu_random[pdf_random.index(max(pdf_random))])), 
             fontweight="bold", fontstyle= "italic", color = 'black')
    
    plt.show()
    
if __name__ == "__main__":
    # set data samples    
    data = [172,171,166,175,170,165,160]    
    
    mle_diabetes_normal_curve01(data)
    
    mle_diabetes_normal_curve02(data)
    
    mle_diabetes_normal_curve03(data)
    
    map_diabetes_normal_curve01(data)
    
    map_diabetes_normal_curve02(data)