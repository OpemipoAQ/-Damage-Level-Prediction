
import streamlit as st
import pandas as pd
import numpy as np
import pickle
from PIL import Image

st.write("""
# STRIKES PREDICTION APP
""")
image=Image.open('bird_strike.jpg')
st.image(image, width=500)

model=pickle.load(open('bird_model.pkl','rb'))

scaler=pickle.load(open('bird_scaler.pkl','rb'))

st.sidebar.header('Post Strike Parameters')

def user_input_features():
    Season=st.selectbox('Choose season',('Fall','Summer','Spring','Winter'))
    if Season=='Fall':
        Season=4
    if Season=='Summer':
        Season=3
    if Season=='Spring':
        Season=2                   
    else:
        Season=1
    Sky=st.selectbox('Any clouds?',('No Cloud', 'Overcast', 'Some Cloud'))   
    if Sky=='No Cloud':
        Sky=3
    if Sky=='Overcast':
        Sky=2
    else:
        Sky=1
    Precipitation=st.selectbox('What is the precipitation status?',('None', 'Fog', 'Rain', 'Snow', 'Fog, Rain', 'Rain, Snow',
       'Fog, Snow', 'Fog, Rain, Snow'))
    if Precipitation=='None':
        Precipitation=8
    if Precipitation=='Fog':
        Precipitation=7
    if Precipitation=='Rain':
        Precipitation=6
    if Precipitation=='Snow':
        Precipitation=5 
    if Precipitation=='Fog,Rain':
        Precipitation=4
    if Precipitation=='Rain,Snow':
        Precipitation=3
    if Precipitation=='Fog,Snow':
        Precipitation=2
    else:
        Precipitation=1
    Time_of_day=st.selectbox('When is the flight scheduled for?',('Night','Day', 'Dawn', 'Dusk'))
    if Time_of_day=='Night':
        Time_of_day=4
    if Time_of_day=='Day':
        Time_of_day=3
    if Time_of_day=='Dawn':
        Time_of_day=2
    else:
        Time_of_day=1
    Num_Engs =st.selectbox('How many engines has the aircraft?',('1.','2.', '3.', '4.'))
    if Num_Engs=='1.':
        Num_Engs=4
    if Num_Engs=='2.':
        Num_Engs=3
    if Num_Engs=='3.':
        Num_Engs=2
    else:
        Num_Engs=1
    Type_Engs=st.selectbox('What type of engine does the aircraft have?',('A', 'D', 'C', 'F', 'B', 'Y', 'E'))
    if Type_Engs=='A':
         Type_Engs=7
    if Type_Engs=='D':
         Type_Engs=6                   
    if Type_Engs=='C':
        Type_Engs=5
    if Type_Engs=='F':
        Type_Engs=4
    if Type_Engs=='B':
        Type_Engs=3
    if Type_Engs=='Y':
        Type_Engs=2
    else:
        Type_Engs=1
    FAAREGION=st.selectbox('What region is the airport situated?',('AGL', 'ASW', 'ANE', 'ANM', 
                                                                   'ASO', 'AWP', 'AEA', 'ACE', 'AAL','FGN'))
    if FAAREGION=='AGL':
        FAAREGION=10
    if FAAREGION=='ASW':
        FAAREGION=9
    if FAAREGION=='ANE':
        FAAREGION=8
    if FAAREGION=='ANM':
        FAAREGION=7
    if FAAREGION=='ASO':
        FAAREGION=6
    if FAAREGION=='AWP':
        FAAREGION=5
    if FAAREGION=='AEA':
        FAAREGION=4
    if FAAREGION=='ACE':
        FAAREGION=3
    if FAAREGION=='FGN':
        FAAREGION=2
    else:
        FAAREGION=1
    DAMAGE_RISK=st.sidebar.selectbox('Risk Level',('High Risk','Potential Risk','Low Risk','Undetermined'))
    if DAMAGE_RISK=='High Risk':
        DAMAGE_RISK=4
    if DAMAGE_RISK=='Potential Risk':
        DAMAGE_RISK=3
    if DAMAGE_RISK=='Low Risk':
        DAMAGE_RISK=2
    else:
        DAMAGE_RISK=1
    DAMAGE_LEVEL=st.sidebar.selectbox('Damage Level',('N', 'S', 'M', 'M?', 'D'))
    if DAMAGE_LEVEL=='D':
        DAMAGE_LEVEL=3
    if DAMAGE_LEVEL=='M?':
        DAMAGE_LEVEL=4
    if DAMAGE_LEVEL=='M':
        DAMAGE_LEVEL=3
    if DAMAGE_LEVEL=='S?':
        DAMAGE_LEVEL=2
    else:
        DAMAGE_LEVEL=1
    PHASE_OF_FLIGHT=st.sidebar.selectbox('Flight Phase When Collission Occured?',('Approach', 'Landing Roll', 'Climb', 
                                                                                  'En Route', 'Take-off Run','Taxi', 
                                                                                  'Descent', 'Parked', 'Local', 'Arrival',
                                                                                  'Departure', 'Unknown'))
    if PHASE_OF_FLIGHT=='Approach':
        PHASE_OF_FLIGHT=12
    if PHASE_OF_FLIGHT=='Landing Roll':
        PHASE_OF_FLIGHT=11
    if PHASE_OF_FLIGHT=='Climb':
        PHASE_OF_FLIGHT=10
    if PHASE_OF_FLIGHT=='En Route':
        PHASE_OF_FLIGHT=9
    if PHASE_OF_FLIGHT=='Take-off Run':
        PHASE_OF_FLIGHT=8
    if PHASE_OF_FLIGHT=='Taxi':
        PHASE_OF_FLIGHT=7
    if PHASE_OF_FLIGHT=='Descent':
        PHASE_OF_FLIGHT=6
    if PHASE_OF_FLIGHT=='Parked':
        PHASE_OF_FLIGHT=5
    if PHASE_OF_FLIGHT=='Local':
        PHASE_OF_FLIGHT=4
    if PHASE_OF_FLIGHT=='Arrival':
        PHASE_OF_FLIGHT=3
    if PHASE_OF_FLIGHT=='Departure':
        PHASE_OF_FLIGHT=2
    else:
        PHASE_OF_FLIGHT=1
                                     
    AIRCRAFT=st.sidebar.number_input('What is The Aircraft Type?')
    AIRPORT=st.sidebar.number_input('Enter Airport')
    ENG_1_POS=st.sidebar.number_input('Where is Engine 1 Positioned?')
    ENG_2_POS=st.sidebar.number_input('Where is Engine 2 Postioned?')
    ENG_3_POS=st.sidebar.number_input('Where is Engine 3 Postioned?')
    ENG_4_POS=st.sidebar.number_input('Where is Engine 4 Postioned?')
                        
    data={'SEASON':Season,'SKY':Sky,'PRECIPITATION':Precipitation,'TIME_OF_DAY':Time_of_day,
           'NUM_ENGS':Num_Engs,'TYPE_ENG':Type_Engs,'FAAREGION':FAAREGION,'DAMAGE_LEVEL':DAMAGE_LEVEL,
          'DAMAGE_RISK':DAMAGE_RISK,'PHASE_OF_FLIGHT':PHASE_OF_FLIGHT, 'AIRCRAFT':AIRCRAFT,
          'ENG_1_POS':ENG_1_POS,'ENG_2_POS':ENG_2_POS,'ENG_3_POS':ENG_3_POS,'ENG_4_POS':ENG_4_POS,'AIRPORT':AIRPORT
          }
    features = pd.DataFrame(data,index=[0])
    return features

input_dfs=user_input_features()
input_df=scaler.transform(input_dfs)

    
if st.button('PREDICT'):
    y_out=model.predict(input_df)
    if y_out[0]==1:
        st.write(f' You are at a high damage risk from strikes')
    else:
        st.write(f' You are at a low damage from strikes')  
