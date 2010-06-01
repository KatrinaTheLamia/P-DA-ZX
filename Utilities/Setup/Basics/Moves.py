#!/bin/env python
"""
	#= Moves Database creation script
	Author: [[KatrinaTheLamia_(user)]]
	Groups: [[NIMHLabs_(group)]], [[MonsterAcademy_(group)]], [[TeamTemporal_(group)]]
	Project: [[P*DA_ZX_(Project)]]
	Creation date: 3176-3-6

	'''Moves.py''' is intended to be the database generation file, for 
	anything that Exists as a move like status. Anything that has to do around 
	the move, from its in battle effect, to what it does on the over world, to 
	what it does in a contest should probably go here.

	#== Revisions
		+ 3176-3-6 added cache ids to the tables
		~ 3176-3-6 Properly commented this source code
		+ 3176-3-6 over world moves have there own table now
		~ 3176-3-6 slimmed down battle moves. Overworld scripts are 
			rare enough to go elsewhere
		~ 3176-3-5 made comments look more pythonic
"""

import sqlalchemy as sa

metadata = sa.MetaData()

"""
	#== Tables
	These contain the defintions, via SQL Alchemy that we are to look at
	here.
"""

battle_move_table = sa.Table('battle_moves', metadata,
		"""
			#=== Battle Moves
			id: cache usage
			name: the common name of the move.
			generation: an id for which generation this row 
			    applies to
			description: generic plain english description
			category: special(1), physical(2) or status(3)?
			target: self(0), single(1), my_team(2), their_team(3), 
			    others(4), all(5)
			priority: a priority range from -7 to +7, typically.
			battle type: a string to denote fire/water/elec/etx
			basic_attack: how does this move rate for unadjusted 
			    attack power?
			accuracy: how accurate is this move?
			max_pp: prior to PP Ups, when this move is full, how
			    many power points does this move have?
			attack_script: a simple lua script on what this attack
			    should do.

			this table is for moves that get used in battle.

		"""
			     sa.Column('id', sa.Integer, primary_key=True),
                             sa.Column('name',sa.String),
                             sa.Column('generation',sa.String),
                             sa.Column('description',sa.Text), 
                             sa.Column('category',sa.Integer), 
                             sa.Column('target',sa.Integer), 
                             sa.Column('prioriy', sa.Integer), 
                             sa.Column('battle_type',sa.String), 
                             sa.Column('basic_attack',sa.Integer), 
                             sa.Column('accuracy',sa.Integer), 
                             sa.Column('max_pp',sa.Integer), 
			     sa.Column('attack_script',sa.Text),
                             );

overworld_move_table = sa.Table('overworld_moves', metadata,
		"""
			#===Over World Moves
			id: cache usage
			name: move's typical name
			generation: generation id
			description: english description of overworld effect
			overworld_script: a lua script on what this attack should do
			power: for use with Pokemon Ranger entries only

			Table specifically for moves in use in the overworld.

			To slim down the battle moves table.
		"""
				sa.Column('id', sa.Integer, primary_key=True),
				sa.Column('name', sa.String),
				sa.Column('generation', sa.String),
				sa.Column('description', sa.String),
				sa.Column('overworld_script', sa.Text),
				sa.Column('power', sa.Integer),
				);

contest_move_table = sa.Table('contest_moves', metadata,
		"""
			#=== Contest Moves Table
			id: cache purposes
			name: common name
			generation: generation id string
			description: english description
			contest_type: string to say what contest type it is
			appeal: an appeal number
			jamming: a jamming number
			appeal_script: if it does anything special
			jamming_script: again if it does anything noteworthy.

		"""
			      sa.Column('id',sa.Integer, primary_key=True), 
                              sa.Column('name',sa.String), 
                              sa.Column('generation',sa.String), 
                              sa.Column('description',sa.Text), 
                              sa.Column('contest_type',sa.String), 
                              sa.Column('appeal',sa.Integer), 
                              sa.Column('jamming',sa.Integer), 
                              sa.Column('appeal_script',sa.Text), 
                              sa.column('jamming_script',sa.Text), 
                              );

technical_table = sa.Table('technical_moves', metadata,
		"""
			#=== Technical Move (TM)
			id: cache purposes
			number: what TM numbe
			generation: string for the generation
			move_name: common name for the move.

			Just a table for technical moves
		"""

		     sa.Column('id', sa.Integer, primary_key=True),
		     sa.Column('number', sa.Integer),
		     sa.Column('generation', sa.String),
		     sa.Column('move_name', sa.String),
		     );

hidden_table = sa.Table('hidden_moves', metadata,
		"""
			#=== Hidden Move (HM)
			id: cache purposes
			number: what HM number
			generation: the generation to be found in
			nmove_name: common name for the move
		"""
			sa.Column('id', sa.Integer, primary_key=True),
			sa.Column('number', sa.Integer),
			sa.Column('generation', sa.String),
			sa.Column('move_name', sa.String),
			);


special_learn_moves_table = sa.Table('special_learn_moves', metadata,
		"""
			#=== Special Learn moves
			id: cache purposes
			generation: string for the generation
			method: egg, event:name, trainer:id, etc.
			move_name: common name for the move
		"""
			sa.Column('id', sa.Integer, primary_key=True),
			sa.Column('generation', sa.String),
			sa.Column('method', sa.String),
			sa.Column('move_name', sa.String),
			);


"""
	#== Classes
	Not much here, just the classes to work with SQL Alchemy.
"""
class Battle_Move(object):
    def __init__(self, name, generation, description, category, target, priority, 
                 battle_type, basic_attack, accuracy, max_pp, attack_script, 
                 overworld_script):
        self.name = name
        self.generation = generation
        self.description = description
        self.category = category
        self.target = target
        self.priority = priority
        self.battle_type
        self.basic_attack = basic attack
        self.accuracy = accuracy
        self.max_pp = max_pp
        self.attack_script = attack_script
        self.overworld_script = overworld_script

    def __repr__(self):
        return "<Battle_Move('%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s')>" % \
            (self.name, self.generation, self.category, self.target, self.priority, self.battle_type, \
             self.basic_attack, self.accuracy, self.max_pp, self.attack_script, self.over_world_script)

class Contest_Move(object):
    def __init__(self, name, generation, description, contest_type, appeal, jamming, appeal_script, jamming_script):
        self.name = name
        self.generation = generation
        self.description = description
        self.contest_type = contest_type
        self.appeal = appeal
        self.jamming = jamming
        self.appeal_script = appeal_script
        self.jamming_script = jamming_script

    def __repr__(self):
        return "<Contest_Move('%s','%s','%s','%s','%s','%s','%s','%s')>" % \
            (self.name, self.generation, self.description, self.contest_type, self.appeal, self.jamming,
             self.appeal_script, self.jamming_script)

	    
class Technical_Move(object):
	def __init__(self, number, generation, name):
		self.number = number
		self.generation = generation
		self.name = name

	def __repr__(self):
		return "<Technical_Move('%s','%s','%s')>" % \
				(self.number, self.generation, self.name)

class Hidden_Move(Technical_Move):
	def __repr__(self):
		return "<Hidden_Move('%s','%s','%s')>" % \
				(self.number, self.generation, self.name)

class Special_Learned_Move(object):
	def __init__(self, generation, method, name):
		self.generation = generation
		self.method = method
		self.name = name

	def __repr__(self):
		return "<Special_Learned_Move('%s','%s','%s')" \
				% (self.generation, self.method, self.name)

def add_engine(engine):
    metadata.create_all(engine)

sa.orm.mapper(Battle_Move, battle_move_table)
sa.orm.mapper(Contest_Move, contest_move_table)
sa.orm.mapper(Technical_Move, technical_table)
sa.orm.mapper(Hidden_Move, hidden_table)
sa.orm.mapper(Specail_Learned_Move, special_learn_moves_table)

if __name__ eq '__main__':
    engine = sa.create_engine('sql:///:memory:',echo=True);
    add_engine(engine);
