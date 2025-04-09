## SQL reference https://livesql.oracle.com/ords/livesql/file/content_O5AEB2HE08PYEPTGCFLZU9YCV.html

import sqlite3

## Connectt to SQlite
connection=sqlite3.connect("employees.db")

# Create a cursor object to insert record,create table

cursor=connection.cursor()

## create dept table
table_info="""
create table dept(   
  deptno     number(2,0),   
  dname      varchar2(14),   
  loc        varchar2(13),   
  constraint pk_dept primary key (deptno)   
)
"""
cursor.execute(table_info)

## Insert Some more records

cursor.execute('''insert into DEPT (DEPTNO, DNAME, LOC) values(10, 'ACCOUNTING', 'NEW YORK')''')
cursor.execute('''insert into dept values(20, 'RESEARCH', 'DALLAS')''')
cursor.execute('''insert into dept values(40, 'OPERATIONS', 'BOSTON')''')


table_info = """create table emp(   
  empno    number(4,0),   
  ename    varchar2(10),   
  job      varchar2(9),   
  mgr      number(4,0),   
  hiredate date,   
  sal      number(7,2),   
  comm     number(7,2),   
  deptno   number(2,0),   
  constraint pk_emp primary key (empno),   
  constraint fk_deptno foreign key (deptno) references dept (deptno)   
)
"""
cursor.execute(table_info)


cursor.execute("""insert into emp   
values(   
 7839, 'KING', 'PRESIDENT', null,   
 '17-11-1981',   
 5000, null, 10   
)""")
cursor.execute("""insert into emp  
values(  
 7698, 'BLAKE', 'MANAGER', 7839,  
 '1-5-1981',  
 2850, null, 30  
)""")
cursor.execute("""insert into emp
values(  
 7782, 'CLARK', 'MANAGER', 7839,  
 '9-6-1981',  
 2450, null, 10  
)""")
cursor.execute("""insert into emp
values(  
 7566, 'JONES', 'MANAGER', 7839,  
 '2-4-1981',  
 2975, null, 20  
)""")
cursor.execute("""insert into emp
values(  
 7788, 'SCOTT', 'ANALYST', 7566,  
 '13-JUL-87' - 85,  
 3000, null, 20  
)""")
cursor.execute("""insert into emp
values(  
 7902, 'FORD', 'ANALYST', 7566,  
 '3-12-1981',  
 3000, null, 20  
)""")
cursor.execute("""insert into emp
               values(  
 7369, 'SMITH', 'CLERK', 7902,  
 '17-12-1980',  
 800, null, 20  
)""")
cursor.execute("""insert into emp
values(  
 7499, 'ALLEN', 'SALESMAN', 7698,  
 '20-2-1981',  
 1600, 300, 30  
)""")
cursor.execute("""insert into emp
values(  
 7521, 'WARD', 'SALESMAN', 7698,  
 '22-2-1981',  
 1250, 500, 30  
)""")
cursor.execute("""insert into emp
values(  
 7654, 'MARTIN', 'SALESMAN', 7698,  
 '28-9-1981',  
 1250, 1400, 30  
)""")
cursor.execute("""insert into emp
values(  
 7844, 'TURNER', 'SALESMAN', 7698,  
 '8-9-1981',  
 1500, 0, 30  
)""")
cursor.execute("""insert into emp
values(  
 7876, 'ADAMS', 'CLERK', 7788,  
 '13-JUL-87' - 51,  
 1100, null, 20  
)""")
cursor.execute("""insert into emp
               values(  
 7900, 'JAMES', 'CLERK', 7698,  
 '3-12-1981',  
 950, null, 30  
)""")
cursor.execute("""insert into emp
values(  
 7934, 'MILLER', 'CLERK', 7782,  
 '23-1-1982',  
 1300, null, 10  
)""")


## Disspaly ALl the records in DEPT

print("The isnerted records are")
data=cursor.execute('''Select * from DEPT''')
for row in data:
    print(row)

## Disspaly ALl the records in EMP

print("The isnerted records are")
data=cursor.execute('''Select * from EMP''')
for row in data:
    print(row)

 
## Commit your changes int he databse
connection.commit()
connection.close()
