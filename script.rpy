define b = Character('Beluga', color="#46B9EC")
define o = Character('Orca', color="#00416F")

label start:

    scene bg ocean

    show beluga
    b "Hello orca whale, we are in a visual novel. How do you feel about this?"
    hide beluga

    show orca
    o "I think it's interesting. I've never been in a visual novel before. But I fear.. something"
    hide orca

    show beluga
    b "What do you fear?"
    hide beluga

    show orca
    o "I fear... Monika. What if she's in all visual novels?"
    hide orca

    show beluga
    b "I don't think she is. Why would she be in this one? This is totally irrelevant. It's just a test run for a visual novel."

    show orca
    o "You never know, beluga, you never know. She could be lurking and overhearing us right now."
