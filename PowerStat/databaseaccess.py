from mysql.connector import Error, MySQLConnection
from python_mysql_dbconfig import read_db_config

def insert_ecb_stats(recordId, residentId, statTime, voltage, current, phase):
    query = "INSERT INTO DOMESTIC_USAGE_STATS(RECORD_ID,RESIDENT_ID,STAT_TIME,VOLTAGE,CURRENT_VALUE,PHASE_ANGEL) " \
            "VALUES(%s,%s,%s,%s,%s,%s)"
    args = (recordId, residentId, statTime, voltage, current, phase)

    try:
        db_config = read_db_config()
        conn = MySQLConnection(**db_config)

        cursor = conn.cursor()
        cursor.execute(query, args)

        if cursor.lastrowid:
            print('last insert id', cursor.lastrowid)
        else:
            print('last insert id not found')

        conn.commit()
    except Error as error:
        print(error)
        return False

    finally:
        cursor.close()
        conn.close()
        return True

def get_ecb_stats(residentId):
    query = "select STAT_TIME, VOLTAGE, CURRENT_VALUE, PHASE_ANGEL from DOMESTIC_USAGE_STATS"
    db_config = read_db_config()
    conn = MySQLConnection(**db_config)

    cursor = conn.cursor()
    args = residentId
    cursor.execute(query, args)

    for (STAT_TIME, VOLTAGE, CURRENT_VALUE, PHASE_ANGEL) in cursor:
        print STAT_TIME
        print VOLTAGE
        print CURRENT_VALUE
        print PHASE_ANGEL

    cursor.close()
    return True
