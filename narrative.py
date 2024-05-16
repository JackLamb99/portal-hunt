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

DEAD_END_TEXT = """
The path has come to an abrupt stop, you have reached a dead end, it is eerily
quiet and nothing of importance seems to be nearby.
"""

MOUNTAINS_DESC_TEXT = """
You are at the entrance to the Mountains.

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

BOW_NEW_ITEM_TEXT = """
Deep within the mountains, you stumble upon a secluded alcove, a hidden gem
within the rugged landscape. The walls are encrusted with shimmering crystals,
casting a soft, ethereal glow across the snow-dusted ground.

At the alcove's centre, resting on a crystalline pedestal, is a bow like no
other. Its translucent frame catches the light, able to channel it into energy
that forms radiant arrows.

This is the Crystal Bow, known for its precision against airborne threats. As
you reach for it, you sense that this weapon might hold the key to your final
battle, the path ahead depending on your skill and bravery.
"""

BOW_EXISTING_ITEM_TEXT = """
Deep within the mountains, you stumble upon a secluded alcove, a hidden gem
within the rugged landscape. The walls, once glimmering with crystalline light,
now seem dimmer, barely illuminating the snow-covered ground.

At the alcove's centre stands a solitary pedestal, its crystalline surface now
empty, once a beacon of hope, now leaving only faint echoes of its former
glory.

The Crystal Bow is already in your inventory.
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

DRAGON_DESC_TEXT = """
You approach the Sky Temple, a towering structure carved into the mountainside.
The stone walls are ancient, etched with intricate designs, though they now
bear the marks of weather and time. High above, the clouds swirl in a restless
dance, casting shifting patterns of light and shadow.

From the temple's highest peak, you catch sight of the Ice Dragon, its scales
glistening like shards of glass, reflecting the dappled sunlight. It spreads
its vast, translucent wings, soaring effortlessly through the air, leaving a
trail of frost in its wake. The Ice Dragon's roar echoes through the mountains,
a chilling sound that shakes the temple's stone.

You feel a faint pull of energy from a nearby portal.
"""

DRAGON_DEFEAT_TEXT = """
As you enter Sky Temple, the Ice Dragon descends from above, its massive wings
creating gusts of freezing wind that chill you to the bone. The air grows cold,
frost forming on the stone walls. The dragon's roar echoes through the
mountains, sending a shiver down your spine.

As it draws closer, it exhales a blast of icy breath that freezes everything
in its path. You attempt to take cover behind ancient stone pillars, but the
dragon's powerful tail sweeps through them, shattering the stone and sending
you tumbling to the ground. The icy blast engulfs you, the bitter cold numbing
your senses.

You try to escape, but the ground is slick with ice, and you lose your footing
as your body succumbs to the relentless cold. The last thing you hear is the
rumble of the dragon's triumphant roar, drowning out all other sounds, as the
beast's massive jaws snap shut around you.

You were not equipped to defeat the Ice Dragon.
"""

DRAGON_VICTORY_TEXT = """
As you enter Sky Temple, the Ice Dragon descends from above, its icy breath
freezing the air as it roars. You ready the Crystal Bow, its translucent frame
catching the sun's rays and forming arrows of pure light. You shoot at the
dragon's wings, the energy-infused arrows splintering the glassy scales.

As it weakens and sinks the stone courtyard, you disorient the dragon with an
ear-splitting swing of the Voltcrusher. Seizing the moment, you grasp the
Frostfire and charge, the blue flames flaring with fierce intensity. You dash
toward the Ice Dragon, thrusting the torch into its frosty scales. The intense
heat shatters the ice, causing the dragon to roar in agony.

With a mighty overhead arc from the Voltcrusher, you deliver the final blow,
sending a shockwave through its body. The Ice Dragon collapses, its roar
silenced as its icy breath fades into the cold air. You stand victorious, the
ancient Sky Temple reclaimed from its chilling grip.

You are now free to travel through this area in peace.
"""

DRAGON_CLEARED_TEXT = """
You have already defeated the Ice Dragon.

You return to the Sky Temple entrance, the air feels less hostile without the
Ice Dragon's chilling presence. The ancient stone walls, once etched with
frost, are now free of ice, and the swirling clouds high above seem gentler.

The courtyard where you battled the dragon bears signs of the conflict,
cracked stones and scattered patches of ice litter the ground. Yet, amidst the
ruins, the temple seems to breathe again, its long-buried beauty emerging from
beneath the icy shroud, the echoes of the dragon's reign now silenced.

You feel a faint pull of energy from a nearby portal.
"""

MOUNTAINS_PORTAL_TEXT = """
You reach the heart of the Sky Temple, where towering stone arches frame a
breathtaking view of the open sky. In the centre, a portal shimmers to life,
swirling with iridescent hues that dance like the northern lights.

The wind weaves through the temple's ancient stones, whispering echoes of
forgotten voices and distant footsteps. As you step closer, the portal's
vibrant glow bathes you in its hopeful light, casting a warm aura that beckons
you toward a long-awaited return home.

Congratulations! You found the Mountains Portal and finished your quest.

With different paths to take, items to find and enemies to battle, every
playthrough can be a brand new adventure. Who knows, you may even find a
secret ending...

Thank you for playing Portal Hunt!
"""

CAVES_DESC_TEXT = """
You are at the entrance to the Caves.

A labyrinthine network of twisting tunnels and caverns, The Caves plunge into
the depths of the earth, shrouded in perpetual darkness. Crystalline
formations glimmer faintly, casting eerie reflections on the damp stone walls.
Mysterious glyphs and ancient carvings hint at a forgotten history.

The air is heavy with the scent of earth and dampness, punctuated by the
occasional drip of water echoing through the shadows. In this subterranean
realm, danger lurks around every corner, but so too are the secrets waiting to
be unearthed.
"""

EVERFLAME_NEW_ITEM_TEXT = """
As you round a bend, deep in the caves, you stumble upon a chamber bathed in a
soft, ethereal glow. The air here is warmer, carrying the scent of burning
embers.

In the centre lies an ancient pedestal, upon which rests the Everflame, a
marble torch adorned with swirling runes. Its flame dances with a steady,
undying brilliance, illuminating the darkness with a comforting warmth.

As you clutch its handle, you feel a surge of power coursing through you,
knowing this enchanted flame will light your path and ward off the dangers
lurking in the shadows.
"""

EVERFLAME_EXISTING_ITEM_TEXT = """
As you round a bend, deep in the caves, you stumble upon the chamber where the
Everflame once rested, but you're greeted by a chilling emptiness. The once-
vibrant glow has faded, leaving only darkness in its wake.

The air feels colder now, devoid of the comforting warmth that the enchanted
flame once provided. You can't shake the feeling of foreboding as you realize
the importance of the torch's absence.

As you gaze upon the vacant space, a strange emptiness fills the chamber and
an overwhelming sense of loss washes over you, as if the very essence of the
place is in mourning.

The Everflame is already in your inventory.
"""

SKELETONS_DESC_TEXT = """
As you delve deeper into the tangled caves, the air becomes heavy with the
weight of forgotten ages. You emerge into a vast chamber, its ceiling lost in
darkness above. Crumbling pillars and fractured statues litter the ground,
remnants of an ancient underground civilization now swallowed by time.

Amongst the ruins, you catch sight of movement, a patrol of Skeletal Warriors,
their hollow eye sockets glowing with a malevolent light. Clad in rusted
armour and wielding ancient weapons, they move with an eerie, rattling grace,
driven by an undying loyalty to a long-lost cause.
"""

SKELETONS_DEFEAT_TEXT = """
As the Skeletal Warriors advance, their bony forms clattering with malice, you
brace yourself for the onslaught. With no blessed weapon to aid you, you fight
valiantly, but the undead horde overwhelms you with relentless ferocity.

Their rusted blades bite deep into your flesh, draining your strength with
each merciless strike. As your vision fades and the darkness closes in, the
echoes of your defeat mingle with the haunting rattles of the skeletal
warriors, a grim reminder of your failure in the depths of the tangled caves.

You were not equipped to defeat the Skeletal Warriors.
"""

SKELETONS_VICTORY_TEXT = """
As the Skeletal Warriors advance, their bony forms clattering with malice, you
wield the Everflame in one hand, its radiant glow pushing back the darkness.
With the other, you grasp the Blessed Mace, its divine light pulsating with
righteous fury.

With each swing, the mace blazes with holy energy, shattering the undead with
a force beyond their comprehension. The Everflame's steady brilliance guides
your strikes, casting away shadows and empowering your righteous onslaught
until the last skeletal foe crumbles before you, vanquished by the combined
might of light and divine power.

As the final Skeletal Warrior falls, you raise the Everflame high, its undying
flame illuminating the chamber with a warm, comforting glow. With a solemn
determination, you bring the torch down upon the shattered remains of the
undead, its flames consuming the bones with a cleansing fire.

You are now free to travel through this area in peace.
"""

SKELETONS_CLEARED_TEXT = """
You have already defeated the Skeletal Warriors.

As you traverse back through the once treacherous chamber, a sense of triumph
fills the air, mingling with the heavy weight of forgotten ages that still
lingers. Crumbling pillars and fractured statues now serve as solemn monuments
to your victory.

The shadows retreat before you, no longer harbouring the threat of the
Skeletal Warriors. With each step, you carry the assurance of a newfound peace,
a testament to your bravery in the tangled depths of the caves.
"""
