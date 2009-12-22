#!/bin/env python
# Comments put in later

import sqlalchemy as sa

metadata = sa.MetaData()

stats_table = sa.Table('stats', metadata,
		sa.Column('id', sa.Integer, primary_key=True),
		sa.Column('Name', sa.String), # What is this stat called?
		sa.Column('Value', sa.Integer), # What is this stats value?
		sa.Column('EV', sa.Integer), # What is this stats EV? (Gen 3 and 4)
		sa.Column('IV', sa.Integer), # What is this stats IVs?
		sa.Column('Experience', sa.Integer), # What is this stats Move Experience? (Gen 1 and 2)
		)

class Stats(object):
	def __init__(self, Name, Value, EV, IV, Experience):
		self.Name = Name
		self.Value = Value
		self.EV = EV
		self.IV = IV
		self.Experience = Experience

	def __repr(self):
		return "<Stats('%s','%s','%s','%s','%s')>" % (self.Name, self.Value, self.EV, self.IV, self.Experience)

def add_engine(engine):
	metadata.create_all(engine)

sa.orm.mapper(Stats, stats_table)

if __name__ eq '__main__':
	engine = sa.create_engine('sql:///:memory:',echo=True)
	add_engine(engine)

