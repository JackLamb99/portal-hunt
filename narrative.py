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

An ancient oak stands at the centre, its trunk knotted and twisted to resemble
a face, with deep-set eyes and a wise, weathered expression. As you approach,
the tree springs to life, its wide eyes locking onto you, branches rustling
softly as it speaks:

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

MACE_NEW_ITEM_TEXT = """
You press through a labyrinth of narrow, winding passages, the damp stone
walls closing in around you. Suddenly, a faint glimmer catches your eye,
leading you to a hidden alcove. The air grows heavy with the scent of damp
earth, and tangled vines ensnare the ground in a chaotic web.

At the heart of the alcove, a towering pedestal stands adorned with ancient
carvings, aglow with a celestial luminescence. Mysterious whispers dance
through the chamber, hinting at the secrets veiled within.

Resting upon the pedestal lies the Blessed Mace, its surface shimmering with a
divine radiance that seems to banish the encroaching shadows. As you reach out
to claim it, you feel a surge of holy power coursing through you, filling you
with the strength to smite the undead lurking within these twisting tunnels.
"""

MACE_EXISTING_ITEM_TEXT = """
You press through a labyrinth of narrow, winding passages, the damp stone
walls closing in around you. Suddenly, a faint glimmer catches your eye,
leading you to a hidden alcove. The air hangs heavy with a sense of desolation,
and the tangled vines that ensnare the ground now seem lifeless as they wither
beneath your boots.

The towering pedestal at the heart of the chamber now stands empty, its
ancient carvings now mere shadows of their former brilliance. This place, once
radiating with hope and life, now seems devoid of energy as the shadows creep
ever closer.

The Blessed Mace is already in your inventory.
"""

COIL_NEW_ITEM_TEXT = """
As you press onward through the labyrinthine of passages, your footsteps echo
against the rugged walls, revealing a passage littered with rusted tools and
shattered stone. Gradually, the passage narrows, forcing you to crawl through
with a determines resolve.

Within the suffocating darkness, an alcove emerges, its entrance shrouded in
twisting vines and sinuous roots that writhe like a nest of serpents. As you
cautiously approach, the verdant foliage seems to shift and sway of its own
accord, creating an eerie atmosphere of primal vitality.

Nestled at the heart of this organic enclave lies the Serpent's Coil, a weapon
resembling a set of bolas, yet its design is far from ordinary. Imbued with
arcane energy, this weapon is capable of hurtling through the air with
supernatural speed and ensnaring the largest of foes with an unyielding grip.
"""

COIL_EXISTING_ITEM_TEXT = """
As you press onward through the labyrinthine passages, your footsteps seem to
fall hollow against the desolate walls, echoing with a sense of abandonment.
The once lively passage appears barren and unresponsive.

Within the oppressive darkness, the alcove stands motionless, the twisted
vines and sinuous roots now wilted and lifeless. The atmosphere, once
pulsating with a primal energy, now hangs heavy with a sense of desolation and
decay.

What was once the heart of this organic enclave, where the Serpent's Coil
resided, is now a void that seems to consume the very essence of any spirit
that remains, leaving behind a hollow shell of what once was.

The Serpent's Coil is already in your inventory.
"""

SPIDER_DESC_TEXT = """
As you venture deeper into the winding tunnels, the air grows thick with the
scent of rot and decay. Shadows dance along the jagged walls, concealing
unseen dangers. Your footsteps echo softly as you navigate the passages, until
suddenly, you stumble upon a collapsed section of an abandoned mine.

Thick strands of sticky webbing stretch across the rubble, a warning sign of a
Giant Spider's lair. You spot it lurking in the shadows, its massive hairy
legs spanning the width of the tunnel, while its bulbous body, marked with
jagged patterns, looms ominously. Its dozen gleaming eyes fixate on you with a
predatory hunger, waiting for you to blunder into its trap.
"""

SPIDER_DEFEAT_TEXT = """
As the Giant Spider emerges from the shadows, its massive hairy legs
skittering across the tunnel floor. In the mere seconds you take to plan your
attack, the spider closes in, its gleaming eyes fixated on you with predatory
intent.

With lightning speed, the spider lashes out, its fangs dripping with venom as
it sinks them into your flesh. Agony courses through your body as the venom
takes hold, paralysing your limbs and clouding your thoughts. You struggle
desperately, but the spider's strength is overwhelming, its massive bulk
pinning you down as it delivers a final, fatal blow.

You were not equipped to defeat the Giant Spider.
"""

SPIDER_VICTORY_TEXT = """
You brandish the Everflame, its enchanted fire casting a defiant glow in the
murky depths of the mine, and charge at the Giant Spider. As it recoils from
the intense heat, you thrust the torch forward, the flames igniting the
spider's thick webbing in a blaze of fury.

With swift jabs and sweeping arcs, you drive the arachnid back, relentless in
your assault. Enraged, it thrashes wildly, but the fire burns with unwavering
resolve, relentlessly searing through its hairy exoskeleton.

With every strike, the spider's movements grow weaker, its monstrous form
faltering under the unyielding brilliance of the Everflame. As the flames
consume it entirely, the creature collapses in defeat, its once-menacing
presence extinguished at last.

You are now free to travel through this area in peace.
"""

SPIDER_CLEARED_TEXT = """
You have already defeated this Giant Spider.

You backtrack through the winding tunnels, the oppressive scent of rot and
decay still lingers in the air, though now tinged with a faint hint of victory.
Shadows still dance along the jagged walls, but the once-concealed dangers
seem diminished, their threat moderated by your triumph.

The Giant Spider's charred body lays motionless in its once-menacing domain.
Your footsteps echo softly as you navigate the passages, the memory of your
battle with the Giant Spider now a testament to your resilience.
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

TROLL_DESC_TEXT = """
You arrive at an overgrown cavern, the largest you've seen in the caves so far,
where thick roots intertwine with towering stalactites and stalagmites.
Bioluminescent fungi cast an eerie glow on the cavern's ceiling, illuminating
the vast chasm below. The air is heavy with the scent of earth and dampness,
while distant echoes hint at hidden streams and potential dangers moving
through the darkness.

Lurking in the darkness you see the towering Cave Troll, its skin rough and
mottled like stone. Massive and lumbering, it can crush anything in its path
with brutal force. Thick tusks protrude from its lower jaw, and its small,
glinting eyes betray a violent temper. The ground trembles with each heavy
step as it roams through the cavern.

You feel a faint pull of energy from a nearby portal.
"""

TROLL_DEFEAT_TEXT = """
As the Cave Troll's menacing form fills the cavern, you steel yourself for the
battle ahead. Despite your efforts, the troll's brute strength overwhelms you,
each thunderous blow driving you further back. The Everflame's radiant glow
dims in the face of the creature's ferocity, casting long shadows that seem to
mock your futile struggle.

With a deafening roar, the troll pins you to the ground, its massive tusks
bared in triumph. Darkness encroaches as your vision fades, the echoes of your
defeat mingling with the troll's victorious roars, a sombre reminder of your
failure in the depths of the overgrown cavern.

You were not equipped to defeat the Cave Troll.
"""

TROLL_VICTORY_TEXT = """
As the Cave Troll looms in the dim cavern, you ready yourself for the imminent
clash. With a swift and calculated throw, you hurl the Everflame into a
distant corner, its radiant glow drawing the troll's attention, casting
shadows dancing across the walls. The troll's small, glinting eyes fixate on
the flickering flame, momentarily distracted from its impending doom.

Seizing the moment, you unleash the Serpent's Coil, its arcane energy
entwining around the troll's massive legs and sending it crashing to the
ground. The cavern trembles with the force of its fall, dust and debris
swirling in the air as the troll roars in fury and frustration, its thick
tusks gnashing against the rocky floor.

With a thunderous roar, the beast struggles against its bindings, but you
close in, brandishing the Blessed Mace. With a resounding strike, empowered by
divine light, you deliver the fatal blow, vanquishing the monstrous foe and
securing your final and lasting victory over The Caves.

You are now free to travel through this area in peace.
"""

TROLL_CLEARED_TEXT = """
You have already defeated the Cave Troll.

As you traverse the overgrown cavern once more, a sense of relief washes over
you, replacing the tension of the past battle with a serene calmness. The
thick roots intertwine with the stalactites and stalagmites, creating an
intricate tapestry that speaks of the resilience of nature. Bioluminescent
fungi still cast their eerie glow, but now it feels like a gentle embrace
rather than a foreboding omen.

The scent of earth and dampness remains, but now it carries a hint of victory,
a testament to your triumph over the dangers that once lurked in the darkness.
With each step, you carry the memory of your hard-fought battle, a reminder of
the strength and courage that led you through the depths of The Caves.

You feel a faint pull of energy from a nearby portal.
"""

CAVES_PORTAL_TEXT = """
After the collapse of the troll, an opening crumbled in the cavern wall,
revealing a hidden passage among the twisted roots that leads to a stone
archway. As you approach, you notice intricate carvings etched into its
surface, hinting at a forgotten history.

The portal shimmers with an ethereal blue light, casting soft, rippling waves
across the walls. You step towards it, feeling the pull of the portal's energy,
signalling the way home. With a final glance back at the conquered cavern, you
step through the portal, leaving behind the echoes of your victory to embark
on the next leg of your journey.

Congratulations! You found the Caves Portal and finished your quest.

With different paths to take, items to find and enemies to battle, every
playthrough can be a brand new adventure. Who knows, you may even find a
secret ending...
"""

SCORCHLANDS_DESC_TEXT = """
You are at the entrance to the Scorchlands.

The fiery realm stretches out before you, heat radiates from the scorched
ground beneath your feet, and the air shimmers with waves of intense warmth.
Wisps of smoke drift lazily from the smouldering remnants of what were once
vibrant forests, now reduced to blackened skeletons, their twisted branches
reaching towards the ashen sky. Despite the devastation, resilient plants push
through the charred earth, offering glimpses of life amidst the desolation.

Fumaroles belch sulphurous clouds into the air, casting an acrid odour over
the landscape. In the distance, the silhouette of a volcano looms ominously,
serving as a constant reminder of the unpredictable nature of this harsh
dominion, where beauty and danger coexist in a delicate balance.
"""

SABRE_NEW_ITEM_TEXT = """
As you venture further into a distant corner of this fiery domain, you stumble
into a secluded ravine, where the remnants of a once-mighty glacier cling
stubbornly to existence. The air grows noticeably colder as you approach, and
the ground is littered with shards of ice.

Amidst the frozen landscape, you spot a cavern half-buried beneath a mound of
snow and ice. As you cautiously step into the cavern, you're enveloped by an
ethereal glow, casting long shadows that dance along the icy walls.
Stalactites hang like crystalline daggers from the ceiling, dripping slowly
with melted frost.

Amidst this frozen sanctuary, upon a pedestal of ice illuminated by a pale
blue light, lies the Frostbite Sabre, its presence a stark contrast to the
surrounding stillness. Its blade glistens with an otherworldly shimmer,
emanating a chilling aura that freezes the very air around it.
"""

SABRE_EXISTING_ITEM_TEXT = """
As you venture once more into a distant corner of this fiery domain, the
ravine seems barren, devoid of the once-potent aura that gripped it. The
remnants of the glacier appear diminished, their icy forms melting slowly
under the relentless heat. The air, once crisp and cold, now feels heavy with
a sense of melancholy.

The cavern, now empty, echoes with a dull hollowness, its walls stripped of
the ethereal glow that once bathed them. With the absence of the Frostbite
Sabre, the sanctuary feels desolate, its former majesty faded into a sombre
shadow of what it once was.

The Frostbite Sabre is already in your inventory.
"""

STAFF_NEW_ITEM_TEXT = """
You stumble upon an unexpected oasis nestled amidst the desolation. Here, a
small, shimmering pool reflects the sunlight that beams through a gap in the
smoky clouds, offering a respite from the oppressive heat.

The oasis exudes an aura of rejuvenation, its life-giving waters seeming to
reclaim the surrounding area from the grasp of the relentless flames. The
vibrant greenery, lush and defiant, sprawls outwards, pushing back against the
encroaching desolation with fervent determination.

At the water's edge stands a weathered stone altar, upon which rests the Water
Staff, its ancient runes glowing softly with the essence of rivers and seas.
The air hums with a soothing tranquillity, beckoning you to claim this relic
of elemental power.
"""

STAFF_EXISTING_ITEM_TEXT = """
You return to the once-vibrant oasis, now a shadow of its former self. The
shimmering pool, once a beacon of life, reflects only the dim glow of dying
embers floating in the air.

The surrounding greenery, once defiant and lush, now withers and curls,
succumbing to the relentless onslaught of the scorching heat. Charred remnants
litter the oasis, a sombre reminder of the power that once thrived here.

The weathered stone altar stands barren, stripped of the Water Staff that once
held sway over this part of the desolate realm. The air hangs heavy with a
palpable sense of loss, a melancholic silence enveloping the forsaken
sanctuary.

The Water Staff is already in your inventory.
"""

EARTHSHAKER_NEW_ITEM_TEXT = """
You come across a secluded gorge, near the foot of the volcano, where the
ground cracks and rumbles with unseen fury. Amidst the scorched terrain,
jagged fissures snake their way through the earth, emitting sulphurous fumes
that sting your nostrils. In the centre of this tumultuous landscape lies a
cavern, its entrance obscured by a curtain of cascading ash.

As you enter, shadows dance eerily upon the walls, illuminated by sporadic
bursts of fiery light that seep through the ash-laden air. In the centre
stands a towering monolith of obsidian, a solemn sentinel amidst the chaos.
Its surface, once smooth and reflective, now bears the marks of time and
turmoil, a testament to the relentless forces that shape this unforgiving
realm.

At its base lies the Earthshaker, a weapon of immense power forged in the
heart of the volcano itself. Its massive form, imbued with the essence of the
earth's fury, is capable of unleashing devastating shockwaves. As you grasp
the hammer's handle, the ground trembles beneath your feet and a sense of
destiny washes over you, hinting at the crucial role it will play in the
battle to come.
"""

EARTHSHAKER_EXISTING_ITEM_TEXT = """
As you return to the secluded gorge, a sense of desolation hangs heavy in the
air, replacing the once-potent aura of power that permeated the surroundings.
Near the foot of the volcano, the ground seems to groan with a mournful lament.
The jagged fissures have grown, pumping ever-growing clouds of sulphurous
fumes.

Within the cavern, shadows flicker upon the now crumbling walls, the ash-laden
air thick with a palpable sense of decay. The towering monolith of obsidian,
once a symbol of strength and resilience, now bears the weight of its own
demise. Cracks mar its surface, a poignant reminder of the Earthshaker's
absence. At its base, the empty pedestal serves as a silent testament to the
loss of power, the cavern itself beginning to crumble, as if mourning the
departure of its guardian weapon.

The Earthshaker is already in your inventory.
"""

WOLVES_DESC_TEXT = """
You enter a desolate expanse, where the air hangs heavy with the scent of
charred earth and smouldering debris. Jagged rocks jut out from the ashen
landscape, casting eerie shadows that dance in the flickering light. In the
distance, the faint crackling of flames can be heard, a grim reminder of the
danger that lurks nearby.

Suddenly, a chorus of low growls echo through the barren terrain as a pack of
Ember Wolves emerge, their large forms moving with a menacing grace. Their
scorched fur hints at their fiery origin, with glowing embers crackling across
their skin, silhouetting this formidable foe against the smoky horizon. Brace
yourself, for these relentless predators strike without warning, leaving
nothing but ash in their wake.
"""

WOLVES_DEFEAT_TEXT = """
As the pack of Ember Wolves closes in, their menacing growls echoing through
the desolate expanse, you find yourself unarmed and unprepared for the
ferocity of their attack. With each lunge and snap of their fiery jaws, you
desperately try to fend them off, but their relentless assault overwhelms you.

The scorching heat of their breath sears your skin, and their claws tear
through your defences with ruthless efficiency. Despite your valiant efforts,
you are swiftly overpowered by the sheer force of their numbers, succumbing to
the vicious predators' relentless onslaught. As darkness descends, the last
thing you hear is their haunting howl of victory echoing across the barren
landscape.

You were not equipped to defeat the Ember Wolves.
"""

WOLVES_VICTORY_TEXT = """
As the pack of Ember Wolves encircles you, their fiery eyes locked onto their
prey, you grasp the Frostbite Sabre tightly, feeling its chilling aura envelop
you in a protective shroud of frost. With each swing of the blade, icy
tendrils lash out, sapping the heat from the air and freezing the ground
beneath your feet.

The wolves, accustomed to the searing heat of their domain, recoil in shock as
the biting cold pierces their scorched fur, slowing their movements. With
calculated strikes, you drive back the relentless predators, the shimmering
blade leaving trails of frost in its wake.

Finally, as the last wolf falls, defeated by the icy grip of the Frostbite
Sabre, a moment of silence descends upon the desolate expanse, broken only by
the crackling of distant flames, now subdued by the victorious chill.

You are now free to travel through this area in peace.
"""

WOLVES_CLEARED_TEXT = """
You have already defeated these Ember Wolves.

As you traverse the desolate expanse once more, a sense of eerie calm pervades
the air, replacing the earlier tension that hung heavy with the threat of the
Ember Wolves. The scent of charred earth lingers faintly, mingling with a
slightly cooler breeze that now sweeps through the jagged rocks jutting out
from the ashen landscape.

No longer do the eerie shadows dance in the flickering light, for the absence
of the predatory pack has lifted the veil of fear that once shrouded this
place. In the distance, the crackling of flames seems subdued, a subtle
reminder of the danger that once lurked nearby. You pass through the once
treacherous terrain, now reclaimed in peaceful victory.
"""

CRAWLER_DESC_TEXT = """
You tread cautiously through a landscape dominated by sulphur pits, a harsh
and acrid setting, where bubbling pools of yellow sulphur churn beneath a
cloud of noxious fumes. The ground is cracked and blistered, with jagged rocks
jutting out at odd angles. The stench of sulphur hangs heavy, with an intense
heat emanating from the pits, stinging your nostrils with their pungent odour.

Amidst the acrid haze, you catch sight of a grotesque silhouette emerging from
the molten depths. The Lava Crawler, a monstrous amalgamation of molten rock
and ancient bones, slithers across the landscape with ominous purpose. Its
segmented body crackles with magma, leaving a trail of searing heat in its
wake. Hundreds of jagged limbs writhe and pulse with fiery energy as it moves,
though slow, its immense weight promises deadly consequences for anything in
its path, ready to crush and incinerate with relentless efficiency.
"""

CRAWLER_DEFEAT_TEXT = """
The Lava Crawler advances toward you, but with nothing keep it at bay, the
blistering heat rapidly envelopes you. The relentless onslaught proves
overwhelming as its molten limbs ensnare you in a fiery embrace. Despite your
efforts to evade its grasp, the searing heat of its touch seeps through your
defences, sapping your strength with each blistering contact.

With a bone-crushing force, it pins you down, the weight of its immense form
pressing upon you like a suffocating inferno. As your vision blurs and
consciousness fades, the scorching heat consumes you, turning your final
moments into an agonizing blaze of defeat amidst the sulphuric haze.

You were not equipped to defeat the Lava Crawler.
"""

CRAWLER_VICTORY_TEXT = """
As the Lava Crawler looms menacingly before you, its fiery aura casting an
ominous glow amidst the sulphur pits, you wield the Water Staff, its ancient
runes glowing softly with the essence of rivers and seas. With a powerful
incantation, you unleash a torrent of water, blasting the creature with a
torrent that sizzles against its molten form.

The Lava Crawler hisses and sputters as its molten form is doused, its
movements slowing under the onslaught. Seizing the opportunity, you swiftly
switch to the Frostbite Sabre, its chilling aura intensifying as you strike
with calculated precision. The blade bites into the now sluggish creature,
each strike sending shards of frozen rock flying.

With a final, decisive blow, the Lava Crawler shatters into a cascade of
brittle fragments, its fiery core extinguished by the combined might of water
and ice. The steam now emanating from the Water Staff disperses the sulphurous
haze around you, allowing a fragment of sunlight to bathe the rocky terrain.

You are now free to travel through this area in peace.
"""

CRAWLER_CLEARED_TEXT = """
You have already defeated Lava Crawler.

As you cautiously traverse the landscape once dominated by the Lava Crawler, a
newfound sense of tranquillity pervades the air, replacing the previous
tension that hung heavy amidst the sulphur pits. The bubbling yellow pools now
swirl with a subdued motion, and the acrid stench lingers less oppressively in
the air. The ground, once cracked and blistered, now shows signs of tentative
healing, with patches of vegetation scattered across the scorched earth.

As the last traces of steam dissipate from the Lava Crawler's remains, the
cloud of sulphurous haze around you has begun to disperse, allowing the sun to
cast a gentle light upon the tranquil scene. You continue your journey through
the now peaceful landscape, the echoes of your hard-won victory lingering
amidst the newfound serenity.
"""

GOLEM_DESC_TEXT = """
You arrive at the foot of the towering volcano, before you stands a coliseum,
its grandeur rivalling the legendary gladiator pits of ancient Rome. Massive
stone arches loom overhead, leading into a circular arena surrounded by
towering tiers of weathered stone seats. As you step through the arches into
the coliseum, you're greeted by the echoes of ancient battles that seem to
linger in the air. The arena floor bears the scars of past encounters,
testament to the ferocity of the challenge that waits within.

Within this hallowed ground, the Magma Golem awaits, a living testament to the
raw power of the volcano from which it was born. Its gargantuan frame,
constructed of solid rock, pulses with streams of molten lava coursing through
its crevices. Each step of the Magma Golem causes the ground to tremble, and
its mighty fists can shatter even the toughest defences.

You feel a faint pull of energy from a nearby portal.
"""

GOLEM_DEFEATED_TEXT = """
As you stand before the colossal Magma Golem, its towering form radiating with
the fiery intensity of the volcano from which it was born, you realize the
magnitude of the challenge before you. With each thunderous step, the ground
trembles beneath its gargantuan weight, and streams of molten lava course
through its fissured frame like veins of liquid fire.

Despite your valiant efforts to evade its relentless onslaught, its mighty
fists descend upon you with unstoppable force, crushing through your defences
with ease. The searing heat of its touch scorches your flesh, leaving trails
of agonizing pain in its wake. As the Magma Golem towers over you, its fiery
gaze locking onto yours, you realize the futility of your struggle. With a
final, crushing blow, darkness envelops you, consumed by the overwhelming
power of the elemental titan.

You were not equipped to defeat the Magma Golem.
"""

GOLEM_VICTORY_TEXT = """
As you face the towering menace of the Magma Golem, you wield the Water Staff.
With a powerful incantation, you summon a flood of water to cascade over the
Magma Golem, temporarily slowing its relentless advance as steam billows from
its molten form.

Seizing the moment, you switch to the Frostbite Sabre, its chilling aura
enveloping you as you dart beneath the creature's towering frame. With a swift,
calculated strike, you slash at its leg, causing it to roar in pain as the
frozen blade bites deep.

As the Magma Golem staggers and falls to its knees, you grasp the Earthshaker,
feeling its immense power coursing through your veins. With a mighty leap, you
soar through the air, the weapon's weight heavy in your hands. With a
resounding crash, you bring the Earthshaker down upon the Magma Golem's chest,
unleashing a devastating shockwave that reverberates through the coliseum. The
creature shatters into a shower of molten fragments, its fiery essence
extinguished by the combined might of water, ice, and earth.

You are now free to travel through this area in peace.
"""

GOLEM_CLEARED_TEXT = """
You have already defeated Magma Golem.

As you return to the coliseum, a sense of tranquillity washes over the once
tumultuous arena. The echoes of ancient battles fade into the background,
replaced by a serene stillness that permeates the air. The scars of past
encounters upon the arena floor now serve as silent reminders of your hard-
fought victory against the Magma Golem.

Beyond the stone arches, the towering volcano stands in solemn silence, its
fiery rage subdued in the wake of the elemental titan's defeat. The intensity
of the heat has lessened, and the volcano seems more dormant, its towering
presence no longer looming with imminent threat.

You feel a faint pull of energy from a nearby portal.
"""

SCORCHLANDS_PORTAL_TEXT = """
You venture deeper into the heart of the volcano, where molten streams flow
like rivers of fire beneath a cavernous expanse. At the epicentre, a portal
materializes, its ethereal glow pulsating with hues of crimson and gold,
casting flickering shadows against the rugged walls.

The heat of the lava fades into the background as you approach, drawn to the
portal's beckoning light. With each step, a sense of anticipation grows,
fuelled by the promise of escape from this fiery realm. As you reach out to
touch the portal, its shimmering surface envelops you, transporting you with a
rush of swirling energy to the safety of home.

Congratulations! You found the Scorchlands Portal and finished your quest.

With different paths to take, items to find and enemies to battle, every
playthrough can be a brand new adventure. Who knows, you may even find a
secret ending...
"""
