/*nimh-libs
 *= C API Battle Stats Structure
 * File : %(P-DA-ZX_Source)path/Scripting_Access/Structures/Battle_Stats.h
 * Author: %(KatrinaTheLamia)user
 * Groups: %(NIMHLabs)group, %(TeamTemporal)group, %(MonsterAcademy)group
 * Projects: %(P-DA-ZX)project, %(Spectrum_Labs_Simulator)project, 
 *           %(TeamTemporal)project
 * Creation: 3176-3-17
 *
 * This file merely deals with the specific stats of Pokemon,
 * Fakemon, Trainers and "Targets" in battle.
 *
 * Functions for interacting with these, are elsewhere
 *
 * Noting that this will be expanded, to allow for other systems to be used
 * in this simulation.
 *
 * Other systems I would love to allow:
 * * Persona
 * * Digimon Tamers
 * * Digimon World (several varients)
 * * Mother
 * * Megaman Net Battler and Megaman StarForce (unlikely)
 * * Pokethulhu
 * * Final Fantasy (and varients)
 *
 *== Revisions
 * + 3176-3-17 File Creation, yay!
 * ~ 3176-3-24 Ironing out some of my retarded mistakes.
 * ! 3176-3-24 Cannot FIND what I was calling most of my retarded mistakes.
 * ~ 3176-3-24 Did however, fix a few pointer arthimetic issues though
 * + 3176-3-24 Function Prototypes are now present here
 *== TODO
 * 3176-3-17 D Complete the file a bit more falling astupid... making sleep 
 *             mistakes.
 * 3176-3-17 ! Properly comment data structures and function prototypes.
 */

#ifndef __P-DA-ZX_BATTLE_STATS_H__
#define __P-DA-ZX_BATTLE_STATS_H__
#ifdef __cplusplus
extern "C" {
#endif // End C++ Hostility

#include "libnimh.h"
#include "pda-zx.h"

/*
 * Right--it may be easier just to point to status based functions.
 */
typedef (void)(pdazx_status_function*)(nimh_object*);

/*
 * You know--I may just need to create a simple hash type for use in
 * libNIMH... to keep this from appearing over and over again in my 
 * code.
 *
 * Just a note for the future.
 */
typedef struct {
	nimh_object *__super;
	nimh_string *name;
	pdazx_status_function stacked_status;
} pdazx_stackables_data pdazx_stackables;

/*
 * And, an array of various stat boosts.
 *
 * This is mostly to include what the stat started at, and how much it has 
 * been boosted thus far.
 *
 * This has the double effect of being able to track stats.
 */
typedef struct {
	nimh_object *__super;
	nimh_string *name;
	signed long long start, modifications;
} pdazx_stat_boost_data pdazx_stat_boost;

/*
 * Right--for now, we are just using this to hold what our current type has
 * for a name. Such as Fighting, Dark, etc.
 *
 * Anything that deals with type effectiveness probably has a better place 
 * somewhere else. These structures are mostly for tracking what is currently
 * going on for the Pokemon and Trainer's state.
 */
typedef struct {
	nimh_object *__super;
	nimh_string *name;
} pdazx_type_data pdazx_type;

/*
 * And, an inventory type. Incase we have enabled that in our training scenario.
 *
 * This will allowed simulations of places like the Battle Frontier.
 */
typedef struct {
	nimh_object *__super;
	nimh_string *pocket;
	pdazx_item *item;
	unsigned long long quantity;
} pdazx_inventory_data pdazx_inventory;

/*
 * Next, we have the current information of the Pokemon being considered.
 *
 * Since there may be an option in the future, to change who controls a certain
 * mon--that is, by adding Snagging into the simulation, these trainers may
 * be required here.
 */
typedef struct {
	nimh_object *__super; 
	unsigned long long original_controller, last_controller, controller;
	unsigned long long my_id;
	nimh_string *name;
	pdazx_species *my_species;
	pdazx_stat_boost *stat_boosts;
	pdazx_status_function *unstackable_status;
	pdazx_stackables *stacking_status;
	pdazx_types *type;
	pdazx_item *held;
	bool is_held;
} pdazx_monster_data pdazx_monster;

/*
 * Figured we would have the trainer also having stats kept track of. Mostly
 * to allow the option to be added into the simulator, of being able to 
 * attack the trainer, rather than the mon.
 */
typedef struct {
	pdazx_monster *__super;
	unsigned char _pokemon_start, _pokemon_faint;
	pdazx_monster *monsters;
	pdazx_inventory *inventory;
} pdazx_trainer_data pdazx_trainer;

/*
 * Create a new trainer
 *
 * Return the trainer's id.
 */
unsigned long long* create_trainer(nimh_book*,nimh_string*);

/*
 * Load from storage a trainer by name
 */
nimh_book* load_trainer(nimh_book*,nimh_string*);

/*
 * Load from storage a trainer by trainer id
 */
nimh_book* load_trainer(nimh_book*,unsigned long long);

/* Change a monster or trainer's name.
 *
 * Changed this to only being done by their id.
 */
nimh_book* change_trainer_name(nimh_book*, unsigned long long, nimh_string*);

/* 
 * Add and remove from inventory
 */
nimh_book* add_to_inventory(nimh_book*, unsigned long long, pdazx_item*);
nimh_book* remove_from_inventory(nimh_book*, unsigned long long, pdazx_item*);

/*
 * Stat mod
 *
 * Yes, changing HP is an alias to this
 *
 * Trainer id, status name, modification amount
 */
nimh_book* status_mod(nimh_book*,unsigned long long, nimh_string*, unsigned long long);

/*
 * Change who is controlling a monster.
 *
 * Also works on trainers, BTW
 *
 * Id of target, id of new controller
 */

nimh_book* change_controller(nimh_book*, unsigned long long, unsigned long long);

nimh_book* change_specieis(nimh_book*, unsigned long long, pdazx_species*);

nimh_book* add_nonstack_status(nimh_book*, unsigned long long, pdazx_status_function);
nimh_book* remove_nonstack_status(nimh_book*, unsigned long long, pdazx_status_function);

nimh_book* stack_status(nimh_book*, unsigned long long, pdazx_status_function);
nimh_book* remove_status_from_stack(nimh_book*, unsigned long long, pdazx_status_function);

nimh_book* add_type(nimh_book*, unsigned long long, pdazx_type*);
nimh_book* remove_type(nimh_book*, unsigned long long, pdazx_type*);

nimh_book* no_hold_item(nimh_book*, unsigned long long);
nimh_book* yes_hold_item(nimh_book*, unsigned long long);

#ifdef __cplusplus
}
#endif // Start C++ Hostility
#endif // __P-DA-ZX_BATTLE_STATS_H__

