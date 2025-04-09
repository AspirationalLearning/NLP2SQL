from dotenv import load_dotenv
load_dotenv() ## load all the environemnt variables

import os
import sqlite3

import google.generativeai as genai
## Configure Genai Key

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

## Function To Load Google Gemini Model and provide queries as response

def get_gemini_response(question,prompt):
    model=genai.GenerativeModel('gemini-1.5-pro-001')
    response=model.generate_content([prompt[0],question])
    return response.text

## Fucntion To retrieve query from the database

def read_sql_query(sql,db):
    conn=sqlite3.connect(db)
    cur=conn.cursor()
    rows=cur.execute(sql)
    for row in rows:
        print(row)
    conn.commit()
    conn.close()

## Define Your Prompt
prompt=[
    """
    You are an expert in converting English questions to SQL query!
    The SQL database has the name EMPLOYEES and has the following tables dept and emp
    table dept stores columns - DEPTNO, DNAME, LOC
    table emp stores columns - EMPNO, ENAME, JOB, MGR, HIREDATE, SAL, COMM, DEPTNO
    The emp table has a foreign key constraint on deptno which references dept table.
    For example,
    Example 1 - How many employees exits?, 
    the SQL command will be something like this SELECT COUNT(*) FROM emp ;
    Example 2 - Tell me all the employees working in accounting?, 
    the SQL command will be something like this SELECT * FROM emp, dept WHERE emp.deptno=dept.deptno AND dept.dname='ACCOUNTING';
    also the sql code should not have ``` in beginning or end and sql word in output
    """
]

question=input("Enter the question: ")
response=get_gemini_response(question,prompt)
print(response)
read_sql_query(response,"employees.db")