import numpy as  np


TEMPERATURE = np.arange(5, 120, 5)
#FIELD = np.arange(25, 65, 1)
FIELD = 44

ZA_LAYER = ["5.1","1.9","1.1","5.6","1.1","4.9","2.8"]
IN_LAYER = ["3.6","1.7","3.2","2.0","2.8","2.2","3.0","2.6","3.0"]
periodos = 3
largo = 0
for i in range(len(ZA_LAYER)):
    largo += int(ZA_LAYER[i])
for i in range(len(IN_LAYER)):
    largo += int(IN_LAYER[i])
largo = int(largo)

M_UP = '"AlGaAs"'
M_DOWN = '"GaAs"'
X1 = 0.33

LAYERS = ' '
for i in range(periodos):
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
    if i == periodos-1:
        for j in range(len(IN_LAYER)):
            if(j%2 == 0 ):
                LAYERS += '{"MATERIAL": '+ M_DOWN+',"THICKNESS": '+IN_LAYER[j]+'},'
            elif j == len(IN_LAYER)-1:
                LAYERS += '{"MATERIAL": '+ M_UP+',"X1": '+str(X1)+',"THICKNESS": '+IN_LAYER[j]+'}'
            else:
                LAYERS += '{"MATERIAL": '+ M_UP+',"X1": '+str(X1)+',"THICKNESS": '+IN_LAYER[j]+'},'

        
for k in range(len(TEMPERATURE)):    
    text_to_save = '{"LAYERS": ['+LAYERS+'],"TEMPERATURE":'+str(TEMPERATURE[k])+',"FIELD": -'+str(FIELD/10000)+'}'
    ### save to text ###
    with open(str(periodos)+'p-EF'+str(FIELD)+'-T'+str(TEMPERATURE[k])+'.str', 'w') as f:
        f.write(text_to_save)

