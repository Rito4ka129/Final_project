import mysql.connector
from connector import ConnectorRead


def print_result(result):
    for i in result:
        print(

            f'title: {i[1]}, description: {i[2]}, year: {i[3]}, category: {i[4]}\n')


def print_result_actor(result):
    for i in result:
        print(
            f'title: {i[1]}, description: {i[2]}, year: {i[3]}, category: {i[4]}, actor_first_name: {i[5]}, actor_last_name: {i[6]}\n')


def query_added(query):
    dbconfig = {
        'host': 'mysql.itcareerhub.de',
        'user': 'ich1',
        'password': 'ich1_password_ilovedbs',
        'database': '310524ptm_Margarita'
    }
    connection = mysql.connector.connect(**dbconfig)
    cursor = connection.cursor()
    cursor.execute(f"SELECT * FROM query_results WHERE query = '{query}'")
    res = cursor.fetchall()

    if len(res) > 0:
        cursor.execute(f"UPDATE query_results SET count = {res[0][-1] + 1} WHERE id = {res[0][0]}")
    else:
        cursor.execute(f"INSERT INTO query_results (query, count) VALUES ('{query}', 1)")

    connection.commit()
    cursor.close()
    connection.close()


def get_result_keyword(search_str):
    select = f"""select distinct
 t1.film_id, t1.title, t1.description, t1.release_year, 
t3.name as name, 
 t5.first_name, t5.last_name
from film as t1
left join film_category as t2
on t1.film_id = t2.film_id
left join category as t3
on t3.category_id = t2.category_id
left join film_actor as t4
on t1.film_id = t4.actor_id
left join actor as t5
on t4.actor_id = t5.actor_id
where title like '%{search_str}%' or 
description like '%{search_str}%' or 
release_year like '%{search_str}%' or
first_name like '%{search_str}%' or
name like '%{search_str}%' limit 5000;
    """

    con = ConnectorRead.get_connect()
    con.connect()
    cursor = con.cursor()
    cursor.execute(select)
    result = cursor.fetchall()
    cursor.close()
    con.close()

    query_added(search_str)
    return print_result(result)


def get_result_category(category):
    select = f"""select distinct
            t1.film_id, t1.title, t1.description, t1.release_year, 
            t3.name as category_name 
            from film as t1
            left join film_category as t2 on t1.film_id = t2.film_id
            left join category as t3 on t3.category_id = t2.category_id
            where t3.name like '%{category}%' limit 10
                        """
    con = ConnectorRead.get_connect()
    con.connect()
    cursor = con.cursor()
    cursor.execute(select)
    result = cursor.fetchall()
    cursor.close()
    con.close()

    query_added(category)
    return result


def get_result_actor(actor):
    select = f"""select distinct
            t1.film_id, t1.title, t1.description, t1.release_year, 
            t3.name as category_name, 
            t5.first_name, t5.last_name
            from film as t1
            left join film_category as t2 on t1.film_id = t2.film_id
            left join category as t3 on t3.category_id = t2.category_id
            left join film_actor as t4 on t1.film_id = t4.film_id
            left join actor as t5 on t4.actor_id = t5.actor_id
            where t5.first_name like '%{actor}%' or t5.last_name like '%{actor}%' limit 10
            """
    con = ConnectorRead.get_connect()
    con.connect()
    cursor = con.cursor()
    cursor.execute(select)
    result = cursor.fetchall()
    cursor.close()
    con.close()

    query_added(actor)
    return result


def get_result_title(title):
    select = f"""select distinct
            t1.film_id, t1.title, t1.description, t1.release_year, 
            t3.name as category_name, 
            t5.first_name, t5.last_name
            from film as t1
            left join film_category as t2 on t1.film_id = t2.film_id
            left join category as t3 on t3.category_id = t2.category_id
            left join film_actor as t4 on t1.film_id = t4.film_id
            left join actor as t5 on t4.actor_id = t5.actor_id
            where t1.title like '%{title}%' limit 10
            """
    con = ConnectorRead.get_connect()
    con.connect()
    cursor = con.cursor()
    cursor.execute(select)
    result = cursor.fetchall()
    cursor.close()
    con.close()

    query_added(title)
    return result


def get_result_description(description):
    select = f"""select distinct
                    t1.film_id, t1.title, t1.description, t1.release_year, 
                    t3.name as category_name, 
                    t5.first_name, t5.last_name
                    from film as t1
                    left join film_category as t2 on t1.film_id = t2.film_id
                    left join category as t3 on t3.category_id = t2.category_id
                    left join film_actor as t4 on t1.film_id = t4.film_id
                    left join actor as t5 on t4.actor_id = t5.actor_id
                    where t1.description like '%{description}%' limit 15
                    """
    con = ConnectorRead.get_connect()
    con.connect()
    cursor = con.cursor()
    cursor.execute(select)
    result = cursor.fetchall()
    cursor.close()
    con.close()

    query_added(description)
    return result


def get_result_year(year):
    select = f"""select distinct
            t1.film_id, t1.title, t1.description, t1.release_year, 
            t3.name as category_name
            from film as t1
            left join film_category as t2 on t1.film_id = t2.film_id
            left join category as t3 on t3.category_id = t2.category_id
            where t1.release_year = '{year}' limit 10
            """
    con = ConnectorRead.get_connect()
    con.connect()
    cursor = con.cursor()
    cursor.execute(select)
    result = cursor.fetchall()
    cursor.close()
    con.close()

    query_added(year)
    return result


def get_top_result():
    dbconfig = {
        'host': 'mysql.itcareerhub.de',
        'user': 'ich1',
        'password': 'ich1_password_ilovedbs',
        'database': '310524ptm_Margarita'
    }
    connection = mysql.connector.connect(**dbconfig)
    cursor = connection.cursor()
    cursor.execute(f"SELECT * FROM query_results order by count desc limit 10")
    res = cursor.fetchall()
    for i in res:
        print(f'{i[1]}\t{i[-1]}')
