# %% [markdown]
# Isp calculation für Lambda 4S-5 Configuration based on Astronautix Data
#     Note: The Thrust is assumed to be liniar, which is indeed not the case.

# %%
def ISP(Thrust,massflow):
    g0=9.8066 #m/(s*s)
    isp=Thrust/massflow/g0
    return isp

# %%
Fbooster = 95000 #Newton
mb_ST = 190 #kg
mb_0 = 500 #kg
mbf= mb_0-mb_ST
tboost= 7.4 #sec
m_bf=mbf/tboost #massflow kg/s

isp_booster=ISP(Fbooster,m_bf)
isp_booster=format(isp_booster,'.4')+'sec'
print('Isp of Booster=',isp_booster)

# %%
Fstage1 = 410000 #Newton
ms1_ST = 2945 #kg
ms1_0 = 5000 #kg
ms1f= ms1_0-ms1_ST
ts1= 29 #sec
m_s1=ms1f/ts1 #massflow kg/s

isp_s1= ISP(Fstage1,m_s1)
print('Isp Stage1=',format((isp_s1),'.4')+'sec')
print('Note: the Isp is for sure wrong,') 
print('i suggest that the Thrust data includes both boosters\nTherfore:')
print('Isp Stage1 reduced:',format((ISP((Fstage1-2*Fbooster),m_s1)),'.4')+'sec')

# %%
Fstage4 = 7800 #Newton
ms4_ST = 15 #kg
ms4_0 =  100 #kg
ms4_f= ms4_0-ms4_ST
ts4=  32#sec
m_s4=ms4_f/ts4 #massflow kg/s

isp_s4= ISP(Fstage4,m_s4)
print('Isp of Stage4=',format((isp_s4),'.4')+'sec')


