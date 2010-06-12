/*nimh-libs
 *= C API Battle Stats Structure
 * File : %(P-DA-ZX_Source)path/Scripting_Access/Structures/Battle_Stats.h
 * Author: %(KatrinaTheLamia)user
 * Groups: %(NIMHLabs)group, %(TeamTemporal)group, %(MonsterAcademy)group
 * Projects: %(P-DA-ZX)project, %(Spectrum_Labs_Simulator)project, 
 *           %(TeamTemporal)project
 * Creation: 3176-3-17
 *
 * This file merely deals with the specific stats of Pokemon, Pokehulhu,
 * Fakemon, Trainers and "Targets" in battle.
 *
 * Functions for interacting with these, are elsewhere
 *
 *== Revisions
 * + 3176-3-17 File Creation, yay!
 *== TODO
 * 3176-3-17 ! Complete the file a bit more falling astupid... making sleep 
 *             mistakes.
 */

#ifndef __P-DA-ZX_BATTLE_STATS_H__
#define __P-DA-ZX_BATTLE_STATS_H__
#ifdef __cplusplus
extern "C" {
#endif // End C++ Hostility

#include "libnimh.h"

enum pda_majors {
	none = 0,
	poison,
	paralyzed,
	burn,
	frozen,
	sleep,
	toxic
};

enum pdazx_stackable_status {
	none = 0,
	confuse = 1,
	spin = 2,
	attract = 4,
	curse = 8,
	trapped = 16,
	torment = 32,
	taunt = 64,
	insomnia = 128,
	embargo = 256,
};

typedef struct {
	nimh_object __super;
	nimh_string name;
	signed long long start;
	signed char boosts;
} pdazx_state_boost_data pdazx_stat_boost;

typedef struct {
	nimh_object __super;
	pdazx_major majors;
	pdazx_stackable_status minors;
} pdazx_status_ailment_data pdazx_status_ailment;

typedef struct {
	nimh_object __super;
	nimh_string name;
} pdazx_types_data pdazx_types;

typedef struct {
	nimh_object __super;
	nimh_string pocket;
	pdazx_item item;
} pdazx_inventory_data pdazx_inventory;

typedef struct {
	/* libNIMH Object Tracker */
	nimh_object __super; 
	/* Trainer Ids */
	unsigned long long original_controller, last_controller, controller
	signed long long Health; /* Pokemon Health */
	pdazx_stat_boost *stat_boosts;
	pdazx_status_ailment *ailments;
	pdazx_types types;
	pdazx_item held;
	bool is_held;
} pdazx_monster_data pdazx_monster;

typedef struct {
	pdazx_monster __super;
	unsigned char pokemon_start, pokemon_faint;
	pdazx_monster *monsters;
	pdazx_inventory inventory;
} pdazx_trainer_data pdazx_trainer;


#ifdef __cplusplus
}
#endif // Start C++ Hostility
#endif // __P-DA-ZX_BATTLE_STATS_H__

