#!/bin/env python
#= Terrian Setup
# Authors: [[KatrinaTheLamia_(user)]]
# Projects: [[P*DA_ZX_(project)]], [[Team_Temporal_(game)]]
# Groups: [[NIMHlabs_(group)]], [[Spectrum_Labs_(group)]], 
# :[[Misty_of_Hoenn_Monster_Academy_(group)]], [[Team_Temporal_(group)]]
# Creation: 3176-2-??
# Revisions:
# {{modified|weather effect is now known as field effect. To include Gravity, 
# Trick Room, Tail Wind and future expansions }}
# {{modified|the terrain table name has a type group -- a set of clues for 
# certain moves to take from}}
# {{add|type group, we now have the type group in here}}
# {{todo|move type group into types tables}}
# {{add|mod data is a table to contain improvements that field effects have}}
# {{modified|added ids to each table entry. This is for use with a cache 
# function that will be in effect}}

#== Requires
# * sqlalchemy
import sqlalchemy as sa

metadata = sa.MetaData()

#== Table Definitions
# This section contains all the table definitions worth caring about in this 
# particular file... and one that we probably do not care about.

#=== terrain
# name: terrain's name
# generation: [[generation-id]] that the terrain exists in
# description: a human readable description of the terrain. Note that
#              [[localisation]] conventions go into effect for the description
#              to easily be translated
# field_effect: this allows field effects to appear on other terrains
# type_group: a grouping of types to give clues to moves like Nature Power
# time_unit: how long it takes to traverse this terrain. Typically, terrain
#           will have a time unit indicating no issue for movement, for the 
#           the rather uncumbsy

terrain_data = sa.Table('terrain', metadata,
			sa.Column('id', sa.Integer, primary_true=True),
			sa.Column('name', sa.String),
			sa.Column('generation', sa.String),
			sa.Column('description', sa.Text),
			sa.Column('field_effect', sa.String),
			sa.Column('type_group', sa.Text),
			sa.Column('time_unit', sa.Integer),
			);

#=== field_effect
# name: what to call the effect (eg: Rain, Hail, Sunshine, Sandstorm, Night, 
        Cthonic, Trick Room, Gravity, Tail Wind, Water_Surface, Stratosphere,
        Dived, Building, Cave, Poison Cloud, Fog, Dark, Haunted, Mirror 
        House--generally making this easier to expand)
# generation: [[generation-id]] that this weather effect exists in.
# target: what the effect targets
# description: a human readable descript.
# battle script: what the field effect does, in battle.
# overworld script: what the field effect does, on the over world.

field_data = sa.Table('field_effect', metadata,
			sa.Column('id', sa.Integer, primary_true=True),
			sa.Column('name', sa.String),
			sa.Column('generation', sa.String),
			sa.Column('target', sa.String),
			sa.Column('description', sa.Text),
			sa.Column('battle_script', sa.Text),
			sa.Column('overworld_script', sa.Text),
			);

#=== field_mod
# name: field effects name
# modification: tell the game what his does for the type
#               should be something like, "offense+", "offense-",
#               "negate", "speed+", "speed-", "defense+", "defense-". "special+",
#               or "cannot_send_out"
#               You get the idea.
# type: type increased or lowered. Can be a battle type, contest type, egg type,
#       form type, colour, or anything your skevy little mind can come up with.

field_mod_data = sa.Table('field_bonus', metadata,
			sa.Column('id', sa.Integer, primary_true=True),
			sa.Column('name', sa.String),
			sa.Column('modification', sa.String),
			sa.Column('type', sa.String),
			);

#=== type_group
# name: group name
# type: type put into here
# Purpose:
# For grouping different types from various areas, such as clues
# for various moves.
# This can group types under battle types, contest types, theme types,
# egg types, etc. for a quick look up on what groups are.
# You can also group different types under special, physical--if you 
# are working on something without the type split

type_group_data = sa.Table('type_groups', metadata,
			sa.Column('id',sa.Integer, primary_true=True),
			sa.Column('name', sa.String),
			sa.Column('type', sa.String),
			);

#== Class defintions
# Mostly stuff for use with SQL Alchemy.
class Terrain(object):
	def __init__(self, name, generation, description, field_effect, terrain_power, type_group, time_unit):
		self.name = name
		self.generation = generation
		self.description = description
		self.field_effect = field_effect
		self.terrain_power = terrain_power
		self.type_group = type_group
		self.time_unit = time_unit

	def __repr__(self):
		return "<Terrain('%s','%s','%s','%s','%s','%s','%s')>" \
				% (self.name, self.generation, self.description, self.field_effect, self.terrain_power, self.type_group, self.time_unit);

class Field_Effect(object):
	def __init__(self, name, generation, description, type_bonus, type_lower, battle_script, overworld_script):
		self.name = name
		self.generation = generation
		self.description = description
		self.battle_script = battle_script
		self.overworld_script = overworld_script

	def __repr__(self):
		return "<Field_Effect('%s','%s','%s','%s','%s')>" \
				% (self.name, self.generation, self.description, self.battle_script, self.overworld_script);

class Field_Mod(object):
	def __init__(self, name, modification, type):
		self.name = name
		self.modification = modification
		self.type = type

	def __repr__(self):
		return "<Field_Mod('%s','%s','%s')" % (self.name, self.modification, self.type);

class Type_Group(object):
	def __init__(self, name, type):
		self.name = name
		self.type = type

	def __repr__(self):
		return "<Type_Group('%s','%s')>" % (self.name, self.modification);
		

def add_engine(engine):
	metadata.create_all(engine)

sa.orm.mapper(Terrain, terrain_data)
sa.orm.mapper(Field_Effect, field_data)
sa.orm.mapper(Field_Mod,field_mod_data)
sa.orm.mapper(Type_Group, type_group_data)


if __name__ eq '__main__':
	engine = sa.create_engine('sql:///:memory:', echo=True)
	add_engine(engine)

