import streamlit as st
import pandas as pd
import numpy as np
import sqlite3
from sqlite3 import Error
mypath = "./"
dbFile = mypath+"hello.db"
	
def readInvoices():
	connect = sqlite3.connect(dbFile)

	query	= ('''
		Select * from Street
	''')
	frame = pd.read_sql_query(query, connect)	
	#connect.close()
	return frame
	
st.title('To je fakt dobrý')
st.text('This is some text.')
st.table(data=readInvoices())