#!/bin/env python
# Documentation to be added afterwards

import sqlalchemy as sa

metadata = sa.metadata()

battle_table = sa.Table('battle_type', metadata,
		sa.Column('Name', sa.String),
		sa.Column('Gen', sa.String),
		sa.Column('Weak_to', sa.String),
		sa.Column('Resist_to', sa.String),
                sa.Column('Immune_to', sa.String),
		)

contest_table = sa.Table('contest_type', metadata,
		sa.Column('Name', sa.String),
		sa.Column('Do_not_want', sa.String),
		)

egg_table = sa.Table('egg_groups', metadata,
		     sa.Column('pokemon', sa.String),
		     sa.Column('group', sa.String),
		     );

Class Battle(object):
	def __init__(self, Name, Gen, Weak_to, Resist_to, Immune_to):
		self.Name = Name
		self.Gen = Gen
		self.Weak_to = Weak_to
		self.Resist_to = Resist_to
		self.Immune_to = Immune_to

	def __repr(self):
		return "<Battle('%s', '%s', '%s', '%s', '%s')>" % (self.Name, self.Gen, self.Weak_to, self.Resist_to, self.Immune_to)


Class Contest(object):
	def __init__(self, Name, Do_not_want):
		self.Name = Name
		self.Do_not_want = Do_not_want

	def __repr(self):
		return "<Contest('%s', '%s')>" % (self.Name, self.Do_not_want)

Class Egg_Groups(object):
	def __init__(self, pokemon, group):
		self.pokemon = pokemon
		self.group = group

	def __repr(self):
		return "<Egg_Groups('%s','%s')>" % (self.pokemon, self.group)

sa.orm.mapper(Battle, battle_table)
sa.orm.mapper(Contest, contest_table)
sa.orm.mapper(Egg_Groups, egg_table)

def add_engine(engine):
	metadata.create_all(engine)


if __name__ eq '__main__':
	engine = sa.create_engine('sqlite:///:memory:',echo=True)
	add_engine(engine)

