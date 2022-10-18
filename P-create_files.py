import numpy as  np


TEMPERATURE = 77
FIELD = 44
#FIELD = -0.0060

ZA_LAYER = ["5.1","1.9","1.1","5.6","1.1","4.9","2.8"]
IN_LAYER = ["3.6","1.7","3.2","2.0","2.8","2.2","3.0","2.6","3.0"]
periodos = np.arange(1, 30, 2)

M_UP = '"AlGaAs"'
M_DOWN = '"GaAs"'
X1 = 0.33


for k in range(len(periodos)):
    LAYERS = ' '
    for i in range(periodos[k]):
        for j in range(len(IN_LAYER)):
            if(j%2 == 0 ):
                LAYERS += '{"MATERIAL": '+ M_DOWN+',"THICKNESS": '+IN_LAYER[j]+'},'
            else:
                LAYERS += '{"MATERIAL": '+ M_UP+',"X1": '+str(X1)+',"THICKNESS": '+IN_LAYER[j]+'},'
        for j in range(len(ZA_LAYER)):
            if(j%2 == 1 ):
                LAYERS += '{"MATERIAL": '+ M_DOWN+',"THICKNESS": '+ZA_LAYER[j]+'},'
            else:
                LAYERS += '{"MATERIAL": '+ M_UP+',"X1": '+str(X1)+',"THICKNESS": '+ZA_LAYER[j]+'},'
        if i == periodos[k]-1:
            for j in range(len(IN_LAYER)):
                if(j%2 == 0 ):
                    LAYERS += '{"MATERIAL": '+ M_DOWN+',"THICKNESS": '+IN_LAYER[j]+'},'
                elif j == len(IN_LAYER)-1:
                    LAYERS += '{"MATERIAL": '+ M_UP+',"X1": '+str(X1)+',"THICKNESS": '+IN_LAYER[j]+'}'
                else:
                    LAYERS += '{"MATERIAL": '+ M_UP+',"X1": '+str(X1)+',"THICKNESS": '+IN_LAYER[j]+'},'   
    text_to_save = '{"LAYERS": ['+LAYERS+'],"TEMPERATURE":'+str(TEMPERATURE)+',"FIELD": -'+str(FIELD/10000)+'}'
        ### save to text ###
    with open(str(periodos[k])+'p-EF'+str(FIELD)+'.str', 'w') as f:
        f.write(text_to_save)

