"""
Narrative Content for Portal Hunt

This module contains all the text and narrative elements used in the story of
the game.

Includes; descriptions of locations, items and enemies, and narrative
sequences that guide the player's interaction.
"""

MENU_TEXT = """
Welcome adventurer, to Portal Hunt, a text-based adventure game where every
decision shapes your destiny.

Your quest is simple: find a portal that will guide you home.

The journey will be perilous, with unseen dangers lurking around any corner,
but fear not, the key to your success lies in the ancient artefacts you will
discover along the way.

Your journey begins now. Prepare to face the unknown, and may you find the
portal that will lead you home. Good luck, adventurer. The world is yours to
explore.
"""

GLADE_TEXT = """
You find yourself in The Glade.

Golden sunlight filters through a canopy of towering trees. The ground is a
lush carpet of moss, dotted with colourful wildflowers. A gentle breeze stirs
the leaves, mingling with the distant birdsong.

An ancient oak stands at the centre, with a message carved into the bark that
reads:

"A warning for the brave of heart,\

With wisdom only a few impart, \

Journey through these lands of old, \

Through caves deep and mountains cold, \

Where ancient dangers freely roam, \

You must seek the portals for passage home."
"""

TAKE_ITEM_TEXT = """
You choose to take this item, it is now in your inventory.
"""

LEAVE_ITEM_TEXT = """
You choose to leave this item, it remains in place.
"""

RETURN_ITEM_TEXT = """
You choose to return the item, it is no longer in your inventory.
"""

KEEP_ITEM_TEXT = """
You choose to keep the item, it remains in your inventory.
"""

CROSSROAD_TEXT = """
You find yourself at an empty crossroad, it is eerily quiet and nothing of
importance seems to be nearby.
"""

FLEE_TEXT = """
You choose to flee from this enemy.
"""

MOUNTAINS_DESC_TEXT = """
You are at the entrance to The Mountains.

A breathtaking landscape of towering, snow-capped peaks that rise dramatically
into the sky. Jagged ridges and sheer cliffs dominate the terrain, with narrow,
winding paths carved into the rock, leading through constricted gorges and
over precipitous drops.

The air is crisp and thin, filled with the echo of distant avalanches and the
whisper of the wind. Amidst the rugged terrain, hardy wildlife and scattered
pine trees find a way to thrive, the landscape is both breathtakingly
beautiful and perilously unforgiving.
"""

FROSTFIRE_NEW_ITEM_TEXT = """
You push through a dense pine grove and a narrow cave entrance catches your
eye. The walls inside are slick with ice, reflecting a ghostly blue light from
within.

At the cave's end, a pedestal stands, encrusted with frost. Ancient runes are
etched into the stone, glowing with an eerie luminescence, and whispers of
forgotten rituals fill the air.

Atop it rests the Frostfire, a glass torch, its flame a vibrant blue that
dances with a fierce intensity. You can feel its warmth even from a distance,
beckoning you to take it.
"""

FROSTFIRE_EXISTING_ITEM_TEXT = """
You push through a dense pine forest and a narrow cave entrance catches your
eye. The walls inside are slick with ice, reflecting a ghostly blue light from
within.

At the cave's end, a pedestal stands, encrusted with frost, now empty. The
surrounding runes have faded, the eerie glow that once illuminated the cave
has dimmed, and the whispers are now silent.

The Frostfire is already in your inventory.
"""

VOLTCRUSHER_NEW_ITEM_TEXT = """
Scaling a steep ridge, you come across a hidden plateau. At its centre, an
ancient stone slab is etched with lightning-bolt patterns.

The air here is charged with electricity, and you can feel the hair on your
arms standing on end. Resting on the slab is a massive axe, its metal head
crackling with arcs of blue electricity.

This is the Voltcrusher, an awe-inspiring weapon rumoured to generate powerful
shockwaves with each strike. As you grasp its handle, a surge of energy pulses
through you, hinting at the raw power it holds.
"""

VOLTCRUSHER_EXISTING_ITEM_TEXT = """
Scaling a steep ridge, you reach a hidden plateau, where the air feels
unnaturally still. At its centre lies an ancient stone slab with faint
lightning-bolt patterns, now fading into cold rock.

Only a scorch mark remains where the mighty hammer once rested, hinting at the
power that once thrived here. The silence is heavy, broken only by a distant
rumble of thunder.

This place, once charged with energy, now feels like a fading memory, slowly
dissolving back into the mountains.

The Voltcrusher is already in your inventory.
"""

GOBLINS_DESC_TEXT = """
You enter a dense thicket of snow-laden pines. The branches hang low, heavy
with frost, forming a canopy that dims the sunlight. Among the trees, you
notice small footprints leading off the main path, a hint of something lurking
nearby.

You spot a gang of Snow Goblins, small and sneaky creatures draped in ragged
furs, clutching crude weapons made of bone and ice. Their pale blue skin
merges with the snowy landscape, and their sharp, glinting teeth reveal the
malice with which they skulk through the shadows, waiting to strike.
"""

GOBLINS_DEFEAT_TEXT = """
You forge ahead, but the Snow Goblins close in quickly, emerging from the
dense thicket of snow-laden pines. They are small and quick, darting through
the snow around you with a sinister agility.

You swing your arms wildly in an attempt to fend them off, but they evade with
practiced ease, closing the gap with terrifying speed.

A heavy blow from a bone club sends you to the ground, the cold snow stinging
as you fall. The goblins swarm around you, their ragged furs the last thing
you see as everything fades to darkness.

You were not equipped to defeat the Snow Goblins.
"""

GOBLINS_VICTORY_TEXT = """
You grasp the Frostfire, its blue flame casting an intense light through the
dense thicket, and charge at the Snow Goblins. They recoil at the heat, their
icy camouflage failing against the fierce glow.

As they try to surround you, you swing the torch in sweeping arcs, leaving
trails of searing heat. The goblins shriek as the fire burns through their
ragged furs and icy weapons.

With each swing, you drive them back, their snowy lair melting into slush. The
goblins flee, their ambush thwarted by the intense power of the Frostfire.

You are now free to travel through this area in peace.
"""

GOBLINS_CLEARED_TEXT = """
You have already defeated these Snow Goblins.

You calmly stride back through the dense thicket of snow-laden pines, the once-
menacing atmosphere feels noticeably lighter. The low-hanging branches, still
heavy with frost, part easily around you.

The ground is strewn with the remnants of the Snow Goblins' ambush, charred
remains of their crude weapons and tattered furs slowly melting into the snow.
The thicket, no longer haunted by their presence, seems quieter, as if nature
itself is sighing with relief. The path is clear, the threat gone, allowing
you to move forward with a sense of accomplishment.
"""

TIGER_DESC_TEXT = """
You come across a wide, open expanse nestled between snow-covered ridges. The
windswept terrain is dotted with sparse clusters of pine trees, the ground a
mix of snow and rocky terrain. Amidst this icy landscape, a trail of paw
prints as large as your hand a sign that something dangerous is near.

You glimpse the Sabre-toothed Tiger lying in wait, its massive frame covered
in tawny and white fur, blending almost seamlessly with the snow. Its golden
eyes gleam as they scan the area, and its long fangs curve menacingly from its
powerful jaw. With a single leap, this massive predator can close the distance,
as agile as it is deadly.
"""

TIGER_DEFEAT_TEXT = """
The Sabre-toothed Tiger leaps from its concealed spot, its massive frame a blur
of tawny and white fur. You barely have time to react before it's upon you, its
powerful paws knocking you to the ground.

The force of the impact leaves you dazed and you struggle to rise as the tiger'
s weight pins you to the icy earth. You fight to free yourself, but it's no
use, as the tiger's curved fangs sink deep into your shoulder.

The last thing you hear is the beast's growl as it vibrates through the air, a
menacing rumble that sends shivers down your spine as the frosty world around
you fades to black.

You were not equipped to defeat the Sabre-toothed Tiger.
"""

TIGER_VICTORY_TEXT = """
As you approach, the Sabre-toothed Tiger leaps from its hiding spot, its
powerful muscles propelling it toward you with terrifying speed. You brandish
the Frostfire, the blue flames illuminating the snowy expanse.

The tiger hesitates, its golden eyes narrowing as it senses the intense heat.
You seize the moment and swing the Voltcrusher into the ground, releasing a
shockwave that sends the tiger staggering. With the tiger disoriented, you
throw the axe with all your strength, delivering a devastating, fatal blow.

The Sabre-toothed Tiger collapses, its final growl fading into the icy wind,
the snowy landscape falling silent as you stand victorious, weapons in hand.

You are now free to travel through this area in peace.
"""

TIGER_CLEARED_TEXT = """
You have already defeated the Sabre-toothed Tiger.

You return to the wide expanse nestled between snow-covered ridges, the
windswept terrain feels almost serene. The clusters of pine trees sway gently
with the breeze, and the once-threatening presence of the Sabre-toothed Tiger
is no more.

The ground, a mix of snow and rocky terrain, bears faint traces of your
earlier battle and the beast's remains are now covered with a thin sheet of
snow. You can traverse the area without fear, knowing the land has been
reclaimed from its deadly predator, now only the distant echoes of nature's
quiet rhythms fill the air.
"""
