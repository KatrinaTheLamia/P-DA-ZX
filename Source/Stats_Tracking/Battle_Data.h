/*nimh-doc
 *= %(PDA-ZX-Includes)path/Script_Tracking/Battle_Stats.h
 * Author : %(KatrinaTheLamia)user
 * Groups : %(NIMHLabs)group, %(TeamTemporal)group, %(MistyOfHoenn)group
 *          %(MOFO-Online)group
 * Licenses: See %(PDA-ZX-Documentation)path/LICENSES.txt
 * Creation : 3176-4-15
 *
 * Battle Stats is a file meant to allow for easy talking to current battle
 * statistics information (defaulting to in memory). Other files will allow
 * different languages to talk to the battle stats.
 *
 *= Revisions
 * + 3176-4-15 Created File
 *
 *= TODO
 * ! 3176-4-15 Finish File
 * ! 3176-4-15 Documenation
 * ! 3176-4-15 Debug
 */

#ifndef __PDA-ZX_Scripting_Battle_Stats_H__
#define __PDA-ZX_Scripting_Battle_Stats_H__

#ifdef __cplusplus /* Allow for C++ to talk to us */
Extern "C" {
#endif /* C++ can now talk to us*/

typedef struct {
  nimh_widget *__super;
  sqlite3 *db;
  nimh_string *storage, *working, *functions;
  nimh_map *functions;  
} pdazx_characters_data pdazx_characters;

/*
 */

/*
 *=== pdazx_characters
 * Type: Constructor
 * Returns: Side Effect function
 * Argument: nimh_book: Our current NIMH Book to talk to
 * Argument: nimh_string: Our variable name
 * Argument: nimh_string: Our grab location
 * Argument: nimh_string: Our working location (defaults to :memory:)
 *
 * Set up a new character data setup
 */
void pdazx_characters(nimh_book*, nimh_string*, nimh_string*,nimh_string*);

/*
 *== pdazx_character_function
 * Type: Forwarder
 * Returns: Side Effect function
 * Argument: nimh_book: Our current NIMH Book to talk wiff
 * Argument: nimh_string: Our character data to talk wiff
 * Argument: nimh_string: Our function to run
 * Throws: Function not found into the error logs
 *
 * Runs SQLite string into the working database as defined by the 
 * map we are running.
 *
 * If we do not have it in memory, we check into our function database to 
 * see if it is there, then store it here.
 */
void pdazx_character_function(nimh_book*,nimh_string*,nimh_string*);

/*
 *== pdazx_character_add_function
 * Type: Adder
 * Returns: Side Effect function
 * Argument: nimh_book: Our current NIMH Book to talk wiff
 * Argument: nimh_string: Our current charater data to talk wiff
 * Argument: nimh_string: Our new function's name
 * Argument: nimh_string: Our new function's contents
 */
void pdazx_character_function_add(nimh_book*,nimh_string*,nimh_string*,nimh_string*);


#ifdef __cplusplus /* clean up our C++ guards */
};
#endif /* C++ guards have been fixed */

#endif /* end of header, __PDA-ZX_Scripting_Battle_Stats_H__ */
