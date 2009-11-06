
/* Blah */

/* P*DA Specific Libraries */

#include <PDA/Flow/widget>
#include <PDA/types>

namespace RaddTeam {
	namespace PDA {
		class Stat : Widget {
			protected:
				/* What is this stat called? */
				RaddTeam::UString name;
				RaddTeam::Number maximum;
				RaddTeam::Number current;
				RaddTeam::IV IV;
				RaddTeam::EVs EVs;
		};
	};
};

