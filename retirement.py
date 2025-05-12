import sqlite3

# Connect to SQLite database 
conn = sqlite3.connect("retirement.db")
cursor = conn.cursor()

# Drop tables if they already exist
cursor.execute("DROP TABLE IF EXISTS Employee")
cursor.execute("DROP TABLE IF EXISTS Pay")
cursor.execute("DROP TABLE IF EXISTS SocialSecurityMin")

# Create Employee table
cursor.execute("""
CREATE TABLE Employee (
    EmployeeID INTEGER PRIMARY KEY,
    Name TEXT
)
""")

# Create Pay table
cursor.execute("""
CREATE TABLE Pay (
    EmployeeID INTEGER,
    Year INTEGER,
    Earnings REAL,
    FOREIGN KEY (EmployeeID) REFERENCES Employee(EmployeeID)
)
""")

# Create SocialSecurityMin table
cursor.execute("""
CREATE TABLE SocialSecurityMin (
    Year INTEGER PRIMARY KEY,
    Minimum REAL
)
""")


employee_data = [
    (1, "Louis Joseph"),
    (2, "Lorraine Marie"),
    (3, "Bentley Louis")
]
cursor.executemany("INSERT INTO Employee (EmployeeID, Name) VALUES (?, ?)", employee_data)


pay_data = [
    (1,2023,32800), (1,2022,32231), (1,2021,32231), (1,2020,29752), (1,2019,29479),
    (1,2018,26214), (1,2017,14298), (1,2016,5486), (1,2015,0), (1,2014,5000),
    (1,2013,2500), (1,2012,5000), (1,2011,4650), (1,2010,2325), (1,2009,26901),
    (1,2008,20889), (1,2007,90294), (1,2006,94200), (1,2005,90000), (1,2004,87900),
    (1,2003,86141), (1,2002,84900), (1,2001,80400), (1,2000,76200), (1,1999,72600),
    (1,1998,68400), (1,1997,65400), (1,1996,62700), (1,1995,61200), (1,1994,52439),
    (1,1993,46343), (1,1992,42503), (1,1991,42593), (1,1990,39217), (1,1989,21865),
    (1,1988,7634), (1,1987,7159), (1,1986,5574), (1,1985,3200), (1,1984,926), (1,1983,650),
    (2,2023,100000), (2,2022,50000), (2,2021,42000), (2,2020,36000), (2,2019,24000),
    (3,2023,45000), (3,2022,15000)
]
cursor.executemany("INSERT INTO Pay (EmployeeID, Year, Earnings) VALUES (?, ?, ?)", pay_data)


social_security_min_data = [
    (1983,6800), (1984,7050), (1985,7425), (1986,7875), (1987,8175), (1988,8400),
    (1989,8925), (1990,9525), (1991,9900), (1992,10350), (1993,10725), (1994,11250),
    (1995,11325), (1996,11625), (1997,12150), (1998,12675), (1999,13425), (2000,14175),
    (2001,14925), (2002,15750), (2003,16125), (2004,16275), (2005,16725), (2006,17475),
    (2007,18150), (2008,18975), (2009,19800), (2010,19800), (2011,19800), (2012,20475),
    (2013,21075), (2014,21750), (2015,22050), (2016,22050), (2017,23625), (2018,23850),
    (2019,24675), (2020,25575), (2021,26550), (2022,27300), (2023,29700)
]
cursor.executemany("INSERT INTO SocialSecurityMin (Year, Minimum) VALUES (?, ?)", social_security_min_data)

# Commit the data
conn.commit()


query = """
SELECT 
    e.EmployeeID,
    e.Name,
    p.Year,
    p.Earnings,
    s.Minimum,
    CASE 
        WHEN p.Earnings >= s.Minimum THEN 'Yes'
        ELSE 'No'
    END AS CountsTowardRetirement
FROM Employee e
JOIN Pay p ON e.EmployeeID = p.EmployeeID
JOIN SocialSecurityMin s ON p.Year = s.Year
ORDER BY e.EmployeeID, p.Year
"""

print("Retirement Eligibility Report:\n")
print(f"{'ID':<4} {'Name':<15} {'Year':<6} {'Earnings':<10} {'Minimum':<10} {'Counts'}")
print("-" * 60)

for row in cursor.execute(query):
    emp_id, name, year, earnings, minimum, counts = row
    print(f"{emp_id:<4} {name:<15} {year:<6} {earnings:<10.0f} {minimum:<10.0f} {counts}")

# Close the connection
conn.close()