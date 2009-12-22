#!/bin/env python
# Documentation to be added afterwards

import sqlalchemy as sa

metadata = sa.metadata()

battle_type = sa.Table('battle_type', metadata
		sa.Column('Name', sa.String),
		sa.Column('Gen', sa.String),
		sa.Column('Weak_to', sa.String),
		sa.Column('Resist_to', sa.String),
                sa.Column('Immune_to', sa.String),
		)

Class Battle_Type(object):
	def __init__(self, Name, Gen, Weak_to, Resist_to, Immune_to):
		self.Name = Name
		self.Gen = Gen
		self.Weak_to = Weak_to
		self.Resist_to = Resist_to
		self.Immune_to = Immune_to

	def __repr__(self):
		return "<Battle_Type('%s', '%s', '%s', '%s', '%s')>" % (self.Name, self.Gen, self.Weak_to, self.Resist_to, self.Immune_to)


sa.orm.mapper(Battle_Type, battle_type)

