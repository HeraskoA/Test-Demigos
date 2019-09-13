import psycopg2


class Db(object):
    def __init__(self):
        self.connection = psycopg2.connect(
            user="admin",
            password="admin_pass",
            host="db",
            dbname="pg_core_db"
        )

    def set_or_update_currency_rate(self, pair, rate):
        cursor = self.connection.cursor()
        cursor.execute(
                    """
                    INSERT INTO rate(pair, price)
                    VALUES('%s', %s) ON CONFLICT (pair) DO UPDATE SET price = %s;
                    """ % (pair, rate, rate)
                )
        self.connection.commit()
        cursor.close()

    def get_rates(self):
        cursor = self.connection.cursor()
        cursor.execute(
            """
            select pair, price from rate;
            """
        )
        data = cursor.fetchall()
        cursor.close()

        return [{"pair": d[0], "rate": d[1]} for d in data]

    def add_pair(self, pair):
        cursor = self.connection.cursor()
        cursor.execute("""INSERT INTO rate(pair, price)
                    VALUES('%s', 0.0) ON CONFLICT (pair) DO nothing""" % pair)
        self.connection.commit()
        cursor.close()

    def get_all_pairs(self):
        cursor = self.connection.cursor()
        cursor.execute(
            """
            select pair from rate;
            """,
        )
        data = cursor.fetchall()
        cursor.close()
        return [d[0] for d in data]

    def close(self):
        self.connection.close()


def get_html(data):
    temp = """<tr><td>{}</td><td>{}</td></tr>"""
    table = ""
    for currency_rate in data:
        table += temp.format(currency_rate["pair"], currency_rate["rate"])

    table = "<table>" + table + "</table>"

    form = """<form action="/add", method="post"><p><b>Add new pair</b></p><input type="text" name="pair" value="">\
    <p><input type="submit"></p></form>""".replace(r"\s", "")
    return table + form
