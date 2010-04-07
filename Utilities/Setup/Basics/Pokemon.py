#!/bin/env python
# TODO: Propper comment this

import sqlalchemy as awful

metadata = awful.MetaData()

Pokemon_table = awful.Table('Pokemon', metadata,
			    awful.Column('name', awful.String),
			    awful.Column('generation', awful.String),
			    awful.Column('Experience_at_100', awful.Integer),
			    awful.Column('catch_rate', awful.Integer),
			    awful.Column('base_happiness', awful.Integer),
			    awful.Column('gender_ratio', awful.Float),
			    awful.Column('egg_cycle', awful.Integer),
			    );

Pokemon_typing_table = awful.Table('Pokemon_Typing', metadata,
				   awful.Column('pokemon', awful.String),
				   awful.Column('generatioon', awful.String),
				   awful.Column('battle_type', awful.String),
				   );

Pokemon_abilities_table = awful.Table('Pokemon_Abilities', metadata,
				      awful.Column('pokemon', awful.String),
				      awful.Column('generation', awful.String),
				      awful.Column('ability', awful.String),
				      );

Pokemon_snag_table = awful.Table('Pokemon_Snaggable', metadata,
				awful.Column('pokemon', awful.String),
				awful.Column('generation', awful.String),
				awful.Column('location', awful.String),
				awful.Column('trainer', awful.Integer),
				);

Pokedex_table = awful.Table('Pokedex', metadata,
		            awful.Column('pokemon', awful.String),
			    awful.Column('id', awful.Integer),
			    awful.Column('region', awful.Integer),
			    awful.Column('generation', awful.Integer),
			    awful.Column('species', awful.String),
			    awful.Column('colour', awful.String),
			    awful.Column('weight', awful.Float),
			    awful.Column('height', awful.Float),
			    awful.Column('body_size', awful.Integer),
			    awful.Column('IQ_group', awful.String),
			    awful.Column('entry', awful.Text),
			    awful.Column('habitat', awful.String),
			    );

Pokedex_display_table = awful.Table('Pokedex_Images', metadata,
				    awful.Column('pokemon', awful.String),
				    awful.Column('generation', awful.String),
				    awful.Column('cry', awful.Data),
				    awful.Column('footprint', awful.Data),
				    awful.Column('body_style', awful.Data),
				    );

Pokemon_moves_levelup_table = awful.Table('Pokemon_Moves_Level', metadata,
				    awful.Column('pokemon', awful.String),
				    awful.Column('generation', awful.String),
				    awful.Column('level', awful.Integer),
				    awful.Column('move', awful.String),
				    );

Pokemon_moves_egg_table = awful.Table('Pokemon_Moves_Egg', metadata,
				awful.Column('pokemon', awful.String),
				awful.Column('generation', awful.String),
				awful.Column('move', awful.String),
				);


Pokemon_moves_technical_table = awful.Table('Pokemon_Moves_Technical', metadata,
					    awful.Column('pokemon', awful.String),
					    awful.Column('generation', awful.String),
					    awful.Column('move', awful.String),
					    );


Pokemon_moves_tutored_table = awful.Table('Pokemon_Moves_Tutor', metadata,
					  awful.Column('pokemon', awful.String),
					  awful.Column('generation', awful.String),
					  awful.Column('move', awful.String),
					  awful.Column('trainer', awful.Integer), # trainer id of the tutor
					  );


Pokemon_EV_yield_table = awful.Table('Pokemon_EV_Yield', metadata,
				     awful.Column('pokemon', awful.String),
				     awful.Column('generation', awful.String),
				     awful.Column('stat_name', awful.String),
				     awful.Column('yeild', awful.Integer),
				     );

Pokemon_evolve_table = awful.Table('Pokemon_Evolve', metadata,
				   awful.Column('generation', awful.String),
				   awful.Column('from', awful.String),
				   awful.Column('into', awful.String),
				   awful.Column('requirements_script', awful.Text),
				   awful.Column('description', awful.Text),
				   );
				 
class Pokemon(object):
	def __init__(self, name, generation, experience_at_100, catch_rate, base_happiness, gender_ratio, egg_cycle):
		self.name = name
		self.generation = generation
		self.experience_at_100 = experience_at_100
		self.catch_rate = catch_rate
		self.base_happiness = base_happiness
		self.gender_ratio = gender_ratio
		self.egg_cycle = egg_cycle

	def __repr(self):
		return "<Pokemon('%s','%s','%s','%s','%s','%s','%s')>" \
				% (self.name, self.generation, self.experience_at_100, self.catch_rate, self.base_happiness, self.gender_ratio, self.egg_cycle)


class Pokemon_Types(object):
	def __init__(self, name, generation, battle_type):
		self.name = name
		self.generation = generation
		self.battle_type = battle_type

	def __repr(self):
		return "<Pokemon_Types('%s','%s','%s')>" \
				% (self.name, self.generation, self.battle_type)

class Pokemon_Abilities(object):
	def __init__(self, name, generation, ability):
		self.name = name
		self.generation = generation
		self.ability = ability

	def __repr(self):
		return "<Pokemon_Abilities('%s','%s','%s')>" \
				% (self.name, self.generation, self.ability)


class Snaggable(object):
	def __init__(self, name, generation, location, trainer):
		self.name = name
		self.generation = generation
		self.location = location
		self.trainer = trainer

	def __repr(self):
		return "<Snaggable('%s','%s','%s', '%s')>" \
				% (self.name, self.generation, self.location, self.trainer)

class Pokedex(object):
	def __init__(self, name, id, region, generation, species, colour, weight, height, body_size, IQ_group, entry, habitat):
		self.name = name
		self.id = id
		self.region = region
		self.generation = generation
		self.species = species
		self.colour = colour
		self.weight = weight
		self.height = height
		self.body_size = body_size
		self.IQ_group = IQ_group
		self.entry = entry
		self.habitat = habitat

	def __repr(self):
		return "<Pokedex('%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s')>" \
				% (self.name, self.id, self.region, self.generation, self.species, self.colour,
						self.weight, self.height, self.body_size, self.IQ_group,
						self.entry, self.habitat);


class Pokedex_Flavour(object):
	def __init__(self, name, generation, cry, footprint, body_style):
		self.name = name
		self.generation = generatioon
		self.cry = cry
		self.footprint = footprint
		self.body_style = body_style

	def __repr(self):
		return "<Pokedex_Flavour>" \
				% (self.name, self.cry, self.footprint, self.body_style);


class Pokemon_Moves_Level(object):
	def __init__(self, pokemon, generation, move, level):
		self.pokemon = pokemon
		self.generation = generation
		self.move = move
		self.level = level

	def __repr(self):
		return "<Pokemon_Moves_Level('%s','%s','%s','%s')>" \
				% (self.pokemon, self.generation, self.move, self.level);

class Pokemon_Moves_Egg(object):
	def __init__(self, pokemon, generation, move):
		self.pokemon = pokemon
		self.generation = genertaion
		self.move = move

	def __repr(self):
		return "<Pokemon_Moves_Egg('%s','%s','%s')>" \
				% (self.pokemon, self.generation, self.move)


class Pokemon_Moves_Technical(object):
	def __init__(self, pokemon, generation, move):
		self.pokemon = pokemon
		self.generation = generation
		self.move = move

	def __repr(self):
		return "<Pokemon_Moves_Technical('%s','%s','%s')>" \
				% (self.pokemon, self.generation, self.move)


class Pokemon_Moves_Tutor(object):
	def __init__(self, pokemon, generation, move, trainer):
		self.pokemon = pokemon
		self.generation = generation
		self.move = move
		self.trainer = trainer

	def __repr(self):
		return "<Pokemon_Moves_Tutor('%s','%s','%s','%s')>" \
				% (self.pokemon, self.generation, self.move, self.trainer)


class Pokemon_EV_Yield(object):
	def __init__(self, pokemon, generation, stat_name, yeild):
		self.pokemon = pokemon
		self.generation = generation
		self.stat_name = stat_name
		self.yeild = yeild

	def __repr(self):
		return "<Pokemon_EV_Yield('%s','%s','%s','%s')>" \
				% (self.pokemon, self.generation, self.stat_name, self.yeild)


class Pokemon_Evolution(object):
	def __init__(self, generation, from_, to_, requirements, description):
		self.generation = generation
		self.from_ = from_
		self.to_ = to_
		self.requirements = requirements
		self.description = description

	def __repr(self):
		return "<Pokemon_Evolution('%s','%s','%s','%s','%s')>" \
				% (self.generation, self.from_, self.to_, self.requirements, self.description)

def add_engine(engine):
	metadata.create_all(engine)

sa.orm.mapper(Pokemon, Pokemon_table)
sa.orm.mapper(Pokemon_Types, Pokemon_typing_table)
sa.orm.mapper(Pokemon_Abilities, Pokemon_abilites_moves_table_
sa.orm.mapper(Snaggable, Pokemon_snag_table)
sa.orm.mapper(Pokedex, Pokedex_table)
sa.orm.mapper(Pokedex_Flavour, Pokedex_display_table)
sa.orm.mapper(Pokemon_Moves_Level, Pokemon_moves_levelup_table)
sa.orm.mapper(Pokemon_Moves_Egg, Pokemon_moves_egg_table)
sa.orm.mapper(Pokemon_Moves_Technical, Pokemon_moves_technical_table)
sa.orm.mapper(Pokemon_Moves_Tutor, Pokemon_moves_tutor_table)
sa.orm.mapper(Pokemon_EV_Yield, Pokemon_EV_yield_table)
sa.orm.mapper(Pokemon_Evolution, Pokemon_evolve_table)

if __name__ eq '__main__':
	engine = sa.create_engine('sqlite:///:memory:', echo=True);
	add_engine(engine)
