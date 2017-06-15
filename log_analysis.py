#!/usr/bin/env python3

import psycopg2

DBNAME = "news"


def execute_query(query):
    """execute_query takes an SQL query as a parameter. Executes the 
    query and returns the results as a list of tuples."""
    try:
        db = psycopg2.connect(database=DBNAME)
        c = db.cursor()
        c.execute(query)
        result = c.fetchall()
        db.close()
        return result
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if c is not None:
            db.close()


def pop_posts():
    """Returns top three articles with most views in descending order"""
    query = """SELECT title, count(*) as views
    FROM articles a, log l
    WHERE a.slug=substring(l.path, 10)
    GROUP BY title 
    ORDER BY views DESC LIMIT 3;"""
    results = execute_query(query)
    print("Most popular articles:")
    for (title, count) in results:
        print("         {} - {} views".format(title, count))
    print("-" * 70)


def pop_auth():
    """Returns author with most article views in descending order"""
    query = """SELECT authors.name AS name, count(*) AS views
       FROM authors, articles, log
       WHERE authors.id = articles.author
         AND log.path = concat('/article/', articles.slug)
       GROUP BY authors.name
       ORDER BY views DESC;"""
    results = execute_query(query)
    print("Most popular authors:")
    for (name, views) in results:
        print("         {} - {} views".format(name, views))
    print("-" * 70)


def bad_days():
    """Returns amount of 404 errors with date/time"""
    query = """SELECT to_char(date, 'FMMonth FMDD, YYYY'), err/total AS ratio
			       FROM (select time::date as date,
			                    count(*) as total,
			                    sum((status != '200 OK')::int)::float as err
			                    from log
			                    group by date) AS errors
			       WHERE err/total > .01;"""
    results = execute_query(query)
    print("Days with more than 1% errors:")
    for (date, errors) in results:
        print("         {} - {}% errors".format(date, int(errors * 100)))
    print("-" * 70)

if __name__ == '__main__':
    pop_posts()
    pop_auth()
    bad_days()
