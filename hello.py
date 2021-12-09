import streamlit as st
import pandas as pd
import numpy as np
# import sqlite3
# from sqlite3 import Error
#mypath = "/mnt/c/projects/AVE/"
#dbFile = mypath+"ave.db"
	
def readInvoices():
	connect = sqlite3.connect(dbFile)

	query	= ('''
		select DISTINCT INVOICE_NUMBER, CAST(PURCHASER_IC AS TEXT) AS PURCHASER_IC, PURCHASER_NAME, PURCHASER_ADDRESS, REALIZED_DATE, FILE_NAME from INVOICE_HEAD_I  order by REALIZED_DATE
	''')
	frame = pd.read_sql_query(query, connect)	
	#connect.close()
	return frame
	
st.title('jOJOC')
st.text('This is some text.')
#st.table(data=readInvoices())