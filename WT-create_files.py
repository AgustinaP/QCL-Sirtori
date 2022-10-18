import numpy as  np


TEMPERATURE = 77
#FIELD = np.arange(5,100, 5)
FIELD = 44

ZA_LAYER = [5.1,1.9,1.1,5.6,1.1,4.9,2.8]
IN_LAYER = [3.6,1.7,3.2,2.0,2.8,2.2,3.0,2.6,3.0]
periodos = 3

M_UP = '"AlGaAs"'
M_DOWN = '"GaAs"'
X1 = 33
ancho = np.arange(-20,50, 1)
for k in range(len(ancho)): 
    LAYERS = ' '
    for i in range(periodos):
        for j in range(len(IN_LAYER)):
            if(j%2 == 0 ):
                LAYERS += '{"MATERIAL": '+ M_DOWN+',"THICKNESS": '+str(IN_LAYER[j]*(1+ancho[k]/100))+'},'
            else:
                LAYERS += '{"MATERIAL": '+ M_UP+',"X1": '+str(X1/100)+',"THICKNESS": '+str(IN_LAYER[j]*(1+ancho[k]/100))+'},'
        for j in range(len(ZA_LAYER)):
            if(j%2 == 1 ):
                LAYERS += '{"MATERIAL": '+ M_DOWN+',"THICKNESS": '+str(ZA_LAYER[j]*(1+ancho[k]/100))+'},'
            else:
                LAYERS += '{"MATERIAL": '+ M_UP+',"X1": '+str(X1/100)+',"THICKNESS": '+str(ZA_LAYER[j]*(1+ancho[k]/100))+'},'
        if i == periodos-1:
            for j in range(len(IN_LAYER)):
                if(j%2 == 0 ):
                    LAYERS += '{"MATERIAL": '+ M_DOWN+',"THICKNESS": '+str(IN_LAYER[j]*(1+ancho[k]/100))+'},'
                elif j == len(IN_LAYER)-1:
                    LAYERS += '{"MATERIAL": '+ M_UP+',"X1": '+str(X1/100)+',"THICKNESS": '+str(IN_LAYER[j]*(1+ancho[k]/100))+'}'
                else:
                    LAYERS += '{"MATERIAL": '+ M_UP+',"X1": '+str(X1/100)+',"THICKNESS": '+str(IN_LAYER[j]*(1+ancho[k]/100))+'},'

   
    text_to_save = '{"LAYERS": ['+LAYERS+'],"TEMPERATURE":'+str(TEMPERATURE)+',"FIELD": -'+str(FIELD/10000)+'}'
    ### save to text ###
    with open(str(periodos)+'p-EF'+str(FIELD)+'-ancho'+str(ancho[k]+100)+'.str', 'w') as f:
        f.write(text_to_save)

