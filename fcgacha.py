import streamlit as st
import random as rn
    
    #initial values
if 'fc_own' not in st.session_state:
    st.session_state.fc_own = set()
if 'gold' not in st.session_state:
    st.session_state.gold = 100

                #character functions
def int1():
    give_creature('Penguin')
def int2():
    give_creature('Terra')
def int3():
    give_creature('Alamo')
def int4():
    give_creature('Blue')
def int5():
    give_creature('Strucker')
def int6():
    give_creature('Zephyr')
    
    #creature collection phrase
def give_creature(name):
    if name not in st.session_state.fc_own:
        st.write(f'you got {name}!')
        st.session_state.fc_own.add(name)
    else:
        st.write(f'you got {name}! But it was a duplicate')
       
           #list of possible rolls
intran = (int1, int2, int3, int4, int5, int6)

                        #roll button
if st.button('click to roll for 10 gold', key = 'roll'):
    if st.session_state.gold > 10:
        st.session_state.gold -= 10
        st.header(f'you have {st.session_state.gold} gold remaining')
        tempget = intran[rn.randint(0,len(intran)-1)]()
    else:
        st.write('insufficient funds')
        st.write('you own:')
        for i in st.session_state.fc_own:
            st.write(i)

            #quit button
if st.button('quit', key = 'quit'):
    st.write('you own:')
    for i in st.session_state.fc_own:
        st.write(i)