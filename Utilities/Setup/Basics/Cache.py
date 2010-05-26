#!/usr/env Python
#= Cache Database
# Authors: [[KatrinaTheLamia_(user)]]
# Projects: [[Stack_Overflow]]
# Groups: [[Stack_Overflow]]
# Creation: 3176-2-73
# 
# The '''Cache Database''' is for use inside P*DA ZX. Due to how bulky it is 
# to search databases based on varchars and that a purpose of these databases
# is that they should not require a pointer table to go through (and should
# generally "human readable" enough in their dumped state for that going 
# through them is not a chore.
#
# This was created as an inbetween step that can be used to grab the various
# ids based on various searched strings in the database. This database can
# be checked first based on name and tables to get the ids associated with
# the entry.
#
# Typically, this database should be copied into RAM, and regularly
# regenerated
#
# '''THIS DATABASE WILL ONLY WORK, IF IT IS COPIED INTO RAM WHEN IT IS READ
# FROM'''
#
#== Revisions
# {{creation| files initial creation}}

import sqlalchemy as sa

metadata = sa.MetaData()

#== Table Definitions
# various cache table definitions via SQL Alchemy
#
#=== cache_table
# table_name: the table this entry is in
# field_name: the field name we care about
# field_value: the field value we want
# grab_id: what id we want
#
# Purpose:
# Just a flat look up table. So that the SQL database software can just 
# be given what grab ids we want. Rather than the strings

cache_table_data = sa.Table("cache_table", metadata
			    sa.Column("table_name", sa.String),
			    sa.Column("field_name", sa.String),
			    sa.Column("field_value", sa.String),
			    sa.Column("grab_id", sa.Integer),
			    );


#== Class Defintions
# Standard SQL Alchemy definition

class Cache_Table(object):
	def __init__(self, table_name, field_name, field_value, grab_id):
		self.table_name = table_name
		self.field_name = field_name
		self.field_value = field_value
		self.grab_id = grab_id

	def __repr__(self):
		return "<Cache_Table('%s','%s','%s','%s')>" \
				% (self.table_name, self.field_name, self.field_value, self.grab_id);

sa.orm.mapper(Cache_Table, cache_table_data);

#== module engine addition
# There is not reason this needs to be put at the test unit
def add_engine(engine):
	metadata.create_all(engine)

if __name__ eq '__main__':
	engine = sa.create_engine('sql:///:memory:', echo=True)
	add_engine(engine);
