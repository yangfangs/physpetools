# ########################## Copyrights and License #############################
#                                                                               #
# Copyright 2016 Yang Fang <yangfangscu@gmail.com>                              #
#                                                                               #
# This file is part of PhySpeTree.                                              #
# https://xiaofeiyangyang.github.io/physpetools/                                #
#                                                                               #
# PhySpeTree is free software: you can redistribute it and/or modify it under   #
# the terms of the GNU Lesser General Public License as published by the Free   #
# Software Foundation, either version 3 of the License, or (at your option)     #
# any later version.                                                            #
#                                                                               #
# PhySpeTree is distributed in the hope that it will be useful, but WITHOUT ANY #
# WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS     #
# FOR A PARTICULAR PURPOSE. See the GNU Lesser General Public License for more  #
# details.                                                                      #
#                                                                               #
# You should have received a copy of the GNU Lesser General Public License      #
# along with PhySpeTree. If not, see <http://www.gnu.org/licenses/>.            #
#                                                                               #
# ###############################################################################

"""
The operate sqlite3 DB class

"""

import sqlite3


class operate_db():
    def __init__(self, db_path):
        """connect a  DB with file path"""
        self.conn = sqlite3.connect(db_path)
        self.conn.text_factory = str
        self.cur = self.conn.cursor()

    def create(self, table, colname_list):
        """create a table with col name"""
        text = ' TEXT, '.join(colname_list)
        print text
        createlist = ["create table if not exists %s" % table, "(id integer primary key autoincrement, NAME TEXT, ",
                      text, " TEXT)"]
        createsql = ''.join(createlist)
        try:
            self.cur.execute(createsql)
            self.done()
        except sqlite3.Error, e:
            print(e)
            self.conn.rollback()

    def insert(self, table, name_list):
        """insert name to table"""
        insert_name = []
        for line in name_list:
            insert_name.append((line,))
        try:
            # self.cur.executemany("INSERT INTO {0}(NAME) VALUES ({1})".format(table, insert_name))
            sql_insert = "INSERT INTO %s (NAME) VALUES (?)" % table
            self.cur.executemany(sql_insert, insert_name)
            self.done()
        except sqlite3.Error, e:
            print(e)
            self.conn.rollback()

    def update(self, table, col_name, name_flag, value):
        """update table example:update('table_one','K02865','hsa','has:2525525')"""
        sql_update = "UPDATE {0} SET {1}=? WHERE NAME=?".format(table, col_name)
        try:
            self.cur.execute(sql_update, (value, name_flag))
            self.done()
        except sqlite3.Error, e:
            print (e)
            self.conn.rollback()

    def display_row(self, table, abb_name):
        """display the row by abb name"""
        sql_disply = "SELECT * FROM {0} WHERE NAME='{1}'".format(table, abb_name)
        try:
            self.cur.execute(sql_disply)
            result = self.cur.fetchall()
            self.done()
            print (result)
        except sqlite3.Error, e:
            print (e)
            self.conn.rollback()

    def dispay_col(self, table, col_name):
        """get the table col data by col name"""
        sql_select = "SELECT {0} FROM {1}".format(col_name, table)
        try:
            self.cur.execute(sql_select)
            col_data = self.cur.fetchall
            self.done()
            return col_data
        except sqlite3.Error, e:
            print (e)
            self.conn.rollback()

    def drop(self, table):
        """drop the table"""
        try:
            self.cur.execute("DROP TABLE IF EXISTS %s" % table)
            self.done()
        except sqlite3.Error, e:
            print e
            self.conn.rollback()

    def done(self):
        """commit"""
        self.conn.commit()

    def close(self):
        """close DB"""
        self.conn.close()
