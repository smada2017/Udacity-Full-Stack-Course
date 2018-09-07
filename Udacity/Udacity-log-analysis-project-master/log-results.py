#!/usr/bin/env python

import psycopg2

DBNAME = "news"

rq1 = "What are the most popular articles of all time?"

query1 = ("SELECT title, count(*) as views FROM articles \n"
          "  JOIN log\n"
          "    ON articles.slug = substring(log.path, 10)\n"
          "    GROUP BY title ORDER BY views DESC LIMIT 3;")

rq2 = "Who are the most popular article authors of all time?"

query2 = ("SELECT authors.name, count(*) as views\n"
          "    FROM articles \n"
          "    JOIN authors\n"
          "      ON articles.author = authors.id \n"
          "      JOIN log \n"
          "      ON articles.slug = substring(log.path, 10)\n"
          "      WHERE log.status LIKE '200 OK'\n"
          "      GROUP BY authors.name ORDER BY views DESC;")

rq3 = "On which days more than 1% of the requests led to error?"

query3 = ("SELECT round((stat*100.0)/visitors, 3) as\n"
          "        solution, to_char(errortime, 'Mon DD, YYYY')\n"
          "        FROM errorcount ORDER BY solution desc limit 1;")

# Connect to the db and retrieve solutions


def queryR(sql_query):

    db = psycopg2.connect(database=DBNAME)
    c = db.cursor()
    c.execute(sql_query)
    solutions = c.fetchall()
    db.close()
    return solutions


def printsolutions(q_list):

    for i in range(len(q_list)):
        res = q_list[i][1]
        title = q_list[i][0]
        print("\t" + "%s - %d" % (title, res) + " views")
    print("\n")


solution1 = queryR(query1)
solution2 = queryR(query2)
solution3 = queryR(query3)

print(rq1)
printsolutions(solution1)
print(rq2)
printsolutions(solution2)
print(rq3)
print("\t" + solution3[0][1] + " - " + str(solution3[0][0]) + "%")
