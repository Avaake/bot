import cx_Oracle
import mysql.connector


class PushSMSUser:

    def start_oracle(self):
        oracledb = cx_Oracle.connect("it_skills_bot/FFjdjjj55_mdmdmddTTE231N@db.it-skills.in.ua:1521/orclpdb")
        oracle_cursor = oracledb.cursor()
        query = "SELECT * FROM test1"
        oracle_cursor.execute(query)
        results = oracle_cursor.fetchall()

        query2 = "SELECT * FROM it_skills.param_values WHERE PARAM_NAME = 'SEND_SMS_TO_STUDENT_ABOUT_A_LONG_ABSENCE2'"
        oracle_cursor.execute(query2)
        results2 = oracle_cursor.fetchall()

        oracle_cursor.close()
        oracledb.close()
        return results, results2

    def start_mysql(self):
        mydb = mysql.connector.connect(
            host='sql.turbosms.ua',
            user='kastanta91',
            password='hdAIe_e12Msk_6sJJ',
            database='users'
        )
        mycursor = mydb.cursor()

        results = self.start_oracle()
        message = results[-1][-1][-3]

        for row in results[0]:
            number = row[-1]
            firs_name = row[1]
            query = "INSERT INTO kastanta91 (number, sign, message) VALUES (%s, %s, %s)"
            values = (number, 'ITskillsUA', message.replace('$', firs_name))
            mycursor.execute(query, values)

        mydb.commit()

        mycursor.close()
        mydb.close()


if __name__ == "__main__":
    c = PushSMSUser()
    c.start_mysql()

