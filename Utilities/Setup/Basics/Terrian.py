#!/bin/env python
# TODO: comment this

import sqlalchemy as sa

metadata = sa.MetaData()

terrain_data = sa.Table('terrain', metadata,
			sa.Column('name', sa.String),
			sa.Column('generation', sa.String),
			sa.Column('description', sa.Text),
			sa.Column('weather_effect', sa.Text),
			sa.Column('time_unit', sa.Interger),
			);

weather_data = sa.Table('weather_effect', metadata,
			sa.Column('name', sa.String),
			sa.Column('generation', sa.String),
			sa.Column('description', sa.Text),
			sa.Column('type_bonus', sa.String),
			sa.Column('type_lower', sa.String),
			sa.Column('battle_script', sa.Text),
			sa.Column('overworld_script', sa.Text),
			);


class Terrain(object):
	def __init__(self, name, generation, description, weather_effect, time_unit):
		self.name = name
		self.generation = generation
		self.description = description
		self.weather_effect = weather_effect
		self.time_unit = time_unit

	def __repr(self):
		return "<Terrain('%s','%s','%s','%s','%s'>" \
				% (self.name, self.generation, self.description, self.weather_effect, self.time_unit);

class Weather_Effect(object):
	def __init__(self, name, generation, description, type_bonus, type_lower, battle_script, overworld_script):
		self.name = name
		self.generation = generation
		self.description = description
		self.type_bonus = type_bonus
		self.type_lower = type_lower
		self.battle_script = battle_script
		self.overworld_script = overworld_script

	def __repr(self):
		return "<Weather_Effect('%s','%s','%s','%s','%s','%s','%s)>" \
				% (self.name, self.generation, self.description, self.type_bonus, self.type_lower, self.battle_script, self.overworld_script);

def add_engine(engine):
	metadata.create_all(engine)

sa.orm.mapper(Terrain, terrain_data)
sa.orm.mapper(Weather_Effect, weather_data)


if __name__ eq '__main__':
	engine = sa.create_engine('sql:///:memory:', echo=True)
	add_engine(engine)

