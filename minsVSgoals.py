import streamlit as st
import app 
import ScatterPlot as sp
import altair as alt

def mins_to_goals(mainfile):
    myfile=mainfile[['Player Names','Goals','Mins','Matches Played']]
    myfile=myfile.groupby('Player Names').agg(
        {
            'Goals': 'sum',
            'Mins':'sum',
            'Matches Played':'sum'
        }
    ).reset_index().sort_values(by='Goals',ascending=False).head(15)
    myfile['GoalsperMatch']=myfile['Goals']/myfile['Matches Played']
    myfile['MinutesPlayedPerMatch']=myfile['Mins']/90
    averageGoals=myfile['GoalsperMatch'].mean()
    reference_line=alt.Chart(myfile).mark_line(color='red').encode(
        x=alt.value(0.7)
    ).interactive()
    st.altair_chart(reference_line)
    scatter_plot=sp.scatter_plot(myfile,'GoalsperMatch','MinutesPlayedPerMatch','Goals scored per 90 mins')
    our_graph=alt.layer(scatter_plot, reference_line)
    
    return st.altair_chart(our_graph,use_container_width=True)